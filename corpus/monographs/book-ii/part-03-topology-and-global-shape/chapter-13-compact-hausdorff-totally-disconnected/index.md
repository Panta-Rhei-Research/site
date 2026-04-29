---
layout: "corpus-monograph-chapter"
title: "Chapter 13: Compact, Hausdorff, Totally Disconnected"
permalink: "/corpus/monographs/book-ii/part-03-topology-and-global-shape/chapter-13-compact-hausdorff-totally-disconnected/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "II"
book_slug: "book-ii"
part_number: 3
part_display: "Part III"
part_slug: "part-03-topology-and-global-shape"
chapter_number: 13
chapter_slug: "chapter-13-compact-hausdorff-totally-disconnected"
page_in_book: 61
prev_chapter_url: "/corpus/monographs/book-ii/part-02-local-domains-cylinders-as-prefix-predicates/chapter-12-split-complex-structure-not-yet-load-bearing/"
prev_chapter_title: "Chapter 12: Split-Complex Structure Not Yet Load-Bearing"
next_chapter_url: "/corpus/monographs/book-ii/part-03-topology-and-global-shape/chapter-14-topology-as-invariant-of-canonical-denotation/"
next_chapter_title: "Chapter 14: Topology as Invariant of Canonical Denotation"
summary_short: "Part III opens by proving the three global topological properties of τ³: compactness (inherent from the profinite inverse-limit structure, not added by compactification), the Hausdorff property (from the ultrametric), and total disconnectedness (from the clopen basis). Together these make τ³ a Stone space."
canonical_book_url: "/corpus/monographs/book-ii/"
canonical_book_title: "Book II: Categorical Holomorphy"
canonical_part_url: "/corpus/monographs/book-ii/part-03-topology-and-global-shape/"
canonical_part_title: "Topology and Global Shape"
publication_book_url: "/publications/books/book-ii/"
legacy_publication_url: "/publications/books/book-ii/part-03-topology-and-global-shape/chapter-13-compact-hausdorff-totally-disconnected/"
right_rail:
  related:
    -
      title: "Book II: Categorical Holomorphy"
      url: "/corpus/monographs/book-ii/"
    -
      title: "Part III: Topology and Global Shape"
      url: "/corpus/monographs/book-ii/part-03-topology-and-global-shape/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-ii/"
    -
      title: "Registry"
      url: "/registry/books/book-ii/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book II"
    part: "Part III"
    layer: "E₀ Mathematics"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 22
construction_layer: "mathematics"
construction_layer_label: "Mathematics"
construction_step_ids:
  - "CS-02"
  - "CS-03"
---

Part II earned the cylinder basis, the ultrametric distance, and the inverted dependency: holomorphic implies continuous. All three results were combinatorial — built from CRT reduction maps, prefix predicates, and first disagreement depth. Part III now promotes this combinatorial infrastructure to a full topological theory. This opening chapter proves the three fundamental global topological properties of τ³: **compactness** (every open cover has a finite subcover), the **Hausdorff** property (distinct points have disjoint neighbourhoods), and **total disconnectedness** (the only connected subsets are singletons). Together these make τ³ a **Stone space** — the Boolean dual of the algebra of cylinder predicates, equivalent characterizations of which include: compact Hausdorff with a clopen basis, and profinite space (inverse limit of finite discrete spaces). The compactness is *inherent*: it follows from τ³ = lim← ℤ/P_k and does not require a compactification procedure that adds points at infinity. The underlying algebraic structure is hyperbolic (j² = +1), not elliptic (i² = -1), and this distinction is critical: the classical Riemann sphere compactification ℂ ↪ S² produces positive curvature that destroys the Euclidean parallel postulate, while τ's profinite compactness remains flat and zero-dimensional.

## What this chapter contributes

Theorems *II.T07* (Compactness), *II.T08* (Hausdorff property), and *II.T09* (Total disconnectedness), together with Definition *II.D14* (Stone space). Compactness is proved twice: via Tychonoff applied to the product of finite discrete spaces, and via a τ-native pigeonhole argument that uses only finite cylinder partitions and countable dependent choice — avoiding full AC. Hausdorff separation is explicit: the separating stage k+1 = δ(x,y)+1 is computable from the ultrametric. Total disconnectedness uses only the clopen basis: any two-point subset is disconnected by the stage-(k+1) cylinder. The chapter also contrasts the classical elliptic compactification (ℂ ↪ S², which curves space and kills non-trivial holomorphy via Liouville) with τ's hyperbolic native compactness (flat profinite Stone space, admits non-trivial ω-germ transformers).

## Lean coverage

*TauLib.BookII.Topology.StoneSpace* (planned). Hausdorff and total disconnectedness are likely the first formal targets; compactness via the native pigeonhole argument requires countable dependent choice, which needs verification in the chosen Lean foundations.

## Where this leads

Stone space status is the platform for Chapter 14's uniqueness argument (any topology satisfying CRT continuity, Hausdorff, and compactness is the profinite topology) and Chapter 15's dimension theorem (dim_τ = 4 from four independent refinement rays). Stone duality — ultrafilters on Clop(τ³) correspond bijectively to coherent families, hence to points of τ³ — previews Book III's spectral analysis, where propositional atoms from cylinder predicates encode the topology logically. The hyperbolic advantage identified here (j² = +1 enables compactness without curvature) recurs when Part IV earns Euclidean geometry from the same totally disconnected Stone space: total disconnectedness does not block geometry because topology and geometry are parallel readouts, as Chapter 18 explains.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-02/part03/ch13-stone-space.tex -->
