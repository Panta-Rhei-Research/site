---
layout: "corpus-monograph-chapter"
title: "Chapter 54: The Global Cartesian Gluing"
permalink: "/corpus/monographs/book-iii/part-08-where-physics-lives/chapter-54-the-global-cartesian-gluing/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "III"
book_slug: "book-iii"
part_number: 8
part_display: "Part VIII"
part_slug: "part-08-where-physics-lives"
chapter_number: 54
chapter_slug: "chapter-54-the-global-cartesian-gluing"
page_in_book: 277
prev_chapter_url: "/corpus/monographs/book-iii/part-08-where-physics-lives/chapter-53-the-eight-guarantees-earned/"
prev_chapter_title: "Chapter 53: The Eight Guarantees Earned"
next_chapter_url: "/corpus/monographs/book-iii/part-08-where-physics-lives/chapter-55-e/"
next_chapter_title: "Chapter 55: E₁"
summary_short: "The Global Cartesian Gluing Theorem (*III.T50*) proves local Hartogs bulk projections glue into M_{τ³}; the Minkowski Extension (*III.D76*) adjoins a temporal base to produce 3+1D spacetime."
canonical_book_url: "/corpus/monographs/book-iii/"
canonical_book_title: "Book III: Categorical Spectrum"
canonical_part_url: "/corpus/monographs/book-iii/part-08-where-physics-lives/"
canonical_part_title: "Where Physics Lives"
publication_book_url: "/publications/books/book-iii/"
legacy_publication_url: "/publications/books/book-iii/part-08-where-physics-lives/chapter-54-the-global-cartesian-gluing/"
right_rail:
  related:
    -
      title: "Book III: Categorical Spectrum"
      url: "/corpus/monographs/book-iii/"
    -
      title: "Part VIII: Where Physics Lives"
      url: "/corpus/monographs/book-iii/part-08-where-physics-lives/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-iii/"
    -
      title: "Registry"
      url: "/registry/books/book-iii/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book III"
    part: "Part VIII"
    layer: "E₀ Mathematics (Hinge)"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 39
construction_layer: "physics"
construction_layer_label: "Physics"
construction_step_ids:
  - "CS-04"
  - "CS-05"
---

Chapter 1 posed the driving question: where does three-dimensional Cartesian space come from? Chapter 2 identified eight coherence guarantees. Chapter 53 exhibited every guarantee as a named structural force backed by an earned theorem. This chapter assembles the payoff. The eight forces constrain the transition maps between overlapping local Hartogs bulks to mutual compatibility, and the Global Cartesian Gluing Theorem (*III.T50*) proves the local projections glue into a unique, globally coherent three-dimensional space M_{τ³}. The Minkowski Extension (*III.D76*) adjoins time as the temporal base τ¹, producing 3+1-dimensional spacetime with Lorentzian signature earned from the split-complex boundary ring. The Constants Firewall separates Book III's structural provision from the values that Books IV–V supply.

## What this chapter contributes

Section 1 establishes the local-to-global argument. At each worldline point x ∈ τ¹, the fiber T²_x of the fibration τ³ = τ¹ ×_f T² is a two-dimensional surface, and the τ-Hartogs extension projects holomorphic data from this surface into a three-dimensional interior — the local Hartogs bulk U_x. For two overlapping worldline points x, y, the transition map φ_{xy}: U_x ∩ U_y → U_x ∩ U_y records how coordinates at x relate to those at y. Each of the eight structural forces imposes a specific compatibility condition on these transition maps: the Spatial Force (Poincaré) ensures φ_{xy} is orientation-preserving and contractible; the Harmonic Force (RH) ensures φ_{xy} preserves the bipolar χ⁺/χ⁻ decomposition; the Regular Force (NS) guarantees φ_{xy} is a diffeomorphism; the Discrete Force (YM) prevents zero-energy modes from accumulating across boundaries; the Legible Force (Hodge) provides NF-addressable labels for overlaps; the Codable Force (BSD) equips the address system with discrete rational-point labels; the Coherent Force (Langlands) supplies the cocycle condition on triple overlaps via boundary functoriality; and the Predictive Force (P vs NP) guarantees the glued structure supports computable witness search.

Section 2 states and proves the Global Cartesian Gluing Theorem (*III.T50*): the local bulks glue into a three-dimensional space M_{τ³} = colim_{x∈τ¹} U_x that is simply connected, spectrally pure, smooth, discrete at ground level, legible, and codable. The proof assembles in five steps: local data from the τ-Hartogs extension; overlap compatibility via three forces (Regular, Harmonic, Discrete); cocycle closure via the Coherent Force with algebraic addresses from the Legible and Codable Forces; global assembly as a colimit unique by rigidity; and canonicality from the No Knobs Theorem (*III.T42*) — every coupling in the transition data is a rational function of ι_τ = 2/(π + e), admitting no free parameters.

Section 3 proves the decompactification limit: as the primorial depth R → ∞, τ³_R → ℝ³, recovering Euclidean three-space with O(ι_τ²) corrections. Newton's law, Maxwell's equations, and Einstein's field equations all emerge at leading order.

Section 4 introduces the Minkowski Extension (*III.D76*): M_τ = τ¹ × M_{τ³}, where the base τ¹ provides the temporal direction and the split-complex boundary ring H_τ = ℤ[j]/(j²−1) forces the Lorentzian signature (−,+,+,+). The split-complex unit j with j² = +1 was forced algebraically by the boundary ring of T² — no choice among signatures arises. Null directions are the zero divisors of H_τ; their global assembly via the Coherent Force produces the causal structure of spacetime.

Section 5 states the Constants Firewall: Book III provides the 4+1 sector decomposition, coupling ratios as rational functions of ι_τ, and the Hinge Theorem (*III.T41*) assigning each downstream book to a specific sector. Books IV–V provide α_EM, G_N, ℏ, and c. No physical constant appears in Book III; constants require a carrier — a specific sector at a specific enrichment level — and carriers have not yet been instantiated here.

## Lean coverage

The proof of *III.T50* cites only earned results at every step. Canonicality depends on *III.T42* (No Knobs); simple connectivity on *III.P13* (Poincaré Gluing Guarantee); cocycle closure on *III.T36* (Functoriality). The Constants Firewall is enforced by the scope boundary of the Hinge Theorem (*III.T41*, Ch. 50): Book III builds the scaffold; the physical values are the business of the downstream books specified by the export contracts of Chapter 51.

## Where this leads

Chapter 55 synthesises: it identifies E₁ as the structural layer where physics becomes definable, presents the E₁-complete export contracts to Books IV and V from a physics perspective, and previews the E₁→E₂ transition that opens Part IX. The Global Cartesian Gluing is the geometric content of that identification; the Minkowski Extension is the causal content.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-03/part08/ch75-the-global-cartesian-gluing.tex -->
