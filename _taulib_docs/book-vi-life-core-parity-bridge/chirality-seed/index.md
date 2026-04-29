---
{
  "projection_kind": "taulib_declaration",
  "title": "ChiralitySeed",
  "permalink": "/verify/taulib/docs/book-vi-life-core-parity-bridge/chirality-seed/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.LifeCore.ParityBridge`.",
  "declaration_id": "TauLib.BookVI.LifeCore.ParityBridge::ChiralitySeed",
  "declaration_slug": "chirality-seed",
  "kind": "structure",
  "name": "ChiralitySeed",
  "module_name": "TauLib.BookVI.LifeCore.ParityBridge",
  "module_url": "/verify/taulib/docs/book-vi-life-core-parity-bridge/",
  "source_line_start": 135,
  "source_line_end": 143,
  "registry_ids": [
    "VI.D72"
  ],
  "related_registry_items": [
    {
      "id": "VI.D72",
      "title": "Chirality Seed",
      "url": "/registry/object/VI.D72/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/ParityBridge.lean#L135-L143",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.LifeCore.ParityBridge",
        "url": "/verify/taulib/docs/book-vi-life-core-parity-bridge/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/ParityBridge.lean#L135-L143",
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

- Module: [TauLib.BookVI.LifeCore.ParityBridge](/verify/taulib/docs/book-vi-life-core-parity-bridge/)
- Source path: [`TauLib/BookVI/LifeCore/ParityBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/ParityBridge.lean#L135-L143)
- Source range: L135-L143
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D72` — Chirality Seed

## Immediate Comment / Docstring

```lean
/-- [VI.D72] Chirality Seed: initial asymmetry from weak parity violation.
    The weak sector couples exclusively to left-handed fermions (V(A)=100%),
    seeding a universal directional bias. The seed magnitude is ~10⁻¹⁷ eV
    but the sign is coherent across all chiral molecules. -/
```

## Source Excerpt

```lean
structure ChiralitySeed where
  /-- Parity violation is maximal (100%) in weak sector. -/
  va_coupling_pct : Nat
  va_maximal : va_coupling_pct = 100
  /-- Seed is coherent: same sign for all amino acids. -/
  coherent : Bool := true
  /-- Source: IV.T146 σ = C_τ (Majorana). -/
  iv_t146_source : Bool := true
  deriving Repr
```
