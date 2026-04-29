---
{
  "projection_kind": "taulib_declaration",
  "title": "uniqueness_canonical_isomorphism_witness",
  "permalink": "/verify/taulib/docs/book-i-polarity-h4-uniqueness-elliptic/uniqueness-canonical-isomorphism-witness/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.H4UniquenessElliptic`.",
  "declaration_id": "TauLib.BookI.Polarity.H4UniquenessElliptic::uniqueness_canonical_isomorphism_witness",
  "declaration_slug": "uniqueness-canonical-isomorphism-witness",
  "kind": "theorem",
  "name": "uniqueness_canonical_isomorphism_witness",
  "module_name": "TauLib.BookI.Polarity.H4UniquenessElliptic",
  "module_url": "/verify/taulib/docs/book-i-polarity-h4-uniqueness-elliptic/",
  "source_line_start": 180,
  "source_line_end": 188,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H4UniquenessElliptic.lean#L180-L188",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.H4UniquenessElliptic",
        "url": "/verify/taulib/docs/book-i-polarity-h4-uniqueness-elliptic/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/verify/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H4UniquenessElliptic.lean#L180-L188",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
    }
  },
  "layout": "taulib-doc",
  "lane": "verify",
  "v2_lane": "verify",
  "status": "Canonical",
  "generated_from": "corpus/taulib-projections",
  "projection_version": "v0.1",
  "canonical_source": "Panta-Rhei-Research/taulib",
  "do_not_edit": true,
  "type": "TauLib Declaration"
}
---

## Declaration Projection

This page is generated directly from the pinned TauLib Lean source snapshot. The source excerpt is public because the active TauLib repository is public.

## Source Provenance

- Module: [TauLib.BookI.Polarity.H4UniquenessElliptic](/verify/taulib/docs/book-i-polarity-h4-uniqueness-elliptic/)
- Source path: [`TauLib/BookI/Polarity/H4UniquenessElliptic.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H4UniquenessElliptic.lean#L180-L188)
- Source range: L180-L188
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper Theorem uniqueness-main `thm:uniqueness-main`**: any
    boundary-algebra datum `(A, σ)` satisfying C1-C4 is
    **canonically isomorphic** to the split-complex algebra
    `R'[j]/(j² - 1)`, with no freedom in the isomorphism.

    **Statement-level form**: any structural witness producing
    `(e_+, e_-)` with the four axioms admits the canonical j-basis
    via `j := e_+ - e_-`, satisfying `j² = 1` and `σ(j) = -j`.

    The full categorical-isomorphism universal-property statement
    requires more abstract algebraic-structure infrastructure
    (R'-algebra homomorphisms, etc.) than fits TauLib's tactics-only
    Mathlib budget; the **structural witness** form here captures
    the algebraic content of the uniqueness theorem at the paper
    Lemma idem-normal level — which IS the uniqueness theorem's
    proof core. -/
```

## Source Excerpt

```lean
theorem uniqueness_canonical_isomorphism_witness :
    -- Given the C1-C4 axioms (verified above) plus the j-construction
    -- via e_+ - e_-, the uniqueness theorem reduces to:
    --   1. j² = 1 (forces split-complex structure, NOT Gaussian)
    SplitComplex.mul SplitComplex.j_canonical SplitComplex.j_canonical
      = SplitComplex.one ∧
    --   2. σ(j) = -j (forces canonical anti-invariance)
    (boundarySigma SplitComplex.j_canonical = SplitComplex.neg SplitComplex.j_canonical) :=
  ⟨j_squared_eq_one, boundarySigma_j_eq_neg_j⟩
```
