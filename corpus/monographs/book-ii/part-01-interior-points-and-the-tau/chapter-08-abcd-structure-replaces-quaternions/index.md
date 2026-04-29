---
layout: "corpus-monograph-chapter"
title: "Chapter 8: ABCD Structure Replaces Quaternions"
permalink: "/corpus/monographs/book-ii/part-01-interior-points-and-the-tau/chapter-08-abcd-structure-replaces-quaternions/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "II"
book_slug: "book-ii"
part_number: 1
part_display: "Part I"
part_slug: "part-01-interior-points-and-the-tau"
chapter_number: 8
chapter_slug: "chapter-08-abcd-structure-replaces-quaternions"
page_in_book: 35
prev_chapter_url: "/corpus/monographs/book-ii/part-01-interior-points-and-the-tau/chapter-07-bipolar-decomposition-of-interior-points/"
prev_chapter_title: "Chapter 7: Bipolar Decomposition of Interior Points"
next_chapter_url: "/corpus/monographs/book-ii/part-02-local-domains-cylinders-as-prefix-predicates/chapter-09-cylinder-domains-from-abcd-refinement/"
next_chapter_title: "Chapter 9: Cylinder Domains from ABCD Refinement"
summary_short: "The 1st Edition's quaternionic proposal for the four-dimensional interior is corrected: quaternions require three imaginary units with i² = j² = k² = −1, but τ provides only j with j² = +1 and no earned noncommutativity; the ABCD fibration with bipolar decomposition supplies holomorphic rigidity without importing any external algebra."
canonical_book_url: "/corpus/monographs/book-ii/"
canonical_book_title: "Book II: Categorical Holomorphy"
canonical_part_url: "/corpus/monographs/book-ii/part-01-interior-points-and-the-tau/"
canonical_part_title: "Interior Points and the τ³"
publication_book_url: "/publications/books/book-ii/"
legacy_publication_url: "/publications/books/book-ii/part-01-interior-points-and-the-tau/chapter-08-abcd-structure-replaces-quaternions/"
right_rail:
  related:
    -
      title: "Book II: Categorical Holomorphy"
      url: "/corpus/monographs/book-ii/"
    -
      title: "Part I: Interior Points and the τ³"
      url: "/corpus/monographs/book-ii/part-01-interior-points-and-the-tau/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-ii/"
    -
      title: "Registry"
      url: "/registry/books/book-ii/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book II"
    part: "Part I"
    layer: "E₀ Mathematics"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 20
construction_layer: "mathematics"
construction_layer_label: "Mathematics"
construction_step_ids:
  - "CS-02"
  - "CS-03"
---

The 1st Edition of this book proposed the quaternion algebra ℍ = {a + bi + cj + dk : a, b, c, d ∈ ℝ} with i² = j² = k² = ijk = −1 as the algebraic skeleton of the four-dimensional interior of τ. The proposal was exploratory. This chapter corrects it by showing why quaternions are not earned and why the ABCD fibration together with the bipolar split-complex algebra H_τ provides the correct and sufficient replacement. The failure of the quaternionic proposal is not a matter of aesthetics but of structural incompatibility on three independent grounds: the coherence kernel furnishes only one algebraic unit beyond the identity (j with j² = +1, not three units with squares −1); the sign j² = +1 is incompatible with the j² = −1 required by the quaternionic multiplication table; and the quaternion algebra is noncommutative while H_τ is commutative by construction, with no source of anticommutativity in K₀–K₆.

## What this chapter contributes

- **Remark *II.R04* — ABCD vs Quaternions:** a comparative table recording the key structural differences: quaternionic scalar algebra ℍ (dim 4, noncommutative) vs. H_τ = ℤ̂_τ[j] (commutative); imaginary units i, j, k with squares −1 vs. j with square +1; no zero divisors (division algebra) vs. e₊ · e₋ = 0 (bipolar); coordinates ℝ⁴ (two-sided axes) vs. ℕ⁴ (one-sided rays); holomorphy from J² = −id on TM vs. holomorphy from ω-germ coherence; bipolarity not native (single S³) vs. native (e₊ and e₋ sectors). The quaternionic approach is not earned; the ABCD approach is.
- **Four canonical rays vs. four axes:** the ABCD coordinates take values in ℕ (one-sided rays), not ℝ (two-sided axes). There is no canonical negation —A or −B within τ. Cartesianizing the rays into axes would require a non-canonical choice not provided by the axioms. The one-sidedness is a structural feature, reflecting the directional character of the primorial ladder.
- **No tangent-bundle complex structure:** τ³ is a profinitely approximated discrete space with no tangent bundle, so there is no bundle endomorphism J : TM → TM on which J² = −id could be imposed. Holomorphy in τ is primitive (ω-germ coherence, *I.D47*), not derived from a complex structure. The split-complex unit j gives J² = +id (a para-complex structure, decomposing into two eigenspaces) — not a rotation but the sector splitting e₊ ⊕ e₋.
- **Proposition *II.P03* — Four-ray rigidity:** the four ABCD rays provide holomorphic rigidity without quaternionic algebra by combining (1) completeness (*I.T04*), (2) bipolar compatibility (sector inheritance from *II.P02*), (3) coherence constraint from the fibered product coupling, and (4) no imports — all structure is earned from K₀–K₆ and the five generators.

## Lean coverage

No Lean module is currently claimed. *II.P03* assembles results from `TauLib.BookI` (Hyperfactorization, bipolar algebra) and the earlier chapters of Book II; its formalization is planned in `TauLib.BookII.Interior.FourRayRigidity`.

## Where this leads

Part I is complete: τ³ has been defined as a set of τ-admissible quadruples (*II.D02*, *II.T01*), its boundary behavior analyzed via the omega readout (*II.D04*, *II.T02*), its fibration structure established (*II.D05*–*II.D07*, *II.T03*), and its bipolar decomposition extended to the interior (*II.D08*, *II.P02*). Part II (Local Domains: Cylinders as Prefix Predicates) begins earning topological structure by constructing cylinder domains from ABCD refinements.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-02/part01/ch08-abcd-vs-quaternions.tex -->
