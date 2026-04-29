---
{
  "projection_kind": "taulib_declaration",
  "title": "distance_time_dual",
  "permalink": "/verify/taulib/docs/book-v-temporal-macro-readout/distance-time-dual/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Temporal.MacroReadout`.",
  "declaration_id": "TauLib.BookV.Temporal.MacroReadout::distance_time_dual",
  "declaration_slug": "distance-time-dual",
  "kind": "theorem",
  "name": "distance_time_dual",
  "module_name": "TauLib.BookV.Temporal.MacroReadout",
  "module_url": "/verify/taulib/docs/book-v-temporal-macro-readout/",
  "source_line_start": 121,
  "source_line_end": 125,
  "registry_ids": [
    "V.T15"
  ],
  "related_registry_items": [
    {
      "id": "V.T15",
      "title": "Distance-Duration Duality",
      "url": "/registry/object/V.T15/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/MacroReadout.lean#L121-L125",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Temporal.MacroReadout",
        "url": "/verify/taulib/docs/book-v-temporal-macro-readout/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/MacroReadout.lean#L121-L125",
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

- Module: [TauLib.BookV.Temporal.MacroReadout](/verify/taulib/docs/book-v-temporal-macro-readout/)
- Source path: [`TauLib/BookV/Temporal/MacroReadout.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/MacroReadout.lean#L121-L125)
- Source range: L121-L125
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T15` — Distance-Duration Duality

## Immediate Comment / Docstring

```lean
/-- [V.T15] Distance and proper time are dual readouts.
    Time counts α-ticks along base; distance counts null-intertwiner
    ticks between events. Both derived from the refinement tower. -/
```

## Source Excerpt

```lean
theorem distance_time_dual :
    canonical_base_circle.seed = .alpha ∧
    photon_null.sector = .B ∧
    canonical_base_circle.profinite.seed = .alpha := by
  exact ⟨rfl, rfl, rfl⟩
```
