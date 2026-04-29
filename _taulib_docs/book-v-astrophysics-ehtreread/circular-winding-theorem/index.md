---
{
  "projection_kind": "taulib_declaration",
  "title": "circular_winding_theorem",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-ehtreread/circular-winding-theorem/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.EHTReread`.",
  "declaration_id": "TauLib.BookV.Astrophysics.EHTReread::circular_winding_theorem",
  "declaration_slug": "circular-winding-theorem",
  "kind": "theorem",
  "name": "circular_winding_theorem",
  "module_name": "TauLib.BookV.Astrophysics.EHTReread",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-ehtreread/",
  "source_line_start": 569,
  "source_line_end": 571,
  "registry_ids": [
    "V.T229"
  ],
  "related_registry_items": [
    {
      "id": "V.T229",
      "title": "Circular Polarization Winding",
      "url": "/registry/object/V.T229/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L569-L571",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.EHTReread",
        "url": "/verify/taulib/docs/book-v-astrophysics-ehtreread/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L569-L571",
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

- Module: [TauLib.BookV.Astrophysics.EHTReread](/verify/taulib/docs/book-v-astrophysics-ehtreread/)
- Source path: [`TauLib/BookV/Astrophysics/EHTReread.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L569-L571)
- Source range: L569-L571
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T229` — Circular Polarization Winding

## Immediate Comment / Docstring

```lean
/-- [V.T229] Circular Polarization Winding: w_V = 2 for T², 1 for S². -/
```

## Source Excerpt

```lean
theorem circular_winding_theorem :
    "w_V(T²) = 2, w_V(S²) = 1" =
    "w_V(T²) = 2, w_V(S²) = 1" := rfl
```
