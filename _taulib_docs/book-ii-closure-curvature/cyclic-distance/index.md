---
{
  "projection_kind": "taulib_declaration",
  "title": "cyclic_distance",
  "permalink": "/verify/taulib/docs/book-ii-closure-curvature/cyclic-distance/",
  "summary_short": "`def` declaration in `TauLib.BookII.Closure.Curvature`.",
  "declaration_id": "TauLib.BookII.Closure.Curvature::cyclic_distance",
  "declaration_slug": "cyclic-distance",
  "kind": "def",
  "name": "cyclic_distance",
  "module_name": "TauLib.BookII.Closure.Curvature",
  "module_url": "/verify/taulib/docs/book-ii-closure-curvature/",
  "source_line_start": 79,
  "source_line_end": 83,
  "registry_ids": [
    "II.D81"
  ],
  "related_registry_items": [
    {
      "id": "II.D81",
      "title": "τ-Geodesic",
      "url": "/registry/object/II.D81/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Curvature.lean#L79-L83",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Closure.Curvature",
        "url": "/verify/taulib/docs/book-ii-closure-curvature/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Curvature.lean#L79-L83",
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

- Module: [TauLib.BookII.Closure.Curvature](/verify/taulib/docs/book-ii-closure-curvature/)
- Source path: [`TauLib/BookII/Closure/Curvature.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Curvature.lean#L79-L83)
- Source range: L79-L83
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D81` — τ-Geodesic

## Immediate Comment / Docstring

```lean
/-- [II.D81] Distance in Z/M_k Z: min(|x-y|, M_k - |x-y|). -/
```

## Source Excerpt

```lean
def cyclic_distance (x y k : Nat) : Nat :=
  let pk := primorial k
  let d := if x ≥ y then x - y else y - x
  let d_mod := d % pk
  min d_mod (pk - d_mod)
```
