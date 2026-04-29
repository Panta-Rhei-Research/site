---
{
  "projection_kind": "taulib_declaration",
  "title": "tauEq_refl",
  "permalink": "/verify/taulib/docs/book-i-addressability-address-resolution/tau-eq-refl/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Addressability.AddressResolution`.",
  "declaration_id": "TauLib.BookI.Addressability.AddressResolution::tauEq_refl",
  "declaration_slug": "tau-eq-refl",
  "kind": "theorem",
  "name": "tauEq_refl",
  "module_name": "TauLib.BookI.Addressability.AddressResolution",
  "module_url": "/verify/taulib/docs/book-i-addressability-address-resolution/",
  "source_line_start": 94,
  "source_line_end": 95,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/AddressResolution.lean#L94-L95",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Addressability.AddressResolution",
        "url": "/verify/taulib/docs/book-i-addressability-address-resolution/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/AddressResolution.lean#L94-L95",
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

- Module: [TauLib.BookI.Addressability.AddressResolution](/verify/taulib/docs/book-i-addressability-address-resolution/)
- Source path: [`TauLib/BookI/Addressability/AddressResolution.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/AddressResolution.lean#L94-L95)
- Source range: L94-L95
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
No immediate Lean doc/comment block was detected for this declaration.
```

## Source Excerpt

```lean
theorem tauEq_refl (p : Program) : tauEq p p :=
  nfEquiv_refl _
```
