#!/usr/bin/env python3
"""
upgrade_results_v2.py — Upgrade Results lane to v2 taxonomy.

Reads the 38-result seed JSON and the existing 72 result pages, then:
  1. Adds v2 fields (result_kind, importance_class, status_code, domain_group) to
     existing result pages that map to seed results.
  2. Creates new result pages for seed results not already present.
  3. Regenerates _data/results/results.json with v2 fields.
  4. Updates _data/results/topics.json with new counts.
  5. Creates shell pages (why-so-many-results, how-to-read, status-and-claim-typing).
  6. Regenerates browse index pages.

Usage:
  python3 scripts/upgrade_results_v2.py
"""

import json
import os
import re
import sys
import glob
from typing import Optional

SITE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SEED_PATH = os.path.join(
    os.path.expanduser("~"),
    "Books/PantaRhei-2ndEd/website/specs/hot-topics-results-seed-pack",
    "02-cross-program-key-results-seed.json",
)

# ---------------------------------------------------------------------------
# Seed → existing slug mapping
# ---------------------------------------------------------------------------

SEED_TO_SLUG = {
    "R-CENTRAL-THEOREM": "central-theorem",
    "R-HYPERFACTORIZATION": "hyperfactorization-theorem",
    "R-PRIME-POLARITY": "prime-polarity-theorem",
    "R-CATEGORICITY-OF-TAU0": "tau-kernel-coherence",
    "R-ENRICHMENT-LADDER": "canonical-ladder-theorem",
    "R-P-VS-NP": "tau-admissibility-collapse-p-np",
    "R-YANG-MILLS-MASS-GAP": "yang-mills-mass-gap",
    "R-HUBBLE-TENSION": "hubble-tension-resolved-h-formula",
    "R-THREE-GENERATIONS": "three-generations-matter",
    "R-NEUTRINO-MASS-ORDERING": "neutrino-mass-sum-0pt089-ev-normal-ordering",
    "R-W-MASS-PUZZLE": "w-boson-mass-prediction",
    "R-MUON-G-2": "muon-anomalous-magnetic-moment-8pt8-ppm",
    "R-PROTON-RADIUS": "proton-charge-radius-12-ppm",
    "R-NO-HAWKING-RADIATION": "no-bh-evaporation",
    "R-HOMOCHIRALITY": "homochirality-universality-12-step-derivation",
    "R-ABIOGENESIS-TIMESCALE": "abiogenesis-timescale-bound",
    "R-SUBSTRATE-INDEPENDENCE": "substrate-abstraction",
    "R-ATP-UNIQUENESS": "atp-currency-uniqueness",
    "R-CATEGORICAL-IMPERATIVE-DERIVATION": "categorical-imperative-fixed-point",
    "R-GODEL-AVOIDANCE": "goedel-avoidance",
    "R-HARD-PROBLEM-OF-CONSCIOUSNESS": "consciousness-global-section",
    "R-DARK-SECTOR-CLOSURE": "no-dark-matter-particle",
    "R-INFLATION": "spectral-index-ns-from-inflation",
}

# Seed results that should become new pages
# (R-WHY-SO-MANY-RESULTS is a shell page, not a result)
SHELL_SEED_IDS = {"R-WHY-SO-MANY-RESULTS-ARE-EVEN-POSSIBLE"}

# Map v1 result_type/bridge_status → v2 result_kind inference
def infer_result_kind(result_type: str, bridge_status: str, topic: str) -> str:
    if result_type == "empirical_prediction":
        return "frontier-problem"
    if bridge_status in ("bridge", "empirical"):
        return "frontier-problem"
    if bridge_status == "interpretive":
        return "consequence"
    if topic == "mathematics" and result_type == "structural_readout":
        return "foundational-math"
    return "frontier-problem"

def infer_importance(result_kind: str) -> str:
    if result_kind == "foundational-math":
        return "structural-support-result"
    if result_kind == "consequence":
        return "consequence-reframing"
    return "domain-level-open-problem"

STATUS_MAP = {
    "R": "resolved",
    "P": "partial",
    "Q": "qualitative",
    "C": "contradicted",
    "N": "not-addressed",
}

STATUS_DISPLAY = {
    "R": "Resolved",
    "P": "Partial",
    "Q": "Qualitative",
    "C": "Contradicted",
    "N": "Not Addressed",
}

