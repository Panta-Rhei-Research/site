---
layout: "corpus-monograph-chapter"
title: "Chapter 28: Omega-Germs on the Ontic Elements"
permalink: "/corpus/monographs/book-i/part-07-omega-germs-the-algebraic-lemniscate/chapter-28-omega-germs-on-the-ontic-elements/"
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
chapter_number: 28
chapter_slug: "chapter-28-omega-germs-on-the-ontic-elements"
page_in_book: 105
prev_chapter_url: "/corpus/monographs/book-i/part-06-the-prime-polarity-theorem/chapter-27-the-prime-polarity-theorem/"
prev_chapter_title: "Chapter 27: The Prime Polarity Theorem"
next_chapter_url: "/corpus/monographs/book-i/part-07-omega-germs-the-algebraic-lemniscate/chapter-29-polarized-omega-germs/"
next_chapter_title: "Chapter 29: Polarized Omega-Germs"
summary_short: "Omega-tails (*I.D25*) are compatible towers on the primorial ladder — the τ-native analogue of Cauchy sequences. Constructed on bare-metal ontic elements with no imported topology, they carry an ultrametric and a compact profinite structure."
canonical_book_url: "/corpus/monographs/book-i/"
canonical_book_title: "Book I: Categorical Foundations"
canonical_part_url: "/corpus/monographs/book-i/part-07-omega-germs-the-algebraic-lemniscate/"
canonical_part_title: "Omega-Germs & the Algebraic Lemniscate"
publication_book_url: "/publications/books/book-i/"
legacy_publication_url: "/publications/books/book-i/part-07-omega-germs-the-algebraic-lemniscate/chapter-28-omega-germs-on-the-ontic-elements/"
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

The Prime Polarity Theorem classified each internal prime as B-dominant or C-dominant using finite, decidable computations on individual primes. Part VII passes from the finite regime to the infinite limit. The foundational object is the primorial ladder: the sequence of primorials M_k = p₁ · p₂ · · · p_k together with reduction maps π_{ℓ→k} : ℤ/M_ℓℤ → ℤ/M_kℤ that form a compatible inverse system. An omega-tail (*I.D25*) is a family (x_k)_{k ≥ 1} with x_k ∈ ℤ/M_kℤ satisfying the coherence condition π_{ℓ→k}(x_ℓ) = x_k for all k ≤ ℓ. This is the τ-native analogue of a Cauchy sequence: not a metric notion but an algebraic one — coherence under reduction maps — constructed entirely within τ-Idx arithmetic with no imported topology, no coordinates, and no interior points.

## What this chapter contributes

The chapter constructs the primorial ladder as a canonical filtration of τ-Idx, establishes the compatibility of the reduction maps, and defines omega-tails (*I.D25*) as the elements of the inverse system lim← ℤ/M_kℤ. Tail-equivalence (two omega-tails agree at every finite stage) and tail-stable predicates (predicates invariant under tail-equivalence) formalize the notion of properties that eventually stabilize. A key example: the polarity map pol: ℙ_τ → {+, −} is tail-stable, because the scaled-gap inequality that determines polarity stabilizes after finitely many primorial stages. This is the structural link between the finite-regime Prime Polarity Theorem and the infinite-limit boundary data. The chapter also defines the divergence depth d(t, t') — the reciprocal of the first stage at which two tails disagree — and proves it is an ultrametric (*I.P20*, *I.P21*). Two formally verified propositions follow from this construction: `ultra_dist_self` (d(t, t) = 0) and `congruent_tails_agree` (n ≡ m mod M_k implies the canonical embeddings agree at stage k). The inverse limit is compact in the profinite topology — the τ-analogue of Cauchy-completeness — and will become the boundary ring ℤ̂_τ in Chapter 30. All proofs in modules `TauLib.BookI.Polarity.OmegaGerms` and `TauLib.BookI.Denotation.Structural` compile without `sorry`.

## Lean coverage

Formalized in `TauLib.BookI.Polarity.OmegaGerms` and `TauLib.BookI.Denotation.Structural`. The modules include `OmegaTail` (compatible towers), `ultra_triangle` (full ultrametric triangle inequality), `mk_omega_tail_compat` (canonical embedding produces compatible towers), `ultra_dist_self` (*I.P20*), and `congruent_tails_agree` (*I.P21*). All proofs compile with zero `sorry`.

## Where this leads

Chapter 29 introduces polarization: at each refinement depth, the local fiber of an omega-germ has two channel quotients B_n and C_n, and a germ is polarized when one channel eventually freezes. Chapter 30 asks what scalar algebra is forced by the bipolar structure and discovers split-complex numbers, assembling the algebraic lemniscate ℒ. Chapter 31 synthesizes the local–global bridge and previews Parts VIII–XVI.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-01/part07/ch28-omega-germs.tex -->
