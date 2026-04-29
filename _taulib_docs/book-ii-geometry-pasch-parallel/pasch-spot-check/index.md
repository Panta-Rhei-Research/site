---
{
  "projection_kind": "taulib_declaration",
  "title": "pasch_spot_check",
  "permalink": "/verify/taulib/docs/book-ii-geometry-pasch-parallel/pasch-spot-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Geometry.PaschParallel`.",
  "declaration_id": "TauLib.BookII.Geometry.PaschParallel::pasch_spot_check",
  "declaration_slug": "pasch-spot-check",
  "kind": "def",
  "name": "pasch_spot_check",
  "module_name": "TauLib.BookII.Geometry.PaschParallel",
  "module_url": "/verify/taulib/docs/book-ii-geometry-pasch-parallel/",
  "source_line_start": 58,
  "source_line_end": 62,
  "registry_ids": [
    "II.T17"
  ],
  "related_registry_items": [
    {
      "id": "II.T17",
      "title": "Pasch Axiom",
      "url": "/registry/object/II.T17/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/PaschParallel.lean#L58-L62",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Geometry.PaschParallel",
        "url": "/verify/taulib/docs/book-ii-geometry-pasch-parallel/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/PaschParallel.lean#L58-L62",
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

- Module: [TauLib.BookII.Geometry.PaschParallel](/verify/taulib/docs/book-ii-geometry-pasch-parallel/)
- Source path: [`TauLib/BookII/Geometry/PaschParallel.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/PaschParallel.lean#L58-L62)
- Source range: L58-L62
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T17` — Pasch Axiom

## Immediate Comment / Docstring

```lean
/-- [II.T17] Pasch axiom spot check: verify collinearity for
    representative triangles spanning different tree configurations.
    Since all triples are collinear, Pasch is vacuously true
    (its hypothesis requires a non-collinear triangle). -/
```

## Source Excerpt

```lean
def pasch_spot_check (db : TauIdx) : Bool :=
  collinear_triple 3 5 7 db &&
  collinear_triple 2 9 12 db &&
  collinear_triple 3 7 10 db &&
  collinear_triple 2 4 8 db
```
