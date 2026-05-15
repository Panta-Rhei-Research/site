---
{
  "projection_kind": "taulib_declaration",
  "title": "galois_order_2",
  "permalink": "/corpus/taulib/docs/book-i-boundary-galois/galois-order-2/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.Galois`.",
  "declaration_id": "TauLib.BookI.Boundary.Galois::galois_order_2",
  "declaration_slug": "galois-order-2",
  "kind": "theorem",
  "name": "galois_order_2",
  "module_name": "TauLib.BookI.Boundary.Galois",
  "module_url": "/corpus/taulib/docs/book-i-boundary-galois/",
  "source_line_start": 227,
  "source_line_end": 227,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Galois.lean#L227-L227",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.Galois",
        "url": "/corpus/taulib/docs/book-i-boundary-galois/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Galois.lean#L227-L227",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookI.Boundary.Galois](/corpus/taulib/docs/book-i-boundary-galois/)
- Source path: [`TauLib/BookI/Boundary/Galois.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Galois.lean#L227-L227)
- Source range: L227-L227
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [I.D96a] φ(6) = 2. -/
```

## Source Excerpt

```lean
theorem galois_order_2 : galois_group_order 2 = 2 := by native_decide
```
