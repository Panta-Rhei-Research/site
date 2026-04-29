---
layout: "corpus-monograph-chapter"
title: "Chapter 57: BSD Bridge: Proto-Rationality in Split-Complex Regime"
permalink: "/corpus/monographs/book-ii/part-10-closure-synthesis-and-bridge-to-book-iii/chapter-57-bsd-bridge-proto-rationality-in-split-complex-regime/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "II"
book_slug: "book-ii"
part_number: 10
part_display: "Part X"
part_slug: "part-10-closure-synthesis-and-bridge-to-book-iii"
chapter_number: 57
chapter_slug: "chapter-57-bsd-bridge-proto-rationality-in-split-complex-regime"
page_in_book: 351
prev_chapter_url: "/corpus/monographs/book-ii/part-10-closure-synthesis-and-bridge-to-book-iii/chapter-56-differential-geometric-agenda-for-book-iii/"
prev_chapter_title: "Chapter 56: Differential-Geometric Agenda for Book~III"
next_chapter_url: "/corpus/monographs/book-ii/part-10-closure-synthesis-and-bridge-to-book-iii/chapter-58-forward-to-book-iii-spectral-forces-in-h-tau/"
next_chapter_title: "Chapter 58: Forward to Book~III — Spectral Forces in H_τ"
summary_short: "Bridges Book II's Central Theorem toward the BSD Conjecture by defining proto-rationality in the split-complex regime and identifying what Layers 1–2 provide versus what Book III must add for Layers 3–4."
canonical_book_url: "/corpus/monographs/book-ii/"
canonical_book_title: "Book II: Categorical Holomorphy"
canonical_part_url: "/corpus/monographs/book-ii/part-10-closure-synthesis-and-bridge-to-book-iii/"
canonical_part_title: "Closure: Synthesis and Bridge to Book III"
publication_book_url: "/publications/books/book-ii/"
legacy_publication_url: "/publications/books/book-ii/part-10-closure-synthesis-and-bridge-to-book-iii/chapter-57-bsd-bridge-proto-rationality-in-split-complex-regime/"
right_rail:
  related:
    -
      title: "Book II: Categorical Holomorphy"
      url: "/corpus/monographs/book-ii/"
    -
      title: "Part X: Closure: Synthesis and Bridge to Book III"
      url: "/corpus/monographs/book-ii/part-10-closure-synthesis-and-bridge-to-book-iii/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-ii/"
    -
      title: "Registry"
      url: "/registry/books/book-ii/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book II"
    part: "Part X"
    layer: "E₀ Mathematics"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 29
construction_layer: "mathematics"
construction_layer_label: "Mathematics"
construction_step_ids:
  - "CS-02"
  - "CS-03"
---

Chapter 57 bridges from Book II's Central Theorem to the Birch and Swinnerton-Dyer (BSD) Conjecture — one of the seven Millennium Problems. Book II does not prove BSD; that requires the spectral force machinery of Book III at enrichment layer E₂. What this chapter establishes is the structural prerequisite: proto-rationality (*II.D66*), the condition that spectral coefficients of τ-L-functions lie in the image of the canonical basis 𝒷_τ (*II.D45*) and are determined by finitely many prime-indexed data. The split-complex codomain H_τ (with j² = +1) fundamentally reshapes the analytic rank: the idempotent decomposition (*II.L07*) splits the τ-L-function into bipolar components L₊ and L₋, with independent orders of vanishing r₊ and r₋ at the critical point, and the total τ-analytic rank r_τ = r₊ + r₋ is the conjectured sum that equals the Mordell–Weil rank of E(ℚ). The BSD Bridge remark (*II.R18*) then identifies the four-layer structure: Layer 1 (Central Theorem, earned) and Layer 2 (proto-rationality, earned) are Book II's contribution; Layer 3 (τ-L-function with analytic continuation, functional equation, and Euler product in H_τ) and Layer 4 (force-theoretic rank computation via a τ-Gross–Zagier theory) must be earned by Book III. This chapter is a bridge, not a proof; it is honest about the distance from proto-rationality to BSD.

## What this chapter contributes

- **Registry entry *II.D66* — Proto-Rationality:** a holomorphic function f ∈ 𝒪(τ³) is proto-rational if its spectral coefficients {φ_{mn}} satisfy (1) finite spectral support (guaranteed by *II.T31*), (2) the basis image condition — each φ_{mn} is an H_τ-linear combination of cylinder generators from *II.D46* — and (3) prime determinacy — finitely many primes Π ⊂ ℙ_τ determine f completely. The sub-algebra 𝒪_pr(τ³) of proto-rational functions is closed under composition and idempotent projection.
- **Registry entry *II.R18* — BSD Bridge:** the four-layer architecture (Central Theorem + proto-rationality from Book II; τ-L-function theory + force-theoretic rank computation from Book III). Layers 3–4 require the bipolar analytic continuation (along two independent real directions, not a single complex variable), a j-compatible functional equation producing a bipolar root number (w₊, w₋) ∈ {+1,−1}², and τ-Selmer group computation via bipolar cohomology.
- **Bipolar analytic rank:** r₊ := ord_{s=1} L₊(E,s) and r₋ := ord_{s=1} L₋(E,s). The asymmetry r₊ − r₋ is a new invariant with no classical counterpart. In the limit ι_τ → 0 the channels decouple and r₊ = r₋ = r_an; at the physical value ι_τ = 2/(π + e) coupling is non-trivial.
- **Proto-rationality as a bi-square condition:** f is proto-rational precisely when its spectral expansion respects the bi-square (*I.T41*) at every finite stage — tower coherence (left face, condition (3)) and spectral naturality (right face, condition (2)).
- **Three Millennium readings:** proto-rationality is the common algebraic prerequisite for RH (spectral decomposition reading), BSD (rational points reading), and Langlands₀ (functoriality reading). The three readings diverge at Layer 3 in how the L-function is constructed.

## Lean coverage

The Lean formalization target is `BookII.Closure.BSDbridge`. The module defines the `is_proto_rational` predicate, `proto_rational_stage` (the minimal stabilization stage), `proto_rational_abcd` (ABCD coordinate representation), and `proto_rational_count_at_stage` (arithmetic complexity measure). All four compile without sorry. The full BSD bridge (Layers 3–4) will be formalized in Book III's TauLib modules.

## Where this leads

Chapter 58 (Forward to Book III — Spectral Forces in H_τ) pulls back from the BSD example to the general case: it specifies the complete E₁ Export Package (*II.D67*) that Book III receives, previews all eight spectral forces and their classical Millennium Problem connections, and states precisely what Book III must do to earn them.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-02/part10/ch56-bsd-bridge.tex -->
