---
layout: "corpus-monograph-chapter"
title: "Chapter 17: The Calibration Triangle: Neutron →"
permalink: "/corpus/monographs/book-v/part-02-the-connection-gravity-earned/chapter-17-the-calibration-triangle-neutron/"
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
chapter_number: 17
chapter_slug: "chapter-17-the-calibration-triangle-neutron"
page_in_book: 117
prev_chapter_url: "/corpus/monographs/book-v/part-02-the-connection-gravity-earned/chapter-16-tov-phase-boundary-and-forced-topology-relaxation/"
prev_chapter_title: "Chapter 16: TOV Phase Boundary and Forced Topology Relaxation"
next_chapter_url: "/corpus/monographs/book-v/part-02-the-connection-gravity-earned/chapter-18-the-gravitational-closing-identity/"
next_chapter_title: "Chapter 18: The Gravitational Closing Identity"
summary_short: "The calibration triangle connects three scales — neutron (micro), TOV limit (meso), and minimal black hole (macro) — through dimensionless ratios Ξ_τ = (1−ι_τ)·ι_τ, all internal to Category τ. SI units enter only as readout conventions; the structural relations among the three vertices are derivable from ι_τ alone."
canonical_book_url: "/corpus/monographs/book-v/"
canonical_book_title: "Book V: Categorical Macrocosm"
canonical_part_url: "/corpus/monographs/book-v/part-02-the-connection-gravity-earned/"
canonical_part_title: "The Connection: Gravity Earned"
publication_book_url: "/publications/books/book-v/"
legacy_publication_url: "/publications/books/book-v/part-02-the-connection-gravity-earned/chapter-17-the-calibration-triangle-neutron/"
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

Book IV fixed the neutron mass m_n as the single SI-unit anchor from which all microphysical quantities — electron mass, proton mass, coupling constants — were derived. But m_n is an SI quantity, and the τ-framework is intrinsically unit-free. To connect the unit-free structural relations of Category τ to the world of measured values, a calibration pipeline is needed. This chapter constructs the *calibration triangle*: a three-vertex diagram whose vertices are the neutron micro-scale (N), the TOV stability limit meso-scale (T), and the minimal black hole macro-scale (B). The edges of the triangle are dimensionless ratios expressible in terms of the calibration constant Ξ_τ = (1−ι_τ)·ι_τ. The central result is that the entire triangle is internal to Category τ: the ratios among N, T, and B are determined by the τ axioms (K0–K6) and the master constant ι_τ without any SI input. SI units enter only when the triangle is read out via the readout functor Φ_{p,n} — as conventions, not as structural inputs. The chapter proves the complete dimensional bridge theorem: the ring homomorphism Φ_{p,n} from τ-native calibration constants to SI-unit quantities is well-defined and surjective onto the empirically accessible part of the parameter space. The truncation-pipeline coherence property (*V.P132*) ensures that the calibration is independent of the truncation level at which the τ-NF iteration is stopped.

## What this chapter contributes

**Definitions and axioms**

- *Calibration constant* Ξ_τ = (1−ι_τ)·ι_τ: the dimensionless ratio connecting the three vertices of the calibration triangle; derivable from ι_τ alone
- *Calibration triangle*: the three-vertex diagram (N: neutron, T: TOV limit, B: minimal BH) with edges labeled by Ξ_τ-ratios; a purely τ-native object
- *V.P132* — Truncation-pipeline coherence: the property that the calibration constant Ξ_τ is independent of the truncation level chosen in the τ-NF iteration

**Key results**

- Complete dimensional bridge theorem: the ring homomorphism Φ_{p,n}: τ-native constants → SI-measured values is well-defined; SI is a readout convention, not a structural input
- The three calibration ratios (N→T, T→B, B→N) are all derivable from Ξ_τ = (1−ι_τ)·ι_τ
- The micro–macro scale bridge is internal to Category τ: no external dimensional analysis is required
- Truncation invariance: the calibration triangle is stable under refinement, consistent with *V.P132*

**Notation introduced**

- Ξ_τ = (1−ι_τ)·ι_τ: calibration constant
- Φ_{p,n}: the readout (ring homomorphism) from τ-native calibration constants to SI-unit quantities
- N, T, B: shorthand labels for the three vertices of the calibration triangle

**Dependencies**

- Book III, *III.T28*, *III.T42*: carrier coherence and dimensional bridge theorems for ω-germs
- Chapters 15–16 (star builder and topology relaxation): supply the T and B vertex definitions

## Lean coverage

No standalone Lean module is named for the calibration triangle. The ring homomorphism Φ_{p,n} and the truncation-pipeline coherence property *V.P132* are established as propositions in the `TauLib.BookV.GravityField.TOVStarBuilder` module and its dependencies.

## Where this leads

The calibration triangle closes the micro-to-macro pipeline. Chapter 18 uses it as one of two independent routes to the gravitational constant — the other being the torus vacuum — and proves that the two routes agree: the gravitational closing identity.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-05/part02/ch19-calibration-triangle.tex -->
