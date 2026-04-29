---
{
  "projection_kind": "taulib_declaration",
  "title": "singularity_replaced",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-nonlinear-einstein/singularity-replaced/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.NonlinearEinstein`.",
  "declaration_id": "TauLib.BookV.GravityField.NonlinearEinstein::singularity_replaced",
  "declaration_slug": "singularity-replaced",
  "kind": "theorem",
  "name": "singularity_replaced",
  "module_name": "TauLib.BookV.GravityField.NonlinearEinstein",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-nonlinear-einstein/",
  "source_line_start": 370,
  "source_line_end": 372,
  "registry_ids": [
    "V.P16"
  ],
  "related_registry_items": [
    {
      "id": "V.P16",
      "title": "Saturation replaces singularity",
      "url": "/registry/object/V.P16/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/NonlinearEinstein.lean#L370-L372",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/NonlinearEinstein.lean#L370-L372",
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
- Source path: [`TauLib/BookV/GravityField/NonlinearEinstein.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/NonlinearEinstein.lean#L370-L372)
- Source range: L370-L372
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P16` — Saturation replaces singularity

## Immediate Comment / Docstring

```lean
/-- [V.P16] Singularity replacement by density saturation: at every
    finite depth, density is bounded above by a finite value.
    Orthodox GR singularities are chart artifacts (V.R67). -/
```

## Source Excerpt

```lean
theorem singularity_replaced (d : DensitySaturation) :
    d.depth > 0 ∧ d.max_density_numer > 0 :=
  ⟨d.depth_pos, d.density_positive⟩
```
