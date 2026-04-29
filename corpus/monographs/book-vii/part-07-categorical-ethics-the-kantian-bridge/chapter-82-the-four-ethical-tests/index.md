---
layout: "corpus-monograph-chapter"
title: "Chapter 82: The Four Ethical Tests"
permalink: "/corpus/monographs/book-vii/part-07-categorical-ethics-the-kantian-bridge/chapter-82-the-four-ethical-tests/"
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
chapter_number: 82
chapter_slug: "chapter-82-the-four-ethical-tests"
page_in_book: 299
prev_chapter_url: "/corpus/monographs/book-vii/part-07-categorical-ethics-the-kantian-bridge/chapter-81-monodromy-and-moral-ambiguity/"
prev_chapter_title: "Chapter 81: Monodromy and Moral Ambiguity"
next_chapter_url: "/corpus/monographs/book-vii/part-07-categorical-ethics-the-kantian-bridge/chapter-83-thermodynamic-ethics/"
next_chapter_title: "Chapter 83: Thermodynamic Ethics"
summary_short: "The structural tools of Chapters 76–81 distil into four decidable tests — universalizability, respect, coherence, monodromy — forming an interlocking filter; a single failure rejects a maxim as inadmissible."
canonical_book_url: "/corpus/monographs/book-vii/"
canonical_book_title: "Book VII: Categorical Metaphysics"
canonical_part_url: "/corpus/monographs/book-vii/part-07-categorical-ethics-the-kantian-bridge/"
canonical_part_title: "Categorical Ethics & the Kantian Bridge"
publication_book_url: "/publications/books/book-vii/"
legacy_publication_url: "/publications/books/book-vii/part-07-categorical-ethics-the-kantian-bridge/chapter-82-the-four-ethical-tests/"
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

The preceding five chapters have established the structural ingredients of categorical ethics — dignity as label-independence, the CI as sheaf condition, the no-conflict theorem, the fairness protocol, and monodromy as moral diagnostic. This chapter asks whether they can be distilled into a practical procedure: given a proposed maxim M and a site of perspectives (P_T, J_T) with a sufficiently fine cover, can admissibility be checked in finitely many steps?

The answer is yes. The procedure runs as follows. First, specify the relevant site and form local enactments s_i ∈ Max(U_i) on each chart. Then apply four tests, any single failure of which rejects the maxim. Test 1 (Universalizability) checks whether the local enactments produce vanishing Čech obstruction ω(M) = 0 in Ȟ¹(U, Max) and glue into a global section s ∈ Max(U). This is the formal test from Chapter 77: a liar who cannot will universal lying fails here, as does the free-rider who cannot will universal free-riding. Test 2 (Respect) verifies D(M(X)) ≅ D(X) for every affected agent X and σ ∘ M = M ∘ σ for all admissible isomorphisms σ — the maxim must preserve identity-invariants and commute with relabelings. Discriminatory exceptions based on contingent labels, and instrumentalization that erases autonomy, fail here. Test 3 (Coherence) confirms that the global section s obtained in Test 1 is compatible with the agent's existing duty portfolio — that the joint enactment of all accepted duties does not produce contradictions. When apparent conflicts arise, the no-conflict theorem directs toward the fairness protocols of Chapter 80. Test 4 (Monodromy Check) requires Hol_M(γ) = Id for all relevant loops γ — role-swaps, temporal cycles, stakeholder rotations — in the perspective space. Hidden exceptions that emerge under role reversal, and policies that shift costs into the future, fail here.

The Four Ethical Tests (VII.D69) packages all four conditions as a formal definition of admissibility. The tests are interlocking rather than independent: universalizability (Test 1) presupposes dignity (Test 2); coherence (Test 3) invokes the no-conflict theorem, which assumes the sheaf condition of Test 1; monodromy (Test 4) detects pathologies that survive Tests 1–3 but manifest under iterated perspective transport. The procedure is finite because the tests are local, operating on a finite cover and a small set of fundamental loops; τ-holomorphy supports propagation from local verification to global coherence.

## What this chapter contributes

- **Definitions / Axioms:** *VII.D69 — Four Ethical Tests* (τ-effective). Packages universalizability (Čech ω = 0), respect (D(M(X)) ≅ D(X) and relabeling commutativity), coherence (compatibility with existing duty portfolio), and monodromy (trivial holonomy on all relevant loops) into a single admissibility definition; a single failure rejects.
- **Key results:** **Key results:** none in formal-derivation form; this chapter establishes the finite, decidable procedure that integrates the results of Chapters 76–81 into a unified filter.
- **Dependencies:** VII.D65 (dignity), VII.T31 (CI as sheaf), VII.T32 (no-conflict), VII.D68, VII.T33 (monodromy).

## Lean coverage

This chapter is prose-only at the current release; its content does not yet have a corresponding TauLib module. The four conditions each correspond to existing mathematical notions formalizable in Mathlib (Čech cohomology, natural transformation, subsheaf intersection, holonomy).

## Where this leads

The four tests are the reference procedure for all subsequent applied chapters. Chapter 83 adds a quantitative ranking of admissible policies via the defect functional. Chapter 84 applies the tests to animal-directed policies, and Chapter 87 deploys them across bioethics, environmental ethics, and AI ethics.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-07/part07/ch82.tex -->
