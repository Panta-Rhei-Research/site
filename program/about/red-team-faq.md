---
layout: program-doc
title: "Red-team FAQ — The Hardest Questions, Answered"
nav_order: 11
lane: program
v2_lane: program
section: about-the-program
summary_short: "The skeptical questions a serious first-pass reviewer asks first, each answered honestly with pointers to the load-bearing evidence. Synthesized from independent frontier-LLM first-pass assessments — including a full re-run of our own published assessment protocols against the live program in May 2026."
right_rail:
  related:
  - title: Standing in the Inquiry of Being
    url: /program/about/standing-in-the-inquiry-of-being/
  - title: Categorical Ontology
    url: /program/about/categorical-ontology/
  - title: Scope, Status & Scrutiny
    url: /program/about/scope-status-and-scrutiny/
  - title: Independence, Scope & Scrutiny
    url: /program/about/independence-scope-and-scrutiny/
  - title: What the Program Refuses
    url: /agenda/what-the-program-refuses/
  - title: Release Manifest
    url: /verify/release-manifest/
  - title: Prediction Timing Ledger
    url: /results/predictions/timing/
  meta:
    type: "FAQ"
    scope: "Program-wide"
    status: "Canonical"
    updated: "May 2026"
---

Three frontier-LLM first-pass assessments were run on the public Panta Rhei Research surface in April 2026. Their red-team question lists converged on roughly the same ten questions. In May 2026 the program re-ran its own [published assessment protocols]({{ '/verify/assessment-protocols/llm-assisted/' | relative_url }}) against the live site — one series-level dossier plus four expert-domain dossiers (pure mathematics, particle physics, formal methods, philosophy of mind). The new dossiers surfaced ~50 additional skeptical framings; this FAQ now incorporates the ones that materially sharpen the original ten and adds three new entries (#11–#13) for high-signal questions the original ten did not yet cover.

This page answers each question directly, with pointers to the load-bearing evidence. No question has been softened or reframed; where the honest answer is "partial" or "not yet," that is what this page says.

The assessment workflow itself is inspectable through [Assessment Protocols]({{ '/verify/assessments/' | relative_url }}), the [dossier schema]({{ '/verify/assessments/dossier-schema/' | relative_url }}), the [three-gate rubric]({{ '/verify/assessments/three-gate-rubric/' | relative_url }}), and the pinned [Release Manifest]({{ '/verify/release-manifest/' | relative_url }}). These links document the current public evidence surface; they are not a substitute for external expert review.

For current claim counts and status distribution, see the [Release Manifest]({{ '/verify/release-manifest/' | relative_url }}) and [Results catalogue]({{ '/results/' | relative_url }}). This FAQ answers the structural risk, not mutable count totals.

The accountability posture behind this FAQ is stated in [Independence, Scope, and Scrutiny]({{ '/program/about/independence-scope-and-scrutiny/' | relative_url }}): independence increases the duty to expose evidence, status, and failure surfaces.

For the philosophical lineage and inquiry posture behind the program, see [Standing in the Inquiry of Being]({{ '/program/about/standing-in-the-inquiry-of-being/' | relative_url }}). This FAQ remains the first-pass objection surface; the charter is not a substitute for verification.

## 1. Is ι<sub>τ</sub> = 2/(π+e) forced or fitted? {#is-iota-tau-fitted-or-forced}

**Answer: structurally forced, not fitted.**

The value ι<sub>τ</sub> = 2/(π+e) ≈ 0.3413 is a theorem of the kernel, not a parameter chosen to match any experiment. The seven axioms (K0–K6) and the five generators (α, π, γ, η, ω) define a kernel whose unique calibration constant is forced by a compactness-and-consistency argument in Book I. The form of the constant (why π+e in the denominator and not π·e or π²+e²) is the content of the uniqueness theorem, not a coincidence or a design decision. **The framework is falsified if ι<sub>τ</sub> is shown to be non-unique given the axioms, or if the axioms are shown to be inconsistent.** This is not a soft target: the entire {% include release-metric.html id="predictions.records" %}-prediction ledger stands or falls on ι<sub>τ</sub> being the value it is, so any slack here collapses the framework.

**Look-elsewhere discipline.** A fair-minded skeptic asks: of all "natural-looking" combinations of {2, π, e, φ, …}, how many land within ε of an interesting target? The published derivation is intended to short-circuit this concern by *proving* the closed form rather than searching for it. The review burden is on the proof in [Hinge 3]({{ '/corpus/foundational-hinges/master-constant-iota-tau/' | relative_url }}) and the linked research paper, not on a numerical coincidence — and any reviewer who can construct an alternative kernel-consistent value is invited to publish the counter-derivation.

Primary review artifact: [Hinge 3 — The Master Constant iota_tau]({{ '/corpus/foundational-hinges/master-constant-iota-tau/' | relative_url }}), with the citable research paper [The Master Constant iota_tau]({{ '/publications/research-papers/master-constant-iota-tau/' | relative_url }}), [PDF]({{ '/assets/pdfs/research-papers/research-paper-2026-04-27-master-constant-iota-tau.pdf' | relative_url }}), and DOI [10.5281/zenodo.19820352](https://doi.org/10.5281/zenodo.19820352). The downstream empirical accounting is kept separate on the [Prediction Timing Ledger]({{ '/results/predictions/timing/' | relative_url }}).

## 2. Are the predictions a priori or post-dictions?

**Answer: structurally a priori; historically category-mixed; the per-prediction split is published.**

As of the April 2026 public release manifest, the {% include release-metric.html id="predictions.records" %} predictions are *structurally* a priori because they flow algebraically from ι<sub>τ</sub>, which is kernel-fixed. *Historically*, they split into three categories — and the [Prediction Timing Ledger]({{ '/results/predictions/timing/' | relative_url }}) labels each entry as one of:

1. **Retro-consistency post-dictions** of pre-existing measured constants (e.g. n<sub>s</sub>, Ω<sub>Λ</sub>, h, S<sub>8</sub>, Y<sub>p</sub> — values that already had Planck/DESI/BBN central measurements when the framework was built; these are honest postdictions, not prophecies).
2. **Forward commitments on open empirical tensions** — predictions taking one side of an active disagreement (Hubble H<sub>0</sub>, W mass, muon g−2, S<sub>8</sub>); falsifiable if the tension resolves to the other side.
3. **Genuine forward predictions on not-yet-measured quantities** — CMB-S4 r ≈ 0.0136, neutrino mass sum, proton stability, 0νββ at τ-predicted half-life, no magnetic monopoles, no SUSY partners.

The framework does not claim per-prediction pre-registration timestamps for category 1 (it does not have dated archival records predating measurement). The strongest evidential weight comes from category 3, and from any category-2 commitment that subsequently resolves the right way. **A reviewer wanting to audit specific predictions should open the [Prediction Timing Ledger]({{ '/results/predictions/timing/' | relative_url }}) and check the per-row category label rather than treat the {% include release-metric.html id="predictions.records" %}-entry catalogue as uniform.**

## 3. Does TauLib introduce custom `axiom` declarations beyond Mathlib's trusted base?

**Answer: yes — 3 custom axioms, each named, documented, and per-theorem auditable.**

The pinned TauLib release (see [Release Manifest]({{ '/verify/release-manifest/' | relative_url }})) contains **3 custom `axiom` declarations**, all in Book III spectral-structure territory: `bridge_functor_exists`, `spectral_correspondence_O3`, and `grand_grh_adelic`. All 3 are named in the [Custom Axioms inventory]({{ '/verify/custom-axioms/' | relative_url }}) with explicit scope labels. A prior v1 release shipped a fourth axiom `central_theorem_physical : True` in Book IV which was retired in `peer-review-fixes-v1` (2026-04-19) as a no-op (`True` is inhabited by `trivial`).

**Per-theorem dependency audit.** Every `#print axioms` invocation on any theorem will surface these three if they participate in the proof chain. The driver `TauLib/Meta/PrintAxioms.lean` runs the full audit; the `verify/` lane does *not* yet embed the literal `#print axioms` output for every headline theorem on the public page (this is a known gap and is on the verify-lane polish backlog). A formal-methods reviewer cloning at the pinned commit can run the audit locally in minutes — see the [TCB disclosure]({{ '/verify/tcb/' | relative_url }}) for the complete trusted-base inventory and the `native_decide` accounting (~1,824 sites; this extends the TCB to the Lean compiler + LLVM toolchain for those theorems).

**Mathlib import surface.** TauLib's policy is "tactics only" — simp, omega, ring, aesop, decide — and **does not import Mathlib mathematical content modules** (`Mathlib.Algebra.*`, `Mathlib.Data.*`, `Mathlib.CategoryTheory.*` are not in the import graph). A reviewer can grep the import lines of the pinned commit to verify; the [filter-rules page]({{ '/verify/filter-rules/' | relative_url }}) explains the policy and how it interacts with status counting.

## 4. Is τ-internal P=NP the same question as Clay's P vs NP?

**Answer: no. Explicitly and intentionally.**

The τ-admissibility collapse theorem (τ-P<sub>adm</sub> = τ-NP<sub>adm</sub>) states that within τ's E₂-native computational model (the τ-Tower Machine), there is no separation between polynomial-time and nondeterministic-polynomial-time classes. This is **not** a resolution of the Clay Millennium Problem, which concerns separation in the classical Turing-machine model. The framework explicitly flags this scope gap: the two formulations address different computational substrates, and the bridge between them is marked "qualitative" (status Q) rather than "resolved" (status R). See the [Millennium & Langlands briefing]({{ '/results/fields/millennium-langlands/' | relative_url }}) for the scope-by-scope breakdown.

## 5. Are the Millennium resolutions Clay-valid formulations?

**Answer: only one — Poincaré. The other six are τ-internal formulations with explicit bridge gaps.**

Of the seven Millennium problems, only the **Poincaré Conjecture** is solved in a form aligned with the Clay statement (via Perelman's Ricci-flow proof, re-read in τ-language). For the other six — Riemann, P vs NP, Yang-Mills, Navier-Stokes, Hodge, BSD — τ provides **framework-internal formulations** with published agreement at the structural level, but the bridge to the Clay statement is marked as an **open conjecture** on every relevant claim page. The Millennium briefing shows each claim with its honest status code (Partial / Qualitative / Not Addressed), no resolution inflation. The framework is **not** claiming Clay prize eligibility for six of these seven.

**The Riemann Hypothesis case in particular.** The Lean axiom `grand_grh_adelic` follows the explicit *compute-then-axiomatize* pattern: a finite verification is performed, and the universal statement is then asserted as an axiom. Modulo the bridge to the standard adelic formulation, this means the framework's downstream consequences are **conditional on GRH**, not a proof of GRH. We state this as such on the [Custom Axioms]({{ '/verify/custom-axioms/' | relative_url }}) page. The same compute-then-axiomatize pattern applies to `spectral_correspondence_O3` and `bridge_functor_exists`. Reviewers wanting to discharge any of these axioms (or show them inconsistent) are invited to publish the result.

## 6. How does the framework constrain "metaphysics" without diluting the typing discipline?

**Answer: by the No Forced Stance theorem (VII.T47), which is a theorem of the framework that explicitly bounds what τ can and cannot establish.**

Book VII proves a meta-theorem: **τ cannot force a stance on the ω-germ question**. Any such stance belongs to the "commitment register," not to proof. This is not a disclaimer — it is a load-bearing theorem inside the formal system that marks exactly where proof ends and commitment begins. The metaphysics claims on the site (Categorical Imperative, Beauty as structural invariance, Problem of Universals, etc.) are either (a) structurally derived theorems with formal proofs in Book VII, or (b) explicitly labeled as commitments. The [Foundational Philosophy briefing]({{ '/results/fields/philosophy-foundational/' | relative_url }}) makes this separation visible. The typing discipline is preserved because the *theorem vs commitment* boundary is itself a theorem.

## 7. Are there topological or set-theoretic paradoxes at scale?

**Answer: addressed through five named mechanisms, but the claim itself is part of the review burden.**

The framework is Gödel-aware, not Gödel-dogmatic. It claims to avoid certain hypotheses under which standard incompleteness or continuum problems arise, but that claim itself is part of the review burden. The relevant question is whether the formal core has the arithmetic strength and proof-theoretic properties required for Gödel-style limits to apply, and if so what follows. The program may not ignore the issue either way.

Book I proves a **Gödel-avoidance result** via five named mechanisms (Hyperfactorization, Tower Separation, Boundary Constraint, Orbit Directedness, Carrier Closure). The claim is not that Gödel's theorems are false in τ — it is that τ does not meet the conditions under which they apply. Similarly, the framework treats **Cantor's diagonal argument as inapplicable** in τ because it refuses the unrestricted self-application the argument requires, and **ω is the unique infinity** in τ (no cardinal hierarchy). These are stated as theorems inside τ; whether they discharge the meta-logical burden is a question for external review. The framework also contains an explicit **Contradicted-status claim** on ZFC Identity Slippage — τ rejects ZFC's treatment of identity under the Axiom of Choice as structurally unstable. See the [Foundations, Logic & CS briefing]({{ '/results/fields/foundations-logic/' | relative_url }}) for the full set.

## 8. Is there a semantic gap between the prose in the books and the Lean formalization?

**Answer: the registry ID discipline is designed to catch exactly this; the gap is minimized but not closed to zero, and Book VI/VII formalization is partial.**

Every claim page on the site carries a **registry ID** (e.g., `II.T40`, `VI.D44`) that points to a specific entry in the Lean-structured registry. Every Lean theorem that is formalized has a docstring naming the registry ID it proves, and every registry entry with formalization status "formalized" has a corresponding Lean theorem. This is the **traceability chain** that closes the prose↔Lean gap for formalized claims. For claims with formalization status "planned" (notably most of Book VI and Book VII methodological claims), the prose stands and the Lean theorem does not yet exist. The **Release Manifest** makes this per-book status explicit.

**Book VI–VII specifically.** Several Book VI/VII Lean modules — particularly the Mind/Consciousness modules and the four-register Reg_E/P/D/C declarations in Book VII — currently take a *bookkeeping* shape: `structure` definitions whose fields default to `true : Bool`, with associated "theorems" that reduce to `rfl` over those defaults. We do not present these as substantive derivations of phenomenal content; they are scaffolding declarations whose role is to fix the namespace and the type signatures while the substantive formalization is still being authored. The corresponding Challenge Responses and result pages mark these claims as "partially addressed" or "structurally constrained," not "internally addressed." A reviewer opening a load-bearing Book VI/VII claim should expect to find scaffolding plus prose, not yet a reduced-to-`rfl`-of-substance theorem; the registry status reflects this, and the [SCL Mind/Consciousness/Self/Agency cluster]({{ '/agenda/structural-challenge-ledger/metaphysics/mind-consciousness-self-agency/' | relative_url }}) is the canonical accountability surface.

An auditor opening any three headline claim IDs and following them to their Lean theorem (and running `#print axioms` on each) is the diagnostic check that validates the chain end-to-end. We recommend doing this for at least one Book II claim (mature formalization) and one Book VI/VII claim (partial formalization) to see the contrast directly.

## 9. Is the claim catalogue inflated by relabeling or redefinition?

**Answer: no. The typing discipline exposes rather than hides.**

The catalogue is enumerated in the [Release Manifest]({{ '/verify/release-manifest/' | relative_url }}) and the [Results catalogue]({{ '/results/' | relative_url }}); for current totals and per-status breakdowns, follow those routes rather than relying on prose figures here. Claims are grouped by bridge status:

- **Internally addressed (R)** — full τ-internal theorem with formal proof chain closed to the orthodox public formulation
- **Internal** — τ-internal structural readout (no external bridge target; most metaphysics + many biology entries)
- **Partial (P)** — τ-internal result with explicit conjectural bridge gap
- **Qualitative or Not Addressed (Q/N)** — non-quantitative or unresolved
- **Contradicted (C)** — framework takes a falsifiable opposing position (No Hawking Radiation, No Axion Needed, Not MOND, Panpsychism Excluded, ZFC Identity Slippage)

The typing discipline *surfaces* Partial, Qualitative, Contradicted, and Not-Addressed claims rather than reclassifying them as internally addressed. **A framework that hides failures compresses its catalogue; the τ framework deliberately expands its catalogue to include claims where it concedes ground.**

**Where redefinition risk is highest.** Book VI (life predicate) and Book VII (consciousness, Reg_C commitment register, "consciousness as global section") are where the derivation-vs-redefinition distinction is most load-bearing — and a fair-minded reviewer should treat the `Commitment` structures and the four-register declarations as *stipulations of vocabulary* rather than reductive accounts until the substantive formalization is published. The relevant Challenge Responses — for example [Hard Problem of Consciousness]({{ '/results/challenge-responses/metaphysics/mind-consciousness-self-agency/hard-problem-consciousness/' | relative_url }}) — mark this as "partially addressed" specifically because we acknowledge the bridge from categorical structure to phenomenal experience is not closed. See also Q12 below for the bookkeeping-shaped Lean theorem concern, and Q13 for the hard-problem-relocation concern.

## 10. What single result could falsify the entire framework?

**Answer: CMB-S4 measurement of r inconsistent with ι<sub>τ</sub><sup>4</sup> ≈ 0.0136 at ≥5σ.**

The framework commits in writing to r = ι<sub>τ</sub><sup>4</sup> = (2/(π+e))<sup>4</sup> ≈ 0.01363. CMB-S4 targets σ(r) ≈ 0.001 over the 2028–2035 observing window, giving 14σ discriminant power. **If the measured value is inconsistent with 0.01363 at ≥5σ, the framework's cosmological sector fails.** This is the principal falsification seam and is documented as entry N9 in the [Falsification Pack]({{ '/results/falsifications/browse/' | relative_url }}).

Other single-result falsifiers, each with 5σ thresholds and named experiments:

- **Non-detection of 0νββ at or beyond τ-predicted half-life**, or detection inconsistent with the τ-derived half-life at ≥5σ → refutes the framework's Majorana-neutrino prediction (IV.T146, C-sector zero holonomy requires Majorana mass terms)
- **Confirmed proton decay** at any scale → refutes the Proton Stability theorem
- **Confirmed magnetic monopole detection** → refutes the Homogeneous Maxwell theorem
- **Confirmed supersymmetric partner detection** → refutes Sector Exhaustion

The framework does **not** treat any single result as sufficient to validate it (validation requires the joint agreement across many sectors). But each of the five results above is sufficient to falsify it.

## 11. Why is α "predicted at 9.8 ppm" presented in the same Tier A as m<sub>e</sub> "predicted at 0.025 ppm"?

**Answer: precision tiers in our predictions catalogue label structural derivation status, not measurement-grade agreement — and a single prediction can have multiple legitimate derivation routes at different precision bands.**

The fine-structure constant α is one of the most precisely measured quantities in physics (relative precision ≈ 10<sup>−10</sup>). The framework derives α via two routes that should be read together:

- **Closed-form algebraic LO**: α = (11/15)<sup>2</sup>·ι<sub>τ</sub><sup>4</sup> = (121/225)·ι<sub>τ</sub><sup>4</sup> reproduces the CODATA central value to **~9.8 ppm**. This is the route that fits on a single line and is the right entry point for a first-pass reviewer; (11/15)² is itself derived as the EM-tensor density 121/225 in `A_spec(L)^{⊗2}` ([IV.T133]({{ '/results/additional-noteworthy-results/physics/em-tensor-density-theorem-iv-t133/' | relative_url }})). The arithmetic: ι<sub>τ</sub> = 2/(π+e) ≈ 0.341304; ι<sub>τ</sub><sup>4</sup> ≈ 0.0135695; (11/15)<sup>2</sup> ≈ 0.537778; product ≈ 0.0072978; CODATA α ≈ 0.0072974; relative deviation ≈ 9.8 ppm.
- **Full multi-loop derivation** (`IV.T107`): leading-order κ_B = ι<sub>τ</sub><sup>2</sup> + NLO holonomy (`IV.T49`) + NNLO window algebra (`IV.D337`) reaches **~0 ppm** vs CODATA 137.035999. This is the framework's full claim, published in [Book IV Chapter 10]({{ '/corpus/monographs/book-iv/part-01-the-joint-core-from-neutron-to-hydrogen/chapter-10-the-fine-structure-constant/' | relative_url }}) and on the [α prediction page]({{ '/results/problem/fine-structure-constant-alpha-inverse-137/' | relative_url }}).

So which is "the" α prediction? Both are: the LO closed-form is the auditable shortcut (9.8 ppm) and the multi-loop route is the framework's full result (~0 ppm). They co-exist deliberately. The [numerical physics ledger]({{ '/publications/monograph-supplements/numerical-physics-ledger/' | relative_url }}) line on α records the LO 9.8 ppm number explicitly because it is a falsifiable single-line claim that does not depend on multi-loop bookkeeping; the ~0 ppm headline on the α prediction page is the result that includes NLO + NNLO and is correspondingly heavier to verify.

The electron mass m<sub>e</sub>, derived via the kernel-anchored cascade with the neutron mass as the dimensional anchor, agrees with the CODATA central value to ~0.025 parts-per-million. **Both α and m<sub>e</sub> are listed as "Tier A" — and that label means *structural derivation present in the kernel chain*, not "agreement at measurement precision."** Treat the LO α match as a partial agreement worth structural follow-through; treat the m<sub>e</sub> match as a closer hit that is nevertheless a *fit of the dimensionless ratio* m<sub>e</sub>/m<sub>n</sub> rather than an absolute prediction (m<sub>n</sub> is the dimensional anchor). The [Predictions catalogue]({{ '/results/predictions/' | relative_url }}) and [Calibration Cascade]({{ '/results/physics/cascade/' | relative_url }}) make the per-tier definitions and the dimensional-anchoring chain explicit. **The earlier presentation could read as overstating uniform precision.** Per-row precision-band chips (sub-10 ppm / 10–1000 ppm / 1–5% / structural) are now displayed on every card in the [predictions browse grid]({{ '/results/predictions/browse/' | relative_url }}), so the band is readable at a glance — but a reviewer should still open the per-prediction page rather than trust the headline tier badge alone.

## 12. Are the Lean theorems in Book VI/VII consciousness modules substantive proofs or `rfl` over Boolean defaults?

**Answer: bookkeeping-shaped, by design and by acknowledged status.**

A philosophically-trained reviewer opening the raw Lean source for `BookVI.Mind.Consciousness` and `BookVII.Meta.Registers` will find that several "theorems" — for example `consciousness_requires_mixed_sector` and `register_orthogonality` — reduce to `⟨rfl, rfl, rfl, rfl⟩` over `structure` fields that default to `true : Bool`. **These are not derivations; they are scaffolding that fixes namespaces and type signatures while the substantive formalization is still being authored.** The framework does not claim phenomenal content has been mechanically proved from category theory. The corresponding registry entries carry "planned" formalization status; the [Hard Problem of Consciousness]({{ '/results/challenge-responses/metaphysics/mind-consciousness-self-agency/hard-problem-consciousness/' | relative_url }}) Challenge Response is marked "partially addressed"; the [SCL Mind cluster]({{ '/agenda/structural-challenge-ledger/metaphysics/mind-consciousness-self-agency/' | relative_url }}) is the canonical accountability surface. Reviewers should not treat the Book VI/VII Mind Lean modules as the load-bearing evidence for consciousness claims — the load-bearing evidence is the prose of Book VII plus, where present, formal proofs in Book I–III machinery the Mind module imports.

## 13. Does Book VII *solve* the hard problem of consciousness, or *relocate* it?

**Answer: relocate, deliberately, and honestly.**

The hard problem of consciousness — why categorical/physical structure is accompanied by phenomenal character at all — is **not** claimed to be solved by τ. The four-register decomposition (Reg_E empirical / Reg_P practical / Reg_D diagrammatic / Reg_C commitment) is a structural reformulation that locates the phenomenal-content question at the Reg_E ↔ Reg_C interface; it does not derive phenomenal character from category theory and we do not claim it does. A philosophical zombie with identical Reg_E/P/D/C readouts is a coherent posit *within* the framework — which is precisely why the [Hard Problem of Consciousness Challenge Response]({{ '/results/challenge-responses/metaphysics/mind-consciousness-self-agency/hard-problem-consciousness/' | relative_url }}) carries "partially addressed" status, not "internally addressed." The framework's contribution to the philosophy-of-mind literature is the *register-typing discipline* and the explicit boundary between proof-content and stance-content (No Forced Stance theorem, VII.T47 — see Q6); whether that discipline materially advances the hard problem is a question for the philosophy-of-mind community to answer, not for the framework to answer about itself.

Reviewers familiar with Chalmers, Levine, Block, and Nagel will find the framework's posture closer to Sellars/Brandom (commitment as a primitive level of content) than to a reductive account; we welcome philosophy-of-mind specialists who can evaluate whether the structural relocation is a step or a renaming.

---

## Framing note

These thirteen questions are not the framework's own marketing pitch. They were reconstructed from the red-team question lists in independent frontier-LLM first-pass assessments — the original three that established questions 1–10 in April 2026, and a May 2026 self-test in which the program ran its own [published assessment protocols]({{ '/verify/assessment-protocols/llm-assisted/' | relative_url }}) (one series-level run plus four expert-domain runs across pure mathematics, particle physics, formal methods, and philosophy of mind). The May 2026 run sharpened questions 1–3, 5, 8, and 9, and surfaced questions 11–13 as net-new high-signal additions.

The framework earns its review-readiness not by having comfortable answers to these questions but by having *testable* answers with load-bearing evidence. Every pointer in this FAQ leads to that evidence.

A reader who finds an answer insufficient is exactly the reader this FAQ is written for. The framework's response to "insufficient" is the invitation to inspect the Lean proof, follow the registry chain, run our own assessment protocols, or bring the question to formal review — not to refine the marketing copy.

## Cross-links

- [Scope, Status & Scrutiny]({{ '/program/about/scope-status-and-scrutiny/' | relative_url }}) — the program's own methodological self-description
- [What the Program Refuses]({{ '/agenda/what-the-program-refuses/' | relative_url }}) — explicit boundaries
- [Prior-Art Comparisons]({{ '/agenda/kernel-model-reality/related-approaches/deep-comparison/' | relative_url }}) — honest comparisons against Fueter, Hilbert-Pólya, Furey/octonionic, autopoiesis/IIT/FEP, and MOND/Verlinde
- [Release Manifest]({{ '/verify/release-manifest/' | relative_url }}) — pinned commit, build status, axiom inventory, drift reconciliation
- [Prediction Timing Ledger]({{ '/results/predictions/timing/' | relative_url }}) — a-priori vs post-diction breakdown for the {% include release-metric.html id="predictions.records" %} predictions
- [Falsification Pack]({{ '/results/falsifications/browse/' | relative_url }}) — {% include release-metric.html id="falsifications.records" %} named experimental tests

For broader context, see:

- [Inspection Architecture for High-Scope Open Research]({{ '/publications/white-papers/inspection-architecture-high-scope-open-research/' | relative_url }})
- [The Shape of a Theory of Reality]({{ '/publications/white-papers/the-shape-of-a-theory-of-reality/' | relative_url }})
- [Building a Public Research Observatory]({{ '/publications/white-papers/building-a-public-research-observatory/' | relative_url }})