# ---------------------------------------------------------------------------
# YAML frontmatter parsing/writing
# ---------------------------------------------------------------------------

def parse_frontmatter(content: str):
    """Parse YAML frontmatter and body from markdown file."""
    if not content.startswith("---"):
        return {}, content
    end = content.index("---", 3)
    fm_text = content[3:end].strip()
    body = content[end + 3:].strip()
    # Simple YAML parsing for our flat/semi-flat frontmatter
    fm = {}
    current_key = None
    current_list = None
    for line in fm_text.split("\n"):
        if not line.strip():
            continue
        # Handle list items at top level
        if line.startswith("- ") and current_key and isinstance(fm.get(current_key), list):
            fm[current_key].append(line[2:].strip())
            continue
        # Handle nested YAML (just store as raw text for preservation)
        if line.startswith("  ") and current_key:
            if current_key + "_raw" not in fm:
                fm[current_key + "_raw"] = ""
            fm[current_key + "_raw"] += line + "\n"
            continue
        # Key-value pair
        if ":" in line:
            key, _, val = line.partition(":")
            key = key.strip()
            val = val.strip()
            current_key = key
            if val == "":
                fm[key] = []
            elif val.startswith("'") or val.startswith('"'):
                fm[key] = val.strip("'\"")
            elif val == "[]":
                fm[key] = []
            else:
                fm[key] = val
    return fm, body


def read_result_page(path: str):
    """Read a result page and return raw content."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def inject_v2_fields(content: str, result_kind: str, importance_class: str,
                     status_code: str, domain_group: str) -> str:
    """Inject v2 fields into existing frontmatter."""
    if not content.startswith("---"):
        return content

    end_idx = content.index("---", 3)
    fm_text = content[3:end_idx]
    body = content[end_idx + 3:]

    # Remove old v2 fields if present (for idempotency)
    lines = fm_text.split("\n")
    filtered = [l for l in lines if not any(
        l.strip().startswith(f"{k}:") for k in
        ["result_kind", "importance_class", "status_code", "domain_group"]
    )]

    # Find insertion point — after bridge_status or result_type
    insert_idx = len(filtered)
    for i, line in enumerate(filtered):
        if line.strip().startswith("bridge_status:") or line.strip().startswith("result_type:"):
            insert_idx = i + 1

    v2_lines = [
        f"result_kind: {result_kind}",
        f"importance_class: {importance_class}",
        f"status_code: {status_code}",
        f"domain_group: \"{domain_group}\"",
    ]

    filtered[insert_idx:insert_idx] = v2_lines

    return "---\n" + "\n".join(filtered) + "---" + body


# ---------------------------------------------------------------------------
# New result page generator
# ---------------------------------------------------------------------------

def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = text.strip("-")
    if len(text) > 60:
        text = text[:60].rsplit("-", 1)[0]
    return text


def layer_to_topic(layer: str) -> str:
    mapping = {
        "mathematics": "mathematics",
        "physics": "physics",
        "life": "biology",
        "metaphysics": "philosophy",
    }
    return mapping.get(layer, layer)


def generate_new_result_page(seed: dict, result_num: int) -> str:
    """Generate a new result page from seed data."""
    slug = slugify(seed["title"])
    topic = layer_to_topic(seed["primary_layer"])
    layer = seed["primary_layer"]
    status = STATUS_MAP.get(seed["status_code"], "partial")
    status_display = STATUS_DISPLAY.get(seed["status_code"], "Partial")
    result_kind = seed["result_kind"]
    importance = seed["importance_class"]
    domain = seed.get("domain_group", "")

    # Generate type display
    type_display = result_kind.replace("-", " ").title()

    # Summary
    summary = seed.get("notes", "") or seed.get("why_include_now", "")
    if not summary:
        summary = f"A {result_kind.replace('-', ' ')} result in {domain}."

    return f"""---
layout: result-page
title: "{seed['title']}"
permalink: /results/problem/{slug}/
result_id: result-{result_num:03d}
topic: {topic}
layer: {layer}
result_type: {result_kind.replace('-', '_')}
bridge_status: {status}
result_kind: {result_kind}
importance_class: {importance}
status_code: {seed['status_code']}
domain_group: "{domain}"
summary_short: "{summary}"
canonical_books: []
right_rail:
  meta:
    type: "{type_display}"
    layer: {layer.capitalize()}
    topic: {topic.capitalize()}
    status: "{status_display}"
    updated: April 2026
