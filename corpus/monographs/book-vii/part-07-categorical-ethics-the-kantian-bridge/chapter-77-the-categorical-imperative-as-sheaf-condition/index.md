---
layout: "corpus-monograph-chapter"
title: "Chapter 77: The Categorical Imperative as Sheaf Condition"
permalink: "/corpus/monographs/book-vii/part-07-categorical-ethics-the-kantian-bridge/chapter-77-the-categorical-imperative-as-sheaf-condition/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "VII"
book_slug: "book-vii"
part_number: 7
part_display: "Part VII"
part_slug: "part-07-categorical-ethics-the-kantian-bridge"
chapter_number: 77
chapter_slug: "chapter-77-the-categorical-imperative-as-sheaf-condition"
page_in_book: 283
prev_chapter_url: "/corpus/monographs/book-vii/part-07-categorical-ethics-the-kantian-bridge/chapter-76-dignity-as-meta-ethical-foundation/"
prev_chapter_title: "Chapter 76: Dignity as Meta-Ethical Foundation"
next_chapter_url: "/corpus/monographs/book-vii/part-07-categorical-ethics-the-kantian-bridge/chapter-78-the-no-conflict-theorem/"
next_chapter_title: "Chapter 78: The No-Conflict Theorem"
summary_short: "Kant's categorical imperative is the sheaf condition on the presheaf of dignity-filtered enactments over the Grothendieck site of rational perspectives: a maxim is universalizable iff its local enactments glue uniquely into a global section."
canonical_book_url: "/corpus/monographs/book-vii/"
canonical_book_title: "Book VII: Categorical Metaphysics"
canonical_part_url: "/corpus/monographs/book-vii/part-07-categorical-ethics-the-kantian-bridge/"
canonical_part_title: "Categorical Ethics & the Kantian Bridge"
publication_book_url: "/publications/books/book-vii/"
legacy_publication_url: "/publications/books/book-vii/part-07-categorical-ethics-the-kantian-bridge/chapter-77-the-categorical-imperative-as-sheaf-condition/"
right_rail:
  related:
    -
      title: "Book VII: Categorical Metaphysics"
      url: "/corpus/monographs/book-vii/"
    -
      title: "Part VII: Categorical Ethics & the Kantian Bridge"
      url: "/corpus/monographs/book-vii/part-07-categorical-ethics-the-kantian-bridge/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-vii/"
    -
      title: "Registry"
      url: "/registry/books/book-vii/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book VII"
    part: "Part VII"
    layer: "E₃ Metaphysics"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 75
construction_layer: "metaphysics"
construction_layer_label: "Metaphysics"
construction_step_ids:
  - "CS-08"
  - "CS-09"
  - "CS-10"
---

Inside the admissible world A_dig, which policies are universalizable? This chapter answers by translating Kant's categorical imperative into the language of sheaf theory. A proposed maxim M generates a presheaf Max_M over the Grothendieck site (P, J) of rational perspectives, assigning to each perspective the dignity-filtered enactments of M. The site's objects are agent-context perspectives (roles, situations, viewpoints), its morphisms are admissible reindexings preserving structural data, and its covering families encode the requirement that all relevant viewpoints are represented.

The CI as Naturality Constraint (VII.D66) requires that Max_M define a natural transformation with respect to all admissible reindexings — equivalently, that Max_M be separated: two enactments agreeing on every member of a covering family are identical. Separation is the precise categorical translation of Kant's first formulation: "Act only on that maxim which you can will as universal law" means the prescription must be stable under every admissible perspective change. A maxim that prescribes different actions depending on who enacts it, without structural justification, fails naturality and is rejected before the gluing check begins.

Full universalizability demands more: for every covering family and every compatible family of local enactments, there must exist a unique global enactment restricting to each local one. When this holds at the terminal cover, a single perspective-independent policy exists that every rational agent can adopt simultaneously. The CI-Sheaf Equivalence (VII.T31) proves that the sheaf condition is jointly equivalent to Kant's universalizability test, and also equivalent to the combination of naturality, local realizability, and trivially compatible cocycles. Failure modes are structurally classified: dignity breaks (non-separatedness, where relabeling breaks overlap agreement), Čech obstructions (contradiction in conception, nontrivial cocycles on triple overlaps preventing any global section), and tension obstructions (contradiction in will, where the global section forces unbounded tension). The second formulation — "treat persons always as ends, never merely as means" — is captured by the respect operator R acting as the identity on identity-invariants within each perspective. Under τ-holomorphy, local verification on a sufficiently fine cover propagates coherence to the entire τ-connected component by the identity principle.

## What this chapter contributes

- **Definitions / Axioms:** *VII.D66 — CI as Naturality Constraint* (τ-effective). Formalizes the categorical imperative as the requirement that Max_M be a separated presheaf on the site of rational perspectives, with restriction maps preserving enactment identity under perspective change.
- **Key results:** *VII.T31 — CI-Sheaf Equivalence*: Kantian universalizability is equivalent to the sheaf condition on Max_M; the three failure modes (dignity break, Čech obstruction, tension obstruction) correspond precisely to Kant's two contradiction types plus a pre-sheaf separatedness failure.
- **Notation introduced:** (P, J) (site of perspectives), Max_M (presheaf of enactments), respect operator R.
- **Dependencies:** VII.D65, VII.T30 (Chapter 76); Grothendieck site and sheaf theory; τ-holomorphy (Books I–II).

## Lean coverage

This chapter is prose-only at the current release; its content does not yet have a corresponding TauLib module. The sheaf-theoretic infrastructure (Grothendieck sites, Čech cohomology, separated presheaves) is available in Mathlib but has not been assembled into a dedicated ethics module.

## Where this leads

The CI-Sheaf Equivalence is the central formal result of Part VII. Chapter 78 applies it to prove that properly typed duties cannot conflict. Chapter 82 distils it into four decidable ethical tests. Chapter 88 deepens the result by showing that the CI is the unique minimal j-closed fixed point of the dignity modality.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-07/part07/ch77.tex -->
