---
{
  "projection_kind": "taulib_declaration",
  "title": "HomochiralityScopeUpgrade",
  "permalink": "/verify/taulib/docs/book-vi-persistence-temporal-lemniscate/homochirality-scope-upgrade/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Persistence.TemporalLemniscate`.",
  "declaration_id": "TauLib.BookVI.Persistence.TemporalLemniscate::HomochiralityScopeUpgrade",
  "declaration_slug": "homochirality-scope-upgrade",
  "kind": "structure",
  "name": "HomochiralityScopeUpgrade",
  "module_name": "TauLib.BookVI.Persistence.TemporalLemniscate",
  "module_url": "/verify/taulib/docs/book-vi-persistence-temporal-lemniscate/",
  "source_line_start": 270,
  "source_line_end": 280,
  "registry_ids": [
    "VI.R26"
  ],
  "related_registry_items": [
    {
      "id": "VI.R26",
      "title": "Homochirality Scope Upgrade",
      "url": "/registry/object/VI.R26/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L270-L280",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Persistence.TemporalLemniscate",
        "url": "/verify/taulib/docs/book-vi-persistence-temporal-lemniscate/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L270-L280",
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

- Module: [TauLib.BookVI.Persistence.TemporalLemniscate](/verify/taulib/docs/book-vi-persistence-temporal-lemniscate/)
- Source path: [`TauLib/BookVI/Persistence/TemporalLemniscate.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L270-L280)
- Source range: L270-L280
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.R26` — Homochirality Scope Upgrade

## Immediate Comment / Docstring

```lean
/-- [VI.R26] Homochirality Scope Upgrade: documents the complete derivation
    chain that upgrades homochirality from conjectural to τ-effective.
    Chain: K0-K6 → ι_τ → holonomy sectors → σ_A-admissibility (IV.D112)
    → σ = C_τ Majorana (IV.T146) → Parity Bridge (VI.T01)
    → Polarity Propagation (VI.D71) → Chirality Seed (VI.D72)
    → Propagation Preserves Chirality (VI.T41)
    → Stereochemical Selection (VI.T42) → ee → 1 (VI.P21)
    → Homochirality Universality (VI.T43).
    Every link is τ-effective; no conjectural step remains. -/
```

## Source Excerpt

```lean
structure HomochiralityScopeUpgrade where
  /-- Previous scope. -/
  previous_scope : String := "conjectural"
  /-- New scope. -/
  new_scope : String := "tau_effective"
  /-- Derivation chain length. -/
  chain_length : Nat
  chain_complete : chain_length = 12
  /-- VI.OP9 status upgrade. -/
  op9_status : String := "SOLVED"
  deriving Repr
```