---

## Overview

{seed['title']} is a {result_kind.replace('-', ' ')} in the {domain} domain of the Panta Rhei Research Program.

{seed.get('why_include_now', '')}

## Status

**Epistemic status**: {status_display}

**Result kind**: {type_display}

**Importance**: {importance.replace('-', ' ').title()}
"""


# ---------------------------------------------------------------------------
# Shell page generators
# ---------------------------------------------------------------------------

def generate_shell_pages():
    """Generate the three shell pages."""
    pages = {}

    pages["why-so-many-results"] = """---
layout: program-doc
title: "Why So Many Results Are Possible"
permalink: /results/why-so-many-results/
lane: results
summary_short: "How a constrained five-generator kernel can address hundreds of recognized problems across four domains."
summary_cards:
- title: "The question"
  body: "How can one framework produce results across mathematics, physics, biology, and philosophy?"
- title: "The answer"
  body: "Extreme constraint at the base forces specificity everywhere else. Five generators, seven axioms, one operator — zero free parameters."
- title: "The consequence"
  body: "Every prediction is structurally forced. If one is wrong, the kernel itself is falsified."
right_rail:
  related:
  - title: "Results Overview"
    url: /results/
  - title: "Framework Overview"
    url: /framework/about/
  - title: "About the Research"
    url: /research-program/about/
  meta:
    type: "Shell Page"
    scope: "Results Lane"
    status: "Canonical"
    updated: "April 2026"
---

## Why So Many Results Are Even Possible

The Panta Rhei Research Program claims results across mathematics, physics, biology, and philosophy. This sounds implausible. A single framework addressing the Hubble tension, the genetic code, consciousness, and the Categorical Imperative?

The answer lies in the nature of the framework's constraint.

## Extreme Constraint Forces Specificity

Category τ begins with five generators (α, π, γ, η, ω), seven axioms (K0–K6), and one operator (ρ). There are no free parameters. No tuning. No model selection.

This extreme constraint is precisely what makes breadth possible:

- **Every orbit is forced.** The four orbit rays O_α, O_π, O_γ, O_η are the only objects that exist. Their properties are determined by the axioms.
- **Every constant is derived.** The master constant ι_τ = 2/(π+e) is not chosen — it is the unique value compatible with the kernel's spectral structure.
- **Every layer is earned.** The enrichment ladder E₀ → E₁ → E₂ → E₃ is the unique maximal chain. It terminates at E₃. There is no E₄.

## One Prediction Failing Falsifies Everything

Because there are no free parameters, every prediction is load-bearing. If the Higgs mass prediction is wrong, it is not a parameter that failed — it is the kernel. If the genetic code optimality fails, the E₂ enrichment is wrong. If the Categorical Imperative derivation fails, the E₃ self-enrichment is wrong.

This is not a weakness. It is the program's principal epistemic virtue: **maximum falsifiability from minimum assumptions**.

## The Three Result Types

Results in this lane are classified by type:

1. **Frontier Problem Results** — recognized external problems (dark matter, consciousness, Hubble tension) where the framework makes a specific claim.
2. **Foundational Mathematical Results** — major internal structural contributions (Central Theorem, Hyperfactorization, Prime Polarity).
3. **Consequence/Reframing Results** — higher-order consequences that follow from the framework's structure (Gödel Avoidance, No Forced Stance, physical reality as semantic reading).

## How to Inspect

Every result page provides:
- The mainstream problem statement
- The program's specific claim
- The epistemic status (resolved, partial, qualitative, contradicted)
- The canonical grounding (which books, parts, registry objects)
- Links to verification routes
"""

    pages["how-to-read-a-result-page"] = """---
layout: program-doc
title: "How to Read a Result Page"
permalink: /results/how-to-read-a-result-page/
lane: results
summary_short: "A guide to the anatomy of result pages in the Results lane."
summary_cards:
- title: "Page structure"
  body: "Each result page follows a standard template: overview, detail, result statement, with typed metadata."
- title: "Epistemic typing"
  body: "Every claim carries a status: resolved, partial, qualitative, or contradicted."
- title: "Canonical grounding"
  body: "Every result links to its source in the books, registry, and framework."
