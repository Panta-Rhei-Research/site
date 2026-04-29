---
{
  "projection_kind": "taulib_declaration",
  "title": "PlaquetteDefect",
  "permalink": "/verify/taulib/docs/book-iv-strong-yang-mills-gap/plaquette-defect/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.YangMillsGap`.",
  "declaration_id": "TauLib.BookIV.Strong.YangMillsGap::PlaquetteDefect",
  "declaration_slug": "plaquette-defect",
  "kind": "structure",
  "name": "PlaquetteDefect",
  "module_name": "TauLib.BookIV.Strong.YangMillsGap",
  "module_url": "/verify/taulib/docs/book-iv-strong-yang-mills-gap/",
  "source_line_start": 108,
  "source_line_end": 115,
  "registry_ids": [
    "IV.D172"
  ],
  "related_registry_items": [
    {
      "id": "IV.D172",
      "title": "Plaquette-aggregated strong defect",
      "url": "/registry/object/IV.D172/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/YangMillsGap.lean#L108-L115",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Strong.YangMillsGap",
        "url": "/verify/taulib/docs/book-iv-strong-yang-mills-gap/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/YangMillsGap.lean#L108-L115",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "status": "defined"
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

- Module: [TauLib.BookIV.Strong.YangMillsGap](/verify/taulib/docs/book-iv-strong-yang-mills-gap/)
- Source path: [`TauLib/BookIV/Strong/YangMillsGap.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/YangMillsGap.lean#L108-L115)
- Source range: L108-L115
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D172` — Plaquette-aggregated strong defect

## Immediate Comment / Docstring

```lean
/-- [IV.D172] V_n^s(Gamma_n) = Agg({F_n^s(Box) | Box in P_n^s}):
    canonical aggregation of curvatures over all plaquettes.
    The plaquette reformulation of the gap-loop defect. -/
```

## Source Excerpt

```lean
structure PlaquetteDefect where
  /-- Aggregation over all plaquettes. -/
  aggregation_method : String := "canonical aggregation over P_n^s"
  /-- Non-negative. -/
  nonneg : Bool := true
  /-- Vanishes on flat connections. -/
  vanishes_on_flat : Bool := true
  deriving Repr
```
