---
{
  "projection_kind": "taulib_declaration",
  "title": "PolarityFunctional",
  "permalink": "/corpus/taulib/docs/book-vi-life-core-parity-bridge/polarity-functional/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.LifeCore.ParityBridge`.",
  "declaration_id": "TauLib.BookVI.LifeCore.ParityBridge::PolarityFunctional",
  "declaration_slug": "polarity-functional",
  "kind": "structure",
  "name": "PolarityFunctional",
  "module_name": "TauLib.BookVI.LifeCore.ParityBridge",
  "module_url": "/corpus/taulib/docs/book-vi-life-core-parity-bridge/",
  "source_line_start": 28,
  "source_line_end": 33,
  "registry_ids": [
    "VI.D01"
  ],
  "related_registry_items": [
    {
      "id": "VI.D01",
      "title": "Polarity Functional",
      "url": "/registry/object/VI.D01/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/ParityBridge.lean#L28-L33",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.LifeCore.ParityBridge",
        "url": "/corpus/taulib/docs/book-vi-life-core-parity-bridge/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/ParityBridge.lean#L28-L33",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "role": "type/data schema",
      "status": "type/data schema"
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

- Module: [TauLib.BookVI.LifeCore.ParityBridge](/corpus/taulib/docs/book-vi-life-core-parity-bridge/)
- Source path: [`TauLib/BookVI/LifeCore/ParityBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/ParityBridge.lean#L28-L33)
- Source range: L28-L33
- Kind: `structure`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- `VI.D01` — Polarity Functional

## Immediate Comment / Docstring

```lean
/-- [VI.D01] Polarity functional: map P_S: End(S) → 2_τ testing whether
    a holonomy sector carries intrinsic parity asymmetry.
    Trivial for EM, Strong, Gravity; nontrivial uniquely for Weak. -/
```

## Source Excerpt

```lean
structure PolarityFunctional where
  sectors_tested : Nat
  nontrivial_count : Nat
  unique_nontrivial : nontrivial_count = 1
  all_tested : sectors_tested = 4
  deriving Repr
```
