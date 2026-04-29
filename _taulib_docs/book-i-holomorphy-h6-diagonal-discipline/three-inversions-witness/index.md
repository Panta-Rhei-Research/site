---
{
  "projection_kind": "taulib_declaration",
  "title": "three_inversions_witness",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-h6-diagonal-discipline/three-inversions-witness/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Holomorphy.H6DiagonalDiscipline`.",
  "declaration_id": "TauLib.BookI.Holomorphy.H6DiagonalDiscipline::three_inversions_witness",
  "declaration_slug": "three-inversions-witness",
  "kind": "theorem",
  "name": "three_inversions_witness",
  "module_name": "TauLib.BookI.Holomorphy.H6DiagonalDiscipline",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-h6-diagonal-discipline/",
  "source_line_start": 178,
  "source_line_end": 186,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/H6DiagonalDiscipline.lean#L178-L186",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/H6DiagonalDiscipline.lean#L178-L186",
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
- Source path: [`TauLib/BookI/Holomorphy/H6DiagonalDiscipline.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/H6DiagonalDiscipline.lean#L178-L186)
- Source range: L178-L186
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper Theorem `three-inversions` synthesis**: the three
    inversions (I1) DD1–DD4, (I2) j² = +1, (I3) wave equation
    are mutually equivalent at the structural-witness level.

    (I3) is rendered as the *consequence* of (I2): the
    split-complex signature `j² = +1` produces the hyperbolic
    sign in the second-order operator `∂_x² - ∂_y²`, which is
    the wave equation rather than Laplace.  The full PDE
    formalization is Wave 28's job (paper §5 wave-CR).  Wave 27
    captures the structural-equivalence content via the
    (I1) ↔ (I2) bidirection above, with (I3) flagged as
    forthcoming. -/
```

## Source Excerpt

```lean
theorem three_inversions_witness :
    -- (I1) DD-discipline ↔ (I2) split-complex j² = +1
    -- packaged at the structural-witness level
    (SplitComplex.mul SplitComplex.j_canonical SplitComplex.j_canonical
       = SplitComplex.one ∧
     GaussianElliptic.mul ⟨1, 1⟩ ⟨1, -1⟩ ≠ GaussianElliptic.zero) ∧
    -- (I2) ↔ (I1) reverse direction: split-complex orthogonality
    SplitComplex.mul ⟨1, 1⟩ ⟨1, -1⟩ = SplitComplex.zero :=
  ⟨three_inversions_I1_to_I2_witness, three_inversions_I2_to_I1_witness⟩
```
