---
{
  "projection_kind": "taulib_declaration",
  "title": "delta_cp_prediction_conj",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/delta-cp-prediction-conj/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::delta_cp_prediction_conj",
  "declaration_slug": "delta-cp-prediction-conj",
  "kind": "theorem",
  "name": "delta_cp_prediction_conj",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 1945,
  "source_line_end": 1950,
  "registry_ids": [
    "IV.P204"
  ],
  "related_registry_items": [
    {
      "id": "IV.P204",
      "title": "δ_CP = π + arctan(ι_τ) at +9365 ppm",
      "url": "/registry/object/IV.P204/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1945-L1950",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.ThreeGenerations",
        "url": "/verify/taulib/docs/book-iv-particles-three-generations/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1945-L1950",
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

- Module: [TauLib.BookIV.Particles.ThreeGenerations](/verify/taulib/docs/book-iv-particles-three-generations/)
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1945-L1950)
- Source range: L1945-L1950
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.P204` — δ_CP = π + arctan(ι_τ) at +9365 ppm

## Immediate Comment / Docstring

```lean
/-- [IV.P204] Conjunction: base 180°, prediction, PDG, deviation. -/
```

## Source Excerpt

```lean
theorem delta_cp_prediction_conj :
    delta_cp_prediction.base_degrees = 180 ∧
    delta_cp_prediction.predicted_deg_x100 = 19884 ∧
    delta_cp_prediction.pdg_deg_x100 = 19700 ∧
    delta_cp_prediction.deviation_ppm = 9365 :=
  ⟨rfl, rfl, rfl, rfl⟩
```
