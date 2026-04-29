---
layout: "corpus-monograph-chapter"
title: "Chapter 29: Polarized Omega-Germs"
permalink: "/corpus/monographs/book-i/part-07-omega-germs-the-algebraic-lemniscate/chapter-29-polarized-omega-germs/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "I"
book_slug: "book-i"
part_number: 7
part_display: "Part VII"
part_slug: "part-07-omega-germs-the-algebraic-lemniscate"
chapter_number: 29
chapter_slug: "chapter-29-polarized-omega-germs"
page_in_book: 111
prev_chapter_url: "/corpus/monographs/book-i/part-07-omega-germs-the-algebraic-lemniscate/chapter-28-omega-germs-on-the-ontic-elements/"
prev_chapter_title: "Chapter 28: Omega-Germs on the Ontic Elements"
next_chapter_url: "/corpus/monographs/book-i/part-07-omega-germs-the-algebraic-lemniscate/chapter-30-the-bipolar-spectral-algebra/"
next_chapter_title: "Chapter 30: The Bipolar Spectral Algebra"
summary_short: "Polarized omega-germs (*I.D26*) are omega-tails at which one of the two channel fibers (B or C) eventually freezes. The unique crossing-point germ, where neither channel freezes, corresponds to the beacon ω and sits at the junction of the two lemniscate lobes."
canonical_book_url: "/corpus/monographs/book-i/"
canonical_book_title: "Book I: Categorical Foundations"
canonical_part_url: "/corpus/monographs/book-i/part-07-omega-germs-the-algebraic-lemniscate/"
canonical_part_title: "Omega-Germs & the Algebraic Lemniscate"
publication_book_url: "/publications/books/book-i/"
legacy_publication_url: "/publications/books/book-i/part-07-omega-germs-the-algebraic-lemniscate/chapter-29-polarized-omega-germs/"
right_rail:
  related:
    -
      title: "Book I: Categorical Foundations"
      url: "/corpus/monographs/book-i/"
    -
      title: "Part VII: Omega-Germs & the Algebraic Lemniscate"
      url: "/corpus/monographs/book-i/part-07-omega-germs-the-algebraic-lemniscate/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-i/"
    -
      title: "Registry"
      url: "/registry/books/book-i/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book I"
    part: "Part VII"
    layer: "E₀ Mathematics"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 8
construction_layer: "mathematics"
construction_layer_label: "Mathematics"
construction_step_ids:
  - "CS-01"
  - "CS-02"
---

Chapter 28 built omega-tails as the pre-topological boundary data of τ. This chapter introduces the decisive structural refinement: polarization. At each finite refinement depth n along the primorial ladder, the local fiber of an omega-germ splits into two channel quotients — B_n and C_n — and their product T_n = B_n × C_n forms a two-dimensional local fiber. Successive refinements produce an inverse system T_1 ← T_2 ← T_3 ← ⋯ with projections induced componentwise. A germ is polarized when one of the two factor systems eventually becomes trivially constant — its refinement maps become isomorphisms beyond some finite depth — while the other continues to produce genuinely new structure. B-polarized germs correspond to B-dominant primes; C-polarized germs correspond to C-dominant primes. The unique germ where neither channel freezes, where both angular degrees of freedom remain active in the infinite limit, is the crossing-point germ, identified with the beacon ω.

## What this chapter contributes

The chapter formalizes eventual constancy (a factor system eventually stops refining), uses it to define B-polarized and C-polarized omega-germs (*I.D26*), and connects polarization directly to the Prime Polarity Theorem. The Polarity-Generates-Polarization Proposition shows that every B-dominant prime generates a family of B-polarized germs and every C-dominant prime generates a family of C-polarized germs, with both families infinite by the Prime Polarity Theorem. The crossing-point germ is defined as the unique omega-germ where both channel systems are cofinal (never eventually constant), and its uniqueness is established: only the beacon ω can sit at the boundary of both polarity classes simultaneously. A remark on Lipschitz descent notes that the rate at which channel imbalance grows away from the crossing point along the primorial ladder is a question of holomorphic regularity on ℒ, deferred to Book II. The chapter also defines the PolStream — the infinite binary sequence recording the polarity sign of each prime in order — and proves it is aperiodic: any eventual period would force one polarity class to be finite, contradicting the Prime Polarity Theorem. Lean formalization targets `TauLib.BookI.Polarity.PolarizedGerms` with types `BPolarized`, `CPolarized`, `CrossingGerm`, and decidable checks `b_polarized_check`, `c_polarized_check`. All definitions compile without `sorry`.

## Lean coverage

Formalized in `TauLib.BookI.Polarity.PolarizedGerms`. Key constructs: `eventually_constant`, `cofinal`, `BPolarized`, `CPolarized`, `CrossingGerm`, and the decidable predicates `b_polarized_check` and `c_polarized_check`. All definitions compile with zero `sorry`.

## Where this leads

Chapter 30 asks what scalar ring is forced by the bipolar structure of the boundary. Three requirements — bipolar encoding, internal origin, and diagonal-free compatibility — uniquely determine split-complex scalars (j² = +1). Together with the crossing-point germ as identity and the polarity involution σ, this gives the algebraic lemniscate ℒ = (H_τ, ω_ℒ, σ).

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-01/part07/ch29-polarized-omega-germs.tex -->
