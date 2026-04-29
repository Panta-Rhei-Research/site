---
layout: "corpus-monograph-chapter"
title: "Chapter 49: The No-Shrink Theorem: Mature Black Holes Cannot Shrink"
permalink: "/corpus/monographs/book-v/part-06-eternal-dynamics/chapter-50-the-no-shrink-theorem-mature-black-holes-cannot-shrink/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "V"
book_slug: "book-v"
part_number: 6
part_display: "Part VI"
part_slug: "part-06-eternal-dynamics"
chapter_number: 50
chapter_slug: "chapter-50-the-no-shrink-theorem-mature-black-holes-cannot-shrink"
page_in_book: 383
prev_chapter_url: "/corpus/monographs/book-v/part-06-eternal-dynamics/chapter-48-black-hole-bipolarity-and-blueprint-fusion/"
prev_chapter_title: "Chapter 48: Black Hole Bipolarity and Blueprint Fusion"
next_chapter_url: "/corpus/monographs/book-v/part-06-eternal-dynamics/chapter-50-the-merger-normal-form-and-bh-astrophysics/"
next_chapter_title: "Chapter 50: The Merger Normal Form and BH Astrophysics"
summary_short: "Can a black hole lose mass? In orthodox general relativity, the answer was ``no'' until 1975. Hawking's celebrated calculation — quantum fields on a curved…"
canonical_book_url: "/corpus/monographs/book-v/"
canonical_book_title: "Book V: Categorical Macrocosm"
canonical_part_url: "/corpus/monographs/book-v/part-06-eternal-dynamics/"
canonical_part_title: "Eternal Dynamics"
publication_book_url: "/publications/books/book-v/"
legacy_publication_url: "/publications/books/book-v/part-06-eternal-dynamics/chapter-50-the-no-shrink-theorem-mature-black-holes-cannot-shrink/"
right_rail:
  related:
    -
      title: "Book V: Categorical Macrocosm"
      url: "/corpus/monographs/book-v/"
    -
      title: "Part VI: Eternal Dynamics"
      url: "/corpus/monographs/book-v/part-06-eternal-dynamics/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-v/"
    -
      title: "Registry"
      url: "/registry/books/book-v/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book V"
    part: "Part VI"
    layer: "E₁ Physics (Macrocosm)"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 57
construction_layer: "physics"
construction_layer_label: "Physics"
construction_step_ids:
  - "CS-05"
  - "CS-06"
---

Can a black hole lose mass? In orthodox general relativity, the answer was "no" until 1975. Hawking's celebrated calculation — quantum fields on a curved spacetime background — predicted thermal radiation at a temperature inversely proportional to mass, implying that black holes slowly evaporate and eventually disappear. This prediction created the information paradox: where does the information go when a black hole evaporates? Five decades of effort — from black hole complementarity to firewalls to replica wormholes — have not produced a consensus resolution. Category τ answers the original question differently. A *mature* black hole — one that has completed ringdown and achieved torus-vacuum stabilization — cannot lose mass. Hawking's thermal spectrum exists as a readout at the empirical layer, but it does not correspond to ontic mass loss. The information paradox dissolves: no information is lost because no mass is lost.

## What this chapter contributes

The chapter defines **maturity** (*V.D71*): a black hole is mature when its linking class is geometrically stable, all transient defect components (mobile, vorticity, compression) have relaxed to zero, and the boundary character coincides with the torus-vacuum state. The **No-Shrink Theorem** (*V.T40*, τ-effective, Lean-verified as `TauLib.BookV.Gravity.Schwarzschild.NoShrinkProperty`) proves that a mature black hole's mass is non-decreasing: mass decrease would require an increase in defect entropy S_def, which would violate the Categorical Second Law (Theorem from Chapter 21). The **Defect-Mass Coupling Theorem** (*V.T41*) establishes the quantitative link between the topological defect component d_top = 1 and the gravitational mass readout. The **Hawking Readout Proposition** (*V.P26*) reinterprets Hawking radiation not as ontic evaporation but as the Readout Gibbs State (*V.D276*) at the empirical layer: the Readout Temperature Theorem (*V.T217*) confirms the Planckian spectrum (*V.P148*) and standard T_H = ℏc³/(8πGMk_B) temperature formula as a chart-level consequence, while the No-Evaporation Corollary (*V.C12*) follows directly. A Wave-48D supplement provides the Readout Channel Entropy Bound (*V.T272*), Ontic Entropy Monotonicity (*V.T273*), and a Page Curve Analog (*V.P191*); V.OP6 (BH entropy Page curve) is now PARTIAL-IMPROVED. The **Permanence Hallmark** (*V.D72*) concept is introduced: a structural property that, once acquired, cannot be reversed. The No-Shrink Theorem is the first permanence hallmark and the third structural export to Book VI alongside bipolarity and the blueprint monoid.

## Lean coverage

`TauLib.BookV.Gravity.Schwarzschild` (`NoShrinkProperty` verified) — scope τ-effective throughout. The Hawking readout results are τ-effective; the conjectural element is the precise calibration of the readout temperature in SI units, which depends on the dimensional bridge from Part II. The Page Curve Analog is τ-effective with an honest caveat that the analogy is structural, not a derivation of the full Page curve from first principles.

## Where this leads

The No-Shrink Theorem is the stability pillar for the entire late-time cosmology. Chapter 50 (Merger Normal Form) uses it directly: the monotone growth of BH mass under mergers follows from the no-shrink property. Chapter 51 (Global Finiteness) relies on the non-decreasing count of topological excisions to bound the complexity of the universe. The Eternal Circulation endstate (Chapter 52) is stable because no BH can release its mass to reverse the entropy splitting. The Falsification Pack (Chapter 53) enters the no-evaporation prediction as a structural falsifier: confirmed Hawking evaporation of any mature black hole would invalidate the τ framework.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-05/part06/ch52-no-shrink-theorem.tex -->
