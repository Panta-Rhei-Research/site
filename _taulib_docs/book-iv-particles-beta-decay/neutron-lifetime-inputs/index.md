---
{
  "projection_kind": "taulib_declaration",
  "title": "NeutronLifetimeInputs",
  "permalink": "/verify/taulib/docs/book-iv-particles-beta-decay/neutron-lifetime-inputs/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.BetaDecay`.",
  "declaration_id": "TauLib.BookIV.Particles.BetaDecay::NeutronLifetimeInputs",
  "declaration_slug": "neutron-lifetime-inputs",
  "kind": "structure",
  "name": "NeutronLifetimeInputs",
  "module_name": "TauLib.BookIV.Particles.BetaDecay",
  "module_url": "/verify/taulib/docs/book-iv-particles-beta-decay/",
  "source_line_start": 368,
  "source_line_end": 379,
  "registry_ids": [
    "IV.D383"
  ],
  "related_registry_items": [
    {
      "id": "IV.D383",
      "title": "Neutron Lifetime Input Table (Wave 46)",
      "url": "/registry/object/IV.D383/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/BetaDecay.lean#L368-L379",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.BetaDecay",
        "url": "/verify/taulib/docs/book-iv-particles-beta-decay/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/BetaDecay.lean#L368-L379",
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

- Module: [TauLib.BookIV.Particles.BetaDecay](/verify/taulib/docs/book-iv-particles-beta-decay/)
- Source path: [`TauLib/BookIV/Particles/BetaDecay.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/BetaDecay.lean#L368-L379)
- Source range: L368-L379
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D383` — Neutron Lifetime Input Table (Wave 46)

## Immediate Comment / Docstring

```lean
/-- [IV.D383] Complete input table for neutron lifetime precision prediction.
    All inputs ι_τ-derived except PDG prefactor K. -/
```

## Source Excerpt

```lean
structure NeutronLifetimeInputs where
  /-- g_A deviation (ppm ×10). -/
  ga_ppm_x10 : Nat := 55
  /-- |V_ud| deviation (ppm). -/
  vud_ppm : Nat := 16
  /-- Δ_r deviation (ppm ×10). -/
  delta_r_ppm_x10 : Nat := 95
  /-- PDG prefactor K (s ×10). -/
  K_s_x10 : Nat := 49087
  /-- Number of ι_τ-derived inputs. -/
  iota_derived_count : Nat := 4
  deriving Repr
```
