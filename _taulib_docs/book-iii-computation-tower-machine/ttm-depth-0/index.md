---
{
  "projection_kind": "taulib_declaration",
  "title": "ttm_depth_0",
  "permalink": "/verify/taulib/docs/book-iii-computation-tower-machine/ttm-depth-0/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Computation.TowerMachine`.",
  "declaration_id": "TauLib.BookIII.Computation.TowerMachine::ttm_depth_0",
  "declaration_slug": "ttm-depth-0",
  "kind": "theorem",
  "name": "ttm_depth_0",
  "module_name": "TauLib.BookIII.Computation.TowerMachine",
  "module_url": "/verify/taulib/docs/book-iii-computation-tower-machine/",
  "source_line_start": 201,
  "source_line_end": 202,
  "registry_ids": [
    "III.D51"
  ],
  "related_registry_items": [
    {
      "id": "III.D51",
      "title": "τ-Tower Machine",
      "url": "/registry/object/III.D51/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/TowerMachine.lean#L201-L202",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Computation.TowerMachine",
        "url": "/verify/taulib/docs/book-iii-computation-tower-machine/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/TowerMachine.lean#L201-L202",
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

- Module: [TauLib.BookIII.Computation.TowerMachine](/verify/taulib/docs/book-iii-computation-tower-machine/)
- Source path: [`TauLib/BookIII/Computation/TowerMachine.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/TowerMachine.lean#L201-L202)
- Source range: L201-L202
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.D51` — τ-Tower Machine

## Immediate Comment / Docstring

```lean
/-- [III.D51] Structural: TTM at depth 0 (Prim(0)=1, all ops mod 1). -/
```

## Source Excerpt

```lean
theorem ttm_depth_0 :
    (ttm_step ⟨0, 42, 7, 0⟩).depth = 0 := by native_decide
```
