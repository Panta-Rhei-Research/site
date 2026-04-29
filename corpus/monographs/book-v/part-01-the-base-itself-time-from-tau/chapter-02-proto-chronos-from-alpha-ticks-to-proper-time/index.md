---
layout: "corpus-monograph-chapter"
title: "Chapter 2: Proto-Chronos: From α-Ticks to Proper Time"
permalink: "/corpus/monographs/book-v/part-01-the-base-itself-time-from-tau/chapter-02-proto-chronos-from-alpha-ticks-to-proper-time/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "V"
book_slug: "book-v"
part_number: 1
part_display: "Part I"
part_slug: "part-01-the-base-itself-time-from-tau"
chapter_number: 2
chapter_slug: "chapter-02-proto-chronos-from-alpha-ticks-to-proper-time"
page_in_book: 11
prev_chapter_url: "/corpus/monographs/book-v/part-00-the-hermetic-principle/chapter-01-the-hermetic-principle-fiber-complete-base-awaits/"
prev_chapter_title: "Chapter 1: The Hermetic Principle: Fiber Complete, Base Awaits"
next_chapter_url: "/corpus/monographs/book-v/part-01-the-base-itself-time-from-tau/chapter-03-the-temporal-ignition-why-a-time-epoch-starts/"
next_chapter_title: "Chapter 3: The Temporal Ignition: Why a ``Time Epoch'' Starts"
summary_short: "Physical time is derived, not postulated. Each step of the α-orbit is one α-tick; proper time is accumulated arc length t(n) = Σ p_k⁻¹, strictly increasing and bounded above by t∞ ≈ 0.7052."
canonical_book_url: "/corpus/monographs/book-v/"
canonical_book_title: "Book V: Categorical Macrocosm"
canonical_part_url: "/corpus/monographs/book-v/part-01-the-base-itself-time-from-tau/"
canonical_part_title: "The Base Itself: Time from τ¹"
publication_book_url: "/publications/books/book-v/"
legacy_publication_url: "/publications/books/book-v/part-01-the-base-itself-time-from-tau/chapter-02-proto-chronos-from-alpha-ticks-to-proper-time/"
right_rail:
  related:
    -
      title: "Book V: Categorical Macrocosm"
      url: "/corpus/monographs/book-v/"
    -
      title: "Part I: The Base Itself: Time from τ¹"
      url: "/corpus/monographs/book-v/part-01-the-base-itself-time-from-tau/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-v/"
    -
      title: "Registry"
      url: "/registry/books/book-v/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book V"
    part: "Part I"
    layer: "E₁ Physics (Macrocosm)"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 52
construction_layer: "physics"
construction_layer_label: "Physics"
construction_step_ids:
  - "CS-05"
  - "CS-06"
---

Every physical theory must decide what time is before it can do anything else. Newtonian mechanics postulates it as an external, uniformly flowing parameter. General relativity internalises it as arc length along a Lorentzian worldline—an improvement, but the manifold in which that worldline lives is still postulated. Category τ takes a further step: time is derived from the base circle τ¹ = ⟨α, π⟩, a compact profinite space whose metric structure is fixed entirely by the kernel axioms K0–K6. No external time parameter is introduced at any point in the derivation.

The bridge from counting to measuring runs as follows. Book IV defined proto-time as the ρ-iteration depth t_p(α_n) = n—a discrete, structural label on the refinement tower. To convert labels into durations one needs a metric. The ultrametric on the α-orbit assigns distance d_α(α_m, α_n) = p_min(m,n)⁻¹ to non-coincident levels, where p_k is the k-th primorial. Proper time is then the accumulated arc length t(n) = Σ_{k=1}^{n-1} p_k⁻¹ = 1/2 + 1/6 + 1/30 + …. Because primorials grow super-exponentially, this series converges: t∞ = Σ p_k⁻¹ ≈ 0.7052 in natural units. Physical time is therefore bounded—the base circle is compact. The arrow of time is the generative direction of the α-orbit, irreversible because ρ has no inverse in the kernel specification. Causality is orbit ordering: α_m ≺ α_n iff m < n, a total, transitive, irreflexive relation that excludes closed timelike curves at the structural level. Duration between causally ordered events is Δt(m,n) = Σ_{k=m}^{n-1} p_k⁻¹, a genuine metric on the α-orbit that extends by continuity to the profinite completion.

## What this chapter contributes

- **Definitions / Axioms:** *V.D12 — Base Circle τ¹ (Macroscopic)* (τ-effective). *V.D13 — α-Tick* (τ-effective). *V.D14 — Proper Time (Arc Length)* (τ-effective). *V.D15 — Causal Ordering Relation* (τ-effective). *V.D16 — Geodesic Duration* (τ-effective).
- **Key results:** *V.T06 — Time Derivation Theorem* (τ-effective): proper time t(n) is well-defined, strictly increasing, bounded in [0, t∞), and uniquely determined by the kernel axioms up to an overall calibration scale. *V.T07 — Causal Ordering Theorem* (τ-effective): the ordering α_m ≺ α_n is structurally enforced; no backward causation exists in Category τ. *V.T08 — Bounded Time Theorem* (τ-effective): t∞ < ∞; the universe has finite temporal extent. *V.P03 — Arrow of Time = Orbit Direction* (τ-effective): the temporal direction is the unique, irreversible generative direction of the α-orbit. *V.R04 — No Background Time* (τ-effective): the problem of time in canonical quantum gravity does not arise because time is structural, not parametric.
- **Notation introduced:** α-tick Δ_k; arc-length metric d_time; primorial p_k; accumulation point α_o.
- **Dependencies:** IV.D03 (Refinement Tower), IV.D05 (Proto-Time), IV.T01 (Structural Arrow of Time), I.D02 (Progression Operator), I.K1–K5 (Kernel Axioms).

## Lean coverage

`TauLib.BookV.Temporal.BaseCircle` — the Time Derivation Theorem and Bounded Time Theorem are verified; convergence of Σ p_k⁻¹ is proved via the estimate p_k > k! for k ≥ 2.

## Where this leads

The arc-length metric on τ¹ and the causal ordering are the two structural inputs that every subsequent chapter of Part I and the whole gravitational programme of Part II depend on; the Bounded Time Theorem also seeds the cosmological endstate discussion of Part VI.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-05/part01/ch04-proto-chronos.tex -->
