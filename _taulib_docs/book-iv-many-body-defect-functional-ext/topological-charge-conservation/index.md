---
{
  "projection_kind": "taulib_declaration",
  "title": "TopologicalChargeConservation",
  "permalink": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/topological-charge-conservation/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.ManyBody.DefectFunctionalExt`.",
  "declaration_id": "TauLib.BookIV.ManyBody.DefectFunctionalExt::TopologicalChargeConservation",
  "declaration_slug": "topological-charge-conservation",
  "kind": "structure",
  "name": "TopologicalChargeConservation",
  "module_name": "TauLib.BookIV.ManyBody.DefectFunctionalExt",
  "module_url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/",
  "source_line_start": 197,
  "source_line_end": 204,
  "registry_ids": [
    "IV.P134"
  ],
  "related_registry_items": [
    {
      "id": "IV.P134",
      "title": "Topological charge conservation",
      "url": "/registry/object/IV.P134/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L197-L204",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.ManyBody.DefectFunctionalExt",
        "url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L197-L204",
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

- Module: [TauLib.BookIV.ManyBody.DefectFunctionalExt](/verify/taulib/docs/book-iv-many-body-defect-functional-ext/)
- Source path: [`TauLib/BookIV/ManyBody/DefectFunctionalExt.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L197-L204)
- Source range: L197-L204
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P134` — Topological charge conservation

## Immediate Comment / Docstring

```lean
/-- [IV.P134] Total topological charge is conserved under any process
    that does not create or annihilate defect bundles:
    theta^tot(C_{n+1}) = theta^tot(C_n) for all primorial stages n.
    This reflects homotopy invariance of winding numbers on T^2. -/
```

## Source Excerpt

```lean
structure TopologicalChargeConservation where
  /-- Charge at stage n. -/
  charge_n : Int
  /-- Charge at stage n+1. -/
  charge_n_plus_1 : Int
  /-- Conservation: equal across stages. -/
  conserved : charge_n = charge_n_plus_1
  deriving Repr
```