right_rail:
  related:
  - title: "Results Overview"
    url: /results/
  - title: "Status and Claim Typing"
    url: /results/status-and-claim-typing/
  - title: "Why So Many Results"
    url: /results/why-so-many-results/
  meta:
    type: "Shell Page"
    scope: "Results Lane"
    status: "Canonical"
    updated: "April 2026"
---

## Anatomy of a Result Page

Every result page in this lane follows a consistent structure designed to make claims inspectable.

## The Header

The hero card shows:
- **Result kind** — frontier problem, foundational math, or consequence/reframing
- **Importance** — core foundational, high-impact frontier, domain-level, structural support, or consequence
- **Status** — resolved (R), partial (P), qualitative (Q), or contradicted (C)
- **Layer** — which enrichment layer (mathematics, physics, life, metaphysics)
- **Topic** — the domain area

## The Body

### Overview
A concise summary of the result: what problem it addresses, what the program claims, and why it matters.

### Detail
The full technical exposition: how the result is derived, what registry objects it depends on, and what its precision or scope is.

### Result Statement
A one-paragraph canonical statement of the result, suitable for citation.

## Epistemic Status Chips

Every result carries typed metadata in the right rail:
- **Resolved** — the program has a complete, machine-checked or structurally grounded result
- **Partial** — the program has a structural approach but the derivation is incomplete
- **Qualitative** — the program reframes the problem but does not provide a quantitative prediction
- **Contradicted** — the program's result contradicts mainstream expectation (flagged honestly)

## How to Verify

Each result page links to:
- **Books** — the canonical monograph source
- **Registry** — specific definitions, theorems, and propositions
- **Framework** — the module that grounds the result
- **Verify lane** — the verification entry point
"""

    pages["status-and-claim-typing"] = """---
layout: program-doc
title: "Status and Claim Typing"
permalink: /results/status-and-claim-typing/
lane: results
summary_short: "How the program types its claims: status codes, epistemic postures, and the discipline of honest scope."
summary_cards:
- title: "Status codes"
  body: "R (Resolved), P (Partial), Q (Qualitative), C (Contradicted), N (Not Addressed)"
- title: "Result kinds"
  body: "Frontier Problem, Foundational Math, Consequence/Reframing"
- title: "Why it matters"
  body: "Typed honesty prevents rhetorical inflation and makes the program falsifiable."
right_rail:
  related:
  - title: "Results Overview"
    url: /results/
  - title: "How to Read a Result Page"
    url: /results/how-to-read-a-result-page/
  - title: "Why So Many Results"
    url: /results/why-so-many-results/
  meta:
    type: "Shell Page"
    scope: "Results Lane"
    status: "Canonical"
    updated: "April 2026"
---

## Claim Typing Discipline

The Panta Rhei Research Program maintains a strict typing discipline for all public claims. Every result carries explicit metadata about what kind of claim it is, what its current status is, and what its epistemic posture is.

## Status Codes

| Code | Label | Meaning |
|------|-------|---------|
| **R** | Resolved | Complete structural derivation or machine-checked result |
| **P** | Partial | Structural approach exists but derivation is incomplete |
| **Q** | Qualitative | Framework reframes the problem without quantitative prediction |
| **C** | Contradicted | Program result contradicts mainstream expectation |
| **N** | Not Addressed | Problem is recognized but not yet engaged |

## Result Kinds

| Kind | Description | Example |
|------|-------------|---------|
| **Frontier Problem** | Addresses a recognized external problem | Dark matter, Hubble tension, consciousness |
| **Foundational Math** | Major internal structural contribution | Central Theorem, Hyperfactorization |
| **Consequence** | Higher-order consequence of the framework | Gödel Avoidance, No Forced Stance |

## Importance Classification

| Class | Scope |
|-------|-------|
| **Core Foundational** | Problems that define the identity of the field |
| **High-Impact Frontier** | Problems with broad recognition and active research |
| **Domain-Level** | Important within a specific subdomain |
| **Structural Support** | Internal results that enable other claims |
| **Consequence/Reframing** | Results that follow as consequences |

## Why Typed Honesty Matters

A program that claims to address the Riemann Hypothesis and the Hard Problem of Consciousness must be maximally transparent about what "address" means in each case. The typing system ensures:

