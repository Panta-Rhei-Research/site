---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L332",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-tovstar-builder/eval-l332/",
  "summary_short": "`eval` declaration in `TauLib.BookV.GravityField.TOVStarBuilder`.",
  "declaration_id": "TauLib.BookV.GravityField.TOVStarBuilder::#eval:332",
  "declaration_slug": "eval-l332",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.BookV.GravityField.TOVStarBuilder",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-tovstar-builder/",
  "source_line_start": 332,
  "source_line_end": 332,
  "registry_ids": [
    "V.R89",
    "V.R90",
    "V.R91",
    "V.R92",
    "V.R93"
  ],
  "related_registry_items": [
    {
      "id": "V.R89",
      "title": "Spherical neq static",
      "url": "/registry/object/V.R89/"
    },
    {
      "id": "V.R90",
      "title": "The star builder as constructive proof",
      "url": "/registry/object/V.R90/"
    },
    {
      "id": "V.R91",
      "title": "Not an ODE",
      "url": "/registry/object/V.R91/"
    },
    {
      "id": "V.R92",
      "title": "No free parameter",
      "url": "/registry/object/V.R92/"
    },
    {
      "id": "V.R93",
      "title": "The TOV maximum mass",
      "url": "/registry/object/V.R93/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVStarBuilder.lean#L332-L332",
  "formal_status": "computed",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.TOVStarBuilder",
        "url": "/verify/taulib/docs/book-v-gravity-field-tovstar-builder/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVStarBuilder.lean#L332-L332",
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

- Module: [TauLib.BookV.GravityField.TOVStarBuilder](/verify/taulib/docs/book-v-gravity-field-tovstar-builder/)
- Source path: [`TauLib/BookV/GravityField/TOVStarBuilder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVStarBuilder.lean#L332-L332)
- Source range: L332-L332
- Kind: `eval`
- Formal status hint: `computed`

## Registry Links

- `V.R89` — Spherical neq static
- `V.R90` — The star builder as constructive proof
- `V.R91` — Not an ODE
- `V.R92` — No free parameter
- `V.R93` — The TOV maximum mass

## Immediate Comment / Docstring

```lean
-- ============================================================
-- REMARKS (comment-only)
-- ============================================================

-- [V.R89] Non-Staticity: real stars are never perfectly static;
-- the TOV model is the equilibrium limit of slow evolution.
-- [V.R90] Constructive Existence: the star builder is constructive,
-- not just an existence proof -- it produces an explicit model.
-- [V.R91] Algebraic Identity: TOV is a tau-algebraic identity, not a PDE.
-- [V.R92] Chandrasekhar Not Free: M_Ch is derived from iota_tau, not input.
-- [V.R93] Strong Support above M_Ch: strong sector coupling provides
-- additional support beyond electron degeneracy pressure.

-- ============================================================
-- SMOKE TESTS
-- ============================================================
```

## Source Excerpt

```lean
#eval chandrasekhar_canonical.toFloat
```
