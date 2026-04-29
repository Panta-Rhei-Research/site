---
{
  "projection_kind": "taulib_declaration",
  "title": "gamma_decay_mode",
  "permalink": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/gamma-decay-mode/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Particles.HadronsNuclei`.",
  "declaration_id": "TauLib.BookIV.Particles.HadronsNuclei::gamma_decay_mode",
  "declaration_slug": "gamma-decay-mode",
  "kind": "def",
  "name": "gamma_decay_mode",
  "module_name": "TauLib.BookIV.Particles.HadronsNuclei",
  "module_url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/",
  "source_line_start": 374,
  "source_line_end": 375,
  "registry_ids": [
    "IV.R139"
  ],
  "related_registry_items": [
    {
      "id": "IV.R139",
      "title": "Gamma-decay as mode transition",
      "url": "/registry/object/IV.R139/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/HadronsNuclei.lean#L374-L375",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/HadronsNuclei.lean#L374-L375",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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
- Source path: [`TauLib/BookIV/Particles/HadronsNuclei.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/HadronsNuclei.lean#L374-L375)
- Source range: L374-L375
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.R139` — Gamma-decay as mode transition

## Immediate Comment / Docstring

```lean
/-- [IV.R139] Gamma-decay is the same mechanism as atomic spectral lines:
    a T²-winding mode transition with energy carried by a B-sector photon.
    Only difference: scale (MeV nuclear vs eV atomic). -/
```

## Source Excerpt

```lean
def gamma_decay_mode : String :=
  "Gamma-decay: T^2 mode transition at MeV scale (same mechanism as atomic lines)"
```
