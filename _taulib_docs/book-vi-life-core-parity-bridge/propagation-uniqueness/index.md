---
{
  "projection_kind": "taulib_declaration",
  "title": "propagation_uniqueness",
  "permalink": "/verify/taulib/docs/book-vi-life-core-parity-bridge/propagation-uniqueness/",
  "summary_short": "`theorem` declaration in `TauLib.BookVI.LifeCore.ParityBridge`.",
  "declaration_id": "TauLib.BookVI.LifeCore.ParityBridge::propagation_uniqueness",
  "declaration_slug": "propagation-uniqueness",
  "kind": "theorem",
  "name": "propagation_uniqueness",
  "module_name": "TauLib.BookVI.LifeCore.ParityBridge",
  "module_url": "/verify/taulib/docs/book-vi-life-core-parity-bridge/",
  "source_line_start": 172,
  "source_line_end": 177,
  "registry_ids": [
    "VI.L14"
  ],
  "related_registry_items": [
    {
      "id": "VI.L14",
      "title": "Propagation Uniqueness",
      "url": "/registry/object/VI.L14/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/ParityBridge.lean#L172-L177",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/ParityBridge.lean#L172-L177",
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
- Source path: [`TauLib/BookVI/LifeCore/ParityBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/ParityBridge.lean#L172-L177)
- Source range: L172-L177
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VI.L14` — Propagation Uniqueness

## Immediate Comment / Docstring

```lean
/-- [VI.L14] Propagation Uniqueness: weak-sector uniqueness (VI.L01) implies
    the propagation path is unique. Since only one sector has nontrivial
    polarity, there is exactly one route from parity violation to chirality seed. -/
```

## Source Excerpt

```lean
theorem propagation_uniqueness :
    polarity_functional.nontrivial_count = 1 ∧
    polarity_propagation.bridge_path_count = 1 :=
  ⟨rfl, rfl⟩

end Tau.BookVI.ParityBridge
```
