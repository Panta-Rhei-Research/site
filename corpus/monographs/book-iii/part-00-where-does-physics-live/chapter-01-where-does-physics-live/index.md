---
layout: "corpus-monograph-chapter"
title: "Chapter 1: Where Does Physics Live?"
permalink: "/corpus/monographs/book-iii/part-00-where-does-physics-live/chapter-01-where-does-physics-live/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "III"
book_slug: "book-iii"
part_number: 0
part_display: "Prologue"
part_slug: "part-00-where-does-physics-live"
chapter_number: 1
chapter_slug: "chapter-01-where-does-physics-live"
page_in_book: 3
next_chapter_url: "/corpus/monographs/book-iii/part-00-where-does-physics-live/chapter-02-the-eight-guarantees/"
next_chapter_title: "Chapter 2: The Eight Guarantees"
summary_short: "Books I–II built τ³ = τ¹ ×_f T² and proved O(τ³) ≅ A_spec(𝕃). This chapter identifies the solenoidal-vs-Cartesian coordinate gap and resolves it: perceived 3D space is the Hartogs bulk of T². Physics is E₁."
canonical_book_url: "/corpus/monographs/book-iii/"
canonical_book_title: "Book III: Categorical Spectrum"
canonical_part_url: "/corpus/monographs/book-iii/part-00-where-does-physics-live/"
canonical_part_title: "Where Does Physics Live?"
publication_book_url: "/publications/books/book-iii/"
legacy_publication_url: "/publications/books/book-iii/part-00-where-does-physics-live/chapter-01-where-does-physics-live/"
right_rail:
  related:
    -
      title: "Book III: Categorical Spectrum"
      url: "/corpus/monographs/book-iii/"
    -
      title: "Prologue: Where Does Physics Live?"
      url: "/corpus/monographs/book-iii/part-00-where-does-physics-live/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-iii/"
    -
      title: "Registry"
      url: "/registry/books/book-iii/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book III"
    part: "Prologue"
    layer: "E₀ Mathematics (Hinge)"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 31
construction_layer: "physics"
construction_layer_label: "Physics"
construction_step_ids:
  - "CS-04"
  - "CS-05"
---

Books I and II constructed a complete mathematical universe from five generators and seven axioms, culminating in the Central Theorem O(τ³) ≅ A_spec(𝕃). But this universe does not look like the three-dimensional Cartesian space where physics is formulated. The fibered product τ³ = τ¹ ×_f T² has four coordinates, all solenoidal — one-sided, angular, with no canonical ± symmetry — while quantum field theory and general relativity live in ℝ^{1,3} whose spatial coordinates are two-sided, linear, and Cartesian. This chapter identifies the gap and resolves it: the three-dimensional Cartesian space of physics arises as the Hartogs bulk of the fiber T². At each worldline point p ∈ τ¹ the fiber T²_p is a two-dimensional surface, and the Hartogs extension (*I.T31*) projects boundary data from that surface into a three-dimensional interior whose coordinates are genuinely linear and two-sided. Perceived space is this bulk. The central task of Book III is then to show that local bulk projections — one per worldline point — glue into a single globally coherent space, and that this gluing is precisely the content of the self-enrichment layer E₁. Physics *is* E₁.

## What this chapter contributes

**Definitions / Axioms**
- *Hartogs bulk principle* (established consequence of *I.T31*): the three-dimensional Cartesian space perceived at worldline point p ∈ τ¹ is the Hartogs bulk of the fiber T²_p — the unique holomorphic extension of two-dimensional boundary data on T²_p into its three-dimensional interior. The ± symmetry absent on the solenoidal boundary is created by analytic continuation into the bulk.

**Key results**
- *Coordinate mismatch* (established): a solenoidal coordinate (winding number in ℕ) carries no canonical ± splitting and no linear structure. The naive identification (π, γ, η) ↔ (x, y, z) is structurally impossible — there is no non-trivial homomorphism from (ℕ, +) to (ℝ, +) that is ℝ-linear.
- *Cartesian from solenoidal* (τ-effective consequence of *I.T31*, *II.T40*): the Hartogs extension maps boundary data on the solenoidal surface T² into an interior with genuinely linear, two-sided coordinates. This is not a coordinate trick but a theorem about holomorphic extensions in several complex variables. The decompactification limit τ³_R → ℝ³ as R → ∞ recovers continuous Cartesian space with O(ι_τ²) corrections.
- *Physics as global coherence* (τ-effective): E₁ is the minimal self-enrichment of E₀ that forces local bulk projections to cohere globally. At E₀, local Hartogs extensions exist but there is no guarantee that transition maps between overlapping bulks respect spectral structure. At E₁, Hom spaces acquire split-complex structure, and the enrichment constraints force global compatibility. In this precise sense, physics is E₁.
- *Role of the Millennium Problems* (τ-effective, seven of eight; established, one): each of the eight spectral forces secures one piece of the local-to-global gluing. The full correspondence is previewed here and earned in Parts IV–VI and IX.

**Notation**
- τ³ = τ¹ ×_f T² (fibered product); 𝕃 = S¹ ∨ S¹ (algebraic lemniscate); ι_τ = 2/(π+e) ≈ 0.341304 (master constant); O(τ³) ≅ A_spec(𝕃) (*II.T40*); Hartogs bulk at p = holomorphic extension of T²_p data

**Dependencies**
- *I.T04* (Hyperfactorization / ABCD decomposition), *I.T31* (Global Hartogs extension), *I.T41* (Bi-square characterization)
- *II.T40* (Central Theorem), *II.T49* (Geometric bi-square)

## Lean coverage

No registry entries are defined in this chapter — it is the driving-question chapter of the Prologue, framing the problem rather than producing formal output. The Hartogs bulk principle is stated as a consequence of *I.T31*, which has a planned Lean 4 counterpart in `TauLib/BookI/`. The coordinate-mismatch observation (no non-trivial ℕ → ℝ homomorphism) reduces to a trivial algebraic statement and is a strong Lean target whenever the relevant algebraic structures are in scope. No completed Lean 4 entry recorded at time of projection.

## Where this leads

Chapter 2 identifies the eight structural guarantees — seven Clay Millennium Problems plus the Langlands programme — that collectively ensure the local Hartogs bulk projections cohere into a single global three-dimensional space, and organises them into the Millennium-Problem Gluing Table (*III.D02*).

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-03/part00/ch01-where-does-physics-live.tex -->
