---
{
  "projection_kind": "taulib_declaration",
  "title": "between_mono_z",
  "permalink": "/verify/taulib/docs/book-ii-geometry-orthodox-bridge/between-mono-z/",
  "summary_short": "`def` declaration in `TauLib.BookII.Geometry.OrthodoxBridge`.",
  "declaration_id": "TauLib.BookII.Geometry.OrthodoxBridge::between_mono_z",
  "declaration_slug": "between-mono-z",
  "kind": "def",
  "name": "between_mono_z",
  "module_name": "TauLib.BookII.Geometry.OrthodoxBridge",
  "module_url": "/verify/taulib/docs/book-ii-geometry-orthodox-bridge/",
  "source_line_start": 158,
  "source_line_end": 168,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/OrthodoxBridge.lean#L158-L168",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/OrthodoxBridge.lean#L158-L168",
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
- Source path: [`TauLib/BookII/Geometry/OrthodoxBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/OrthodoxBridge.lean#L158-L168)
- Source range: L158-L168
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Inner loop: iterate over z for fixed x, y. -/
```

## Source Excerpt

```lean
def between_mono_z (x y bound db stages : TauIdx) : Bool :=
  go 2 (bound + 1)
where
  go (z fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if z > bound then true
    else if !between x y z db then
      go (z + 1) (fuel - 1)
    else
      between_mono_stages x y z db stages && go (z + 1) (fuel - 1)
  termination_by fuel
```
