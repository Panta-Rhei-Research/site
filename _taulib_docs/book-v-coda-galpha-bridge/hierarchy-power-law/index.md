---
{
  "projection_kind": "taulib_declaration",
  "title": "HierarchyPowerLaw",
  "permalink": "/verify/taulib/docs/book-v-coda-galpha-bridge/hierarchy-power-law/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Coda.GAlphaBridge`.",
  "declaration_id": "TauLib.BookV.Coda.GAlphaBridge::HierarchyPowerLaw",
  "declaration_slug": "hierarchy-power-law",
  "kind": "structure",
  "name": "HierarchyPowerLaw",
  "module_name": "TauLib.BookV.Coda.GAlphaBridge",
  "module_url": "/verify/taulib/docs/book-v-coda-galpha-bridge/",
  "source_line_start": 156,
  "source_line_end": 163,
  "registry_ids": [
    "V.P115"
  ],
  "related_registry_items": [
    {
      "id": "V.P115",
      "title": "Hierarchy as Power Law",
      "url": "/registry/object/V.P115/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/GAlphaBridge.lean#L156-L163",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Coda.GAlphaBridge",
        "url": "/verify/taulib/docs/book-v-coda-galpha-bridge/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/GAlphaBridge.lean#L156-L163",
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

- Module: [TauLib.BookV.Coda.GAlphaBridge](/verify/taulib/docs/book-v-coda-galpha-bridge/)
- Source path: [`TauLib/BookV/Coda/GAlphaBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/GAlphaBridge.lean#L156-L163)
- Source range: L156-L163
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.P115` — Hierarchy as Power Law

## Immediate Comment / Docstring

```lean
/-- [V.P115] Hierarchy as power law: α/α_G = α⁻¹⁷ · ...
    with exponent 17 = 18 − 1.

    The gravity-EM coupling ratio spans ~39 orders of magnitude.
    This is structurally determined, not fine-tuned. -/
```

## Source Excerpt

```lean
structure HierarchyPowerLaw where
  /-- Power law exponent. -/
  power_exp : Nat
  /-- Exponent is 17. -/
  exp_eq : power_exp = 17
  /-- 17 = 18 − 1. -/
  exp_from_holonomy : power_exp + 1 = 18
  deriving Repr
```
