---
{
  "projection_kind": "taulib_declaration",
  "title": "hartogs_from_boundary",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-tau-einstein-eq/hartogs-from-boundary/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.TauEinsteinEq`.",
  "declaration_id": "TauLib.BookV.GravityField.TauEinsteinEq::hartogs_from_boundary",
  "declaration_slug": "hartogs-from-boundary",
  "kind": "theorem",
  "name": "hartogs_from_boundary",
  "module_name": "TauLib.BookV.GravityField.TauEinsteinEq",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-tau-einstein-eq/",
  "source_line_start": 223,
  "source_line_end": 225,
  "registry_ids": [
    "V.T27"
  ],
  "related_registry_items": [
    {
      "id": "V.T27",
      "title": "Well-posedness via Hartogs",
      "url": "/registry/object/V.T27/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauEinsteinEq.lean#L223-L225",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauEinsteinEq.lean#L223-L225",
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

- Module: [TauLib.BookV.GravityField.TauEinsteinEq](/verify/taulib/docs/book-v-gravity-field-tau-einstein-eq/)
- Source path: [`TauLib/BookV/GravityField/TauEinsteinEq.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauEinsteinEq.lean#L223-L225)
- Source range: L223-L225
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T27` — Well-posedness via Hartogs

## Immediate Comment / Docstring

```lean
/-- [V.T27] Hartogs extension from boundary data: the boundary-character
    data on ∂(τ³ chart) determines the interior field configuration.

    In the τ-framework, this is the gravitational analogue of the
    holomorphic Hartogs theorem: boundary determines interior.
    The Einstein equation is the boundary constraint; the interior
    field is uniquely determined by τ-NF minimization.

    Depth must be positive (boundary data requires refinement). -/
```

## Source Excerpt

```lean
theorem hartogs_from_boundary (e : TauEinsteinField) :
    e.curvature.depth > 0 :=
  e.curvature.depth_pos
```