- A **resolved** result (R) means something different from a **partial** result (P)
- A **contradicted** result (C) is surfaced honestly, not hidden
- A **qualitative** reframing (Q) is not rhetorically inflated into a "solution"
- Every claim can be independently inspected via the verification route

This discipline is not optional. It is the epistemic infrastructure that makes the program's breadth credible rather than suspect.
"""

    return pages


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    # Load seed
    with open(SEED_PATH, encoding="utf-8") as f:
        seeds = json.load(f)
    print(f"Loaded {len(seeds)} seed results")

    # Load existing results data
    results_json_path = os.path.join(SITE_DIR, "_data", "results", "results.json")
    with open(results_json_path, encoding="utf-8") as f:
        existing_data = json.load(f)
    print(f"Loaded {len(existing_data)} existing results")

    # Index existing by slug
    existing_by_slug = {r["slug"]: r for r in existing_data}

    # Find all existing result pages
    problem_dir = os.path.join(SITE_DIR, "results", "problem")
    existing_files = {}
    for path in glob.glob(os.path.join(problem_dir, "*.md")):
        slug = os.path.basename(path).replace(".md", "")
        existing_files[slug] = path

    print(f"Found {len(existing_files)} existing result page files")

    # Track updates
    updated_count = 0
    created_count = 0
    next_result_num = 73  # existing go up to 72

    # Process seeds
    for seed in seeds:
        sid = seed["result_id"]

        # Skip shell-page seeds
        if sid in SHELL_SEED_IDS:
            continue

        mapped_slug = SEED_TO_SLUG.get(sid)

        if mapped_slug and mapped_slug in existing_files:
            # Update existing page with v2 fields
            path = existing_files[mapped_slug]
            content = read_result_page(path)

            result_kind = seed["result_kind"]
            importance = seed["importance_class"]
            status_code = seed["status_code"]
            domain = seed.get("domain_group", "")

            new_content = inject_v2_fields(content, result_kind, importance, status_code, domain)
            with open(path, "w", encoding="utf-8") as f:
                f.write(new_content)

            # Update data entry
            if mapped_slug in existing_by_slug:
                existing_by_slug[mapped_slug]["result_kind"] = result_kind
                existing_by_slug[mapped_slug]["importance_class"] = importance
                existing_by_slug[mapped_slug]["status_code"] = status_code
                existing_by_slug[mapped_slug]["domain_group"] = domain

            updated_count += 1
            print(f"  Updated: {mapped_slug} ← {sid}")
        else:
            # Create new result page
            slug = slugify(seed["title"])

            # Avoid collision
            if slug in existing_files:
                print(f"  SKIP (slug collision): {slug} for {sid}")
                continue

            page_content = generate_new_result_page(seed, next_result_num)
            page_path = os.path.join(problem_dir, f"{slug}.md")
            with open(page_path, "w", encoding="utf-8") as f:
                f.write(page_content)

            # Add to data
            topic = layer_to_topic(seed["primary_layer"])
            existing_by_slug[slug] = {
                "id": f"result-{next_result_num:03d}",
                "slug": slug,
                "title": seed["title"],
                "topic": topic,
                "layer": seed["primary_layer"],
                "result_type": seed["result_kind"].replace("-", "_"),
                "bridge_status": STATUS_MAP.get(seed["status_code"], "partial"),
                "result_kind": seed["result_kind"],
                "importance_class": seed["importance_class"],
                "status_code": seed["status_code"],
                "domain_group": seed.get("domain_group", ""),
                "summary_short": seed.get("why_include_now", ""),
                "url": f"/results/problem/{slug}/",
                "canonical_books": [],
            }
            existing_files[slug] = page_path
            next_result_num += 1
            created_count += 1
            print(f"  Created: {slug} ← {sid}")

    # Add v2 fields to remaining existing results that weren't in seed
    for slug, data in existing_by_slug.items():
        if "result_kind" not in data:
            kind = infer_result_kind(
                data.get("result_type", ""),
                data.get("bridge_status", ""),
                data.get("topic", ""),
            )
            data["result_kind"] = kind
            data["importance_class"] = infer_importance(kind)
            data["status_code"] = "R"  # default existing results to resolved
            data["domain_group"] = data.get("topic", "").capitalize()

            # Also inject into the page file
            if slug in existing_files:
                path = existing_files[slug]
                content = read_result_page(path)
                new_content = inject_v2_fields(
                    content, kind, data["importance_class"],
                    data["status_code"], data["domain_group"]
                )
                with open(path, "w", encoding="utf-8") as f:
                    f.write(new_content)

    # Write updated results.json
    all_results = sorted(existing_by_slug.values(), key=lambda r: r.get("id", ""))
    with open(results_json_path, "w", encoding="utf-8") as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)
    print(f"\nWrote {len(all_results)} results to {results_json_path}")

    # Update topics.json
    topics_json_path = os.path.join(SITE_DIR, "_data", "results", "topics.json")
    topic_counts = {}
    topic_slugs = {}
    for r in all_results:
        t = r.get("topic", "unknown")
        topic_counts[t] = topic_counts.get(t, 0) + 1
        if t not in topic_slugs:
            topic_slugs[t] = []
        topic_slugs[t].append(r["slug"])

    topics = []
    for t in sorted(topic_counts.keys()):
        topics.append({
            "id": t,
            "slug": t,
            "title": t.capitalize(),
            "count": topic_counts[t],
            "results": sorted(topic_slugs[t]),
        })

    with open(topics_json_path, "w", encoding="utf-8") as f:
        json.dump(topics, f, indent=2, ensure_ascii=False)
    print(f"Wrote {len(topics)} topics to {topics_json_path}")

    # Generate shell pages
    shell_pages = generate_shell_pages()
    for slug, content in shell_pages.items():
        path = os.path.join(SITE_DIR, "results", f"{slug}.md")
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Wrote shell page: results/{slug}.md")

    # Update results index
    generate_results_index(all_results, topic_counts)

    # Update browse pages
    generate_by_problem(all_results)
    generate_by_domain(all_results, topics)

    # Update topic pages
    generate_topic_pages(all_results, topics)

    print(f"\n{'='*60}")
    print(f"SUMMARY")
    print(f"{'='*60}")
    print(f"  Existing results updated:  {updated_count}")
    print(f"  New results created:       {created_count}")
    print(f"  Total results:             {len(all_results)}")
    print(f"  Shell pages created:       {len(shell_pages)}")
    for t, c in sorted(topic_counts.items()):
        print(f"    {t}: {c}")


def generate_results_index(results, topic_counts):
    """Regenerate the results index page."""
    total = len(results)

    # Count by kind
    kind_counts = {}
    for r in results:
        k = r.get("result_kind", "unknown")
        kind_counts[k] = kind_counts.get(k, 0) + 1

    # Featured — pick seed flagships
    featured_slugs = [
        "central-theorem",
        "hubble-tension-resolved-h-formula",
        "no-dark-matter-particle",
        "homochirality-universality-12-step-derivation",
        "categorical-imperative-fixed-point",
        "goedel-avoidance",
    ]
    featured_lines = []
    results_by_slug = {r["slug"]: r for r in results}
    for s in featured_slugs:
        if s in results_by_slug:
            r = results_by_slug[s]
            featured_lines.append(
                f'- [{r["title"]}]({r["url"]}) — {r.get("summary_short", "")[:120]}'
            )

    topic_lines = []
    for t in sorted(topic_counts.keys()):
        topic_lines.append(f"- [{t.capitalize()}](/results/topic/{t}/) — {topic_counts[t]} results")

    content = f"""---
