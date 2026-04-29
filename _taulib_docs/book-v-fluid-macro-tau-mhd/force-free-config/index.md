---
{
  "projection_kind": "taulib_declaration",
  "title": "ForceFreeConfig",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-tau-mhd/force-free-config/",
  "summary_short": "`structure` declaration in `TauLib.BookV.FluidMacro.TauMHD`.",
  "declaration_id": "TauLib.BookV.FluidMacro.TauMHD::ForceFreeConfig",
  "declaration_slug": "force-free-config",
  "kind": "structure",
  "name": "ForceFreeConfig",
  "module_name": "TauLib.BookV.FluidMacro.TauMHD",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-tau-mhd/",
  "source_line_start": 257,
  "source_line_end": 264,
  "registry_ids": [
    "V.P51"
  ],
  "related_registry_items": [
    {
      "id": "V.P51",
      "title": "Magnetosonic dispersion",
      "url": "/registry/object/V.P51/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauMHD.lean#L257-L264",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.FluidMacro.TauMHD",
        "url": "/verify/taulib/docs/book-v-fluid-macro-tau-mhd/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauMHD.lean#L257-L264",
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

- Module: [TauLib.BookV.FluidMacro.TauMHD](/verify/taulib/docs/book-v-fluid-macro-tau-mhd/)
- Source path: [`TauLib/BookV/FluidMacro/TauMHD.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauMHD.lean#L257-L264)
- Source range: L257-L264
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.P51` — Magnetosonic dispersion

## Immediate Comment / Docstring

```lean
/-- [V.P51] Force-free equilibrium: a magnetic configuration where
    the Lorentz force vanishes: J × B = 0.

    Equivalently: J ∥ B (current flows along field lines).
    Relevant for: stellar coronae, relativistic jets, pulsar magnetospheres. -/
```

## Source Excerpt

```lean
structure ForceFreeConfig where
  /-- Whether the configuration is force-free (J × B = 0). -/
  is_force_free : Bool := true
  /-- Whether the configuration is linear force-free (∇ × B = αB). -/
  is_linear : Bool
  /-- Force-free parameter α (scaled). -/
  alpha_param : Nat
  deriving Repr
```
