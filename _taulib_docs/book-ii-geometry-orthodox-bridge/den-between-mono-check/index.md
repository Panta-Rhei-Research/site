---
{
  "projection_kind": "taulib_declaration",
  "title": "den_between_mono_check",
  "permalink": "/verify/taulib/docs/book-ii-geometry-orthodox-bridge/den-between-mono-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Geometry.OrthodoxBridge`.",
  "declaration_id": "TauLib.BookII.Geometry.OrthodoxBridge::den_between_mono_check",
  "declaration_slug": "den-between-mono-check",
  "kind": "def",
  "name": "den_between_mono_check",
  "module_name": "TauLib.BookII.Geometry.OrthodoxBridge",
  "module_url": "/verify/taulib/docs/book-ii-geometry-orthodox-bridge/",
  "source_line_start": 184,
  "source_line_end": 192,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/OrthodoxBridge.lean#L184-L192",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Geometry.OrthodoxBridge",
        "url": "/verify/taulib/docs/book-ii-geometry-orthodox-bridge/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/OrthodoxBridge.lean#L184-L192",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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

- Module: [TauLib.BookII.Geometry.OrthodoxBridge](/verify/taulib/docs/book-ii-geometry-orthodox-bridge/)
- Source path: [`TauLib/BookII/Geometry/OrthodoxBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/OrthodoxBridge.lean#L184-L192)
- Source range: L184-L192
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Betweenness monotonicity: if B(x,y,z) at full resolution,
    then B(reduce x k, reduce y k, reduce z k) at stage k.
    Approximation preserves the tree structure. -/
```

## Source Excerpt

```lean
def den_between_mono_check (bound db stages : TauIdx) : Bool :=
  go 2 (bound + 1)
where
  go (x fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else
      between_mono_y x bound db stages && go (x + 1) (fuel - 1)
  termination_by fuel
```
