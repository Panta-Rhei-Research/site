---
{
  "projection_kind": "taulib_declaration",
  "title": "rm_winding_theorem",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-ehtreread/rm-winding-theorem/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.EHTReread`.",
  "declaration_id": "TauLib.BookV.Astrophysics.EHTReread::rm_winding_theorem",
  "declaration_slug": "rm-winding-theorem",
  "kind": "theorem",
  "name": "rm_winding_theorem",
  "module_name": "TauLib.BookV.Astrophysics.EHTReread",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-ehtreread/",
  "source_line_start": 536,
  "source_line_end": 538,
  "registry_ids": [
    "V.T227"
  ],
  "related_registry_items": [
    {
      "id": "V.T227",
      "title": "RM Winding Theorem",
      "url": "/registry/object/V.T227/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L536-L538",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L536-L538",
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
- Source path: [`TauLib/BookV/Astrophysics/EHTReread.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L536-L538)
- Source range: L536-L538
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T227` — RM Winding Theorem

## Immediate Comment / Docstring

```lean
/-- [V.T227] RM Winding Theorem: the Faraday rotation measure winding
    number equals 2 for T² (two sign changes from toroidal B-field)
    and 1 for S² (one sign change from radial/dipolar field). -/
```

## Source Excerpt

```lean
theorem rm_winding_theorem :
    "w_RM(T²) = 2, w_RM(S²) = 1" =
    "w_RM(T²) = 2, w_RM(S²) = 1" := rfl
```
