---
layout: "corpus-monograph-chapter"
title: "Chapter 33: The Consumer Mixer: Uniqueness on (γ, η)"
permalink: "/corpus/monographs/book-vi/part-06-consumer-animals-and-the-mixed-sector/chapter-33-the-consumer-mixer-uniqueness-on-gamma-eta/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "VI"
book_slug: "book-vi"
part_number: 6
part_display: "Part VI"
part_slug: "part-06-consumer-animals-and-the-mixed-sector"
chapter_number: 33
chapter_slug: "chapter-33-the-consumer-mixer-uniqueness-on-gamma-eta"
page_in_book: 197
prev_chapter_url: "/corpus/monographs/book-vi/part-05-closure-fungi-and-the-recycling-fiber/chapter-32-healing-regeneration-and-the-repair-budget/"
prev_chapter_title: "Chapter 32: Healing, Regeneration, and the Repair Budget"
next_chapter_url: "/corpus/monographs/book-vi/part-06-consumer-animals-and-the-mixed-sector/chapter-34-eukarya-as-fiber-enabled-regime-not-sector/"
next_chapter_title: "Chapter 34: Eukarya as Fiber-Enabled Regime, Not Sector"
summary_short: "The consumer sector is the unique mixed sector on the (γ, η) metabolic fiber pair. A consumer carrier couples production and recycling channels to acquire…"
canonical_book_url: "/corpus/monographs/book-vi/"
canonical_book_title: "Book VI: Categorical Life"
canonical_part_url: "/corpus/monographs/book-vi/part-06-consumer-animals-and-the-mixed-sector/"
canonical_part_title: "Consumer — Animals and the Mixed Sector"
publication_book_url: "/publications/books/book-vi/"
legacy_publication_url: "/publications/books/book-vi/part-06-consumer-animals-and-the-mixed-sector/chapter-33-the-consumer-mixer-uniqueness-on-gamma-eta/"
right_rail:
  related:
    -
      title: "Book VI: Categorical Life"
      url: "/corpus/monographs/book-vi/"
    -
      title: "Part VI: Consumer — Animals and the Mixed Sector"
      url: "/corpus/monographs/book-vi/part-06-consumer-animals-and-the-mixed-sector/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-vi/"
    -
      title: "Registry"
      url: "/registry/books/book-vi/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book VI"
    part: "Part VI"
    layer: "E₂ Life"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 65
construction_layer: "life"
construction_layer_label: "Life"
construction_step_ids:
  - "CS-07"
---

The consumer sector occupies a structurally singular position in the Life template: it is the one sector whose carriers must couple two fiber generators simultaneously. All four primitive sectors — persistence (α), agency (π), source (γ), closure (η) — are each dominated by a single generator. The consumer sector is dominated by the pair (γ, η), requiring nontrivial winding along both circles of the fiber torus T² = S¹ × S¹. The resulting mixed winding is not a design choice but a topological necessity: signature rigidity of τ³ forces exactly one stable mixed sector, and it falls on (γ, η). No base–base pairing and no base–fiber pairing can sustain a stable mixed Life loop, as the uniqueness theorem demonstrates. Animals are the biological archetype of this sector because they are obligate heterotrophs: they ingest other Life carriers, recycle the ingested structure (η winding), and synthesize their own biomass (γ winding). This coupling also imposes a structural requirement that no primitive sector faces — the consumer must model other Life carriers to acquire them, and modeling another carrier's distinction is SelfDesc applied to SelfDesc, the second-order evaluator Eval⁽²⁾ that serves as the bridge-head from E₂ (Life) to E₃ (Mind). The chapter also establishes the 4+1 structure of the sector template: four primitive sectors each dominated by a single generator, plus one compound consumer sector requiring simultaneous nontrivial winding on two generators. This asymmetry is not conventional; it is topological, and it is the reason prokaryotes inhabit the primitive sectors while complex multicellular animals occupy the mixed sector.

## What this chapter contributes

- **Defs/Axioms:** *VI.D46* — Consumer Mixer on (γ, η): the full subcategory of Loop_L with w_γ > 0, w_η > 0, and (γ, η) co-dominant winding.
- **Key results:** *VI.T25* — Signature Rigidity Determines Uniqueness: the consumer sector Con_(γ,η) is the unique mixed sector in the Life template; *VI.L07* — Consumer as Bridge-Head to E₃: Eval⁽²⁾ = Eval ∘ Eval is structurally prerequisite for E₃ enrichment and is required only by the consumer sector.
- **Notation:** w_γ, w_η for fiber winding numbers; Con_(γ,η) for the consumer sector subcategory; Eval⁽²⁾ for second-order self-evaluation.
- **Dependencies:** Sector template (Ch. 8), metabolic fiber decomposition (Part V), SelfDesc predicate (earlier in Book VI).

## Lean coverage

*TauLib.BookVI.Life.DefectFunctionals (ConsumerMixerUnique)* covers *VI.T25* and *VI.D46*. *VI.L07* is prose-level; the bridge-head argument depends on the SelfDesc formalization which is addressed in separate Lean files.

## Where this leads

The uniqueness result motivates the two corrections that follow: Chapter 34 separates the mixed sector from the Eukarya technology, and Chapters 35–42 develop the biological and cognitive consequences of the (γ, η) coupling for animals in particular.

<!-- regenerated 2026-04-29 | source: manuscript-sources/book-06/part06/ch33-consumer-mixer.tex -->
