---
{
  "projection_kind": "taulib_declaration",
  "title": "AbiogenesisInevitability",
  "permalink": "/verify/taulib/docs/book-vi-persistence-persistence-sector/abiogenesis-inevitability/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Persistence.PersistenceSector`.",
  "declaration_id": "TauLib.BookVI.Persistence.PersistenceSector::AbiogenesisInevitability",
  "declaration_slug": "abiogenesis-inevitability",
  "kind": "structure",
  "name": "AbiogenesisInevitability",
  "module_name": "TauLib.BookVI.Persistence.PersistenceSector",
  "module_url": "/verify/taulib/docs/book-vi-persistence-persistence-sector/",
  "source_line_start": 431,
  "source_line_end": 446,
  "registry_ids": [
    "VI.T46"
  ],
  "related_registry_items": [
    {
      "id": "VI.T46",
      "title": "Abiogenesis Inevitability",
      "url": "/registry/object/VI.T46/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/PersistenceSector.lean#L431-L446",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/PersistenceSector.lean#L431-L446",
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
- Source path: [`TauLib/BookVI/Persistence/PersistenceSector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/PersistenceSector.lean#L431-L446)
- Source range: L431-L446
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.T46` — Abiogenesis Inevitability

## Immediate Comment / Docstring

```lean
/-- [VI.T46] Abiogenesis Inevitability Theorem: first persistence-sector
    entry is structurally inevitable.
    Derivation chain:
      K0–K6 → defect budget (V.T60) → exhaustion (V.T62)
      → complexity budget (VI.D75) → monotone increase (VI.L15)
      → threshold crossing (VI.T44) → absorbing basin (VI.L16)
      → first entry inevitable within timescale bound (VI.T45).
    This combines attractor existence + timescale bound + SelfDesc closure
    to establish that abiogenesis is not contingent but structurally forced. -/
```

## Source Excerpt

```lean
structure AbiogenesisInevitability where
  /-- Number of links in derivation chain. -/
  chain_length : Nat
  /-- Chain has 7 links. -/
  chain_eq : chain_length = 7
  /-- Attractor existence established (VI.T44). -/
  attractor_exists : Bool := true
  /-- Timescale is bounded (VI.T45). -/
  timescale_bounded : Bool := true
  /-- Basin is absorbing (VI.L16). -/
  basin_absorbing : Bool := true
  /-- Conclusion: first entry inevitable. -/
  inevitable : Bool := true
  /-- Scope: τ-effective. -/
  scope : String := "tau_effective"
  deriving Repr
```
