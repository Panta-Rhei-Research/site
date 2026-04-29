---
{
  "projection_kind": "taulib_declaration",
  "title": "StereochemicalSelection",
  "permalink": "/verify/taulib/docs/book-vi-persistence-temporal-lemniscate/stereochemical-selection/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Persistence.TemporalLemniscate`.",
  "declaration_id": "TauLib.BookVI.Persistence.TemporalLemniscate::StereochemicalSelection",
  "declaration_slug": "stereochemical-selection",
  "kind": "structure",
  "name": "StereochemicalSelection",
  "module_name": "TauLib.BookVI.Persistence.TemporalLemniscate",
  "module_url": "/verify/taulib/docs/book-vi-persistence-temporal-lemniscate/",
  "source_line_start": 180,
  "source_line_end": 189,
  "registry_ids": [
    "VI.T42"
  ],
  "related_registry_items": [
    {
      "id": "VI.T42",
      "title": "Stereochemical Selection",
      "url": "/registry/object/VI.T42/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L180-L189",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L180-L189",
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
- Source path: [`TauLib/BookVI/Persistence/TemporalLemniscate.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L180-L189)
- Source range: L180-L189
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.T42` — Stereochemical Selection

## Immediate Comment / Docstring

```lean
/-- [VI.T42] Stereochemical Selection Theorem: SelfDesc closure (VI.T03)
    amplifies the chirality seed (VI.D72) to full enantiomeric excess.
    The polarity propagation (VI.D71) provides the initial asymmetry;
    SelfDesc closure drives ee(n) → 1 monotonically. -/
```

## Source Excerpt

```lean
structure StereochemicalSelection where
  /-- SelfDesc closure amplifies chirality. -/
  selfdesc_amplification : Bool := true
  /-- Chirality seed source: VI.D72. -/
  seed_from_parity_bridge : Bool := true
  /-- Amplification is exponential (gain g per level). -/
  exponential_gain : Bool := true
  /-- Result: ee = 1 at convergence. -/
  final_ee_is_one : Bool := true
  deriving Repr
```
