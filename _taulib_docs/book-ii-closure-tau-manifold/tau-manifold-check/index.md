---
{
  "projection_kind": "taulib_declaration",
  "title": "tau_manifold_check",
  "permalink": "/verify/taulib/docs/book-ii-closure-tau-manifold/tau-manifold-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Closure.TauManifold`.",
  "declaration_id": "TauLib.BookII.Closure.TauManifold::tau_manifold_check",
  "declaration_slug": "tau-manifold-check",
  "kind": "def",
  "name": "tau_manifold_check",
  "module_name": "TauLib.BookII.Closure.TauManifold",
  "module_url": "/verify/taulib/docs/book-ii-closure-tau-manifold/",
  "source_line_start": 196,
  "source_line_end": 198,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/TauManifold.lean#L196-L198",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/TauManifold.lean#L196-L198",
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
- Source path: [`TauLib/BookII/Closure/TauManifold.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/TauManifold.lean#L196-L198)
- Source range: L196-L198
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D62` — Tau-Manifold

## Immediate Comment / Docstring

```lean
/-- [II.D62] Full tau-manifold check: atlas + transitions + d^2 = 0. -/
```

## Source Excerpt

```lean
def tau_manifold_check (db bound : TauIdx) : Bool :=
  let m := compute_tau_manifold db bound
  m.has_atlas && m.has_transitions && m.has_d_squared_zero
```
