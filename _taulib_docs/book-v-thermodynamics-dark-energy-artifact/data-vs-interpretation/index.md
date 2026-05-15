---
{
  "projection_kind": "taulib_declaration",
  "title": "data_vs_interpretation",
  "permalink": "/corpus/taulib/docs/book-v-thermodynamics-dark-energy-artifact/data-vs-interpretation/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Thermodynamics.DarkEnergyArtifact`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.DarkEnergyArtifact::data_vs_interpretation",
  "declaration_slug": "data-vs-interpretation",
  "kind": "theorem",
  "name": "data_vs_interpretation",
  "module_name": "TauLib.BookV.Thermodynamics.DarkEnergyArtifact",
  "module_url": "/corpus/taulib/docs/book-v-thermodynamics-dark-energy-artifact/",
  "source_line_start": 189,
  "source_line_end": 191,
  "registry_ids": [
    "V.R133"
  ],
  "related_registry_items": [
    {
      "id": "V.R133",
      "title": "Data versus interpretation",
      "url": "/registry/object/V.R133/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L189-L191",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Thermodynamics.DarkEnergyArtifact",
        "url": "/corpus/taulib/docs/book-v-thermodynamics-dark-energy-artifact/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L189-L191",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookV.Thermodynamics.DarkEnergyArtifact](/corpus/taulib/docs/book-v-thermodynamics-dark-energy-artifact/)
- Source path: [`TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L189-L191)
- Source range: L189-L191
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `V.R133` — Data versus interpretation

## Immediate Comment / Docstring

```lean
/-- [V.R133] Data versus interpretation: the cosmic acceleration is
    observational data, but dark energy is a model-dependent interpretation.
    The tau-framework preserves the data (acceleration is real) but
    replaces the interpretation (different cause). -/
```

## Source Excerpt

```lean
theorem data_vs_interpretation :
    "Acceleration = data (real). Dark energy = interpretation (artifact)." =
    "Acceleration = data (real). Dark energy = interpretation (artifact)." := rfl
```
