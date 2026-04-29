---
{
  "projection_kind": "taulib_declaration",
  "title": "BohrRadius",
  "permalink": "/verify/taulib/docs/book-iv-particles-beta-decay/bohr-radius/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.BetaDecay`.",
  "declaration_id": "TauLib.BookIV.Particles.BetaDecay::BohrRadius",
  "declaration_slug": "bohr-radius",
  "kind": "structure",
  "name": "BohrRadius",
  "module_name": "TauLib.BookIV.Particles.BetaDecay",
  "module_url": "/verify/taulib/docs/book-iv-particles-beta-decay/",
  "source_line_start": 131,
  "source_line_end": 140,
  "registry_ids": [
    "IV.P126"
  ],
  "related_registry_items": [
    {
      "id": "IV.P126",
      "title": "Bohr radius from iota_tau",
      "url": "/registry/object/IV.P126/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/BetaDecay.lean#L131-L140",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/BetaDecay.lean#L131-L140",
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
- Source path: [`TauLib/BookIV/Particles/BetaDecay.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/BetaDecay.lean#L131-L140)
- Source range: L131-L140
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P126` — Bohr radius from iota_tau

## Immediate Comment / Docstring

```lean
/-- [IV.P126] a₀ = R/(α_em · m_n) × (ℏ/c) is fully determined by ι_τ and m_n.
    Both R = m_n/m_e and α_em ≈ (8/15)·ι_τ⁴ are rational functions of ι_τ.

    CODATA: a₀ ≈ 5.29177210544 × 10⁻¹¹ m.
    Precision limited by m_e at 0.025 ppm. -/
```

## Source Excerpt

```lean
structure BohrRadius where
  /-- Prediction matches CODATA. -/
  matches_codata : Bool := true
  /-- Derived from ι_τ and m_n only. -/
  iota_and_mn_only : Bool := true
  /-- CODATA value (pm, ×1000 for integer). -/
  codata_pm_x1000 : Nat := 52918
  /-- Precision limited by m_e (ppm). -/
  precision_ppm : Nat := 25
  deriving Repr
```
