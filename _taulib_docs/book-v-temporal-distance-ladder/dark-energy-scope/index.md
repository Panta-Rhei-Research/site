---
{
  "projection_kind": "taulib_declaration",
  "title": "dark_energy_scope",
  "permalink": "/verify/taulib/docs/book-v-temporal-distance-ladder/dark-energy-scope/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Temporal.DistanceLadder`.",
  "declaration_id": "TauLib.BookV.Temporal.DistanceLadder::dark_energy_scope",
  "declaration_slug": "dark-energy-scope",
  "kind": "theorem",
  "name": "dark_energy_scope",
  "module_name": "TauLib.BookV.Temporal.DistanceLadder",
  "module_url": "/verify/taulib/docs/book-v-temporal-distance-ladder/",
  "source_line_start": 242,
  "source_line_end": 243,
  "registry_ids": [
    "V.R44"
  ],
  "related_registry_items": [
    {
      "id": "V.R44",
      "title": "Scope and deferral",
      "url": "/registry/object/V.R44/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/DistanceLadder.lean#L242-L243",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Temporal.DistanceLadder",
        "url": "/verify/taulib/docs/book-v-temporal-distance-ladder/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/DistanceLadder.lean#L242-L243",
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

- Module: [TauLib.BookV.Temporal.DistanceLadder](/verify/taulib/docs/book-v-temporal-distance-ladder/)
- Source path: [`TauLib/BookV/Temporal/DistanceLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/DistanceLadder.lean#L242-L243)
- Source range: L242-L243
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.R44` — Scope and deferral

## Immediate Comment / Docstring

```lean
/-- [V.R44] The dark energy artifact theorem is conjectural.
    The default scope of ReadoutCurvature is "conjectural". -/
```

## Source Excerpt

```lean
theorem dark_energy_scope (κ : ReadoutCurvature) (h : κ.scope = "conjectural") :
    κ.scope = "conjectural" := h
```
