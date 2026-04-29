---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L313",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-linear-einstein/eval-l313/",
  "summary_short": "`eval` declaration in `TauLib.BookV.GravityField.LinearEinstein`.",
  "declaration_id": "TauLib.BookV.GravityField.LinearEinstein::#eval:313",
  "declaration_slug": "eval-l313",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.BookV.GravityField.LinearEinstein",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-linear-einstein/",
  "source_line_start": 313,
  "source_line_end": 313,
  "registry_ids": [
    "V.R70",
    "V.R71"
  ],
  "related_registry_items": [
    {
      "id": "V.R70",
      "title": "No fitting",
      "url": "/registry/object/V.R70/"
    },
    {
      "id": "V.R71",
      "title": "Two polarizations from two fiber directions",
      "url": "/registry/object/V.R71/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/LinearEinstein.lean#L313-L313",
  "formal_status": "computed",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.LinearEinstein",
        "url": "/verify/taulib/docs/book-v-gravity-field-linear-einstein/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/LinearEinstein.lean#L313-L313",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "eval",
      "status": "computed"
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

- Module: [TauLib.BookV.GravityField.LinearEinstein](/verify/taulib/docs/book-v-gravity-field-linear-einstein/)
- Source path: [`TauLib/BookV/GravityField/LinearEinstein.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/LinearEinstein.lean#L313-L313)
- Source range: L313-L313
- Kind: `eval`
- Formal status hint: `computed`

## Registry Links

- `V.R70` — No fitting
- `V.R71` — Two polarizations from two fiber directions

## Immediate Comment / Docstring

```lean
-- ============================================================
-- [V.R70] NO FREE PARAMETERS IN PRECESSION
-- ============================================================

-- [V.R70] The Mercury precession prediction (43"/century) involves
-- NO free parameters. The coupling κ_τ = 1 − ι_τ is determined by
-- the master constant; the precession follows from the first
-- post-Newtonian correction. Same as GR: different derivation.

-- ============================================================
-- [V.R71] TWO POLARIZATIONS FROM T²
-- ============================================================

-- [V.R71] The two GW polarization modes (plus and cross) correspond
-- to the two independent vibrational modes of the fiber T²:
-- toroidal (plus) and poloidal (cross). This explains why gravity
-- is spin-2: the metric perturbation h_μν has 2 independent
-- transverse-traceless degrees of freedom from T².

-- ============================================================
-- SMOKE TESTS
-- ============================================================
```

## Source Excerpt

```lean
#eval first_order_einstein.order       -- 1
```
