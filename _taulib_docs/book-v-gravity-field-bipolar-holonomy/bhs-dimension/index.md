---
{
  "projection_kind": "taulib_declaration",
  "title": "bhs_dimension",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-bipolar-holonomy/bhs-dimension/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.BipolarHolonomy`.",
  "declaration_id": "TauLib.BookV.GravityField.BipolarHolonomy::bhs_dimension",
  "declaration_slug": "bhs-dimension",
  "kind": "theorem",
  "name": "bhs_dimension",
  "module_name": "TauLib.BookV.GravityField.BipolarHolonomy",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-bipolar-holonomy/",
  "source_line_start": 87,
  "source_line_end": 87,
  "registry_ids": [
    "V.T84"
  ],
  "related_registry_items": [
    {
      "id": "V.T84",
      "title": "Kepler's Third Law --- V.T36",
      "url": "/registry/object/V.T84/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/BipolarHolonomy.lean#L87-L87",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.BipolarHolonomy",
        "url": "/verify/taulib/docs/book-v-gravity-field-bipolar-holonomy/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/BipolarHolonomy.lean#L87-L87",
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

- Module: [TauLib.BookV.GravityField.BipolarHolonomy](/verify/taulib/docs/book-v-gravity-field-bipolar-holonomy/)
- Source path: [`TauLib/BookV/GravityField/BipolarHolonomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/BipolarHolonomy.lean#L87-L87)
- Source range: L87-L87
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T84` — Kepler's Third Law --- V.T36

## Immediate Comment / Docstring

```lean
/-- [V.T84] The dimension of the Bipolar Holonomy Space is 18.

    dim(BHS) = b₁(τ³) · b¹(τ³) · b₁(L) = 3 · 3 · 2 = 18

    This is THE key theorem: the exponent 18 is the dimension of a
    single tensor product space, not three ad hoc factors multiplied. -/
```

## Source Excerpt

```lean
theorem bhs_dimension : canonical_bhs.dim = 18 := by rfl
```
