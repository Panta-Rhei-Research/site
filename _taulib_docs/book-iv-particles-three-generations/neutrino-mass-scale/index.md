---
{
  "projection_kind": "taulib_declaration",
  "title": "NeutrinoMassScale",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/neutrino-mass-scale/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::NeutrinoMassScale",
  "declaration_slug": "neutrino-mass-scale",
  "kind": "structure",
  "name": "NeutrinoMassScale",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 327,
  "source_line_end": 338,
  "registry_ids": [
    "IV.P124"
  ],
  "related_registry_items": [
    {
      "id": "IV.P124",
      "title": "Neutrino mass scale",
      "url": "/registry/object/IV.P124/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L327-L338",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.ThreeGenerations",
        "url": "/verify/taulib/docs/book-iv-particles-three-generations/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L327-L338",
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

- Module: [TauLib.BookIV.Particles.ThreeGenerations](/verify/taulib/docs/book-iv-particles-three-generations/)
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L327-L338)
- Source range: L327-L338
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P124` — Neutrino mass scale

## Immediate Comment / Docstring

```lean
/-- [IV.P124] m₃(ν) ≈ m_e · ι_τ¹⁵ ≈ 50.7 meV.
    Exponent 15 = 7 + 8, where 7 is the electron's level and 8 = 2×4
    is the fiber spectral dimension gap.

    Experimental: ≈ 49.5 meV (cosmological bounds).
    Scope: conjectural. -/
```

## Source Excerpt

```lean
structure NeutrinoMassScale where
  /-- Exponent in ι_τ power. -/
  exponent : Nat := 15
  /-- Electron level. -/
  electron_level : Nat := 7
  /-- Spectral gap. -/
  spectral_gap : Nat := 8
  /-- Predicted mass (meV ×10). -/
  predicted_mev_x10 : Nat := 507
  /-- Scope. -/
  scope : String := "tau-effective"
  deriving Repr
```
