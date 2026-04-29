---
layout: "corpus-monograph-chapter"
title: "Chapter 14: The τ-Schwarzschild Readout: Torus Vacuum"
permalink: "/corpus/monographs/book-v/part-02-the-connection-gravity-earned/chapter-14-the-tau-schwarzschild-readout-torus-vacuum/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "V"
book_slug: "book-v"
part_number: 2
part_display: "Part II"
part_slug: "part-02-the-connection-gravity-earned"
chapter_number: 14
chapter_slug: "chapter-14-the-tau-schwarzschild-readout-torus-vacuum"
page_in_book: 93
prev_chapter_url: "/corpus/monographs/book-v/part-02-the-connection-gravity-earned/chapter-13-nonlinear-tau-einstein-address-resolution-not-pde-solving/"
prev_chapter_title: "Chapter 13: Nonlinear τ-Einstein: Address Resolution, Not PDE Solving"
next_chapter_url: "/corpus/monographs/book-v/part-02-the-connection-gravity-earned/chapter-15-tov-existence-and-the-star-builder/"
next_chapter_title: "Chapter 15: TOV Existence and the Star Builder"
summary_short: "The τ-Schwarzschild relation R_S = 2G_τM is derived as a readout of the stabilized torus vacuum, not from a PDE solution. The torus core replaces the classical singularity at r = 0, Hawking evaporation is structurally forbidden, and the No-Shrink Theorem (V.T03) bounds the minimum radius of any compact object."
canonical_book_url: "/corpus/monographs/book-v/"
canonical_book_title: "Book V: Categorical Macrocosm"
canonical_part_url: "/corpus/monographs/book-v/part-02-the-connection-gravity-earned/"
canonical_part_title: "The Connection: Gravity Earned"
publication_book_url: "/publications/books/book-v/"
legacy_publication_url: "/publications/books/book-v/part-02-the-connection-gravity-earned/chapter-14-the-tau-schwarzschild-readout-torus-vacuum/"
right_rail:
  related:
    -
      title: "Book V: Categorical Macrocosm"
      url: "/corpus/monographs/book-v/"
    -
      title: "Part II: The Connection: Gravity Earned"
      url: "/corpus/monographs/book-v/part-02-the-connection-gravity-earned/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-v/"
    -
      title: "Registry"
      url: "/registry/books/book-v/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book V"
    part: "Part II"
    layer: "E₁ Physics (Macrocosm)"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 53
construction_layer: "physics"
construction_layer_label: "Physics"
construction_step_ids:
  - "CS-05"
  - "CS-06"
---

The classical Schwarzschild solution — the first exact solution of the Einstein equations, obtained in 1916 — is a vacuum metric surrounding a spherically symmetric mass. It carries a coordinate singularity at r = R_S (removable by Kruskal–Szekeres coordinates) and a genuine curvature singularity at r = 0 (not removable). A century of subsequent work has clarified the first difficulty but not the second. This chapter derives the τ-native analogue not by solving a PDE on a manifold but by reading off the stabilized torus vacuum. The τ-native starting point is the torus vacuum *V.D01*: when the D-sector of the τ³ fibration saturates, the fiber torus T² settles into the stabilized shape with r/R = ι_τ. From this configuration, G_τ (*V.D02*) emerges as the coherence conversion invariant (*V.P01*) relating the radius index to the mass index. The Schwarzschild radius R_S = 2G_τM (*V.D08*) is then a theorem about the boundary character of the saturated D-sector, derived from *V.D01*, *V.D02*, and *V.T01*. It is important to be clear: R_S = 2G_τM is *derived*, not postulated. The orthodox Schwarzschild metric is recovered as a sphere-proxy corollary: the chart readout Φ_p projects the torus-shaped boundary character onto a spherically symmetric coordinate metric. No singularity forms at r = 0 because the profinite density cap prevents any boundary character from concentrating to a point; the torus core occupies the region that the orthodox solution assigns to the singularity. The chapter also establishes three modes of black hole evolution in the τ-framework (*V.D09*), previews the No-Shrink Theorem (*V.T03*), and proves that Hawking-type thermal evaporation is structurally absent in the τ formulation (*V.R02*).

## What this chapter contributes

**Definitions and axioms**

- *V.D07* — Schwarzschild boundary character: the unique zero-defect boundary character of the spherically symmetric D-sector vacuum; the τ-native object underlying the classical metric
- *V.D08* — τ-Schwarzschild radius: R_S = 2G_τM; derived from the stabilized torus vacuum geometry
- *V.D09* — Black hole evolution modes: the three structural evolution channels available to a saturated D-sector configuration (geometric relaxation, topological settling, and radiative discharge)
- *V.P01* — Coherence conversion invariant: G_τ as the canonical map from the mass index to the radius index in the D-sector; proven (not postulated) from the torus vacuum
- *V.T03* — No-Shrink Theorem (previewed here, proved in a later chapter): every compact object in the τ-framework has a minimum radius set by the torus core; no object can shrink to a point

**Key results**

- R_S = 2G_τM is *derived* from the stabilized torus vacuum; it is a theorem, not a definition
- The torus core structurally replaces the r = 0 singularity; no curvature singularity exists in the τ-native geometry
- Two-channel relaxation: geometric (shape normalization, fast) and topological (handle settling, slow)
- Hawking evaporation is structurally forbidden (*V.R02*): the thermal radiation mechanism depends on the point-singularity structure absent in the τ formulation
- Sphere-proxy corollary: the classical Schwarzschild metric is recovered as a chart shadow, confirming empirical adequacy in the weak-to-moderate field regime

**Dependencies**

- *V.D01*, *V.D02*, *V.T01* (Chapter 9): torus vacuum and gravitational constant
- *V.D06* (Chapter 11): τ-Einstein equation, whose nonlinear solution scheme (Chapter 13) yields the boundary character
- Book III, *III.T25*: fiber equilibrium and profinite density cap

## Lean coverage

The stabilized torus vacuum, coherence conversion invariant, and Schwarzschild radius derivation are formalized in `TauLib.BookV.Gravity.GravitationalConstant` (*V.D01*, *V.D02*, *V.T01*, *V.P01*) and `TauLib.BookV.Gravity.Schwarzschild` (*V.D07*, *V.D08*, *V.D09*, *V.T03*, *V.R02*).

## Where this leads

The torus-core black hole geometry feeds directly into the stellar structure analysis of Chapters 15–16, where the same stabilized torus vacuum appears as the endpoint of neutron-star collapse.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-05/part02/ch16-tau-schwarzschild.tex -->
