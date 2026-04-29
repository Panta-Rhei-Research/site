---
{
  "projection_kind": "taulib_declaration",
  "title": "TauYukawaCoupling",
  "permalink": "/verify/taulib/docs/book-iv-particles-sector-atlas/tau-yukawa-coupling/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.SectorAtlas`.",
  "declaration_id": "TauLib.BookIV.Particles.SectorAtlas::TauYukawaCoupling",
  "declaration_slug": "tau-yukawa-coupling",
  "kind": "structure",
  "name": "TauYukawaCoupling",
  "module_name": "TauLib.BookIV.Particles.SectorAtlas",
  "module_url": "/verify/taulib/docs/book-iv-particles-sector-atlas/",
  "source_line_start": 191,
  "source_line_end": 206,
  "registry_ids": [
    "IV.D195"
  ],
  "related_registry_items": [
    {
      "id": "IV.D195",
      "title": "tau-Yukawa coupling",
      "url": "/registry/object/IV.D195/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/SectorAtlas.lean#L191-L206",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.SectorAtlas",
        "url": "/verify/taulib/docs/book-iv-particles-sector-atlas/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/SectorAtlas.lean#L191-L206",
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

- Module: [TauLib.BookIV.Particles.SectorAtlas](/verify/taulib/docs/book-iv-particles-sector-atlas/)
- Source path: [`TauLib/BookIV/Particles/SectorAtlas.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/SectorAtlas.lean#L191-L206)
- Source range: L191-L206
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D195` — tau-Yukawa coupling

## Immediate Comment / Docstring

```lean
/-- [IV.D195] τ-Yukawa coupling: the coupling of a fermion mode χ_{m,n}
    in sector X to the Higgs sector ω.

    y_f = κ(ω) / √(m² + n²·ι_τ²) × Γ_gen(f)

    Determined by winding-mode overlap with the ω-sector crossing character.
    NOT a free parameter — a readout of fiber geometry. -/
```

## Source Excerpt

```lean
structure TauYukawaCoupling where
  /-- Fermion name. -/
  fermion : String
  /-- Sector. -/
  sector : Sector
  /-- Generation (1, 2, or 3). -/
  generation : Nat
  /-- Approximate coupling (numerator, scaled ×10⁶). -/
  coupling_numer : Nat
  /-- Coupling denominator. -/
  coupling_denom : Nat
  /-- Denominator positive. -/
  denom_pos : coupling_denom > 0 := by omega
  /-- Valid generation. -/
  gen_valid : generation ≥ 1 ∧ generation ≤ 3
  deriving Repr
```
