---
layout: "corpus-monograph-chapter"
title: "Chapter 34: Rotation Curves Without Dark Matter"
permalink: "/corpus/monographs/book-v/part-05-global-structure/chapter-35-rotation-curves-without-dark-matter/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "V"
book_slug: "book-v"
part_number: 5
part_display: "Part V"
part_slug: "part-05-global-structure"
chapter_number: 35
chapter_slug: "chapter-35-rotation-curves-without-dark-matter"
page_in_book: 241
prev_chapter_url: "/corpus/monographs/book-v/part-05-global-structure/chapter-33-the-galaxy-as-relational-object/"
prev_chapter_title: "Chapter 33: The Galaxy as Relational Object"
next_chapter_url: "/corpus/monographs/book-v/part-05-global-structure/chapter-35-the-compact-object-ladder/"
next_chapter_title: "Chapter 35: The Compact-Object Ladder"
summary_short: "The D-sector capacity gradient — forced by κ(D;1) = 1 − ι_τ with no free parameters — flattens spiral galaxy rotation curves without invoking dark matter halos."
canonical_book_url: "/corpus/monographs/book-v/"
canonical_book_title: "Book V: Categorical Macrocosm"
canonical_part_url: "/corpus/monographs/book-v/part-05-global-structure/"
canonical_part_title: "Global Structure"
publication_book_url: "/publications/books/book-v/"
legacy_publication_url: "/publications/books/book-v/part-05-global-structure/chapter-35-rotation-curves-without-dark-matter/"
right_rail:
  related:
    -
      title: "Book V: Categorical Macrocosm"
      url: "/corpus/monographs/book-v/"
    -
      title: "Part V: Global Structure"
      url: "/corpus/monographs/book-v/part-05-global-structure/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-v/"
    -
      title: "Registry"
      url: "/registry/books/book-v/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book V"
    part: "Part V"
    layer: "E₁ Physics (Macrocosm)"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 56
construction_layer: "physics"
construction_layer_label: "Physics"
construction_step_ids:
  - "CS-05"
  - "CS-06"
---

The flat rotation curves of spiral galaxies are the single most cited piece of evidence
for the existence of dark matter.
The observation is simple:
stellar and gas velocities at the periphery of spiral galaxies
do not decline as v ∝ r^{−1/2} (the Keplerian falloff predicted for the visible mass)
but remain approximately constant out to the last measured point.
In the dark matter paradigm this flatness is explained
by embedding the visible galaxy in an extended halo of non-baryonic dark matter
whose density profile is tuned to produce the observed curve.
This chapter provides the τ-native explanation.
The D-sector coupling κ(D;1) = 1 − ι_τ — a value forced by the No Knobs Theorem
(Book III, III.T42) with no free parameter — produces a capacity gradient ∇𝒞_D
at galactic scales that enhances the gravitational acceleration beyond the Newtonian prediction.
The enhancement is sufficient to flatten the rotation curve without introducing any new matter.
The chapter develops the capacity equation sourced by the baryonic density,
derives the flat-curve theorem, tests it galaxy-by-galaxy,
compares with MOND (identifying the MOND acceleration scale a₀
as a proxy for the classical validity scale ℓ_cl),
and catalogues falsifiable signatures by which future observations
can discriminate the τ-prediction from dark-matter halos.
The key structural feature is that the capacity profile 𝒞_D(r) is determined
by the τ-Einstein equation with the given baryonic boundary conditions —
no halo mass function, no concentration parameter, no fitting.

## What this chapter contributes

**Definitions**
- *Galactic Capacity Profile* (*V.D123*, τ-effective) — solution of the nonlinear capacity equation ∇²ln 𝒞_D = −(4πG/c²)Σ_b − ℓ_τ⁻² ln(𝒞_D/𝒞_D^∞); encodes both baryonic source and cosmological relaxation.

**Key results**
- *Flat Rotation Curve Theorem* (τ-effective) — v_c²(r) = v_N²(r) + v_cap²(r) where v_cap²(r) = −(c²r/2) ∂_r ln 𝒞_D(r); the capacity gradient supplies the surplus acceleration that orthodox analyses attribute to dark matter halos.
- *No-Free-Parameter Fit* (τ-effective) — κ(D;1) = 1 − ι_τ is fixed by No Knobs (III.T42); galaxy-by-galaxy variation is in boundary conditions, not in the dynamics.
- *MOND Scale as Classical Validity Proxy* (τ-effective) — Milgrom's a₀ ≈ 1.2×10⁻¹⁰ m/s² is the Newtonian acceleration at r = ℓ_cl for a typical galaxy; MOND is a phenomenological projection of the τ-two-regime readout.
- *Structural Impossibility of Dark Halos* (τ-effective) — the coupling budget is exhausted by four sectors (proved in Chapter 41); a fifth matter component has no available sector to inhabit.
- Falsifiable signatures catalogue: baryonic Tully-Fisher tightening, residual correlation with gas fraction, lensing-dynamical mass equality.

**Notation**
κ(D;1) = 1 − ι_τ (D-sector coupling), 𝒞_D^∞ (cosmological background capacity), ℓ_τ (τ-scale length), a₀ (MOND scale as ℓ_cl proxy).

**Dependencies**
- τ-Einstein equation (ch13), Schwarzschild solution (ch16)
- Capacity gradient and classical illusion (ch31); galaxy as relational object (ch33)
- D-sector coupling IV.D05; No Knobs Theorem Book III III.T42

## Lean coverage

`TauLib.BookV.GlobalStructure.RotationCurves` — capacity equation definition, flat-curve derivation, MOND comparison. Galaxy-by-galaxy quantitative fits are τ-effective in mechanism but conjectural in numerical detail; full numerical verification deferred.

## Where this leads

The no-free-parameter mechanism demonstrated here is the empirical anchor for the Sector Exhaustion Theorem of Chapter 41: because the rotation-curve data are fully explained by the existing four-sector structure, no observational pressure requires a fifth sector.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-05/part05/ch37-rotation-curves.tex -->
