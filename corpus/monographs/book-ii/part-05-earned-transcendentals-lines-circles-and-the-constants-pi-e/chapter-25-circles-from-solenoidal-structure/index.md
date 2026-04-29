---
layout: "corpus-monograph-chapter"
title: "Chapter 25: Circles from Solenoidal Structure"
permalink: "/corpus/monographs/book-ii/part-05-earned-transcendentals-lines-circles-and-the-constants-pi-e/chapter-25-circles-from-solenoidal-structure/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "II"
book_slug: "book-ii"
part_number: 5
part_display: "Part V"
part_slug: "part-05-earned-transcendentals-lines-circles-and-the-constants-pi-e"
chapter_number: 25
chapter_slug: "chapter-25-circles-from-solenoidal-structure"
page_in_book: 119
prev_chapter_url: "/corpus/monographs/book-ii/part-05-earned-transcendentals-lines-circles-and-the-constants-pi-e/chapter-24-lines-from-countable-structure/"
prev_chapter_title: "Chapter 24: Lines from Countable Structure"
next_chapter_url: "/corpus/monographs/book-ii/part-05-earned-transcendentals-lines-circles-and-the-constants-pi-e/chapter-26-three-perspectives-on-pi/"
next_chapter_title: "Chapter 26: Three Perspectives on π"
summary_short: "The solenoidal circle — inverse limit of finite cyclic angular groups in the primorial tower — is constructed, and S¹ is identified as its Archimedean shadow via a continuous surjection, unifying geometric and topological circles without any ambient plane."
canonical_book_url: "/corpus/monographs/book-ii/"
canonical_book_title: "Book II: Categorical Holomorphy"
canonical_part_url: "/corpus/monographs/book-ii/part-05-earned-transcendentals-lines-circles-and-the-constants-pi-e/"
canonical_part_title: "Earned Transcendentals: Lines, Circles, and the Constants π, e, j"
publication_book_url: "/publications/books/book-ii/"
legacy_publication_url: "/publications/books/book-ii/part-05-earned-transcendentals-lines-circles-and-the-constants-pi-e/chapter-25-circles-from-solenoidal-structure/"
right_rail:
  related:
    -
      title: "Book II: Categorical Holomorphy"
      url: "/corpus/monographs/book-ii/"
    -
      title: "Part V: Earned Transcendentals: Lines, Circles, and the Constants π, e, j"
      url: "/corpus/monographs/book-ii/part-05-earned-transcendentals-lines-circles-and-the-constants-pi-e/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-ii/"
    -
      title: "Registry"
      url: "/registry/books/book-ii/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book II"
    part: "Part V"
    layer: "E₀ Mathematics"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 24
construction_layer: "mathematics"
construction_layer_label: "Mathematics"
construction_step_ids:
  - "CS-02"
  - "CS-03"
---

Chapter 24 earned the real line as the Archimedean shadow of the radial α-ray and introduced level circles Λ_k^X as finite cyclic groups at each NF stage. This chapter takes the inverse limit of those level circles along each angular direction X ∈ {A, B, C} and produces the *solenoidal circle* S^X = lim_← C_k^X — a compact, totally disconnected, torsion-free profinite group. The angular denotation map den^X : S^X → S¹ is a continuous surjection of topological groups (*II.T21*, *S¹ as Profinite Limit*): every point on the classical circle arises as the Archimedean limit of a coherent angular sequence, and no uncountable continuum is presupposed (consistent with I.T35). A key structural point is that torsion-freeness prevents any element from wrapping back in finitely many steps — the profinite circle is genuinely different from any finite cyclic group yet maps onto S¹. The three solenoidal circles S^A, S^B, S^C combine to give S^A × S^B × S^C with Archimedean projection S¹ × S¹ × S¹ = T³, manifesting the 1+3 split (II.T11) in angular terms: one base circle, two fiber circles. *II.D27* (*Geometric-Topological Unification*) identifies the geometric circle (constant ultrametric distance from center, measured through cylinder structure) with the topological circle (ℝ/ℤ, the unique compact connected 1-manifold) as the same Archimedean shadow of the solenoidal tower. The identification avoids both cos/sin and any ambient Euclidean plane; it rests entirely on the denotation map calibrated against the primorial inverse system. The chapter sets the stage for Chapter 26 by providing the earned circle S¹ that the Archimedes polygon sequence will approximate from within.

## What this chapter contributes

**Definitions / Axioms**
- *II.D26* — Solenoidal circle S^X: the inverse limit lim_← C_k^X of finite cyclic angular groups in direction X, with ultrametric, profinite group structure, and compactness
- *II.D27* — Geometric-Topological Unification: identification of S¹_geo = S¹_top = den^X(S^X), avoiding cos/sin and the ambient plane

**Key results**
- *II.T21* — *S¹ as Profinite Limit*: den^X : S^X → S¹ is a continuous surjection of topological groups; S¹ arises from countable data without uncountable posit; product map gives T³

**Notation**
- C_k^X for the stage-k angular cyclic group in direction X; Q_k^X = ∏ p_{j(m)} for the cumulative angular prime product; den^X for the angular denotation map

**Dependencies**
- *I.T04* (CRT independence), *I.T18*, *I.T35*, *II.D13* (ultrametric), *II.D14*, *II.D15*, *II.T11* (ABCD chart), *II.D24* (α-ray, Chapter 24), *II.D25* (level circles, Chapter 24), *II.T20* (Chapter 24)

## Lean coverage

`BookII.Transcendentals.Circles` (planned). No Lean proofs present at this writing.

## Where this leads

With S¹ in hand as an earned object, Chapter 26 can define the Archimedes polygon sequence on the solenoidal level circles and extract π as the circumference-to-diameter ratio of the limit circle. The fiber torus T² = S^B × S^C reappears throughout Parts VI–IX as the angular arena of holomorphic analysis.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-02/part05/ch24-circles-solenoidal.tex -->
