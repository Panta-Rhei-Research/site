---
{
  "projection_kind": "taulib_declaration",
  "title": "bhs_equals_exponent",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-bipolar-holonomy/bhs-equals-exponent/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.BipolarHolonomy`.",
  "declaration_id": "TauLib.BookV.GravityField.BipolarHolonomy::bhs_equals_exponent",
  "declaration_slug": "bhs-equals-exponent",
  "kind": "theorem",
  "name": "bhs_equals_exponent",
  "module_name": "TauLib.BookV.GravityField.BipolarHolonomy",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-bipolar-holonomy/",
  "source_line_start": 121,
  "source_line_end": 122,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/BipolarHolonomy.lean#L121-L122",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/BipolarHolonomy.lean#L121-L122",
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
- Source path: [`TauLib/BookV/GravityField/BipolarHolonomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/BipolarHolonomy.lean#L121-L122)
- Source range: L121-L122
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T85` — Flat Rotation Curve Theorem --- V.T37

## Immediate Comment / Docstring

```lean
/-- [V.T85] The BHS dimension equals the ExponentFactors product.

    dim(BHS) = 18 = ExponentFactors.product

    This bridges the new (cohomological) and old (geometric) formulations.
    The factorizations differ — BHS: 3·3·2, ExponentFactors: 2·3·3 —
    but both yield 18 because they count the same holonomy passages
    from different vantage points. -/
```

## Source Excerpt

```lean
theorem bhs_equals_exponent :
    canonical_bhs.dim = canonical_factors.product := by rfl
```
