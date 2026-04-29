---
{
  "projection_kind": "taulib_declaration",
  "title": "density_bound",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-nonlinear-einstein/density-bound/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.NonlinearEinstein`.",
  "declaration_id": "TauLib.BookV.GravityField.NonlinearEinstein::density_bound",
  "declaration_slug": "density-bound",
  "kind": "theorem",
  "name": "density_bound",
  "module_name": "TauLib.BookV.GravityField.NonlinearEinstein",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-nonlinear-einstein/",
  "source_line_start": 331,
  "source_line_end": 333,
  "registry_ids": [
    "V.T36"
  ],
  "related_registry_items": [
    {
      "id": "V.T36",
      "title": "Density cap",
      "url": "/registry/object/V.T36/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/NonlinearEinstein.lean#L331-L333",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.NonlinearEinstein",
        "url": "/verify/taulib/docs/book-v-gravity-field-nonlinear-einstein/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/NonlinearEinstein.lean#L331-L333",
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

- Module: [TauLib.BookV.GravityField.NonlinearEinstein](/verify/taulib/docs/book-v-gravity-field-nonlinear-einstein/)
- Source path: [`TauLib/BookV/GravityField/NonlinearEinstein.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/NonlinearEinstein.lean#L331-L333)
- Source range: L331-L333
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T36` — Density cap

## Immediate Comment / Docstring

```lean
/-- [V.T36] Density bound: the saturation density is positive
    and finite at every finite refinement depth.

    This is the τ-native singularity avoidance theorem:
    no infinite density, no geodesic incompleteness. -/
```

## Source Excerpt

```lean
theorem density_bound (d : DensitySaturation) :
    d.max_density_numer > 0 ∧ d.max_density_denom > 0 :=
  ⟨d.density_positive, d.denom_pos⟩
```
