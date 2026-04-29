---
{
  "projection_kind": "taulib_declaration",
  "title": "manifold_tower_coherence",
  "permalink": "/verify/taulib/docs/book-ii-closure-tau-manifold/manifold-tower-coherence/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Closure.TauManifold`.",
  "declaration_id": "TauLib.BookII.Closure.TauManifold::manifold_tower_coherence",
  "declaration_slug": "manifold-tower-coherence",
  "kind": "theorem",
  "name": "manifold_tower_coherence",
  "module_name": "TauLib.BookII.Closure.TauManifold",
  "module_url": "/verify/taulib/docs/book-ii-closure-tau-manifold/",
  "source_line_start": 322,
  "source_line_end": 326,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/TauManifold.lean#L322-L326",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/TauManifold.lean#L322-L326",
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
- Source path: [`TauLib/BookII/Closure/TauManifold.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/TauManifold.lean#L322-L326)
- Source range: L322-L326
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.P15` — Tau3 Is a Tau-Manifold

## Immediate Comment / Docstring

```lean
/-- [II.P15] tau^3 manifold: tower coherence gives chart transitions.
    reduce(reduce(x, l), k) = reduce(x, k) for k <= l. -/
```

## Source Excerpt

```lean
theorem manifold_tower_coherence (x : TauIdx) {k l : TauIdx} (h : k ≤ l) :
    reduce (reduce x l) k = reduce x k :=
  reduction_compat x h

end Tau.BookII.Closure
```
