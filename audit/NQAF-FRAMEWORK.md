# Narrative Quality Assessment Framework (NQAF) v1.0

**Panta Rhei Research Program — Site Narrative Audit Framework**
**Date:** April 2026
**Companion to:** CQNF v1.0 (Content Quality & Narrative Flow)

---

## Purpose

The CQNF framework evaluates **per-page content quality** (bottom-up): prose substance, reader orientation, narrative coherence, trust language, craft quality. The site scores ~20.5/25 mean CQNF with all critical pages above threshold.

The NQAF evaluates whether the **site as a whole tells a coherent story** (top-down). It answers one master question:

> **Does this website successfully communicate what the Panta Rhei Research Program is, what it claims, how those claims can be inspected, and why a serious reader should engage — without overpromising, underdelivering, or losing anyone along the way?**

A site can score well on CQNF and poorly on NQAF (great pages, bad story) or vice versa (great story, thin pages). Both must pass for release.

---

## Eight Dimensions (scored 1–5 each, total /40)

### D1 — First-Contact Promise (FCP)

**What it measures:** Can a new visitor understand what this is, what it claims, and what posture it takes — within 30 seconds of landing?

| Score | Criteria |
|:-----:|----------|
| 5 | Homepage delivers program identity, epistemic posture, scope, verification commitment, and a clear next step within one scroll. No jargon without context. A journalist, a physicist, and a philosopher each know where to go. |
| 4 | Promise is clear and credible but one audience segment has a weaker entry point, or one key element (scope, posture, verification) is buried below the fold. |
| 3 | Visitor understands it is a research program, but cannot articulate what makes it different from any other theory-of-everything attempt within 30 seconds. |
| 2 | Homepage is cluttered, overlong, or leads with jargon. The core promise is present but lost in noise. |
| 1 | Homepage fails to communicate what the site is. New visitors bounce without understanding the research program or its claims. |

**Acceptance test:** Show the homepage to 3 imagined readers (journalist, mathematician, general intellectual). Can each state in one sentence what the program is and where they'd click next?

---

### D2 — Audience Routing Precision (ARP)

**What it measures:** Does each target audience segment find its optimal entry point within 2 clicks from the homepage?

**Nine audience segments:**
1. First-time visitor / intellectual generalist
2. Skeptical auditor / technical deep-diver
3. Domain expert (mathematician, physicist, biologist, philosopher)
4. Book buyer / canonical text reader
5. Scholar / citation user
6. Journalist / media professional
7. Institutional stakeholder / impact-focused reader
8. Formal verification enthusiast / code auditor
9. Follower / ongoing engagement participant

| Score | Criteria |
|:-----:|----------|
| 5 | All 9 segments reach their optimal lane within 2 clicks. Entry points are explicitly named or visually distinct. No segment requires guessing. |
| 4 | 7–8 segments routed well; 1–2 segments require a third click or a non-obvious path. |
| 3 | 5–6 segments routed well; remaining segments may land in a generic page that doesn't speak to their needs. |
| 2 | Routing depends on already knowing the site structure. Generic navigation labels hide the right content. |
| 1 | Most visitors cannot find content relevant to their role without extensive exploration. |

**Acceptance test:** For each of the 9 segments, trace the click path from homepage to their target page. Count clicks. Score 5 only if all are ≤ 2.

**Checklist:**
- [ ] Journalist → Media Kit (≤ 2 clicks)
- [ ] Skeptic → Verify / Results → specific result (≤ 2 clicks)
- [ ] Mathematician → Framework / Results by Domain → Mathematics (≤ 2 clicks)
- [ ] Book buyer → Publications → Book page (≤ 2 clicks)
- [ ] Scholar → Cite / Bibliography (≤ 2 clicks)
- [ ] Impact reader → Impact → Portfolio (≤ 2 clicks)
- [ ] Verification auditor → Verify → TauLib (≤ 2 clicks)
- [ ] Follower → Engage → Subscribe (≤ 2 clicks)
- [ ] General intellectual → Framework About → What the Tau Framework Is (≤ 2 clicks)

---

