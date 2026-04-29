---
{
  "projection_kind": "taulib_declaration",
  "title": "monoid_assoc",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-boundary-interior/monoid-assoc/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Holomorphy.BoundaryInterior`.",
  "declaration_id": "TauLib.BookI.Holomorphy.BoundaryInterior::monoid_assoc",
  "declaration_slug": "monoid-assoc",
  "kind": "theorem",
  "name": "monoid_assoc",
  "module_name": "TauLib.BookI.Holomorphy.BoundaryInterior",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-boundary-interior/",
  "source_line_start": 136,
  "source_line_end": 140,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/BoundaryInterior.lean#L136-L140",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Holomorphy.BoundaryInterior",
        "url": "/verify/taulib/docs/book-i-holomorphy-boundary-interior/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/BoundaryInterior.lean#L136-L140",
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

- Module: [TauLib.BookI.Holomorphy.BoundaryInterior](/verify/taulib/docs/book-i-holomorphy-boundary-interior/)
- Source path: [`TauLib/BookI/Holomorphy/BoundaryInterior.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/BoundaryInterior.lean#L136-L140)
- Source range: L136-L140
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Book I summary: the program monoid is associative. -/
```

## Source Excerpt

```lean
theorem monoid_assoc :
    ∀ f₁ f₂ f₃ : StageFun,
    StageFun.comp (StageFun.comp f₁ f₂) f₃ =
    StageFun.comp f₁ (StageFun.comp f₂ f₃) :=
  stagefun_comp_assoc
```
