---
{
  "projection_kind": "taulib_declaration",
  "title": "TopologicalRelaxation",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-heat-em/topological-relaxation/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Thermodynamics.HeatEM`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.HeatEM::TopologicalRelaxation",
  "declaration_slug": "topological-relaxation",
  "kind": "structure",
  "name": "TopologicalRelaxation",
  "module_name": "TauLib.BookV.Thermodynamics.HeatEM",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-heat-em/",
  "source_line_start": 208,
  "source_line_end": 217,
  "registry_ids": [
    "V.D93"
  ],
  "related_registry_items": [
    {
      "id": "V.D93",
      "title": "Topological relaxation",
      "url": "/registry/object/V.D93/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/HeatEM.lean#L208-L217",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Thermodynamics.HeatEM",
        "url": "/verify/taulib/docs/book-v-thermodynamics-heat-em/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/HeatEM.lean#L208-L217",
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

- Module: [TauLib.BookV.Thermodynamics.HeatEM](/verify/taulib/docs/book-v-thermodynamics-heat-em/)
- Source path: [`TauLib/BookV/Thermodynamics/HeatEM.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/HeatEM.lean#L208-L217)
- Source range: L208-L217
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D93` — Topological relaxation

## Immediate Comment / Docstring

```lean
/-- [V.D93] Topological relaxation: the process by which a defect
    bundle is absorbed by the lemniscate boundary L = S^1 v S^1
    through a change in topological sector.

    Energy release from the variation of holonomy characters at L.
    Much slower than geometric relaxation. -/
```

## Source Excerpt

```lean
structure TopologicalRelaxation where
  /-- Initial defect count. -/
  defects_initial : Nat
  /-- Final defect count (after topological absorption). -/
  defects_final : Nat
  /-- Defect count decreases. -/
  defects_decrease : defects_final ≤ defects_initial
  /-- Whether the topological sector changes. -/
  sector_changes : Bool := true
  deriving Repr
```
