---
{
  "projection_kind": "taulib_declaration",
  "title": "TauManifoldData",
  "permalink": "/verify/taulib/docs/book-ii-closure-tau-manifold/tau-manifold-data/",
  "summary_short": "`structure` declaration in `TauLib.BookII.Closure.TauManifold`.",
  "declaration_id": "TauLib.BookII.Closure.TauManifold::TauManifoldData",
  "declaration_slug": "tau-manifold-data",
  "kind": "structure",
  "name": "TauManifoldData",
  "module_name": "TauLib.BookII.Closure.TauManifold",
  "module_url": "/verify/taulib/docs/book-ii-closure-tau-manifold/",
  "source_line_start": 178,
  "source_line_end": 182,
  "registry_ids": [
    "II.D62"
  ],
  "related_registry_items": [
    {
      "id": "II.D62",
      "title": "Tau-Manifold",
      "url": "/registry/object/II.D62/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/TauManifold.lean#L178-L182",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Closure.TauManifold",
        "url": "/verify/taulib/docs/book-ii-closure-tau-manifold/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/TauManifold.lean#L178-L182",
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

- Module: [TauLib.BookII.Closure.TauManifold](/verify/taulib/docs/book-ii-closure-tau-manifold/)
- Source path: [`TauLib/BookII/Closure/TauManifold.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/TauManifold.lean#L178-L182)
- Source range: L178-L182
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `II.D62` — Tau-Manifold

## Immediate Comment / Docstring

```lean
/-- [II.D62] tau-Manifold data: a primorial tower with atlas verification
    results and exterior derivative properties. -/
```

## Source Excerpt

```lean
structure TauManifoldData where
  has_atlas : Bool
  has_transitions : Bool
  has_d_squared_zero : Bool
  deriving Repr, DecidableEq
```
