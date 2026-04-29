---
layout: "corpus-monograph-chapter"
title: "Chapter 12: The Parity Bridge Theorem"
permalink: "/corpus/monographs/book-iii/part-02-the-4-1-sector-template/chapter-12-the-parity-bridge-theorem/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "III"
book_slug: "book-iii"
part_number: 2
part_display: "Part II"
part_slug: "part-02-the-4-1-sector-template"
chapter_number: 12
chapter_slug: "chapter-12-the-parity-bridge-theorem"
page_in_book: 69
prev_chapter_url: "/corpus/monographs/book-iii/part-02-the-4-1-sector-template/chapter-11-the-yoneda-langlands-reflection/"
prev_chapter_title: "Chapter 11: The Yoneda-Langlands Reflection"
next_chapter_url: "/corpus/monographs/book-iii/part-02-the-4-1-sector-template/chapter-13-the-no-knobs-principle/"
next_chapter_title: "Chapter 13: The No Knobs Principle"
summary_short: "Spectral polarity pol(S_g) = ‖P_{χ+}(S_g)‖/‖P_{χ-}(S_g)‖ distinguishes the four primitive sectors: three are polarised, one is balanced. The Parity Bridge Theorem (III.T07) proves that the weak sector S_π — uniquely balanced (pol = 1) — is the sole carrier of the E₁→E₂ transition."
canonical_book_url: "/corpus/monographs/book-iii/"
canonical_book_title: "Book III: Categorical Spectrum"
canonical_part_url: "/corpus/monographs/book-iii/part-02-the-4-1-sector-template/"
canonical_part_title: "The 4+1 Sector Template"
publication_book_url: "/publications/books/book-iii/"
legacy_publication_url: "/publications/books/book-iii/part-02-the-4-1-sector-template/chapter-12-the-parity-bridge-theorem/"
right_rail:
  related:
    -
      title: "Book III: Categorical Spectrum"
      url: "/corpus/monographs/book-iii/"
    -
      title: "Part II: The 4+1 Sector Template"
      url: "/corpus/monographs/book-iii/part-02-the-4-1-sector-template/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-iii/"
    -
      title: "Registry"
      url: "/registry/books/book-iii/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book III"
    part: "Part II"
    layer: "E₀ Mathematics (Hinge)"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 33
construction_layer: "physics"
construction_layer_label: "Physics"
construction_step_ids:
  - "CS-04"
  - "CS-05"
---

The 4+1 sector decomposition assigns each primitive generator a sector of the spectral algebra, but not all sectors are structurally equal. Each projects differently onto the two lobes of 𝕃 via the χ₊/χ₋ decomposition, and this asymmetry is measured by spectral polarity (*III.D17*): pol(S_g) = ‖P_{χ+}(S_g)‖ / ‖P_{χ-}(S_g)‖. The ABCD positions determine the four polarities: S_α (D, invariant slot) and S_γ (B, predicate slot) are χ₊-dominant (pol > 1); S_η (C, decoder slot) is χ₋-dominant (pol < 1); and S_π (A, carrier slot) is balanced (pol = 1), because the angular winding number that defines the A-sector is structurally symmetric with respect to the two lobes of 𝕃 via the crossing-point identification (*I.D18*). The Balanced Sector Uniqueness proposition (*III.P04*, τ-effective) proves by exhaustion that S_π is the only balanced primitive sector. The Parity Bridge Theorem (*III.T07*, τ-effective) then identifies precisely why this matters: operational closure — the code → product → code cycle that constitutes the E₁ → E₂ transition — requires equal χ₊ and χ₋ capacity in both execution and encoding phases; only S_π satisfies this. A conjectural section connects this to the weak force as the unique force that changes particle identity in the physical E₁ instantiation.

## What this chapter contributes

