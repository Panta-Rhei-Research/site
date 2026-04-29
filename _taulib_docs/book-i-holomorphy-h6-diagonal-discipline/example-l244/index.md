---
{
  "projection_kind": "taulib_declaration",
  "title": "example at L244",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-h6-diagonal-discipline/example-l244/",
  "summary_short": "`example` declaration in `TauLib.BookI.Holomorphy.H6DiagonalDiscipline`.",
  "declaration_id": "TauLib.BookI.Holomorphy.H6DiagonalDiscipline::#eval:244",
  "declaration_slug": "example-l244",
  "kind": "example",
  "name": null,
  "module_name": "TauLib.BookI.Holomorphy.H6DiagonalDiscipline",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-h6-diagonal-discipline/",
  "source_line_start": 244,
  "source_line_end": 245,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/H6DiagonalDiscipline.lean#L244-L245",
  "formal_status": "example",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/H6DiagonalDiscipline.lean#L244-L245",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "example",
      "status": "example"
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
- Source path: [`TauLib/BookI/Holomorphy/H6DiagonalDiscipline.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/H6DiagonalDiscipline.lean#L244-L245)
- Source range: L244-L245
- Kind: `example`
- Formal status hint: `example`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The concrete arithmetic: in elliptic, `(1+i)·(1-i) = ⟨2, 0⟩ ≠ 0`. -/
```

## Source Excerpt

```lean
example : GaussianElliptic.mul ⟨1, 1⟩ ⟨1, -1⟩ = ⟨2, 0⟩ := by
  decide
```
