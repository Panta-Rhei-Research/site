# CQNF Phase 2 — Deep Dive Assessment

**Date:** April 14, 2026
**Pages scored:** 97 (Tier 2 stratified sample)
**Combined with Phase 1:** 140 pages total (43 + 97)
**Framework:** CQNF v1.0

---

## Combined Site-Level Metrics (140 pages)

| Metric | Phase 1 (43) | Phase 2 (97) | Combined (140) |
|--------|:------------:|:------------:|:--------------:|
| **Mean CQNF** | 21.3 | 16.7 | **18.1** |
| **Median CQNF** | 22 | 17 | **18** |
| **Floor score** | 16 | 12 | **12** |

### Tier Distribution (140 pages)

| Tier | Count | % |
|------|:-----:|:-:|
| **Frontier (22-25)** | 32 | 22.9% |
| **Strong (18-21)** | 35 | 25.0% |
| **Adequate (14-17)** | 60 | 42.9% |
| **Thin (10-13)** | 13 | 9.3% |
| **Critical (5-9)** | 0 | 0% |

### Dimension Means (140 pages)

| Dimension | Mean | Interpretation |
|-----------|:----:|----------------|
| **TL (Trust Language)** | 3.79 | Strongest — consistent across all types |
| **RO (Reader Orientation)** | 3.59 | Good — layouts do structural work |
| **NC (Narrative Coherence)** | 3.36 | Moderate — cross-linking improved in Phase 3 |
| **PS (Prose Substance)** | 3.24 | Weakest — many generated/stub pages |
| **CQ (Craft Quality)** | 3.21 | Weakest — tracks with PS |

---

## Phase 2 Batch Results

### Batch A: Book + Archived Pages (14 pages)

| Metric | Value |
|--------|-------|
| Mean CQNF | 18.5 |
| Frontier | 2 (14%) |
| Strong | 4 (29%) |
| Adequate | 8 (57%) |
| Floor | 16 |

**Key finding**: Book II and V are Frontier (23); Book VI is the only 2nd-ed book below baseline (PS=3, CQNF 17). Archived pages cluster at 16-17 — structurally limited but acceptable.

### Batch B: Part + Chapter Pages (28 pages)

| Metric | Value |
|--------|-------|
| Mean CQNF | 18.5 |
| Frontier | 3 (11%) |
| Strong | 13 (46%) |
| Adequate | 12 (43%) |
| Floor | 14 |

**Key finding**: Book II dominates (3 Frontier pages). Book VI is weakest (floor at 14). Two chapter pages have PS=2 (stubs). Part pages lack prev/next navigation (layout gap).

### Batch C: Result Pages (20 pages)

| Metric | Value |
|--------|-------|
| Mean CQNF | 18.6 |
| Frontier | 5 (25%) |
| Strong | 9 (45%) |
| Adequate | 5 (25%) |
| Thin | 1 (5%) |
| Floor | 12 |

**Key finding**: Resolved (R) results average 22.0 — excellent. Not-addressed (N) results average 14.2 — expected stubs. One Thin page: `no-hawking-radiation` at 12 (near-duplicate of `no-bh-evaporation`). Trust Language is the standout (mean 4.30).

### Batch D: Framework Modules + Bibliography (20 pages)

| Metric | Value |
|--------|-------|
| Mean CQNF | 13.6 |
| Adequate | 11 (55%) |
| Thin | 9 (45%) |
| Floor | 13 |

**Critical finding**: All 10 framework modules score 13 (Thin) — they have rich frontmatter but only ~35 words of body prose. These are the intellectual core of the site but present as metadata-rendered stubs. Bibliography entries are flat but acceptable at 14.

### Batch E: Changelog + Impact + Registry (15 pages)

| Metric | Value |
|--------|-------|
| Mean CQNF | 17.1 |
| Strong | 5 (33%) |
| Adequate | 10 (67%) |
| Floor | 14 |

**Key finding**: Impact portfolios are uniformly Strong (all 5 at 20). Registry dashboards are at the 14-point floor (zero prose, pure data tables). Changelog entries are functional at 15-17.

---

## Pages Below Threshold

### Thin Tier (CQNF 10-13) — 13 pages

