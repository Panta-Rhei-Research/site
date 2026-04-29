---
{
  "projection_kind": "taulib_declaration",
  "title": "dark_energy_artifact",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/dark-energy-artifact/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Thermodynamics.DarkEnergyArtifact`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.DarkEnergyArtifact::dark_energy_artifact",
  "declaration_slug": "dark-energy-artifact",
  "kind": "theorem",
  "name": "dark_energy_artifact",
  "module_name": "TauLib.BookV.Thermodynamics.DarkEnergyArtifact",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/",
  "source_line_start": 164,
  "source_line_end": 166,
  "registry_ids": [
    "V.T69"
  ],
  "related_registry_items": [
    {
      "id": "V.T69",
      "title": "Dark energy is a readout artifact",
      "url": "/registry/object/V.T69/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L164-L166",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Thermodynamics.DarkEnergyArtifact",
        "url": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L164-L166",
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

- Module: [TauLib.BookV.Thermodynamics.DarkEnergyArtifact](/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/)
- Source path: [`TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L164-L166)
- Source range: L164-L166
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T69` — Dark energy is a readout artifact

## Immediate Comment / Docstring

```lean
/-- [V.T69] Dark energy is a readout artifact: the cosmic acceleration
    attributed to Lambda in Lambda-CDM arises from the defect-to-refinement
    transition on base tau^1.

    The orthodox readout functor misidentifies the decreasing defect
    entropy (ordering) as a repulsive energy source. -/
```

## Source Excerpt

```lean
theorem dark_energy_artifact :
    "Lambda-CDM dark energy = readout artifact from S_def -> S_ref transition" =
    "Lambda-CDM dark energy = readout artifact from S_def -> S_ref transition" := rfl
```
