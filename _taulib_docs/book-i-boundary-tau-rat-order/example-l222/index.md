---
{
  "projection_kind": "taulib_declaration",
  "title": "example at L222",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-rat-order/example-l222/",
  "summary_short": "`example` declaration in `TauLib.BookI.Boundary.TauRatOrder`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRatOrder::#eval:222",
  "declaration_slug": "example-l222",
  "kind": "example",
  "name": null,
  "module_name": "TauLib.BookI.Boundary.TauRatOrder",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-rat-order/",
  "source_line_start": 222,
  "source_line_end": 223,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatOrder.lean#L222-L223",
  "formal_status": "example",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.TauRatOrder",
        "url": "/verify/taulib/docs/book-i-boundary-tau-rat-order/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatOrder.lean#L222-L223",
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

- Module: [TauLib.BookI.Boundary.TauRatOrder](/verify/taulib/docs/book-i-boundary-tau-rat-order/)
- Source path: [`TauLib/BookI/Boundary/TauRatOrder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatOrder.lean#L222-L223)
- Source range: L222-L223
- Kind: `example`
- Formal status hint: `example`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
-- 1/2 ≤ 1/2
```

## Source Excerpt

```lean
example : TauRat.le (⟨⟨1, 0⟩, 2, by norm_num⟩ : TauRat) ⟨⟨1, 0⟩, 2, by norm_num⟩ :=
  TauRat.le_refl _
```
