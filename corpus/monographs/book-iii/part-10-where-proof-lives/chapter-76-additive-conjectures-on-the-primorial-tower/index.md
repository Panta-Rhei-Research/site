---
layout: "corpus-monograph-chapter"
title: "Chapter 76: Additive Conjectures on the Primorial Tower"
permalink: "/corpus/monographs/book-iii/part-10-where-proof-lives/chapter-76-additive-conjectures-on-the-primorial-tower/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "III"
book_slug: "book-iii"
part_number: 10
part_display: "Part X"
part_slug: "part-10-where-proof-lives"
chapter_number: 76
chapter_slug: "chapter-76-additive-conjectures-on-the-primorial-tower"
page_in_book: 373
prev_chapter_url: "/corpus/monographs/book-iii/part-10-where-proof-lives/chapter-75-the-architecture-of-reality/"
prev_chapter_title: "Chapter 75: The Architecture of Reality"
summary_short: "Goldbach, twin primes, and ABC are each verified at primorial levels and diagnosed with a three-gap taxonomy (parity, density, structural); all three gaps map to the exponential quantification forbidden move."
canonical_book_url: "/corpus/monographs/book-iii/"
canonical_book_title: "Book III: Categorical Spectrum"
canonical_part_url: "/corpus/monographs/book-iii/part-10-where-proof-lives/"
canonical_part_title: "Where Proof Lives"
publication_book_url: "/publications/books/book-iii/"
legacy_publication_url: "/publications/books/book-iii/part-10-where-proof-lives/chapter-76-additive-conjectures-on-the-primorial-tower/"
right_rail:
  related:
    -
      title: "Book III: Categorical Spectrum"
      url: "/corpus/monographs/book-iii/"
    -
      title: "Part X: Where Proof Lives"
      url: "/corpus/monographs/book-iii/part-10-where-proof-lives/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-iii/"
    -
      title: "Registry"
      url: "/registry/books/book-iii/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book III"
    part: "Part X"
    layer: "E₀ Mathematics (Hinge)"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 41
construction_layer: "physics"
construction_layer_label: "Physics"
construction_step_ids:
  - "CS-04"
  - "CS-05"
---

The primorial tower is a natural arena for three of number theory's deepest unsolved problems: Goldbach's conjecture, the twin prime conjecture, and the ABC conjecture. This chapter deploys the sieve infrastructure and the bridge discipline established in earlier chapters to push computational verification to new bounds, prove structural theorems at primorial levels, and precisely characterise what the τ framework can and cannot establish about each conjecture. The sieve of Eratosthenes is formalised as a computable function over the tower (*III.D99*), prime counts and Brun sieve counts are defined (*III.D100*, *III.D101*), and compatibility with CRT and Euler totient is proved. On Goldbach: every even number from 4 to 500 is verified to have a prime-pair representation (*III.T68*), partition counts grow with primorial depth (*III.T70*), and the local CRT conditions are always satisfiable (*III.P43*) — but the parity barrier prevents any sieve-based method from lifting these local solutions to a global proof. On twin primes: π₂(500) ≥ 20 is established (*III.T72*), CRT-admissible residues are nonempty at every depth (*III.T75*), but infinitude requires analytic equidistribution unavailable to the framework. On ABC: weak ABC holds for all coprime pairs up to 100 (*III.T76*), the primorial tower is entirely squarefree (*III.T78*), and squarefree triples automatically satisfy ABC (*III.P47*) — but the genuine difficulty of ABC lies in perfect-power factors, which the squarefree primorial tower avoids by construction. The chapter crystallises these findings into a three-gap taxonomy: parity, density, structural. All three gaps map to the same forbidden move: exponential quantification (K4 violation).

## What this chapter contributes

The chapter introduces fifteen definitions (*III.D99–III.D113*) and fifteen theorems (*III.T66–III.T80*) forming a complete Lean-verified sieve infrastructure integrated with the primorial tower. All finite-level results are *τ-effective*, verified by `native_decide` with zero `sorry`. *III.T80* (Bridge Necessary but Insufficient) is the chapter's principal honesty statement and is *established*: the bridge axiom is necessary to connect τ-internal results to the classical conjectures, but even with the bridge the analytic content (circle method, Bombieri–Vinogradov for twin primes, height theory for ABC) needed for the infinite case is absent from any finitary framework. *III.D112* (Gap Types) and *III.D113* (Forbidden Move Mapping) crystallise the taxonomy: parity gap, density gap, structural gap — all routing to exponential quantification with bridge damage 3 (break). *III.R47* (Classical Comparison) identifies the τ contribution precisely as the algebraic component — CRT, local conditions, admissibility, sieve compatibility — separate from the analytic component that classical number theory supplies independently.

## Lean coverage

All finite-level results (*III.T66–III.T79*) are *τ-effective*, verified in `SieveInfrastructure.lean` and `ConjectureGaps.lean`. *III.T80* and the gap propositions (*III.P44*, *III.P46*, *III.P48*) are *established* (meta-theorems about proof limitations). Infinite-level claims are *conjectural*. Zero `sorry` in the accompanying Lean files.

## Where this leads

This is the final chapter of Part X and of Book III. The three-gap taxonomy (*III.D112*) and Bridge Necessary but Insufficient (*III.T80*) close the programme's treatment of additive number theory with the same honest accounting pattern established for the Millennium Problems in Chapters 70–71. Book III is complete. The Architecture of Reality (*III.R35*) and the Coherence Certificate (*III.R36*) in Chapter 75 constitute the formal handoff to Books IV–VII.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-03/part10/ch81-additive-conjectures-deep.tex -->
