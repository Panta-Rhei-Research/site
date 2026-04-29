---
layout: "corpus-monograph-part"
title: "Part IX: Earned Number Systems"
permalink: "/corpus/monographs/book-i/part-09-earned-number-systems/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Part"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_part"
book_id: "I"
book_slug: "book-i"
part_number: 9
part_display: "Part IX"
part_slug: "part-09-earned-number-systems"
chapter_count: 4
summary_short: "Part VIII introduced the number tower ℕ_τ ⊆ ℤ_τ ⊆ ℚ_τ ⊆ ℝ_τ ⊆ ℂ_τ (Chapter [ch:number-tower]), establishing definitions and basic properties for each level.…"
canonical_book_url: "/corpus/monographs/book-i/"
canonical_book_title: "Book I: Categorical Foundations"
publication_book_url: "/publications/books/book-i/"
legacy_publication_url: "/publications/books/book-i/part-09-earned-number-systems/"
right_rail:
  related:
    -
      title: "Book I: Categorical Foundations"
      url: "/corpus/monographs/book-i/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-i/"
    -
      title: "Registry"
      url: "/registry/books/book-i/"
  meta:
    type: "Corpus Monograph Part"
    book: "Book I"
    layer: "E₀ Mathematics"
    chapters: "4"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 10
construction_layer: "mathematics"
construction_layer_label: "Mathematics"
construction_step_ids:
  - "CS-01"
  - "CS-02"
chapter_refs:
  -
    id: "book-i-ch-36"
    chapter_number: 36
    title: "The Constructive Reals: Ordered Field and Completeness"
    url: "/corpus/monographs/book-i/part-09-earned-number-systems/chapter-36-the-constructive-reals-ordered-field-and-completeness/"
    slug: "chapter-36-the-constructive-reals-ordered-field-and-completeness"
  -
    id: "book-i-ch-37"
    chapter_number: 37
    title: "The Elliptic Complex Field"
    url: "/corpus/monographs/book-i/part-09-earned-number-systems/chapter-37-the-elliptic-complex-field/"
    slug: "chapter-37-the-elliptic-complex-field"
  -
    id: "book-i-ch-38"
    chapter_number: 38
    title: "The Elliptic Quaternions"
    url: "/corpus/monographs/book-i/part-09-earned-number-systems/chapter-38-the-elliptic-quaternions/"
    slug: "chapter-38-the-elliptic-quaternions"
  -
    id: "book-i-ch-39"
    chapter_number: 39
    title: "Cyclotomic Fields and Roots of Unity"
    url: "/corpus/monographs/book-i/part-09-earned-number-systems/chapter-39-cyclotomic-fields-and-roots-of-unity/"
    slug: "chapter-39-cyclotomic-fields-and-roots-of-unity"
registry_refs:
  -
    id: "I.D37"
    url: "/registry/object/I.D37/"
  -
    id: "I.R22"
    url: "/registry/object/I.R22/"
  -
    id: "I.T44"
    url: "/registry/object/I.T44/"
taulib_refs:
  -
    module: "TauLib.BookI.Boundary.Characters"
    title: "TauLib.BookI.Boundary.Characters"
    status: "available"
    url: "/corpus/taulib/docs/book-i-boundary-characters/"
    registry_ids:
      - "I.D37"
  -
    module: "TauLib.BookI.Boundary.Quaternions"
    title: "TauLib.BookI.Boundary.Quaternions"
    status: "available"
    url: "/corpus/taulib/docs/book-i-boundary-quaternions/"
    registry_ids:
      - "I.R22"
      - "I.T44"
  -
    module: "TauLib.BookI.KernelFoundation.ScalarBridges"
    title: "TauLib.BookI.KernelFoundation.ScalarBridges"
    status: "available"
    url: "/corpus/taulib/docs/book-i-kernel-foundation-scalar-bridges/"
    registry_ids:
      - "I.D37"
previous_part:
  construction_sequence: 9
  title: "The Spectral Ring"
  url: "/corpus/monographs/book-i/part-08-the-spectral-ring/"
next_part:
  construction_sequence: 11
  title: "Lemniscate Characters"
  url: "/corpus/monographs/book-i/part-10-lemniscate-characters/"
---

Part VIII introduced the number tower
ℕ_τ ⊆ ℤ_τ ⊆ ℚ_τ
⊆ ℝ_τ ⊆ ℂ_τ
,
establishing definitions and basic properties for each level.
The first three levels — naturals, integers, rationals —
were *fully earned* from the 7 axioms and 5 generators
via finite algebraic constructions.

This Part develops the upper levels of the tower
into fully operational algebraic objects.
The constructive reals ℝ_τ
receive their complete ordered field structure
and the Archimedean property that distinguishes them
from the profinite boundary ring ℤ_τ.
The elliptic complex field ℂ_τ = ℝ_τ[i]
with i² = -1 is placed alongside its hyperbolic counterpart
ℤ_τ[j] with j² = +1,
making the *elliptic–hyperbolic dichotomy* explicit.

Two new algebraic structures complete the picture.
The **elliptic quaternions**
ℍ_τ = ℝ_τ[i,j,k]
earn non-commutativity as a structural consequence
of extending beyond two dimensions,
and give τ its first non-commutative division algebra.
The **cyclotomic fields**
ℚ^cyc_τ = ℚ_τ(ζ_n)
connect the roots of unity
to the CRT decomposition that already pervades
the boundary ring and spectral characters,
providing the algebraic infrastructure
for Galois theory in later books.

Every construction in this Part is purely algebraic —
no topology, no geometry, no analysis beyond
the constructive Cauchy completion.
The number systems are hosted by the spectral character algebra
H_τ and serve as the scalar fields
for all subsequent enrichment layers.
