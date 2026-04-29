---
{
  "projection_kind": "taulib_declaration",
  "title": "ThermodynamicInevitability",
  "permalink": "/verify/taulib/docs/book-vi-persistence-persistence-sector/thermodynamic-inevitability/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Persistence.PersistenceSector`.",
  "declaration_id": "TauLib.BookVI.Persistence.PersistenceSector::ThermodynamicInevitability",
  "declaration_slug": "thermodynamic-inevitability",
  "kind": "structure",
  "name": "ThermodynamicInevitability",
  "module_name": "TauLib.BookVI.Persistence.PersistenceSector",
  "module_url": "/verify/taulib/docs/book-vi-persistence-persistence-sector/",
  "source_line_start": 159,
  "source_line_end": 172,
  "registry_ids": [
    "VI.P08"
  ],
  "related_registry_items": [
    {
      "id": "VI.P08",
      "title": "Thermodynamic Inevitability of Life",
      "url": "/registry/object/VI.P08/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/PersistenceSector.lean#L159-L172",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Persistence.PersistenceSector",
        "url": "/verify/taulib/docs/book-vi-persistence-persistence-sector/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/PersistenceSector.lean#L159-L172",
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

- Module: [TauLib.BookVI.Persistence.PersistenceSector](/verify/taulib/docs/book-vi-persistence-persistence-sector/)
- Source path: [`TauLib/BookVI/Persistence/PersistenceSector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/PersistenceSector.lean#L159-L172)
- Source range: L159-L172
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.P08` — Thermodynamic Inevitability of Life

## Immediate Comment / Docstring

```lean
/-- [VI.P08] Thermodynamic Inevitability of Life (τ-effective).
    Life is a thermodynamic attractor with positive-measure basin.
    Three-step argument: entropy production → SelfDesc attractor → speed of abiogenesis.
    Upgraded from conjectural via VI.T46 derivation chain:
    K0–K6 → V.T60 → V.T62 → VI.D75 → VI.L15 → VI.T44 → VI.L16 → VI.T46. -/
```

## Source Excerpt

```lean
structure ThermodynamicInevitability where
  /-- Number of argument steps. -/
  argument_steps : Nat
  /-- Exactly 3 steps. -/
  steps_eq : argument_steps = 3
  /-- (i) Entropy production maximization. -/
  entropy_maximization : Bool := true
  /-- (ii) SelfDesc as thermodynamic attractor. -/
  selfdesc_attractor : Bool := true
  /-- (iii) Speed of abiogenesis (~500 Myr). -/
  rapid_abiogenesis : Bool := true
  /-- Scope: τ-effective (upgraded via VI.T46 derivation chain). -/
  scope : String := "tau_effective"
  deriving Repr
```