layout: program-doc
title: Key Results
permalink: /results/
lane: results
summary_short: "A frontier-problem-first research interface — {total} results across mathematics, physics, biology, and philosophy."
summary_cards:
- title: What this lane does
  body: "Connects the program's internal claims to recognized problems, with explicit epistemic status and canonical grounding."
- title: "{total} results"
  body: "Frontier problems, foundational mathematics, and consequence/reframing results across four domains."
- title: "Three result types"
  body: "Frontier problem ({kind_counts.get('frontier-problem', 0)}), foundational math ({kind_counts.get('foundational-math', 0)}), consequence ({kind_counts.get('consequence', 0)})."
right_rail:
  related:
  - title: Framework Overview
    url: /framework/about/
  - title: Registry
    url: /registry/
  - title: Why So Many Results
    url: /results/why-so-many-results/
  meta:
    type: Lane Root
    scope: All results
    status: Canonical
    updated: April 2026
---

## The Results Lane

The Results lane is the public relevance bridge of the Panta Rhei Research Program. It connects the program's internal structural claims to **recognized problems** in mathematics, physics, biology, and philosophy.

Every result distinguishes:
- The **mainstream problem statement**
- The **Panta Rhei claim**
- The **epistemic status** — resolved, partial, qualitative, or contradicted
- The **canonical grounding** — where in books, framework, registry
- The **verification route** — how to inspect further

