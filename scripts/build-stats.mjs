import { readdir, readFile, mkdir, writeFile } from 'node:fs/promises';
import path from 'node:path';

const root = process.cwd();

const repositoryAreas = [
  { key: 'research_studies', label: 'Research studies', dir: '001_Research_studies' },
  { key: 'evidence', label: 'Evidence items', dir: '002_Evidence' },
  { key: 'needs', label: 'Needs', dir: '003_User_needs' },
  { key: 'behaviours', label: 'Behaviours', dir: '004_Behaviours' },
  { key: 'pain_points', label: 'Pain points', dir: '005_Pain_point' },
  { key: 'insights', label: 'Insights', dir: '006_Insights' },
  { key: 'themes', label: 'Themes', dir: '007_Themes' },
  { key: 'personas', label: 'Personas or archetypes', dir: '008_Personas' },
  { key: 'journeys', label: 'Journeys', dir: '009_Journeys' }
];

const ignoredDirectoryNames = new Set([
  '.git', '.github', '.obsidian', 'node_modules', 'Templates', 'docs', 'scripts'
]);

const defaultCounts = {
  research_studies: 0,
  evidence: 0,
  user_needs: 0,
  civic_needs: 0,
  behaviours: 0,
  pain_points: 0,
  insights: 0,
  themes: 0,
  personas: 0,
  journeys: 0,
  other_markdown_objects: 0
};

const byStatus = {};
const byLifecycleState = {};
const byEvidenceStrength = {};
const serviceAreas = new Set();
const warnings = [];

