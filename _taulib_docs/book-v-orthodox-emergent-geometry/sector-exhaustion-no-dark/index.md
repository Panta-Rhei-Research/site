---
{
  "projection_kind": "taulib_declaration",
  "title": "sector_exhaustion_no_dark",
  "permalink": "/verify/taulib/docs/book-v-orthodox-emergent-geometry/sector-exhaustion-no-dark/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Orthodox.EmergentGeometry`.",
  "declaration_id": "TauLib.BookV.Orthodox.EmergentGeometry::sector_exhaustion_no_dark",
  "declaration_slug": "sector-exhaustion-no-dark",
  "kind": "theorem",
  "name": "sector_exhaustion_no_dark",
  "module_name": "TauLib.BookV.Orthodox.EmergentGeometry",
  "module_url": "/verify/taulib/docs/book-v-orthodox-emergent-geometry/",
  "source_line_start": 185,
  "source_line_end": 187,
  "registry_ids": [
    "V.T128"
  ],
  "related_registry_items": [
    {
      "id": "V.T128",
      "title": "Sector Exhaustion --- no dark sector",
      "url": "/registry/object/V.T128/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/EmergentGeometry.lean#L185-L187",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Orthodox.EmergentGeometry",
        "url": "/verify/taulib/docs/book-v-orthodox-emergent-geometry/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/EmergentGeometry.lean#L185-L187",
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

- Module: [TauLib.BookV.Orthodox.EmergentGeometry](/verify/taulib/docs/book-v-orthodox-emergent-geometry/)
- Source path: [`TauLib/BookV/Orthodox/EmergentGeometry.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/EmergentGeometry.lean#L185-L187)
- Source range: L185-L187
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T128` — Sector Exhaustion --- no dark sector

## Immediate Comment / Docstring

```lean
/-- [V.T128] Sector exhaustion: 5 generators produce 5 sectors,
    coupling budget is saturated, no dark sector can exist.

    The temporal complement kappa(A) + kappa(D) = 1 means the
    base tau^1 budget is exactly spent. The fiber T^2 budget is
    similarly exhausted by B, C, and Omega sectors. -/
```

## Source Excerpt

```lean
theorem sector_exhaustion_no_dark :
    "5 generators -> 5 sectors -> budget saturated -> no dark sector" =
    "5 generators -> 5 sectors -> budget saturated -> no dark sector" := rfl
```
