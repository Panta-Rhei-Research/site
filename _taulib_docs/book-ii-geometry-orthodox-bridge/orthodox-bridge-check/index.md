---
{
  "projection_kind": "taulib_declaration",
  "title": "orthodox_bridge_check",
  "permalink": "/verify/taulib/docs/book-ii-geometry-orthodox-bridge/orthodox-bridge-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Geometry.OrthodoxBridge`.",
  "declaration_id": "TauLib.BookII.Geometry.OrthodoxBridge::orthodox_bridge_check",
  "declaration_slug": "orthodox-bridge-check",
  "kind": "def",
  "name": "orthodox_bridge_check",
  "module_name": "TauLib.BookII.Geometry.OrthodoxBridge",
  "module_url": "/verify/taulib/docs/book-ii-geometry-orthodox-bridge/",
  "source_line_start": 229,
  "source_line_end": 232,
  "registry_ids": [
    "II.R07"
  ],
  "related_registry_items": [
    {
      "id": "II.R07",
      "title": "Orthodox Denotation Bridge",
      "url": "/registry/object/II.R07/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/OrthodoxBridge.lean#L229-L232",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/OrthodoxBridge.lean#L229-L232",
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
- Source path: [`TauLib/BookII/Geometry/OrthodoxBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/OrthodoxBridge.lean#L229-L232)
- Source range: L229-L232
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.R07` — Orthodox Denotation Bridge

## Immediate Comment / Docstring

```lean
/-- [II.R07] Orthodox denotation bridge: the full compatibility check.
    The earned denotation (ABCD chart) is compatible with the orthodox
    Tarski geometry (betweenness + congruence + Pasch). -/
```

## Source Excerpt

```lean
def orthodox_bridge_check (bound db stages : TauIdx) : Bool :=
  den_cauchy_check bound stages &&
  den_injective_check bound stages &&
  den_between_mono_check bound db stages
```
