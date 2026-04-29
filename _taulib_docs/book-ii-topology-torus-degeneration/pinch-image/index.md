---
{
  "projection_kind": "taulib_declaration",
  "title": "PinchImage",
  "permalink": "/verify/taulib/docs/book-ii-topology-torus-degeneration/pinch-image/",
  "summary_short": "`inductive` declaration in `TauLib.BookII.Topology.TorusDegeneration`.",
  "declaration_id": "TauLib.BookII.Topology.TorusDegeneration::PinchImage",
  "declaration_slug": "pinch-image",
  "kind": "inductive",
  "name": "PinchImage",
  "module_name": "TauLib.BookII.Topology.TorusDegeneration",
  "module_url": "/verify/taulib/docs/book-ii-topology-torus-degeneration/",
  "source_line_start": 39,
  "source_line_end": 43,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/TorusDegeneration.lean#L39-L43",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Topology.TorusDegeneration",
        "url": "/verify/taulib/docs/book-ii-topology-torus-degeneration/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/TorusDegeneration.lean#L39-L43",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
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

- Module: [TauLib.BookII.Topology.TorusDegeneration](/verify/taulib/docs/book-ii-topology-torus-degeneration/)
- Source path: [`TauLib/BookII/Topology/TorusDegeneration.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/TorusDegeneration.lean#L39-L43)
- Source range: L39-L43
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Fiber classification under the pinch map.
    At finite depth, (B,C) lives in T² = ℤ × ℤ.
    The pinch map collapses the diagonal (B = C) to the wedge point. -/
```

## Source Excerpt

```lean
inductive PinchImage where
  | plus_lobe : Int → PinchImage    -- B > C: e₊-lobe
  | minus_lobe : Int → PinchImage   -- C > B: e₋-lobe
  | wedge : PinchImage              -- B = C: crossing point
  deriving Repr, DecidableEq
```
