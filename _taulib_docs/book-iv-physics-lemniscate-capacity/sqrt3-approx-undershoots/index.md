---
{
  "projection_kind": "taulib_declaration",
  "title": "sqrt3_approx_undershoots",
  "permalink": "/verify/taulib/docs/book-iv-physics-lemniscate-capacity/sqrt3-approx-undershoots/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Physics.LemniscateCapacity`.",
  "declaration_id": "TauLib.BookIV.Physics.LemniscateCapacity::sqrt3_approx_undershoots",
  "declaration_slug": "sqrt3-approx-undershoots",
  "kind": "theorem",
  "name": "sqrt3_approx_undershoots",
  "module_name": "TauLib.BookIV.Physics.LemniscateCapacity",
  "module_url": "/verify/taulib/docs/book-iv-physics-lemniscate-capacity/",
  "source_line_start": 163,
  "source_line_end": 164,
  "registry_ids": [
    "IV.P06"
  ],
  "related_registry_items": [
    {
      "id": "IV.P06",
      "title": "√3 Approximation Quality",
      "url": "/registry/object/IV.P06/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/LemniscateCapacity.lean#L163-L164",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Physics.LemniscateCapacity",
        "url": "/verify/taulib/docs/book-iv-physics-lemniscate-capacity/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/LemniscateCapacity.lean#L163-L164",
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

- Module: [TauLib.BookIV.Physics.LemniscateCapacity](/verify/taulib/docs/book-iv-physics-lemniscate-capacity/)
- Source path: [`TauLib/BookIV/Physics/LemniscateCapacity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/LemniscateCapacity.lean#L163-L164)
- Source range: L163-L164
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.P06` — √3 Approximation Quality

## Immediate Comment / Docstring

```lean
/-- [IV.P06] The √3 approximation satisfies (√3_approx)² < 3 (undershoots).
    17320508² < 3 × 10000000². -/
```

## Source Excerpt

```lean
theorem sqrt3_approx_undershoots :
    sqrt3_numer * sqrt3_numer < 3 * sqrt3_denom * sqrt3_denom := by native_decide
```