function normaliseValue(value) {
  return String(value || '')
    .trim()
    .replace(/^['\"]|['\"]$/g, '')
    .replace(/\s+/g, ' ');
}

function normaliseKey(value) {
  return normaliseValue(value)
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '_')
    .replace(/^_+|_+$/g, '');
}

function addCount(map, rawValue) {
  const value = normaliseValue(rawValue);
  if (!value) return;
  map[value] = (map[value] || 0) + 1;
}

function addValues(callback, rawValue) {
  if (!rawValue) return;

  if (Array.isArray(rawValue)) {
    rawValue.forEach((item) => addValues(callback, item));
    return;
  }

  const value = normaliseValue(rawValue);
  if (!value) return;

  if (value.startsWith('[') && value.endsWith(']')) {
    value
      .slice(1, -1)
      .split(',')
      .map(normaliseValue)
      .filter(Boolean)
      .forEach(callback);
    return;
  }

  callback(value);
}

function parseFrontmatter(content) {
  if (!content.startsWith('---\n')) return {};

  const end = content.indexOf('\n---', 4);
  if (end === -1) return {};

  const frontmatter = content.slice(4, end).split('\n');
  const metadata = {};
  let currentKey = null;

  for (const line of frontmatter) {
    if (!line.trim() || line.trim().startsWith('#')) continue;

    const keyValueMatch = line.match(/^([A-Za-z0-9_-]+):\s*(.*)$/);
    if (keyValueMatch) {
      currentKey = keyValueMatch[1];
      const rawValue = keyValueMatch[2].trim();

      if (!rawValue) {
        metadata[currentKey] = [];
      } else if (rawValue.startsWith('[') && rawValue.endsWith(']')) {
        metadata[currentKey] = rawValue
          .slice(1, -1)
          .split(',')
          .map(normaliseValue)
          .filter(Boolean);
      } else {
        metadata[currentKey] = normaliseValue(rawValue);
      }
      continue;
    }

    const listMatch = line.match(/^\s*-\s+(.+)$/);
    if (listMatch && currentKey) {
      if (!Array.isArray(metadata[currentKey])) metadata[currentKey] = [metadata[currentKey]].filter(Boolean);
      metadata[currentKey].push(normaliseValue(listMatch[1]));
    }
  }

  return metadata;
}

function classifyObject(areaKey, filePath, metadata) {
  const fileName = path.basename(filePath, '.md');
  const objectType = normaliseKey(
    metadata.object_type ||
    metadata.type ||
    metadata.kind ||
    metadata.object ||
    metadata.need_type ||
    ''
  );

  const id = normaliseValue(metadata.id || metadata.object_id || fileName).toUpperCase();

  if (objectType.includes('civic_need') || id.startsWith('CN_') || id.startsWith('CN-')) return 'civic_needs';
  if (objectType.includes('user_need') || id.startsWith('UN_') || id.startsWith('UN-')) return 'user_needs';
  if (objectType.includes('pain')) return 'pain_points';
  if (objectType.includes('evidence')) return 'evidence';
  if (objectType.includes('behaviour') || objectType.includes('behavior')) return 'behaviours';
  if (objectType.includes('insight')) return 'insights';
  if (objectType.includes('theme')) return 'themes';
  if (objectType.includes('persona') || objectType.includes('archetype')) return 'personas';
  if (objectType.includes('journey')) return 'journeys';
  if (objectType.includes('study') || objectType.includes('research')) return 'research_studies';

  if (areaKey === 'needs') return 'user_needs';
  if (areaKey in defaultCounts) return areaKey;
  return 'other_markdown_objects';
}

async function directoryExists(directory) {
  try {
    const entries = await readdir(directory);
    return Array.isArray(entries);
  } catch {
    return false;
  }
}

async function listMarkdownFiles(directory) {
  const entries = await readdir(directory, { withFileTypes: true });
  const files = [];

  for (const entry of entries) {
    if (ignoredDirectoryNames.has(entry.name)) continue;
    const fullPath = path.join(directory, entry.name);

    if (entry.isDirectory()) {
      files.push(...await listMarkdownFiles(fullPath));
    } else if (entry.isFile() && entry.name.endsWith('.md')) {
      files.push(fullPath);
    }
  }

  return files;
}

async function main() {
  const counts = { ...defaultCounts };
  const areaSummaries = [];
  let totalObjects = 0;

  for (const area of repositoryAreas) {
    const absoluteDir = path.join(root, area.dir);
    const exists = await directoryExists(absoluteDir);

    if (!exists) {
      areaSummaries.push({ ...area, count: 0, exists: false });
      warnings.push(`${area.dir} was not found, so its count is zero.`);
      continue;
    }

    const files = await listMarkdownFiles(absoluteDir);
    areaSummaries.push({ ...area, count: files.length, exists: true });

    for (const file of files) {
      const content = await readFile(file, 'utf8');
      const metadata = parseFrontmatter(content);
      const objectClass = classifyObject(area.key, file, metadata);

      counts[objectClass] = (counts[objectClass] || 0) + 1;
      totalObjects += 1;

      addCount(byStatus, metadata.status || metadata.review_status || metadata.maturity || 'No status metadata');
      addCount(byLifecycleState, metadata.lifecycle_state || metadata.state || 'No lifecycle metadata');
      addCount(byEvidenceStrength, metadata.evidence_strength || metadata.confidence || 'No evidence-strength metadata');

      addValues((value) => serviceAreas.add(value), metadata.service_area);
      addValues((value) => serviceAreas.add(value), metadata.service_areas);
      addValues((value) => serviceAreas.add(value), metadata.domain);
      addValues((value) => serviceAreas.add(value), metadata.domains);
    }
  }

  const stats = {
    generated_at: new Date().toISOString(),
    generated_from: 'Repository markdown files in numbered knowledge-object folders',
    scope_note: 'Counts are generated from repository folders and frontmatter where available. Missing metadata is counted explicitly rather than inferred as reviewed or validated.',
    totals: {
      service_areas: serviceAreas.size,
      repository_areas: repositoryAreas.length,
      knowledge_layers: 3,
      markdown_objects: totalObjects,
      ...counts
    },
    service_areas: [...serviceAreas].sort(),
    repository_areas: areaSummaries,
    by_status: byStatus,
    by_lifecycle_state: byLifecycleState,
    by_evidence_strength: byEvidenceStrength,
    warnings
  };

  await mkdir(path.join(root, 'docs'), { recursive: true });
  await writeFile(path.join(root, 'docs', 'stats.json'), `${JSON.stringify(stats, null, 2)}\n`, 'utf8');
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
