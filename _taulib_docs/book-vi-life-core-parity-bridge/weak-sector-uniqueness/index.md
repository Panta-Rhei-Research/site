---
{
  "projection_kind": "taulib_declaration",
  "title": "weak_sector_uniqueness",
  "permalink": "/verify/taulib/docs/book-vi-life-core-parity-bridge/weak-sector-uniqueness/",
  "summary_short": "`theorem` declaration in `TauLib.BookVI.LifeCore.ParityBridge`.",
  "declaration_id": "TauLib.BookVI.LifeCore.ParityBridge::weak_sector_uniqueness",
  "declaration_slug": "weak-sector-uniqueness",
  "kind": "theorem",
  "name": "weak_sector_uniqueness",
  "module_name": "TauLib.BookVI.LifeCore.ParityBridge",
  "module_url": "/verify/taulib/docs/book-vi-life-core-parity-bridge/",
  "source_line_start": 66,
  "source_line_end": 69,
  "registry_ids": [
    "VI.L01"
  ],
  "related_registry_items": [
    {
      "id": "VI.L01",
      "title": "Weak-Sector Uniqueness",
      "url": "/registry/object/VI.L01/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/ParityBridge.lean#L66-L69",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/ParityBridge.lean#L66-L69",
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
- Source path: [`TauLib/BookVI/LifeCore/ParityBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/ParityBridge.lean#L66-L69)
- Source range: L66-L69
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VI.L01` — Weak-Sector Uniqueness

## Immediate Comment / Docstring

```lean
/-- [VI.L01] Weak-sector uniqueness: among 4 primitive sectors,
    weak is the unique one with nontrivial polarity. -/
```

## Source Excerpt

```lean
theorem weak_sector_uniqueness :
    polarity_functional.nontrivial_count = 1 ∧
    polarity_functional.sectors_tested = 4 :=
  ⟨rfl, rfl⟩
```
