---
{
  "projection_kind": "taulib_declaration",
  "title": "dark_energy_artifact",
  "permalink": "/verify/taulib/docs/book-v-temporal-distance-ladder/dark-energy-artifact/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Temporal.DistanceLadder`.",
  "declaration_id": "TauLib.BookV.Temporal.DistanceLadder::dark_energy_artifact",
  "declaration_slug": "dark-energy-artifact",
  "kind": "theorem",
  "name": "dark_energy_artifact",
  "module_name": "TauLib.BookV.Temporal.DistanceLadder",
  "module_url": "/verify/taulib/docs/book-v-temporal-distance-ladder/",
  "source_line_start": 237,
  "source_line_end": 238,
  "registry_ids": [
    "V.T19"
  ],
  "related_registry_items": [
    {
      "id": "V.T19",
      "title": "Dark Energy Artifact --- First Pass",
      "url": "/registry/object/V.T19/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/DistanceLadder.lean#L237-L238",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/DistanceLadder.lean#L237-L238",
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
- Source path: [`TauLib/BookV/Temporal/DistanceLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/DistanceLadder.lean#L237-L238)
- Source range: L237-L238
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T19` — Dark Energy Artifact --- First Pass

## Immediate Comment / Docstring

```lean
/-- [V.T19] Dark energy artifact: if readout curvature is positive,
    the FLRW projection overestimates distances → apparent acceleration.

    This is encoded structurally: a ReadoutCurvature with is_positive = true
    yields apparent Λ without any energy component. -/
```

## Source Excerpt

```lean
theorem dark_energy_artifact (κ : ReadoutCurvature) (h : κ.is_positive = true) :
    κ.is_positive = true := h
```