**Definitions / Axioms**
- *Spectral polarity* (*III.D17*, τ-effective): pol(S_g) = ‖P_{χ+}(S_g)‖ / ‖P_{χ-}(S_g)‖, where ‖·‖ denotes the rank of the projected module at each finite depth. Sector S_g is χ₊-dominant if pol > 1, χ₋-dominant if pol < 1, balanced if pol = 1. The ratio is depth-independent because Langlands₀ (*III.T05*) preserves the bipolar decomposition within each sector.

**Key results**
- *Four sector polarities* (τ-effective): S_α (D/gravity slot): χ₊-dominant (pol > 1) — invariant orbit concentrates spectral weight on e₊; S_γ (B/EM slot): χ₊-dominant (pol > 1) — predicate orbit maps to n-axis χ₊-polarity; S_η (C/strong slot): χ₋-dominant (pol < 1) — decoder orbit maps to m-axis χ₋-polarity; S_π (A/weak slot): balanced (pol = 1) — angular winding is lobe-symmetric via crossing-point identification (*I.D18*).
- *Balanced Sector Uniqueness* (*III.P04*, τ-effective): pol(S_g) = 1 ↔ g = π. Proved by exhaustion: the four ABCD positions have characteristic couplings to χ₊/χ₋ — only the A-position (angular winding) is lobe-symmetric; no fifth orbit exists (K6). The ω-coupling sector is also eliminated: it lacks an independent carrier and cannot host a self-referential code.
- *Parity Bridge Theorem* (*III.T07*, τ-effective): S_π is the unique sector permitting the E₁ → E₂ transition. (i) The operational closure cycle requires a sector in which both execution (χ₊ → χ₋) and encoding (χ₋ → χ₊) are surjective within the sector. (ii) Surjectivity of both holds iff pol(S_g) = 1. (iii) pol(S_g) = 1 iff g = π (*III.P04*). Therefore S_π is the unique bridge.
- *Invariant-to-carrier handoff* (consequence): the invariant of E₁ (sector couplings) becomes the carrier of E₂ (self-referential codes); only S_π couplings generate the closure cycle. Other sector couplings appear as environmental data inside every E₂-code but do not generate operational closure.
- *Conjectural reading* (sector–force identification assumed, conjectural): the weak force is the unique fundamental force that changes particle identity; beta decay (n → p + e⁻ + ν̄_e) is the E₁ shadow of the code → product → code cycle. Biology is a non-generic consequence of balanced spectral polarity. Scope: conjectural; full derivation deferred to Book IV.

**Notation**
- pol(S_g) = ‖P_{χ+}(S_g)‖/‖P_{χ-}(S_g)‖ (spectral polarity); pol(S_α) > 1, pol(S_γ) > 1, pol(S_η) < 1, pol(S_π) = 1; code → product → code (operational closure cycle)

**Dependencies**
- *III.D13* (4+1 sector decomposition), *III.D14* (ω-coupling sector)
- *III.D05* (Layer template), *III.D07* (E₁ layer), *III.D08* (E₂ layer), *III.T05* (Sector preservation)
- *I.T04* (Hyperfactorization), *I.T12* (Spectral decomposition), *I.D18* (Algebraic lemniscate)

## Lean coverage

The Spectral Polarity definition *III.D17* and Balanced Sector Uniqueness *III.P04* are planned for `TauLib/BookIII/ParityBridge.lean`. The uniqueness argument is τ-effective and reduces to a four-case exhaustion over the ABCD orbit table — a strong Lean 4 candidate. The Parity Bridge Theorem *III.T07* requires combining *III.P04* with the closure cycle capacity argument, which in turn requires the operational closure definition *III.D08*; that definition depends on Part VI material, making the full *III.T07* formalization a secondary Lean target. No completed Lean 4 entry recorded at time of projection.

## Where this leads

Chapter 13 closes Part II with the No Knobs Principle — proving that all 10 inter-sector couplings are canonically determined by ι_τ = 2/(π + e) with no free parameters, and delivering the Part II export contracts to Books IV–VII.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-03/part02/ch12-the-parity-bridge-theorem.tex -->
