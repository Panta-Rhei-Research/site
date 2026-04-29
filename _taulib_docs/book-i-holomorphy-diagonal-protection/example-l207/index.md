---
{
  "projection_kind": "taulib_declaration",
  "title": "example at L207",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-diagonal-protection/example-l207/",
  "summary_short": "`example` declaration in `TauLib.BookI.Holomorphy.DiagonalProtection`.",
  "declaration_id": "TauLib.BookI.Holomorphy.DiagonalProtection::#eval:207",
  "declaration_slug": "example-l207",
  "kind": "example",
  "name": null,
  "module_name": "TauLib.BookI.Holomorphy.DiagonalProtection",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-diagonal-protection/",
  "source_line_start": 207,
  "source_line_end": 208,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/DiagonalProtection.lean#L207-L208",
  "formal_status": "example",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Holomorphy.DiagonalProtection",
        "url": "/verify/taulib/docs/book-i-holomorphy-diagonal-protection/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/DiagonalProtection.lean#L207-L208",
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

- Module: [TauLib.BookI.Holomorphy.DiagonalProtection](/verify/taulib/docs/book-i-holomorphy-diagonal-protection/)
- Source path: [`TauLib/BookI/Holomorphy/DiagonalProtection.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/DiagonalProtection.lean#L207-L208)
- Source range: L207-L208
- Kind: `example`
- Formal status hint: `example`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
-- Verify that χ₊ ∘ χ₊ = χ₊ (idempotent)
```

## Source Excerpt

```lean
example : (chi_plus_stage.comp chi_plus_stage).b_fun 17 3 =
          chi_plus_stage.b_fun 17 3 := by native_decide
```
