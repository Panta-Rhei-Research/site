---
{
  "projection_kind": "taulib_declaration",
  "title": "tau3_is_manifold_check",
  "permalink": "/verify/taulib/docs/book-ii-closure-tau-manifold/tau3-is-manifold-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Closure.TauManifold`.",
  "declaration_id": "TauLib.BookII.Closure.TauManifold::tau3_is_manifold_check",
  "declaration_slug": "tau3-is-manifold-check",
  "kind": "def",
  "name": "tau3_is_manifold_check",
  "module_name": "TauLib.BookII.Closure.TauManifold",
  "module_url": "/verify/taulib/docs/book-ii-closure-tau-manifold/",
  "source_line_start": 207,
  "source_line_end": 213,
  "registry_ids": [
    "II.P15"
  ],
  "related_registry_items": [
    {
      "id": "II.P15",
      "title": "Tau3 Is a Tau-Manifold",
      "url": "/registry/object/II.P15/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/TauManifold.lean#L207-L213",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/TauManifold.lean#L207-L213",
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

- Module: [TauLib.BookII.Closure.TauManifold](/verify/taulib/docs/book-ii-closure-tau-manifold/)
- Source path: [`TauLib/BookII/Closure/TauManifold.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/TauManifold.lean#L207-L213)
- Source range: L207-L213
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.P15` — Tau3 Is a Tau-Manifold

## Immediate Comment / Docstring

```lean
/-- [II.P15] tau^3 is a tau-manifold check: combines atlas existence,
    chart reduce-compatibility, exterior derivative well-definedness,
    and the ABCD round-trip from categoricity. -/
```

## Source Excerpt

```lean
def tau3_is_manifold_check (db bound : TauIdx) : Bool :=
  atlas_chart_check db &&
  atlas_transition_check db bound &&
  d_squared_zero_const_check db bound &&
  d_tau_const_is_zero_check db bound &&
  d_squared_zero_tower_check db bound &&
  categoricity_check db bound
```
