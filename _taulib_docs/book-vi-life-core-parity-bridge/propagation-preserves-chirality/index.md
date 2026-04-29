---
{
  "projection_kind": "taulib_declaration",
  "title": "propagation_preserves_chirality",
  "permalink": "/verify/taulib/docs/book-vi-life-core-parity-bridge/propagation-preserves-chirality/",
  "summary_short": "`theorem` declaration in `TauLib.BookVI.LifeCore.ParityBridge`.",
  "declaration_id": "TauLib.BookVI.LifeCore.ParityBridge::propagation_preserves_chirality",
  "declaration_slug": "propagation-preserves-chirality",
  "kind": "theorem",
  "name": "propagation_preserves_chirality",
  "module_name": "TauLib.BookVI.LifeCore.ParityBridge",
  "module_url": "/verify/taulib/docs/book-vi-life-core-parity-bridge/",
  "source_line_start": 158,
  "source_line_end": 163,
  "registry_ids": [
    "VI.T41"
  ],
  "related_registry_items": [
    {
      "id": "VI.T41",
      "title": "Propagation Preserves Chirality",
      "url": "/registry/object/VI.T41/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/ParityBridge.lean#L158-L163",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/ParityBridge.lean#L158-L163",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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
- Source path: [`TauLib/BookVI/LifeCore/ParityBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/ParityBridge.lean#L158-L163)
- Source range: L158-L163
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VI.T41` — Propagation Preserves Chirality

## Immediate Comment / Docstring

```lean
/-- [VI.T41] Propagation Preserves Chirality: left-handed input through the
    Parity Bridge yields a definite polarity sign in 2_τ.
    Proof chain: weak-sector parity violation (ChiralitySeed, VI.D72)
    → unique bridge path (PolarityPropagation, VI.D71)
    → definite polarity (PolarityFunctional, VI.D01). -/
```

## Source Excerpt

```lean
theorem propagation_preserves_chirality :
    polarity_propagation.sign_preserved = true ∧
    polarity_propagation.bridge_path_count = 1 ∧
    chirality_seed.va_coupling_pct = 100 ∧
    chirality_seed.coherent = true :=
  ⟨rfl, rfl, rfl, rfl⟩
```
