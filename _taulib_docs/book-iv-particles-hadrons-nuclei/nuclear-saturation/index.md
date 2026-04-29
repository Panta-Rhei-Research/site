---
{
  "projection_kind": "taulib_declaration",
  "title": "NuclearSaturation",
  "permalink": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/nuclear-saturation/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.HadronsNuclei`.",
  "declaration_id": "TauLib.BookIV.Particles.HadronsNuclei::NuclearSaturation",
  "declaration_slug": "nuclear-saturation",
  "kind": "structure",
  "name": "NuclearSaturation",
  "module_name": "TauLib.BookIV.Particles.HadronsNuclei",
  "module_url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/",
  "source_line_start": 249,
  "source_line_end": 256,
  "registry_ids": [
    "IV.P129"
  ],
  "related_registry_items": [
    {
      "id": "IV.P129",
      "title": "Nuclear force saturation",
      "url": "/registry/object/IV.P129/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/HadronsNuclei.lean#L249-L256",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.HadronsNuclei",
        "url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/HadronsNuclei.lean#L249-L256",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "status": "defined"
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

- Module: [TauLib.BookIV.Particles.HadronsNuclei](/verify/taulib/docs/book-iv-particles-hadrons-nuclei/)
- Source path: [`TauLib/BookIV/Particles/HadronsNuclei.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/HadronsNuclei.lean#L249-L256)
- Source range: L249-L256
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P129` — Nuclear force saturation

## Immediate Comment / Docstring

```lean
/-- [IV.P129] Each nucleon's defect bundle has finite angular extent
    Δθ ≈ ι_τ on the η-circle, so only ~12 nearest neighbors interact.
    Binding energy per nucleon B/A plateaus near 8.8 MeV for large A. -/
```

## Source Excerpt

```lean
structure NuclearSaturation where
  /-- Max neighbors interacting. -/
  max_neighbors : Nat := 12
  /-- B/A plateau (MeV ×10). -/
  ba_plateau_mev_x10 : Nat := 88
  /-- Angular extent determines saturation. -/
  angular_extent : Bool := true
  deriving Repr
```
