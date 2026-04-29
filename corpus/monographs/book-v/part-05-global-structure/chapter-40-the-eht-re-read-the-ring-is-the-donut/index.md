---
layout: "corpus-monograph-chapter"
title: "Chapter 39: The EHT Re-Read: The Ring Is the Donut"
permalink: "/corpus/monographs/book-v/part-05-global-structure/chapter-40-the-eht-re-read-the-ring-is-the-donut/"
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
chapter_number: 40
chapter_slug: "chapter-40-the-eht-re-read-the-ring-is-the-donut"
page_in_book: 283
prev_chapter_url: "/corpus/monographs/book-v/part-05-global-structure/chapter-38-binary-mergers-and-gravitational-wave-readout/"
prev_chapter_title: "Chapter 38: Binary Mergers and Gravitational-Wave Readout"
next_chapter_url: "/corpus/monographs/book-v/part-05-global-structure/chapter-40-the-bullet-cluster-and-large-scale-structure/"
next_chapter_title: "Chapter 40: The Bullet Cluster and Large-Scale Structure"
summary_short: "The EHT ring images of M87* and Sgr A* are re-read as toroidal (T²) readouts — not S² photon spheres — and the Shadow Shape Theorem predicts discriminating signatures in inner-shadow ellipticity, photon subring spacing, and polarization winding."
canonical_book_url: "/corpus/monographs/book-v/"
canonical_book_title: "Book V: Categorical Macrocosm"
canonical_part_url: "/corpus/monographs/book-v/part-05-global-structure/"
canonical_part_title: "Global Structure"
publication_book_url: "/publications/books/book-v/"
legacy_publication_url: "/publications/books/book-v/part-05-global-structure/chapter-40-the-eht-re-read-the-ring-is-the-donut/"
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

In April 2019 the Event Horizon Telescope collaboration released the first image
of a black hole shadow: the supermassive object M87* at the centre of Messier 87.
The image showed a bright ring of emission surrounding a dark central region —
the shadow — with a diameter of ~42 μas,
consistent with the Schwarzschild prediction
for a 6.5 × 10⁹ M_☉ black hole at 16.8 Mpc.
In 2022, the EHT released a second shadow image:
Sgr A*, the 4.3 × 10⁶ M_☉ object at the centre of the Milky Way.
Both images were interpreted within GR,
where the shadow is cast by a spherical (S²) event horizon.
In Category τ the interpretation is fundamentally different.
**The shadow is a toroidal (T²) readout.**
The bright ring is not the photon sphere of a Schwarzschild metric;
it is the equatorial emission from the accretion funnel
wrapped around the *donut*, not the sphere.
The torus has a hole,
and the geodesic structure near the T² compact object differs
from the S² Schwarzschild geometry in three observable ways:
inner-shadow ellipticity (elongated along the torus axis),
photon subring spacing (set by the torus aspect ratio ι_τ),
and polarisation winding patterns (carrying a topological winding number).
This chapter develops the **Shadow Shape Theorem** (*V.T40*),
which quantifies all three differences and identifies them as falsifiable predictions
accessible to next-generation EHT observations with space baselines.
The bright rings of M87* and Sgr A* are re-read in detail,
showing that the current EHT data are consistent with both topologies
and that the discrimination requires the finer angular resolution of the planned space-VLBI array.

## What this chapter contributes

**Definitions**
- *Toroidal Shadow (T² Readout)* (*V.D58*, τ-effective) — the shadow boundary as the projection of the photon capture region of a T²-topology coherent instance; generically elliptical, elongated along the torus symmetry axis.
- *Photon Ring Winding Number* (*V.D59*, τ-effective) — integer n counting the number of half-orbits a photon completes before reaching the observer; discrete in T² topology due to the inner hole.
- *Polarisation Handedness Signature* (*V.D60*, τ-effective) — the net electric-vector position angle (EVPA) winding around the shadow boundary; encodes the topological index of the T² torus axis.

**Key results**
- *Shadow Shape Theorem* (*V.T40*, τ-effective) — a T² compact object of mass M and shape ratio ι_τ produces a shadow with axial ellipticity ε = ι_τ²/2 to leading order; for ι_τ ≈ 0.382, ε ≈ 0.073, discriminable at ~μas resolution.
- *Polarisation Winding Theorem* (*V.T41*, τ-effective) — the net EVPA winding around the shadow boundary is ±1 (mod 2) for T² topology vs. 0 for S² topology; the sign encodes the orientation of the torus axis relative to the observer.
- *Inner Shadow Ellipticity* (*V.P24*) — quantitative bound on the departure from circularity in the inner shadow region.
- *Photon Subring Spacing* (*V.P25*) — the angular spacing between successive photon subrings scales as exp(−π/|∂_θ g_φφ|) evaluated at the torus equator; differs from the S² Lyapunov exponent by a factor ~(1 + ι_τ).
- M87* and Sgr A* re-reads (*V.R32*, *V.R33*) — current EHT data are consistent with T² at the achieved angular resolution; predicted discriminators lie ~30% below current sensitivity.

**Notation**
ε (shadow ellipticity), n (photon ring winding number), EVPA winding (polarisation handedness), ι_τ (torus shape ratio).

**Dependencies**
- Schwarzschild solution (ch16), Jet Collimation Theorem (ch37), Accretion Funnel (ch37)
- τ³ arena and torus topology IV.D04; boundary holonomy IV.D05

## Lean coverage

`TauLib.BookV.Astrophysics.EHTReread` — shadow shape theorem, polarisation winding theorem, photon ring winding number definition. Inner ellipticity and subring spacing propositions are stated with proof sketches; full ray-tracing verification deferred to numerical companions.

## Where this leads

The toroidal-topology predictions of this chapter, combined with the ringdown-echo predictions of Chapter 38, constitute the observational programme for deciding between Category τ and general relativity at the event-horizon scale; Chapter 41 then shows algebraically why the S² interpretation requires a particle-physics sector that the framework cannot accommodate.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-05/part05/ch42-eht-reread.tex -->