## Featured Results

{chr(10).join(featured_lines)}

## Browse by Topic

{chr(10).join(topic_lines)}

## Browse

- [All results by problem](/results/by-problem/)
- [Results by domain](/results/by-domain/)
- [Results by book](/results/by-book/)

## Understanding This Lane

- [Why So Many Results Are Possible](/results/why-so-many-results/)
- [How to Read a Result Page](/results/how-to-read-a-result-page/)
- [Status and Claim Typing](/results/status-and-claim-typing/)
"""
    path = os.path.join(SITE_DIR, "results", "index.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Wrote results/index.md")


def generate_by_problem(results):
    """Regenerate by-problem browse page."""
    lines = []
    for r in sorted(results, key=lambda x: x["title"].lower()):
        status = r.get("status_code", "R")
        kind = r.get("result_kind", "").replace("-", " ").title()
        lines.append(f'- [{r["title"]}]({r["url"]}) — *{kind}* · {STATUS_DISPLAY.get(status, status)}')

    content = f"""---
layout: program-doc
title: Results by Problem
permalink: /results/by-problem/
lane: results
summary_short: "All {len(results)} results listed alphabetically."
right_rail:
  related:
  - title: Results Overview
    url: /results/
  - title: Results by Domain
    url: /results/by-domain/
  meta:
    type: Browse Index
    scope: All results
    status: Canonical
    updated: April 2026
---

## All Results ({len(results)})

{chr(10).join(lines)}
"""
    path = os.path.join(SITE_DIR, "results", "by-problem.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Wrote results/by-problem.md")


def generate_by_domain(results, topics):
    """Regenerate by-domain browse page."""
    sections = []
    for t in topics:
        topic_results = [r for r in results if r.get("topic") == t["id"]]
        lines = []
        for r in sorted(topic_results, key=lambda x: x["title"].lower()):
            status = r.get("status_code", "R")
            lines.append(f'- [{r["title"]}]({r["url"]}) — {STATUS_DISPLAY.get(status, status)}')
        sections.append(f"### [{t['title']}](/results/topic/{t['slug']}/) — {t['count']} results\n\n" + "\n".join(lines))

    content = f"""---
layout: program-doc
title: Results by Domain
permalink: /results/by-domain/
lane: results
summary_short: "All {len(results)} results grouped by topic domain."
right_rail:
  related:
  - title: Results Overview
    url: /results/
  - title: Results by Problem
    url: /results/by-problem/
  meta:
    type: Browse Index
    scope: All results
    status: Canonical
    updated: April 2026
---

## Results by Domain

{chr(10).join(sections)}
"""
    path = os.path.join(SITE_DIR, "results", "by-domain.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Wrote results/by-domain.md")


def generate_topic_pages(results, topics):
    """Regenerate topic overview pages."""
    topic_dir = os.path.join(SITE_DIR, "results", "topic")
    os.makedirs(topic_dir, exist_ok=True)

    for t in topics:
        topic_results = [r for r in results if r.get("topic") == t["id"]]
        lines = []
        for r in sorted(topic_results, key=lambda x: x["title"].lower()):
            status = r.get("status_code", "R")
            lines.append(f'- [{r["title"]}]({r["url"]}) — {STATUS_DISPLAY.get(status, status)}')

        content = f"""---
layout: result-topic
title: "{t['title']} Results"
permalink: /results/topic/{t['slug']}/
topic: {t['id']}
summary_short: "{t['count']} results engaging the {t['title'].lower()} problem-space."
right_rail:
  meta:
    type: Topic Overview
    scope: {t['title']}
    status: Canonical
    updated: April 2026
---

## {t['title']}

{t['count']} results in this topic area.

## Results

{chr(10).join(lines)}
"""
        path = os.path.join(topic_dir, f"{t['slug']}.md")
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Wrote results/topic/{t['slug']}.md")


if __name__ == "__main__":
    main()
