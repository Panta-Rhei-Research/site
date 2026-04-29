---
{
  "projection_kind": "taulib_declaration",
  "title": "two_faces",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/two-faces/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Thermodynamics.DarkEnergyArtifact`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.DarkEnergyArtifact::two_faces",
  "declaration_slug": "two-faces",
  "kind": "theorem",
  "name": "two_faces",
  "module_name": "TauLib.BookV.Thermodynamics.DarkEnergyArtifact",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/",
  "source_line_start": 203,
  "source_line_end": 205,
  "registry_ids": [
    "V.R134"
  ],
  "related_registry_items": [
    {
      "id": "V.R134",
      "title": "Two faces of the same problem",
      "url": "/registry/object/V.R134/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L203-L205",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L203-L205",
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
- Source path: [`TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L203-L205)
- Source range: L203-L205
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.R134` — Two faces of the same problem

## Immediate Comment / Docstring

```lean
/-- [V.R134] Two faces of the cosmological constant problem:
    (i) Why so small? Lambda ~ 10^{-52} m^{-2} vs Planck 10^{68}
    (ii) Why nonzero? Tiny nonzero value requires fine-tuning.

    Both faces dissolve when Lambda = 0 and acceleration comes
    from the defect-to-refinement transition. -/
```

## Source Excerpt

```lean
theorem two_faces :
    "CC problem: (i) why small? (ii) why nonzero? Both dissolve if Lambda = 0" =
    "CC problem: (i) why small? (ii) why nonzero? Both dissolve if Lambda = 0" := rfl
```
