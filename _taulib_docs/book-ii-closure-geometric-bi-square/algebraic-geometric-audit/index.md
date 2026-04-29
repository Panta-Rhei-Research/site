---
{
  "projection_kind": "taulib_declaration",
  "title": "algebraic_geometric_audit",
  "permalink": "/verify/taulib/docs/book-ii-closure-geometric-bi-square/algebraic-geometric-audit/",
  "summary_short": "`def` declaration in `TauLib.BookII.Closure.GeometricBiSquare`.",
  "declaration_id": "TauLib.BookII.Closure.GeometricBiSquare::algebraic_geometric_audit",
  "declaration_slug": "algebraic-geometric-audit",
  "kind": "def",
  "name": "algebraic_geometric_audit",
  "module_name": "TauLib.BookII.Closure.GeometricBiSquare",
  "module_url": "/verify/taulib/docs/book-ii-closure-geometric-bi-square/",
  "source_line_start": 142,
  "source_line_end": 144,
  "registry_ids": [
    "II.R33"
  ],
  "related_registry_items": [
    {
      "id": "II.R33",
      "title": "Algebraic-to-Geometric Audit",
      "url": "/registry/object/II.R33/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/GeometricBiSquare.lean#L142-L144",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Closure.GeometricBiSquare",
        "url": "/verify/taulib/docs/book-ii-closure-geometric-bi-square/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/GeometricBiSquare.lean#L142-L144",
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

- Module: [TauLib.BookII.Closure.GeometricBiSquare](/verify/taulib/docs/book-ii-closure-geometric-bi-square/)
- Source path: [`TauLib/BookII/Closure/GeometricBiSquare.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/GeometricBiSquare.lean#L142-L144)
- Source range: L142-L144
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.R33` — Algebraic-to-Geometric Audit

## Immediate Comment / Docstring

```lean
/-- [II.R33] Algebraic-to-Geometric Audit: record which Book I
    algebraic components have received geometric content in Book II.
    The audit passes when all eight components are earned AND
    the E1 export package is complete. -/
```

## Source Excerpt

```lean
def algebraic_geometric_audit (db bound k_max : TauIdx) : Bool :=
  geometric_bisquare_check db bound &&
  full_export_check db bound k_max
```