### D3 — Master Narrative Fidelity (MNF)

**What it measures:** Do downstream pages reinforce or contradict the five master narratives that the homepage establishes?

**Five master narratives (from homepage):**
1. **Constrained kernel** — one framework, 5 generators, 7 axioms, 1 operator, zero free parameters
2. **Four-layer enrichment** — mathematics → physics → life → metaphysics, each a genuine enrichment
3. **Typed claims with epistemic honesty** — every claim carries a scope label, nothing hidden
4. **Public verification** — books, Lean formalization, registry, predictions, guided tours
5. **Conditional impact** — "if the framework holds" language, not premature certainty

| Score | Criteria |
|:-----:|----------|
| 5 | Every lane root and world-readout page explicitly reinforces at least 2 of the 5 master narratives. No downstream page contradicts any. The site feels like one coherent argument, not 9 disconnected sections. |
| 4 | Master narratives are reinforced on lane roots but some deep pages feel disconnected from the overarching story. |
| 3 | 3–4 master narratives are well-served. One or two are only present on the homepage and not echoed downstream. |
| 2 | Master narratives feel like marketing copy on the homepage but are not operationalized in lane content. |
| 1 | Downstream content actively contradicts the homepage's promises (e.g., untyped claims, hidden scope, hype language). |

**Acceptance test:** Read 5 random deep pages (one per lane). For each, check: does it reference the constrained kernel? Does it use typed claims? Does it maintain conditional language where appropriate? Does it point to verification? Score 5 only if all 5 pass on all applicable criteria.

---

### D4 — Epistemic Transparency Architecture (ETA)

**What it measures:** Is the distinction between proven/derived/conjectural/metaphorical maintained consistently across the entire site?

| Score | Criteria |
|:-----:|----------|
| 5 | Every substantive claim carries explicit or contextually clear epistemic status. Scope labels (established, tau-effective, conjectural, metaphorical) are used where they belong. The "What This Page Does Not Claim" discipline from the prologue is echoed on pages that need it. No page can be quoted out of context as claiming more than it does. |
| 4 | Scope discipline holds on all results and world-readout pages. A few framework or impact pages make claims without explicit scope markers. |
| 3 | Results lane is well-typed, but other lanes sometimes slip into less disciplined language. |
| 2 | Epistemic status is applied inconsistently. Some pages sound like marketing; others are properly scoped. |
| 1 | The site makes unqualified claims that a skeptical reader would flag as dishonest. |

**Acceptance test:** Read the 11 impact portfolio overviews. Does each maintain conditional ("if") language? Read 5 random world-readout pages. Does each distinguish internal-Tau claims from orthodox-bridge claims? Score 5 only if zero violations found.

**Checklist:**
- [ ] All 234 result pages carry status_code (R/P/Q/C/N)
- [ ] All world-readout pages use "on the program's reading" or equivalent qualifier
- [ ] Impact lane prefixes claims with "if the framework holds" or equivalent
- [ ] Framework modules distinguish what is formalized (Lean) from what is narrative exposition
- [ ] Prologue pages separate formal-system claims from world-readout claims from bridge claims
- [ ] No page uses "we have proven" without specifying proven-where (in Tau, in Lean, in the orthodox sense)

---

### D5 — Lane Purpose Clarity (LPC)

**What it measures:** Does each lane have a clear, distinct, non-overlapping narrative purpose?

| Score | Criteria |
|:-----:|----------|
| 5 | Every lane root page answers "What is this lane for?" and "Who is it for?" within its first paragraph. No two lanes overlap in purpose. |
| 4 | 7–8 lanes are clearly distinct. 1–2 have some overlap. |
| 3 | Lane roots are clear, but the relationship between lanes is not spelled out. |
| 2 | Some lanes feel like they exist for structural reasons rather than serving a clear reader need. |
| 1 | Multiple lanes are confusingly similar. |

**Expected lane purposes:**

