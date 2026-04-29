---
{
  "projection_kind": "taulib_declaration",
  "title": "flow_depth_0",
  "permalink": "/verify/taulib/docs/book-iii-physics-hartogs-flow/flow-depth-0/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Physics.HartogsFlow`.",
  "declaration_id": "TauLib.BookIII.Physics.HartogsFlow::flow_depth_0",
  "declaration_slug": "flow-depth-0",
  "kind": "theorem",
  "name": "flow_depth_0",
  "module_name": "TauLib.BookIII.Physics.HartogsFlow",
  "module_url": "/verify/taulib/docs/book-iii-physics-hartogs-flow/",
  "source_line_start": 225,
  "source_line_end": 226,
  "registry_ids": [
    "III.D40"
  ],
  "related_registry_items": [
    {
      "id": "III.D40",
      "title": "Hartogs Flow Operator",
      "url": "/registry/object/III.D40/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/HartogsFlow.lean#L225-L226",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Physics.HartogsFlow",
        "url": "/verify/taulib/docs/book-iii-physics-hartogs-flow/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/HartogsFlow.lean#L225-L226",
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

- Module: [TauLib.BookIII.Physics.HartogsFlow](/verify/taulib/docs/book-iii-physics-hartogs-flow/)
- Source path: [`TauLib/BookIII/Physics/HartogsFlow.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/HartogsFlow.lean#L225-L226)
- Source range: L225-L226
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.D40` — Hartogs Flow Operator

## Immediate Comment / Docstring

```lean
/-- [III.D40] Structural: flow at depth 0 produces trivial BNF. -/
```

## Source Excerpt

```lean
theorem flow_depth_0 :
    hartogs_flow_step 42 0 = ⟨0, 0, 0, 1⟩ := by native_decide
```
