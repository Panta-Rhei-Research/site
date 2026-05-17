#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";

const repoRoot = process.cwd();
const siteRoot = path.join(repoRoot, "_site");
const sourceRoot = path.join(repoRoot, "corpus", "construction-spine");
const stepRoot = path.join(siteRoot, "corpus", "construction-spine", "steps");

const formulaHeavy = new Map([
  ["004-four-block-order-readout", "O_α"],
  ["018-tau-3-as-geometric-readout-tau-1-x-f-t-2", "τ"],
  ["023-earned-constants-pi-tau-e-tau-j", "π"],
  ["024-master-constant-iota-tau", "ι"],
  ["064-tau-einstein-identity", "κ"],
  ["065-lorentzian-signature-from-j-2-plus-1", "j"],
  ["077-e1-to-e2-life-as-predicate-layer", "E"],
  ["091-e2-to-e3-reflective-structure", "E"],
]);

const forbiddenHtmlPatterns = [
  /pending-source-anchor/,
  /kappa_tau/,
  /iota_tau/,
  /pi_tau/,
  /e_tau/,
  /to\s+:\s/,
  /written here as\s*,/,
  /O_α O_π O_γ O_η ω/,
  /\\kappa|\\tau|\\iota|\\pi/,
];

function assert(condition, message) {
  if (!condition) {
    throw new Error(message);
  }
}

function read(filePath) {
  return fs.readFileSync(filePath, "utf8");
}

function exists(filePath) {
  return fs.existsSync(filePath);
}

function stripHtml(html) {
  return html
    .replace(/<script[\s\S]*?<\/script>/gi, " ")
    .replace(/<style[\s\S]*?<\/style>/gi, " ")
    .replace(/<[^>]+>/g, " ")
    .replace(/\s+/g, " ")
    .trim();
}

function listBuiltStepPages() {
  assert(exists(stepRoot), `Missing built step root: ${stepRoot}`);
  return fs
    .readdirSync(stepRoot, { withFileTypes: true })
    .filter((entry) => entry.isDirectory())
    .map((entry) => entry.name)
    .filter((name) => /^\d{3}-/.test(name))
    .sort();
}

function countMacroSources() {
  return fs
    .readdirSync(sourceRoot, { withFileTypes: true })
    .filter((entry) => entry.isDirectory())
    .map((entry) => entry.name)
    .filter((name) => name !== "steps")
    .filter((name) => name !== "define-the-kernel")
    .filter((name) => name !== "internalize-logic")
    .length;
}

assert(exists(path.join(siteRoot, "corpus", "construction-spine", "index.html")), "Missing Construction Spine hub page.");
assert(exists(path.join(stepRoot, "index.html")), "Missing 100-step ledger page.");

const stepPages = listBuiltStepPages();
assert(stepPages.length === 100, `Expected 100 built detail step pages, found ${stepPages.length}.`);
assert(countMacroSources() === 10, `Expected 10 canonical macro source pages, found ${countMacroSources()}.`);

const ledgerHtml = read(path.join(stepRoot, "index.html"));
for (const required of ["100-Step Construction Spine Ledger", "S001", "S042", "S064", "S100"]) {
  assert(ledgerHtml.includes(required), `Ledger page missing ${required}.`);
}

for (const page of stepPages) {
  const htmlPath = path.join(stepRoot, page, "index.html");
  const html = read(htmlPath);
  assert(html.includes("Macro context"), `${page}: missing top macro-context callout.`);
  assert(html.includes("Anchor classification"), `${page}: missing anchor classification.`);
  assert(html.includes("Detailed source anchors pending extraction."), `${page}: missing public-facing pending-source wording.`);
  for (const pattern of forbiddenHtmlPatterns) {
    assert(!pattern.test(html), `${page}: forbidden rendered pattern ${pattern}.`);
  }
}

for (const [slug, token] of formulaHeavy.entries()) {
  const html = read(path.join(stepRoot, slug, "index.html"));
  assert(html.includes("<math"), `${slug}: expected native MathML output.`);
  assert(stripHtml(html).includes(token), `${slug}: expected visible formula token ${token}.`);
}

const s004 = stripHtml(read(path.join(stepRoot, "004-four-block-order-readout", "index.html")));
assert(s004.includes("O_α ≺ O_π ≺ O_γ ≺ O_η ≺ ω"), "S004 loses the order-arrow formula.");

const s064 = stripHtml(read(path.join(stepRoot, "064-tau-einstein-identity", "index.html")));
assert(s064.includes("Rᴴ = κ_τ T"), "S064 loses the Tau-Einstein formula.");

const s077 = stripHtml(read(path.join(stepRoot, "077-e1-to-e2-life-as-predicate-layer", "index.html")));
assert(s077.includes("Life as predicate layer"), "S077 loses the explicit earned label.");
assert(!s077.includes("to :"), "S077 still has stripped-title punctuation.");

const s100Text = stripHtml(read(path.join(stepRoot, "100-logos-boundary-and-ontic-closure-burden", "index.html")));
const s100Matches = s100Text.match(/https:\/\/prrp\.site\/s100/g) || [];
assert(s100Matches.length === 1, `S100 should show the short route once; found ${s100Matches.length}.`);

console.log("Construction Spine routing QA assertions passed.");
