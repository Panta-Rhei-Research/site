---
{
  "projection_kind": "taulib_declaration",
  "title": "FiberEnabledRegime",
  "permalink": "/verify/taulib/docs/book-vi-consumer-fiber-regime/fiber-enabled-regime/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Consumer.FiberRegime`.",
  "declaration_id": "TauLib.BookVI.Consumer.FiberRegime::FiberEnabledRegime",
  "declaration_slug": "fiber-enabled-regime",
  "kind": "structure",
  "name": "FiberEnabledRegime",
  "module_name": "TauLib.BookVI.Consumer.FiberRegime",
  "module_url": "/verify/taulib/docs/book-vi-consumer-fiber-regime/",
  "source_line_start": 37,
  "source_line_end": 52,
  "registry_ids": [
    "VI.D47"
  ],
  "related_registry_items": [
    {
      "id": "VI.D47",
      "title": "Fiber-Enabled Regime",
      "url": "/registry/object/VI.D47/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/FiberRegime.lean#L37-L52",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Consumer.FiberRegime",
        "url": "/verify/taulib/docs/book-vi-consumer-fiber-regime/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/FiberRegime.lean#L37-L52",
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

- Module: [TauLib.BookVI.Consumer.FiberRegime](/verify/taulib/docs/book-vi-consumer-fiber-regime/)
- Source path: [`TauLib/BookVI/Consumer/FiberRegime.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/FiberRegime.lean#L37-L52)
- Source range: L37-L52
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D47` — Fiber-Enabled Regime

## Immediate Comment / Docstring

```lean
/-- [VI.D47] Fiber-Enabled Regime: eukaryotic compartmentalization
    unlocked by mixed-sector access to both fiber generators.
    Four key innovations: nucleus, mitochondria, endomembrane, cytoskeleton. -/
```

## Source Excerpt

```lean
structure FiberEnabledRegime where
  /-- Full compartmentalization achieved. -/
  compartmentalization : Bool := true
  /-- Number of key innovations. -/
  innovation_count : Nat
  /-- Exactly 4 innovations. -/
  count_eq : innovation_count = 4
  /-- Innovation 1: nuclear envelope. -/
  nucleus : Bool := true
  /-- Innovation 2: mitochondria (endosymbiosis). -/
  mitochondria : Bool := true
  /-- Innovation 3: endomembrane system. -/
  endomembrane : Bool := true
  /-- Innovation 4: cytoskeleton. -/
  cytoskeleton : Bool := true
  deriving Repr
```