| Page | Type | CQNF | Primary Issue |
|------|------|:----:|---------------|
| mathematics-coherence-kernel | Framework module | 13 | Stub body (~35 words) |
| mathematics-central-theorem | Framework module | 13 | Stub body |
| mathematics-earned-topos | Framework module | 13 | Stub body |
| physics-fine-structure | Framework module | 13 | Stub body |
| physics-gravity-earned | Framework module | 13 | Stub body |
| life-genetic-code | Framework module | 13 | Stub body |
| life-seven-hallmarks | Framework module | 13 | Stub body |
| metaphysics-categorical-ethics | Framework module | 13 | Stub body |
| metaphysics-ontology | Framework module | 13 | Stub body |
| physics-cmb-pipeline | Framework module | 14 | Slightly better (TL=4) |
| no-hawking-radiation | Result (C) | 12 | Near-duplicate, minimal prose |

**Root cause for framework modules**: The build pipeline produced rich metadata but only stub body prose. The Overview section repeats the frontmatter thesis. These need 300-500 words of authored prose each.

### At Floor (CQNF = 14) — 12 pages

- 5 registry dashboards (zero prose, pure data)
- 5 not-addressed result stubs (expected — PS=2 by design)
- 2 bibliography entries (template editorial notes)

---

## User Journey Scores

| Journey | Score | Assessment |
|---------|:-----:|-----------|
| **J1: First Encounter** | **5** | Homepage → About → Why → Framework staircase: each transition natural, staircase numbering guides forward |
| **J2: Skeptic Audit** | **4** | Verify → Results → Registry works well; but framework modules (the technical depth) are stubs |
| **J3: Book Buyer** | **4** | Publications → Book → Chapters → Amazon: clear path; some chapter pages are thin |
| **J4: Scholar/Citer** | **5** | Cite → DOI → Zenodo → Bibliography → BibTeX: complete and consistent |
| **J5: Engagement** | **5** | Engage → Follow → Subscribe → Notes: frictionless, non-promotional, Buttondown integrated |

---

## Systemic Findings

### 1. Framework modules are the single biggest quality gap
9 of 10 sampled modules are Thin (13/25). These are supposed to be the intellectual core — the bridge between the conceptual staircase (which is Frontier-tier) and the technical registry. Instead, they're metadata stubs. **This is the #1 remediation priority.**

### 2. Trust Language remains the site's signature strength
TL is the highest-scoring dimension in every batch except Batch D. Even not-addressed result stubs score TL=4 for honest "no derivation yet" statements. The site's epistemic discipline is genuine and consistent.

### 3. The quality gap is prose substance, not structure
RO is consistently propped up by excellent layout templates. The structural shell does heavy lifting. Where pages fall below threshold, the cause is almost always PS (not enough authored prose) rather than poor design or broken navigation.

### 4. Book II is the quality exemplar; Book VI is the weakest
Book II has 4 Frontier-tier pages across books, parts, and chapters. Book VI has the weakest scores across every level. This likely reflects the maturity of the underlying content in the canonical books.

---

## Remediation Roadmap

### Wave 1 (Critical — 10 framework modules)
Expand all 60 framework modules from stubs to 300-500 words of authored prose. This is the largest content investment needed. Target: CQNF 19+ per module.

### Wave 2 (High — result + publication pages)
- Fix `no-hawking-radiation` (merge or expand)
- Expand 2 PS=2 chapter stubs
- Expand Book VI book page to PS=4
- Add scope labels to chapter/part summaries

### Wave 3 (Medium — reference pages)
- Add introductory prose to 5 registry dashboards
- Enrich 10+ bibliography editorial notes beyond templates
- Expand thinnest changelog entry

### Wave 4 (Layout improvements)
- Add prev/next navigation to publication-part layout
- Add "Related Results" component to result-page layout
- Add book-specific summary_short to registry dashboards

---

## Targets for Next Phase

| Metric | Current (140 pages) | Target |
|--------|:-------------------:|:------:|
| Mean CQNF | 18.1 | >= 19.0 |
| Floor score | 12 | >= 14 |
| Thin-tier pages | 13 (9.3%) | 0 (0%) |
| PS mean | 3.24 | >= 3.8 |
| Framework module mean | 13.1 | >= 19.0 |
