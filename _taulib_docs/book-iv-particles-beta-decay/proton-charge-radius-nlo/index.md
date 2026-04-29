---
{
  "projection_kind": "taulib_declaration",
  "title": "ProtonChargeRadiusNLO",
  "permalink": "/verify/taulib/docs/book-iv-particles-beta-decay/proton-charge-radius-nlo/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.BetaDecay`.",
  "declaration_id": "TauLib.BookIV.Particles.BetaDecay::ProtonChargeRadiusNLO",
  "declaration_slug": "proton-charge-radius-nlo",
  "kind": "structure",
  "name": "ProtonChargeRadiusNLO",
  "module_name": "TauLib.BookIV.Particles.BetaDecay",
  "module_url": "/verify/taulib/docs/book-iv-particles-beta-decay/",
  "source_line_start": 339,
  "source_line_end": 354,
  "registry_ids": [
    "IV.T202"
  ],
  "related_registry_items": [
    {
      "id": "IV.T202",
      "title": "Proton Charge Radius NLO at +12 ppm",
      "url": "/registry/object/IV.T202/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/BetaDecay.lean#L339-L354",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/BetaDecay.lean#L339-L354",
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
- Source path: [`TauLib/BookIV/Particles/BetaDecay.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/BetaDecay.lean#L339-L354)
- Source range: L339-L354
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T202` — Proton Charge Radius NLO at +12 ppm

## Immediate Comment / Docstring

```lean
/-- [IV.T202] r_p(NLO) = 4λ̄_p(1 − ι_τ²·α/|lobes|) = 0.84088 fm.
    NLO correction from EM dressing: holonomy² × α / lobes.
    CREMA = 0.84087 fm → +12 ppm (36× improvement from LO +440 ppm). -/
```

## Source Excerpt

```lean
structure ProtonChargeRadiusNLO where
  /-- LO value (fm ×100000). -/
  r_p_lo_fm_x100k : Nat := 84124
  /-- NLO correction δ_r (×10⁶). -/
  delta_r_x1e6 : Nat := 425
  /-- NLO value (fm ×100000). -/
  r_p_nlo_fm_x100k : Nat := 84088
  /-- CREMA experimental (fm ×100000). -/
  crema_fm_x100k : Nat := 84087
  /-- Deviation LO (ppm). -/
  deviation_lo_ppm : Nat := 440
  /-- Deviation NLO (ppm). -/
  deviation_nlo_ppm : Nat := 12
  /-- Improvement factor. -/
  improvement_factor : Nat := 36
  deriving Repr
```
