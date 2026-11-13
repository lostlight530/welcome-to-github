// Offline, dependency-free contract check for the Vite Pages artifact.
// Checks local route resolution and declared link targets; never asserts HTTP reachability.
import assert from 'node:assert/strict';
import { existsSync, readFileSync } from 'node:fs';
import { resolve, join } from 'node:path';

const root = process.cwd();
const dist = resolve(root, 'dist');
const base = new URL('https://lostlight530.github.io/welcome-to-github/');
const read = (relative) => readFileSync(resolve(root, relative), 'utf8');
const built = (relative) => readFileSync(join(dist, relative), 'utf8');
const record = { localLinks: 0, localAnchors: 0, externalLinks: 0, dynamicExternalSources: 0, network: 'NOT_VERIFIED', failures: [] };

assert(existsSync(dist), 'Build first: npm run build -- --base=/welcome-to-github/');
const paths = ['index.html', 'yearbook/index.html'];
for (const page of paths) {
  const html = built(page);
  const pageURL = new URL(page, base);
  const ids = new Set([...html.matchAll(/\bid=(["'])([^"']+)\1/g)].map(m => m[2]));
  const anchors = [...html.matchAll(/<a\b[^>]*?\bhref=(["'])(.*?)\1/gs)];
  for (const match of anchors) {
    const raw = match[2];
    if (raw.includes('${')) continue; // Dynamic template is checked in the translations module below.
    const target = new URL(raw, pageURL);
    assert(['https:', 'mailto:'].includes(target.protocol), 'Unexpected scheme: ' + raw);
    if (target.origin !== base.origin) {
      record.externalLinks++;
      continue;
    }
    assert(target.pathname.startsWith(base.pathname), 'Escaped site base: ' + raw);
    const suffix = decodeURIComponent(target.pathname.slice(base.pathname.length));
    const localFile = suffix === '' || suffix.endsWith('/') ? suffix + 'index.html' : suffix;
    assert(existsSync(join(dist, localFile)), 'Missing artifact for ' + page + ' => ' + raw + ' (dist/' + localFile + ')');
    record.localLinks++;
    if (target.hash) {
      const targetIDs = localFile === page ? ids : new Set([...built(localFile).matchAll(/\bid=(["'])([^"']+)\1/g)].map(m => m[2]));
      assert(targetIDs.has(decodeURIComponent(target.hash.slice(1))), 'Missing anchor ' + page + ' => ' + raw);
      record.localAnchors++;
    }
  }
}
const portal = built('index.html');
const yearbook = built('yearbook/index.html');
const readme = read('README.md');
const translations = built('yearbook/src/scripts/translations.js');
const memorial = 'docs/archaeology/legacy_traces/MEMORIAL.md';
assert(existsSync(join(dist, memorial)), 'Missing published Memorial');
assert(yearbook.includes('href="../' + memorial + '"'), 'Yearbook Memorial route mismatch');
assert(yearbook.includes('id="repo-portal-link" href="../"'), 'No explicit yearbook -> portal route');
assert(portal.includes('href="./yearbook/"'), 'No portal -> yearbook route');
assert(portal.includes('id="mobile-nav"') && portal.includes('href="#stack"'), 'Narrow-screen sections missing');
assert(yearbook.includes('aria-expanded="false"') && yearbook.includes("setAttribute('aria-expanded', String(menuOpen))"), 'Yearbook mobile menu state not synchronized');
assert(yearbook.includes("setAttribute('aria-expanded', 'false')"), 'Yearbook menu close state missing');
assert(yearbook.includes('translations.js?v=20261112-badges'), 'Legacy translation cache version changed unexpectedly');
assert(yearbook.includes('legacy-css-fallback'), 'Legacy CSS fallback marker missing');
for (const line of readme.split('\n').filter(line => /Yearbook|年度回顾/.test(line) && /\]\(https:\/\//.test(line))) {
  const markdownLinks = [...line.matchAll(/\]\((https:\/\/[^)\s]+)\)/g)].map(m => new URL(m[1]));
  assert(
    markdownLinks.some(url =>
      url.origin === base.origin &&
      url.pathname === base.pathname + 'yearbook/' &&
      url.search === '' &&
      url.hash === '' &&
      url.username === '' &&
      url.password === ''
    ),
    'README yearbook link must resolve to the exact same-origin yearbook route: ' + line
  );
}
assert(readme.includes('[Current five-core research portal'), 'Current portal entry absent from README');
const sourceURLs = [...translations.matchAll(/\blink:\s*["'](https:\/\/[^"']+)["']/g)].map(m => m[1]);
assert(sourceURLs.length >= 10, 'Expected bilingual public architecture/practice source list');
for (const url of sourceURLs) { assert(new URL(url).protocol === 'https:', 'Unsafe dynamic URL'); }
record.dynamicExternalSources = new Set(sourceURLs).size;
console.log(JSON.stringify({ outcome: 'SOURCE_AND_DIST_ROUTE_PASS', checks: record, caveat: 'External HTTP, real-browser navigation, Tailwind CDN and assistive-technology interactions NOT_VERIFIED' }, null, 2));
