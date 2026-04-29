---
layout: "corpus-monograph-chapter"
title: "Chapter 36: Core Collapse and Supernovae"
permalink: "/corpus/monographs/book-v/part-05-global-structure/chapter-37-core-collapse-and-supernovae/"
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
chapter_number: 37
chapter_slug: "chapter-37-core-collapse-and-supernovae"
page_in_book: 261
prev_chapter_url: "/corpus/monographs/book-v/part-05-global-structure/chapter-35-the-compact-object-ladder/"
prev_chapter_title: "Chapter 35: The Compact-Object Ladder"
next_chapter_url: "/corpus/monographs/book-v/part-05-global-structure/chapter-37-accretion-jets-and-active-galactic-nuclei/"
next_chapter_title: "Chapter 37: Accretion, Jets, and Active Galactic Nuclei"
summary_short: "Core collapse is a topological channel opening in the defect functional — not a failure of pressure support — and the bounce-and-revival explosion is a channel reversal that forges heavy elements through the r-process nucleosynthesis bridge."
canonical_book_url: "/corpus/monographs/book-v/"
canonical_book_title: "Book V: Categorical Macrocosm"
canonical_part_url: "/corpus/monographs/book-v/part-05-global-structure/"
canonical_part_title: "Global Structure"
publication_book_url: "/publications/books/book-v/"
legacy_publication_url: "/publications/books/book-v/part-05-global-structure/chapter-37-core-collapse-and-supernovae/"
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

A massive star (M_ZAMS ≳ 8 M_☉) fuses heavier and heavier elements in concentric shells:
hydrogen, helium, carbon, neon, oxygen, silicon.
When the iron core reaches the Chandrasekhar mass,
no further nuclear fusion can release energy
(iron has the maximum binding energy per nucleon).
In less than one second the core collapses.
What follows is one of the most violent events in the universe: a core-collapse supernova.
This chapter interprets the collapse in the language of Category τ.
The trigger is not a failure of pressure support in the naïve sense.
It is the **opening of a topological channel** —
a transition in the defect functional from d_top = 0 to d_top > 0 —
that occurs when the GR tension
(the difference between D-sector curvature and fiber-sector pressure)
exceeds a critical threshold.
The explosion mechanism (the bounce-and-revival of the shock)
is reinterpreted as a **channel reversal**:
the topological channel that opened inward during collapse
reverses direction at nuclear density, driving a shock outward.
The neutrino-driven mechanism is an A-sector (Weak) energy transfer
from the proto-neutron star to the stalled shock.
The chapter closes with the nucleosynthesis bridge:
the explosive environment forges elements heavier than iron
through rapid neutron capture (the r-process),
connecting the death of a star to the periodic table of Book IV.

## What this chapter contributes

**Definitions**
- *Topological Channel* (*V.D126*, τ-effective) — the set of energetically accessible paths in defect space that increase d_top; closed when all such paths cost energy, open when at least one is favourable.

**Key results**
- *Core Collapse Trigger* (*V.T89*, τ-effective) — the topological channel opens when M_c ≥ M_Ch^eff := M_Ch(1 − f_ec(Y_e)); electron-capture correction f_ec(Y_e) reduces the effective threshold as Y_e drops below 0.5.
- *Channel Reversal as Bounce Mechanism* (τ-effective) — at nuclear saturation density the defect functional barrier reverses; the inward-moving channel front halts and drives a shock outward; orthodox "bounce and revival" is the readout of this reversal.
- *Neutrino-Driven Revival as A-Sector Transfer* (τ-effective) — ~10% of the ~3×10⁵³ erg neutrino luminosity is deposited into the shock via A-sector (Weak) cross-coupling κ(A,D); this is structurally necessary and sufficient to revive the stalled shock.
- *r-Process Nucleosynthesis Bridge* (τ-effective) — the neutron-rich environment of the channel-reversal outflow drives rapid neutron capture; heavy elements are produced and distributed, closing the density-gradient arc from primordial H/He to the full periodic table (Book IV, ch48–49).

**Notation**
d_top (topological defect component), f_ec(Y_e) (electron-capture correction), M_Ch^eff (effective Chandrasekhar mass at finite Y_e).

**Dependencies**
- τ-Einstein equation (ch13), TOV star builder (ch17), TOV phase boundary (ch18)
- Compact-object ladder and Chandrasekhar mass (ch35)
- Defect functional IV.D09; periodic table and nucleosynthesis IV.ch48–49

## Lean coverage

`TauLib.BookV.GlobalStructure.CoreCollapseSupernovae` — topological channel definition and trigger theorem. Channel-reversal mechanism and neutrino-revival proposition are structurally grounded but proof details deferred; r-process bridge is schematic.

## Where this leads

The neutron star remnant produced by the channel reversal is the prototype compact object for accretion (Chapter 37) and binary merger (Chapter 38), and the heavy elements it disperses are the raw material for the stellar populations whose galactic-scale motions were analysed in Chapters 33 and 34.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-05/part05/ch39-core-collapse-supernovae.tex -->
