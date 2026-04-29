---
{
  "projection_kind": "taulib_declaration",
  "title": "three_inversions_I2_to_I1_witness",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-h6-diagonal-discipline/three-inversions-i2-to-i1-witness/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Holomorphy.H6DiagonalDiscipline`.",
  "declaration_id": "TauLib.BookI.Holomorphy.H6DiagonalDiscipline::three_inversions_I2_to_I1_witness",
  "declaration_slug": "three-inversions-i2-to-i1-witness",
  "kind": "theorem",
  "name": "three_inversions_I2_to_I1_witness",
  "module_name": "TauLib.BookI.Holomorphy.H6DiagonalDiscipline",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-h6-diagonal-discipline/",
  "source_line_start": 161,
  "source_line_end": 164,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/H6DiagonalDiscipline.lean#L161-L164",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/H6DiagonalDiscipline.lean#L161-L164",
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
- Source path: [`TauLib/BookI/Holomorphy/H6DiagonalDiscipline.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/H6DiagonalDiscipline.lean#L161-L164)
- Source range: L161-L164
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper Theorem `three-inversions` (I2)→(I1) witness**:
    once the split-complex signature `j² = +1` is fixed, the
    σ-equivariant idempotent pair `(e_+, e_-)` exists with
    `e_+ · e_- = 0` (orthogonality), which is exactly the
    structural content protected by DD1–DD4.

    Concretely: `(1+j)·(1-j) = 1 - j² = 1 - 1 = 0` in
    SplitComplex, the contrast theorem from Wave 25
    (`split_complex_admits_orthogonal_pair`).  Wave 27 here
    repackages this as the (I2)→(I1) direction. -/
```

## Source Excerpt

```lean
theorem three_inversions_I2_to_I1_witness :
    -- The orthogonality (1+j)(1-j) = 0 in split-complex
    SplitComplex.mul ⟨1, 1⟩ ⟨1, -1⟩ = SplitComplex.zero :=
  split_complex_admits_orthogonal_pair
```
