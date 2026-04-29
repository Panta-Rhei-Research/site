---
{
  "projection_kind": "taulib_declaration",
  "title": "SectorAdditivity",
  "permalink": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/sector-additivity/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.ManyBody.DefectFunctionalExt`.",
  "declaration_id": "TauLib.BookIV.ManyBody.DefectFunctionalExt::SectorAdditivity",
  "declaration_slug": "sector-additivity",
  "kind": "structure",
  "name": "SectorAdditivity",
  "module_name": "TauLib.BookIV.ManyBody.DefectFunctionalExt",
  "module_url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/",
  "source_line_start": 289,
  "source_line_end": 298,
  "registry_ids": [
    "IV.T90"
  ],
  "related_registry_items": [
    {
      "id": "IV.T90",
      "title": "Sector additivity",
      "url": "/registry/object/IV.T90/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L289-L298",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L289-L298",
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
- Source path: [`TauLib/BookIV/ManyBody/DefectFunctionalExt.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L289-L298)
- Source range: L289-L298
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T90` — Sector additivity

## Immediate Comment / Docstring

```lean
/-- [IV.T90] Sector additivity: the universal defect functional decomposes as
    delta[omega] = delta_D + delta_A + delta_B + delta_C + delta_omega,
    with each sector functional inheriting tower compatibility, because
    refinement maps commute with sector projection. -/
```

## Source Excerpt

```lean
structure SectorAdditivity where
  /-- Number of sector summands. -/
  num_sectors : Nat := 5
  /-- Sectors: D, A, B, C, omega. -/
  sectors : List String := ["D (Gravity)", "A (Weak)", "B (EM)", "C (Strong)", "omega (Higgs)"]
  /-- Each sector inherits tower compatibility. -/
  each_tower_compatible : Bool := true
  /-- Refinement commutes with sector projection. -/
  refinement_commutes : Bool := true
  deriving Repr
```
