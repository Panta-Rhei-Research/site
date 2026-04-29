---
layout: "corpus-monograph-chapter"
title: "Chapter 20: Entropy Splitting: S_def"
permalink: "/corpus/monographs/book-v/part-03-what-propagates-thermodynamic-inversion/chapter-20-entropy-splitting-sdef/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "V"
book_slug: "book-v"
part_number: 3
part_display: "Part III"
part_slug: "part-03-what-propagates-thermodynamic-inversion"
chapter_number: 20
chapter_slug: "chapter-20-entropy-splitting-sdef"
page_in_book: 143
prev_chapter_url: "/corpus/monographs/book-v/part-03-what-propagates-thermodynamic-inversion/chapter-19-the-180-thermodynamic-inversion/"
prev_chapter_title: "Chapter 19: The 180^ Thermodynamic Inversion"
next_chapter_url: "/corpus/monographs/book-v/part-03-what-propagates-thermodynamic-inversion/chapter-21-global-defect-exhaustion/"
next_chapter_title: "Chapter 21: Global Defect Exhaustion"
summary_short: "Chapter 19 announced the 180° thermodynamic inversion and stated the Categorical Second Law: defect entropy decreases along the α-orbit. The decomposition S = S_def + S_ref was previewed, not proved. This chapter supplies the proof — and explains why orthodox physics has always been measuring the wrong component."
canonical_book_url: "/corpus/monographs/book-v/"
canonical_book_title: "Book V: Categorical Macrocosm"
canonical_part_url: "/corpus/monographs/book-v/part-03-what-propagates-thermodynamic-inversion/"
canonical_part_title: "What Propagates: Thermodynamic Inversion"
publication_book_url: "/publications/books/book-v/"
legacy_publication_url: "/publications/books/book-v/part-03-what-propagates-thermodynamic-inversion/chapter-20-entropy-splitting-sdef/"
right_rail:
  related:
    -
      title: "Book V: Categorical Macrocosm"
      url: "/corpus/monographs/book-v/"
    -
      title: "Part III: What Propagates: Thermodynamic Inversion"
      url: "/corpus/monographs/book-v/part-03-what-propagates-thermodynamic-inversion/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-v/"
    -
      title: "Registry"
      url: "/registry/books/book-v/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book V"
    part: "Part III"
    layer: "E₁ Physics (Macrocosm)"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 54
construction_layer: "physics"
construction_layer_label: "Physics"
construction_step_ids:
  - "CS-05"
  - "CS-06"
---

Chapter 19 announced the 180° thermodynamic inversion and stated the Categorical Second Law: defect entropy decreases along the α-orbit. But the decomposition S = *S*_def + *S*_ref was previewed, not proved. This chapter supplies the proof. The construction is precise: *defect entropy* *S*_def counts holomorphic continuations that pass through at least one non-holomorphic insertion — a node where ∂̄_b f ≠ 0. *Refinement entropy* *S*_ref counts holomorphic continuations that remain holomorphic throughout, paths created by the refinement process itself with no physical defect content. The total holomorphic entropy from Book IV is their sum. The construction connects to the spectral trichotomy of Book III (*III.T14*): three spectral regimes map cleanly onto the two components, with the cross-term bounded and vanishing at the coherence horizon.

## What this chapter contributes

- **Entropy Splitting Theorem** (τ-effective): S(n) = *S*_def(n) + *S*_ref(n) + ε(n), where ε ≤ *S*_def and vanishes when *S*_def = 0.
- **Defect entropy** *S*_def: bounded above by the initial defect budget, monotonically decreasing at rate (1 − *ι*_τ) per orbit step, converging exponentially to zero at the coherence horizon.
- **Refinement entropy** *S*_ref: unbounded, monotonically increasing, growing as at least n·ln p per orbit step. The vacuum itself has nonzero *S*_ref — the ground state carries refinement entropy that carries no physical content.
- **Why the readout functor misreports**: the E₁ readout projects onto the total S, which is dominated by *S*_ref at late times. The decomposition is inaccessible to any E₁ measurement because the defect set 𝒟_n is a τ-native structure with no spatial readout.
- **The *ι*_τ-controlled crossover depth** n* at which defect entropy drops below refinement entropy — the epoch at which the classical second law becomes an accurate (if misleading) description.
- **Connection to the defect functional** δ[ω]: *S*_def = ln|supp(δ[ω]_n)| + O(ln n/n), linking entropy to the 4-tuple (μ, ν, κ, θ) directly.

## Lean coverage

- τ-effective throughout. All results follow from the defect bundle structure of Book IV Chapter 7, the Categorical Second Law of Chapter 19, and the geometric contraction lemma.
- The ideal-gas and black hole examples are illustrative: Sackur–Tetrode entropy is dominated by *S*_ref at cosmological ages; Bekenstein–Hawking entropy is primarily a refinement count.
- Book III dependency: *III.T14* (Spectral Trichotomy).

## Where this leads

The splitting identity is the algebraic foundation for the rest of Part III. Chapter 21 uses the bounded, integer-valued defect count to prove that exhaustion happens in finite orbit steps — not merely asymptotically. Chapter 23 uses the splitting to show that the "dark energy" budget is the refinement component misread as a constant energy density. Beyond Part III, the splitting is the lens through which all thermodynamic language in the monograph should be read: whenever a classical result invokes entropy, the question is always which component it is actually measuring.

<!-- regenerated 2026-04-29 from manuscript-sources/book-05/part03/ch22-entropy-splitting.tex -->
