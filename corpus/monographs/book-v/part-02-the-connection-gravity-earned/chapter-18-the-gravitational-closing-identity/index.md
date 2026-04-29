---
layout: "corpus-monograph-chapter"
title: "Chapter 18: The Gravitational Closing Identity"
permalink: "/corpus/monographs/book-v/part-02-the-connection-gravity-earned/chapter-18-the-gravitational-closing-identity/"
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
chapter_number: 18
chapter_slug: "chapter-18-the-gravitational-closing-identity"
page_in_book: 123
prev_chapter_url: "/corpus/monographs/book-v/part-02-the-connection-gravity-earned/chapter-17-the-calibration-triangle-neutron/"
prev_chapter_title: "Chapter 17: The Calibration Triangle: Neutron →"
next_chapter_url: "/corpus/monographs/book-v/part-03-what-propagates-thermodynamic-inversion/chapter-19-the-180-thermodynamic-inversion/"
next_chapter_title: "Chapter 19: The 180^ Thermodynamic Inversion"
summary_short: "The gravitational closing identity α_G = α¹⁸ · √3 · (1 − (3/π)α) connects the gravitational coupling to the fine-structure constant through a 10-link derivation chain. The torus-vacuum route and the neutronic mass-hierarchy route agree to 3 ppm of CODATA. The coefficient c₁ = 3/π is conjectural; the exponent 18 and √3 factor are derived."
canonical_book_url: "/corpus/monographs/book-v/"
canonical_book_title: "Book V: Categorical Macrocosm"
canonical_part_url: "/corpus/monographs/book-v/part-02-the-connection-gravity-earned/"
canonical_part_title: "The Connection: Gravity Earned"
publication_book_url: "/publications/books/book-v/"
legacy_publication_url: "/publications/books/book-v/part-02-the-connection-gravity-earned/chapter-18-the-gravitational-closing-identity/"
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

Two independent derivation routes lead from the τ axioms to the gravitational constant G. Route 1 passes through the torus vacuum geometry: G = (c³/ℏ)ι_τ² (*V.D02*). Route 2 passes through the neutronic mass hierarchy: the gravitational fine-structure constant α_G = Gm_n²/(ℏc) is connected to the electromagnetic fine-structure constant α through the mass-ratio formula R = m_n/m_e — itself a τ-native derived quantity. For the framework to be internally consistent, these two routes must agree. The *gravitational closing identity* (*V.D11*) is the statement that they do:

α_G = α¹⁸ · √3 · (1 − c₁α),   where c₁ = 3/π

The chapter derives this identity through a 10-link chain from the axioms K0–K6 to the predicted value G ≈ 6.674 × 10⁻¹¹ N·m²·kg⁻², matching CODATA to within 3 ppm. Each factor has a structural origin: the exponent 18 = 3×3×2 counts the composition of three sector projections each of dimension 3, with a 2-fold fiber doubling; the √3 factor arises from the tree-level co-rotor coupling κ_n = 2√3 (*V.D10*); and the leading-order correction factor (1 − c₁α) encodes the first EM-gravitational mixing term. An important honesty note: the derivation of c₁ = 3/π is *conjectural* — the geometric argument for why the coefficient takes this specific value is present in the manuscript but not yet fully rigorous. The exponent 18 and the √3 factor are on firm τ-effective footing. The chapter also establishes R-formula independence (*V.R03*): the mass-ratio formula R = ι_τ⁻⁷ − (√3 + π³α²)ι_τ⁻² is a separate structural result that does not depend on the closing identity. This independence means the two routes to G are genuinely distinct, not circular.

## What this chapter contributes

**Definitions and axioms**

- *V.D10* — Co-rotor coupling: κ_n = 2√3 at tree level; the coupling constant governing the mixing between the gravitational D-sector and the electroweak sector; derived from the sector geometry
- *V.D11* — Gravitational closing identity: α_G = α¹⁸ · (χκ_n/2); expanded as α_G = α¹⁸ · √3 · (1 − (3/π)α); the master relation connecting the weakest and strongest measurable couplings

**Key results**

- Gravitational closing identity (*V.D11*): the two independent routes to G agree; G is predicted to 3 ppm of CODATA
- The exponent 18 = 3×3×2 is derived from the sector composition structure
- The factor √3 arises from the tree-level co-rotor coupling κ_n = 2√3 (*V.D10*)
- The coefficient c₁ = 3/π is *conjectural*: the geometric derivation is outlined but not yet fully rigorous at this stage
- R-formula independence (*V.R03*): the mass-ratio formula is a separate structural theorem, not a consequence of *V.D11*; the derivation chain is not circular
- Signature rigidity: the closing identity is robust to small deformations of the τ axioms; its qualitative form (α^18 leading term) cannot be changed by minor modifications
- 10-link derivation chain: the full pipeline from K0–K6 to m_e = 0.510 998 937 MeV is recapitulated

**Notation introduced**

- α_G = Gm_n²/(ℏc): gravitational fine-structure constant
- κ_n = 2√3: tree-level co-rotor coupling
- c₁ = 3/π: first EM-gravitational mixing coefficient (conjectural derivation)

**Dependencies**

- *V.D02* (Chapter 9): torus-vacuum route to G
- Book III, *III.T19*, *III.T27*: sector composition and coupling algebra

## Lean coverage

The co-rotor coupling definition (*V.D10*) and the closing identity statement (*V.D11*) are formalized in `TauLib.BookV.Gravity.CoRotorCoupling`. The Lean module establishes the tree-level value of κ_n and the structure of the exponent-18 term. The conjectural c₁ = 3/π coefficient is flagged as a `sorry`-bearing proposition pending a complete geometric derivation.

## Where this leads

The gravitational closing identity is the capstone of Part II: it closes the circle between the fiber physics of Book IV (electromagnetism, mass ratios) and the base physics of Book V (gravity, spacetime). Part III turns to what propagates in this framework — the thermodynamic structure that emerges from the τ³ fibration.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-05/part02/ch20-gravitational-closing-identity.tex -->
