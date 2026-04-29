---
{
  "projection_kind": "taulib_declaration",
  "title": "z_acc_within_1sigma",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/z-acc-within-1sigma/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Thermodynamics.DarkEnergyArtifact`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.DarkEnergyArtifact::z_acc_within_1sigma",
  "declaration_slug": "z-acc-within-1sigma",
  "kind": "theorem",
  "name": "z_acc_within_1sigma",
  "module_name": "TauLib.BookV.Thermodynamics.DarkEnergyArtifact",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/",
  "source_line_start": 416,
  "source_line_end": 418,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L416-L418",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L416-L418",
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
- Source path: [`TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L416-L418)
- Source range: L416-L418
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- z_acc within 1σ of observations. -/
```

## Source Excerpt

```lean
theorem z_acc_within_1sigma :
    z_acc_canonical.z_acc_x1000 ≥ z_acc_canonical.observed_x1000 - z_acc_canonical.uncertainty_x1000 := by
  native_decide
```
