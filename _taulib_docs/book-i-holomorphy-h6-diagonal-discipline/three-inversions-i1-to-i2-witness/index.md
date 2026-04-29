---
{
  "projection_kind": "taulib_declaration",
  "title": "three_inversions_I1_to_I2_witness",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-h6-diagonal-discipline/three-inversions-i1-to-i2-witness/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Holomorphy.H6DiagonalDiscipline`.",
  "declaration_id": "TauLib.BookI.Holomorphy.H6DiagonalDiscipline::three_inversions_I1_to_I2_witness",
  "declaration_slug": "three-inversions-i1-to-i2-witness",
  "kind": "theorem",
  "name": "three_inversions_I1_to_I2_witness",
  "module_name": "TauLib.BookI.Holomorphy.H6DiagonalDiscipline",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-h6-diagonal-discipline/",
  "source_line_start": 143,
  "source_line_end": 149,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/H6DiagonalDiscipline.lean#L143-L149",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Holomorphy.H6DiagonalDiscipline",
        "url": "/verify/taulib/docs/book-i-holomorphy-h6-diagonal-discipline/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/H6DiagonalDiscipline.lean#L143-L149",
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

- Module: [TauLib.BookI.Holomorphy.H6DiagonalDiscipline](/verify/taulib/docs/book-i-holomorphy-h6-diagonal-discipline/)
- Source path: [`TauLib/BookI/Holomorphy/H6DiagonalDiscipline.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/H6DiagonalDiscipline.lean#L143-L149)
- Source range: L143-L149
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper Theorem `three-inversions` (I1)→(I2) witness**:
    the split-complex signature `j² = +1` is the structural
    consequence of the diagonal-free discipline.

    Concretely: the diagonal discipline forces the existence
    of σ-equivariant idempotents `(e_+, e_-)` (DD1–DD4 prevent
    the integral-domain collapse that would force elliptic
    `i² = -1`).  Wave 25 verified that `j² = +1` is exactly the
    scalar relation that admits this idempotent structure
    (`j_squared_eq_one`) while elliptic `i² = -1` does not
    (`elliptic_no_sigma_equivariant_idempotent_pair`).

    The witness packages both facts in one structural statement. -/
```

## Source Excerpt

```lean
theorem three_inversions_I1_to_I2_witness :
    -- (I2.a) split-complex signature j² = +1 holds
    SplitComplex.mul SplitComplex.j_canonical SplitComplex.j_canonical
      = SplitComplex.one ∧
    -- (I2.b) elliptic alternative i² = -1 is excluded
    GaussianElliptic.mul ⟨1, 1⟩ ⟨1, -1⟩ ≠ GaussianElliptic.zero :=
  ⟨j_squared_eq_one, elliptic_no_sigma_equivariant_idempotent_pair⟩
```
