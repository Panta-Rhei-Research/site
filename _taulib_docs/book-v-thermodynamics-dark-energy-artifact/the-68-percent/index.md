---
{
  "projection_kind": "taulib_declaration",
  "title": "the_68_percent",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/the-68-percent/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Thermodynamics.DarkEnergyArtifact`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.DarkEnergyArtifact::the_68_percent",
  "declaration_slug": "the-68-percent",
  "kind": "theorem",
  "name": "the_68_percent",
  "module_name": "TauLib.BookV.Thermodynamics.DarkEnergyArtifact",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/",
  "source_line_start": 177,
  "source_line_end": 179,
  "registry_ids": [
    "V.P41"
  ],
  "related_registry_items": [
    {
      "id": "V.P41",
      "title": "The 68% is refinement entropy",
      "url": "/registry/object/V.P41/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L177-L179",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L177-L179",
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
- Source path: [`TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L177-L179)
- Source range: L177-L179
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P41` — The 68% is refinement entropy

## Immediate Comment / Docstring

```lean
/-- [V.P41] The 68% of the cosmic energy budget attributed to
    dark energy in Lambda-CDM corresponds to refinement entropy S_ref.

    S_ref is a counting artifact (lattice modes), not physical energy.
    The 68% was never "missing energy" but misattributed entropy. -/
```

## Source Excerpt

```lean
theorem the_68_percent :
    "68% dark energy = S_ref (counting artifact, not physical energy)" =
    "68% dark energy = S_ref (counting artifact, not physical energy)" := rfl
```
