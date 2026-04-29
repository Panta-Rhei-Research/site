---
{
  "projection_kind": "taulib_declaration",
  "title": "TopologicalMotif",
  "permalink": "/verify/taulib/docs/book-v-cosmology-global-finiteness/topological-motif/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.GlobalFiniteness`.",
  "declaration_id": "TauLib.BookV.Cosmology.GlobalFiniteness::TopologicalMotif",
  "declaration_slug": "topological-motif",
  "kind": "structure",
  "name": "TopologicalMotif",
  "module_name": "TauLib.BookV.Cosmology.GlobalFiniteness",
  "module_url": "/verify/taulib/docs/book-v-cosmology-global-finiteness/",
  "source_line_start": 87,
  "source_line_end": 102,
  "registry_ids": [
    "V.D178"
  ],
  "related_registry_items": [
    {
      "id": "V.D178",
      "title": "Topological motif",
      "url": "/registry/object/V.D178/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/GlobalFiniteness.lean#L87-L102",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.GlobalFiniteness",
        "url": "/verify/taulib/docs/book-v-cosmology-global-finiteness/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/GlobalFiniteness.lean#L87-L102",
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

- Module: [TauLib.BookV.Cosmology.GlobalFiniteness](/verify/taulib/docs/book-v-cosmology-global-finiteness/)
- Source path: [`TauLib/BookV/Cosmology/GlobalFiniteness.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/GlobalFiniteness.lean#L87-L102)
- Source range: L87-L102
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D178` — Topological motif

## Immediate Comment / Docstring

```lean
/-- [V.D178] Topological motif: an equivalence class of defect tuple
    configurations at depth n, classified by topology and sector content.

    Two configurations are equivalent if they have the same stable
    irreducible topology and the same 4-component defect signature. -/
```

## Source Excerpt

```lean
structure TopologicalMotif where
  /-- Defect mobility component. -/
  mobility : Nat
  /-- Defect vorticity component. -/
  vorticity : Nat
  /-- Defect compression component. -/
  compression : Nat
  /-- Defect topological component. -/
  topological : Nat
  /-- Refinement depth. -/
  depth : Nat
  /-- Depth positive. -/
  depth_pos : depth > 0
  /-- Stability classification. -/
  stability : MotifStability
  deriving Repr
```
