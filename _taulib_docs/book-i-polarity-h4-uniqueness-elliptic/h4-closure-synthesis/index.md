---
{
  "projection_kind": "taulib_declaration",
  "title": "h4_closure_synthesis",
  "permalink": "/verify/taulib/docs/book-i-polarity-h4-uniqueness-elliptic/h4-closure-synthesis/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.H4UniquenessElliptic`.",
  "declaration_id": "TauLib.BookI.Polarity.H4UniquenessElliptic::h4_closure_synthesis",
  "declaration_slug": "h4-closure-synthesis",
  "kind": "theorem",
  "name": "h4_closure_synthesis",
  "module_name": "TauLib.BookI.Polarity.H4UniquenessElliptic",
  "module_url": "/verify/taulib/docs/book-i-polarity-h4-uniqueness-elliptic/",
  "source_line_start": 323,
  "source_line_end": 334,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H4UniquenessElliptic.lean#L323-L334",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H4UniquenessElliptic.lean#L323-L334",
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
- Source path: [`TauLib/BookI/Polarity/H4UniquenessElliptic.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H4UniquenessElliptic.lean#L323-L334)
- Source range: L323-L334
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **The H4 closure synthesis**: combining Wave 24's four-atom
    dictionary with Wave 25's uniqueness + elliptic exclusion gives
    the structural picture:

    1. **Uniqueness** (paper §8): any C1-C4 boundary-algebra datum
       is canonically isomorphic to D = R'[j]/(j²-1).
    2. **Elliptic exclusion** (paper §9): the Gaussian alternative
       i² = -1 doesn't satisfy C3 (no σ-equivariant idempotent pair).
    3. **Forced choice**: hence split-complex `j² = +1` is the
       unique scalar choice consistent with the τ-kernel's bipolar
       structure.

    This wave records the synthesis at the structural level. -/
```

## Source Excerpt

```lean
theorem h4_closure_synthesis :
    -- Uniqueness: SplitComplex's j satisfies the canonical relations
    SplitComplex.mul SplitComplex.j_canonical SplitComplex.j_canonical
      = SplitComplex.one ∧
    -- Elliptic exclusion concrete witness:
    -- (1+i)(1-i) ≠ 0 in Gaussian (so e_+·e_- ≠ 0 there)
    GaussianElliptic.mul ⟨1, 1⟩ ⟨1, -1⟩ ≠ GaussianElliptic.zero ∧
    -- Split-complex contrast: (1+j)(1-j) = 0 in SplitComplex
    SplitComplex.mul ⟨1, 1⟩ ⟨1, -1⟩ = SplitComplex.zero :=
  ⟨j_squared_eq_one,
   elliptic_no_sigma_equivariant_idempotent_pair,
   split_complex_admits_orthogonal_pair⟩
```