| Lane | Purpose |
|------|---------|
| Homepage | What this program is and why it matters |
| Research Program | What kind of research object this is |
| Framework | How the formal architecture works |
| Results | What the framework claims to solve |
| Publications | Where the full argument is published |
| Verify | How to machine-check the claims |
| Impact | What could change if the framework holds |
| Registry | The formal theorem/definition graph |
| Bibliography | What the program cites and knows |
| Engage | How to follow, support, and contact |
| Cite | How to reference this academically |
| Media Kit | Resources for journalists and reviewers |

---

### D6 — Discovery Completeness (DC)

**What it measures:** Can every key piece of content be found through at least 2 distinct paths?

| Score | Criteria |
|:-----:|----------|
| 5 | Every key page is reachable through (a) left-rail navigation, (b) at least one in-content cross-link, and (c) either search or a browse index. No content is orphaned. |
| 4 | Nearly all content is multi-path discoverable. A few deep pages are only reachable through one path. |
| 3 | Lane roots and major pages have good discoverability. Deeper pages primarily single-path. |
| 2 | Content is discoverable through navigation only — no in-content cross-linking. |
| 1 | Significant content is hidden from both navigation and search. |

**Acceptance test:** Pick 10 random deep pages. For each, identify all paths to reach it. Score 5 only if all 10 have ≥ 2 paths.

---

### D7 — Narrative Flow & Transitions (NFT)

**What it measures:** Do readers naturally progress from orientation to understanding to engagement?

| Score | Criteria |
|:-----:|----------|
| 5 | Clear narrative arc: Orientation (homepage/research-program) → Understanding (framework/world-readout) → Inspection (results/verify/registry) → Engagement (publications/engage/impact). Transition pages explicitly bridge between layers. Every page tells the reader what to read next. |
| 4 | Narrative arc present but one transition is weak. |
| 3 | Individual lanes well-structured internally, but cross-lane flow is not guided. |
| 2 | Pages end without clear next steps. Reader frequently hits dead ends. |
| 1 | No discernible narrative flow. Each page is isolated. |

**Acceptance test:** Follow the enrichment ladder path: Homepage → Prologue → Physics Readout → Life Readout → Metaphysics Readout → Result Atlas. Does each transition feel natural?

---

### D8 — Tone & Voice Coherence (TVC)

**What it measures:** Does the intellectual voice hold consistently across all surfaces?

| Score | Criteria |
|:-----:|----------|
| 5 | Every page sounds like the same disciplined research voice. Serious but not forbidding, precise but not pedantic, ambitious but not grandiose. No page reads like a sales pitch. |
| 4 | Voice consistent on 90%+ of pages. One or two pages slightly shift register. |
| 3 | Core content has strong voice. Utility pages feel like a different site. |
| 2 | Tone varies noticeably across lanes. |
| 1 | No consistent voice. |

**Acceptance test:** Read one page from each of the 4 world-readout clusters + homepage + media kit + one result page. Does the voice hold?

---

## Quality Tiers

| Tier | Score Range | Meaning |
|------|:-----------:|---------|
| **Frontier** | 35–40 | World-class narrative architecture — the site is itself an argument for the program's coherence |
| **Strong** | 28–34 | Professional, well-architected — serious readers can navigate and evaluate confidently |
| **Adequate** | 21–27 | Functional but with narrative gaps — some audiences underserved |
| **Weak** | 14–20 | Significant storytelling problems — undermines credibility |
| **Critical** | 8–13 | Fundamental narrative failure |

---

## Release Acceptance Criteria

- **Mean NQAF ≥ 32** (Strong-Frontier boundary)
- **No dimension below 3** (no narrative failure on any axis)
- **D4 (Epistemic Transparency) ≥ 4** — non-negotiable
- **D1 (First-Contact Promise) ≥ 4** — the homepage must work
- **All 9 audience routing paths pass** the 2-click test (D2 checklist)

---

## Scoring Method

**Evaluator:** Walk the live site (not source files). Score each dimension using the rubrics above. Record evidence for each score.

**Scope:** Score the site as a unified narrative experience. The question is always: does this contribute to or detract from the site's ability to tell its story?

**Companion framework:** CQNF v1.0 (per-page quality, bottom-up). Both must pass for release.
