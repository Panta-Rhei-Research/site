---
{
  "projection_kind": "taulib_declaration",
  "title": "DecayChannels",
  "permalink": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/decay-channels/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.HadronsNuclei`.",
  "declaration_id": "TauLib.BookIV.Particles.HadronsNuclei::DecayChannels",
  "declaration_slug": "decay-channels",
  "kind": "structure",
  "name": "DecayChannels",
  "module_name": "TauLib.BookIV.Particles.HadronsNuclei",
  "module_url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/",
  "source_line_start": 388,
  "source_line_end": 395,
  "registry_ids": [
    "IV.P132"
  ],
  "related_registry_items": [
    {
      "id": "IV.P132",
      "title": "Decay channels from sector admissibility",
      "url": "/registry/object/IV.P132/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/HadronsNuclei.lean#L388-L395",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/HadronsNuclei.lean#L388-L395",
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
- Source path: [`TauLib/BookIV/Particles/HadronsNuclei.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/HadronsNuclei.lean#L388-L395)
- Source range: L388-L395
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P132` — Decay channels from sector admissibility

## Immediate Comment / Docstring

```lean
/-- [IV.P132] Every radioactive decay satisfies sector admissibility:
    - Color neutrality (η-holonomy trivial mod 3)
    - Baryon number conserved
    - Electric charge conserved (γ-holonomy)
    - Energy-momentum conserved

    Each decay type corresponds to a specific sector-transition pattern. -/
```

## Source Excerpt

```lean
structure DecayChannels where
  /-- Number of conservation laws. -/
  conservation_laws : Nat := 4
  /-- Decay types. -/
  types : List String := ["alpha", "beta", "gamma"]
  /-- All satisfy sector admissibility. -/
  all_admissible : Bool := true
  deriving Repr
```
