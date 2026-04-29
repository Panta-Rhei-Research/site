---
{
  "projection_kind": "taulib_declaration",
  "title": "d_sq_tower_3_10",
  "permalink": "/verify/taulib/docs/book-ii-closure-tau-manifold/d-sq-tower-3-10/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Closure.TauManifold`.",
  "declaration_id": "TauLib.BookII.Closure.TauManifold::d_sq_tower_3_10",
  "declaration_slug": "d-sq-tower-3-10",
  "kind": "theorem",
  "name": "d_sq_tower_3_10",
  "module_name": "TauLib.BookII.Closure.TauManifold",
  "module_url": "/verify/taulib/docs/book-ii-closure-tau-manifold/",
  "source_line_start": 269,
  "source_line_end": 270,
  "registry_ids": [
    "II.D64"
  ],
  "related_registry_items": [
    {
      "id": "II.D64",
      "title": "Tau-Exterior Derivative",
      "url": "/registry/object/II.D64/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/TauManifold.lean#L269-L270",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/TauManifold.lean#L269-L270",
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

- Module: [TauLib.BookII.Closure.TauManifold](/verify/taulib/docs/book-ii-closure-tau-manifold/)
- Source path: [`TauLib/BookII/Closure/TauManifold.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/TauManifold.lean#L269-L270)
- Source range: L269-L270
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.D64` — Tau-Exterior Derivative

## Immediate Comment / Docstring

```lean
-- d^2 = 0 telescoping [II.D64]
```

## Source Excerpt

```lean
theorem d_sq_tower_3_10 :
    d_squared_zero_tower_check 3 10 = true := by native_decide
```
