---
{
  "projection_kind": "taulib_declaration",
  "title": "flow_stable_1",
  "permalink": "/verify/taulib/docs/book-iii-physics-hartogs-flow/flow-stable-1/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Physics.HartogsFlow`.",
  "declaration_id": "TauLib.BookIII.Physics.HartogsFlow::flow_stable_1",
  "declaration_slug": "flow-stable-1",
  "kind": "theorem",
  "name": "flow_stable_1",
  "module_name": "TauLib.BookIII.Physics.HartogsFlow",
  "module_url": "/verify/taulib/docs/book-iii-physics-hartogs-flow/",
  "source_line_start": 233,
  "source_line_end": 236,
  "registry_ids": [
    "III.T24"
  ],
  "related_registry_items": [
    {
      "id": "III.T24",
      "title": "Hartogs Flow Theorem",
      "url": "/registry/object/III.T24/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/HartogsFlow.lean#L233-L236",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/HartogsFlow.lean#L233-L236",
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
- Source path: [`TauLib/BookIII/Physics/HartogsFlow.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/HartogsFlow.lean#L233-L236)
- Source range: L233-L236
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T24` — Hartogs Flow Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T24] Structural: flow stabilization at depth 1. -/
```

## Source Excerpt

```lean
theorem flow_stable_1 :
    flow_stabilization_check 10 1 = true := by native_decide

end Tau.BookIII.Physics
```
