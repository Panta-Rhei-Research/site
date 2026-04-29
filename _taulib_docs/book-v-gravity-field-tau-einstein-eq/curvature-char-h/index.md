---
{
  "projection_kind": "taulib_declaration",
  "title": "CurvatureCharH",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-tau-einstein-eq/curvature-char-h/",
  "summary_short": "`structure` declaration in `TauLib.BookV.GravityField.TauEinsteinEq`.",
  "declaration_id": "TauLib.BookV.GravityField.TauEinsteinEq::CurvatureCharH",
  "declaration_slug": "curvature-char-h",
  "kind": "structure",
  "name": "CurvatureCharH",
  "module_name": "TauLib.BookV.GravityField.TauEinsteinEq",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-tau-einstein-eq/",
  "source_line_start": 82,
  "source_line_end": 97,
  "registry_ids": [
    "V.D49"
  ],
  "related_registry_items": [
    {
      "id": "V.D49",
      "title": "Curvature character --- V.D04",
      "url": "/registry/object/V.D49/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauEinsteinEq.lean#L82-L97",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.TauEinsteinEq",
        "url": "/verify/taulib/docs/book-v-gravity-field-tau-einstein-eq/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauEinsteinEq.lean#L82-L97",
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

- Module: [TauLib.BookV.GravityField.TauEinsteinEq](/verify/taulib/docs/book-v-gravity-field-tau-einstein-eq/)
- Source path: [`TauLib/BookV/GravityField/TauEinsteinEq.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauEinsteinEq.lean#L82-L97)
- Source range: L82-L97
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D49` — Curvature character --- V.D04

## Immediate Comment / Docstring

```lean
/-- [V.D49] Curvature character R^H: the D-sector boundary projection
    of the holonomy at depth n.

    R^H_n(x) lives in H_∂[n] (boundary holonomy algebra), NOT in a
    tensor bundle. It measures how much parallel transport around
    a D-sector loop deviates from the identity.

    Components:
    - frame_defect: deviation from flat transport (holonomy excess)
    - depth: refinement level at which curvature is measured
    - sector: always D (gravity) -/
```

## Source Excerpt

```lean
structure CurvatureCharH where
  /-- Frame holonomy defect numerator. -/
  defect_numer : Nat
  /-- Frame holonomy defect denominator. -/
  defect_denom : Nat
  /-- Denominator positive. -/
  denom_pos : defect_denom > 0
  /-- Refinement depth. -/
  depth : Nat
  /-- Depth positive. -/
  depth_pos : depth > 0
  /-- The sector (always D = gravity). -/
  sector : Sector := .D
  /-- Curvature is D-sector. -/
  sector_is_d : sector = .D := by rfl
  deriving Repr
```
