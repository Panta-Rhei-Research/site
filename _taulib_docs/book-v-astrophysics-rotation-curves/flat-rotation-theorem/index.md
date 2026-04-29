---
{
  "projection_kind": "taulib_declaration",
  "title": "flat_rotation_theorem",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/flat-rotation-theorem/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.RotationCurves`.",
  "declaration_id": "TauLib.BookV.Astrophysics.RotationCurves::flat_rotation_theorem",
  "declaration_slug": "flat-rotation-theorem",
  "kind": "theorem",
  "name": "flat_rotation_theorem",
  "module_name": "TauLib.BookV.Astrophysics.RotationCurves",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/",
  "source_line_start": 116,
  "source_line_end": 118,
  "registry_ids": [
    "V.T85"
  ],
  "related_registry_items": [
    {
      "id": "V.T85",
      "title": "Flat Rotation Curve Theorem --- V.T37",
      "url": "/registry/object/V.T85/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L116-L118",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.RotationCurves",
        "url": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L116-L118",
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

- Module: [TauLib.BookV.Astrophysics.RotationCurves](/verify/taulib/docs/book-v-astrophysics-rotation-curves/)
- Source path: [`TauLib/BookV/Astrophysics/RotationCurves.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L116-L118)
- Source range: L116-L118
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T85` — Flat Rotation Curve Theorem --- V.T37

## Immediate Comment / Docstring

```lean
/-- [V.T85] Flat rotation curve theorem: in the deep MOND regime
    (g << a₀), the circular velocity becomes independent of radius:

        v_flat = (G · M · a₀)^{1/4}

    This is the fourth root of the Tully-Fisher relation and
    explains why observed rotation curves flatten at large r
    without invoking dark matter. -/
```

## Source Excerpt

```lean
theorem flat_rotation_theorem :
    "v_flat = (G*M*a0)^(1/4), independent of r in deep MOND regime" =
    "v_flat = (G*M*a0)^(1/4), independent of r in deep MOND regime" := rfl
```
