---
layout: "corpus-monograph-chapter"
title: "Chapter 35: Laurent Series and Residues"
permalink: "/corpus/monographs/book-ii/part-06-local-hartogs-and-the-holomorphic-interior/chapter-35-laurent-series-and-residues/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
book_id: "II"
book_slug: "book-ii"
part_number: 6
part_display: "Part VI"
part_slug: "part-06-local-hartogs-and-the-holomorphic-interior"
chapter_number: 35
chapter_slug: "chapter-35-laurent-series-and-residues"
page_in_book: 175
prev_chapter_url: "/corpus/monographs/book-ii/part-06-local-hartogs-and-the-holomorphic-interior/chapter-34-composition-identity-associativity/"
prev_chapter_title: "Chapter 34: Composition, Identity, Associativity"
next_chapter_url: "/corpus/monographs/book-ii/part-06-local-hartogs-and-the-holomorphic-interior/chapter-36-the-canonical-holomorphic-basis-b/"
next_chapter_title: "Chapter 36: The Canonical Holomorphic Basis B"
summary_short: "Without SO(2), contour integrals, or annular domains, the τ-setting recovers a full Laurent–Residue theory: bipolar spectral decomposition replaces circular Fourier analysis, and the Residue Theorem (*II.T30*) equates the spectral trace with the sum of residues."
canonical_book_url: "/corpus/monographs/book-ii/"
canonical_book_title: "Book II: Categorical Holomorphy"
canonical_part_url: "/corpus/monographs/book-ii/part-06-local-hartogs-and-the-holomorphic-interior/"
canonical_part_title: "Local Hartogs and the Holomorphic Interior"
publication_book_url: "/publications/books/book-ii/"
legacy_publication_url: "/publications/books/book-ii/part-06-local-hartogs-and-the-holomorphic-interior/chapter-35-laurent-series-and-residues/"
right_rail:
  related:
    -
      title: "Book II: Categorical Holomorphy"
      url: "/corpus/monographs/book-ii/"
    -
      title: "Part VI: Local Hartogs and the Holomorphic Interior"
      url: "/corpus/monographs/book-ii/part-06-local-hartogs-and-the-holomorphic-interior/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-ii/"
    -
      title: "Registry"
      url: "/registry/books/book-ii/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book II"
    part: "Part VI"
    layer: "E₀ Mathematics"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
construction_sequence: 25
construction_layer: "mathematics"
construction_layer_label: "Mathematics"
construction_step_ids:
  - "CS-02"
  - "CS-03"
---

Classical Laurent theory relies on three ingredients that the τ-setting does not possess: circular SO(2) symmetry, contour integration via the 2πi factor, and convergence in the Archimedean topology of ℂ. None survives the passage to the split-complex regime. Yet the central results of Laurent theory — doubly-infinite expansion, residues as distinguished coefficients, and a residue theorem — all have τ-analogues, reconstructed from bipolar spectral decomposition and discrete Fourier transforms on finite cyclic groups.

## What this chapter contributes

- **Definitions:** *II.D42 — Laurent Expansion*: every ω-germ transformer f decomposes as f = Σ_n a_n^(+) e_+ φ_n^(+) + Σ_n a_n^(-) e_- φ_n^(-), where the spectral coefficients a_n^(±) are extracted by finite DFT averages over ℤ/P_kℤ in the limit k → ∞; positive n gives regular terms, negative n gives the principal part. *II.D43 — Residue*: Res_x(f) = a_{-1}^(+) e_+ + a_{-1}^(-) e_- ∈ H_τ — the spectral coefficient at frequency n = −1, extracted independently from each channel without contour integration. *II.D44 — Meromorphic Function*: holomorphic on a co-finite set of τ-admissible points, with finite principal part at each excluded point; meromorphic functions form a category extending *HolEnd_τ*.
- **Key results:** *II.T30 — Residue Theorem*: Tr_spec(f) = Σ_i Res_{x_i}(f), where the spectral trace is the stage-averaged limit of f over ℤ/P_kℤ. Proof: DFT orthogonality on cyclic groups picks out the zeroth coefficient; holomorphic terms contribute zero; only principal-part terms survive. The residue may have a nonzero j-component when the two channel residues differ — a genuinely split-complex phenomenon with no classical analogue.
- **Structural results:** spectral decay bound |a_n^(±)| ≤ C · e^(−ι_τ|n|) for n > 0, coupling e (growth rate, *II.T23*) and ι_τ (*II.T25*) via the BndLift damping; π governs the spectral periodicity of the sector basis functions (*II.T22*). The residue vanishes at x_0 if and only if f extends holomorphically through x_0.
- **Dependencies:** *I.D20*, *I.D21*, *I.T10*, *I.T18*, *I.P02*, *II.D01*, *II.D35*, *II.D39*, *II.D41*, *II.D45*, *II.T25*, *II.T26*, *II.T29*.

## Lean coverage

This chapter is prose-only at the current release; its content does not yet have a corresponding TauLib module. A module `BookII.Hartogs.LaurentResidue` is planned.

## Where this leads

Chapter 36 extracts the underlying basis implicit in the Laurent expansion: the cylinder generators E_{k,v}^(σ), indexed by (stage, peel token, channel) triples, form the canonical holomorphic basis B_τ forced by CRT, bipolar idempotents, and NF addressing — with no coordinate freedom and trivial transition functions across cylinder overlaps.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-02/part06/ch34-laurent-residues.tex -->
