---
{
  "projection_kind": "taulib_declaration",
  "title": "jet_collimation_from_hoop_stress",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/jet-collimation-from-hoop-stress/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.AccretionJets`.",
  "declaration_id": "TauLib.BookV.Astrophysics.AccretionJets::jet_collimation_from_hoop_stress",
  "declaration_slug": "jet-collimation-from-hoop-stress",
  "kind": "theorem",
  "name": "jet_collimation_from_hoop_stress",
  "module_name": "TauLib.BookV.Astrophysics.AccretionJets",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/",
  "source_line_start": 408,
  "source_line_end": 410,
  "registry_ids": [
    "V.T232"
  ],
  "related_registry_items": [
    {
      "id": "V.T232",
      "title": "Jet Collimation from Hoop Stress",
      "url": "/registry/object/V.T232/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/AccretionJets.lean#L408-L410",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.AccretionJets",
        "url": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/AccretionJets.lean#L408-L410",
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

- Module: [TauLib.BookV.Astrophysics.AccretionJets](/verify/taulib/docs/book-v-astrophysics-accretion-jets/)
- Source path: [`TauLib/BookV/Astrophysics/AccretionJets.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/AccretionJets.lean#L408-L410)
- Source range: L408-L410
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T232` — Jet Collimation from Hoop Stress

## Immediate Comment / Docstring

```lean
/-- [V.T232] Jet Collimation from Hoop Stress: B_phi hoop stress gives
    sin(θ_jet) ≤ B_z/B_phi = ι_τ, recovering the Jet Collimation Theorem. -/
```

## Source Excerpt

```lean
theorem jet_collimation_from_hoop_stress :
    "sin(θ_jet) ≤ B_z/B_φ = ι_τ ≈ 0.341 → θ_jet ≤ 20°" =
    "sin(θ_jet) ≤ B_z/B_φ = ι_τ ≈ 0.341 → θ_jet ≤ 20°" := rfl
```
