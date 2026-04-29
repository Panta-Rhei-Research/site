---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L350",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/eval-l350/",
  "summary_short": "`eval` declaration in `TauLib.BookV.GravityField.FrameHolonomy`.",
  "declaration_id": "TauLib.BookV.GravityField.FrameHolonomy::#eval:350",
  "declaration_slug": "eval-l350",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.BookV.GravityField.FrameHolonomy",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/",
  "source_line_start": 350,
  "source_line_end": 350,
  "registry_ids": [
    "V.R56"
  ],
  "related_registry_items": [
    {
      "id": "V.R56",
      "title": "Lean formalization",
      "url": "/registry/object/V.R56/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/FrameHolonomy.lean#L350-L350",
  "formal_status": "computed",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.FrameHolonomy",
        "url": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/FrameHolonomy.lean#L350-L350",
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

- Module: [TauLib.BookV.GravityField.FrameHolonomy](/verify/taulib/docs/book-v-gravity-field-frame-holonomy/)
- Source path: [`TauLib/BookV/GravityField/FrameHolonomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/FrameHolonomy.lean#L350-L350)
- Source range: L350-L350
- Kind: `eval`
- Formal status hint: `computed`

## Registry Links

- `V.R56` — Lean formalization

## Immediate Comment / Docstring

```lean
-- ============================================================
-- [V.R56] LEAN FORMALIZATION
-- ============================================================

-- [V.R56] This module formalizes frame holonomy structures and
-- gravitational coupling κ_τ = 1 − ι_τ from Book V ch11.
-- All definitions zero-sorry. Temporal complement proved by simp.

-- ============================================================
-- SMOKE TESTS
-- ============================================================
```

## Source Excerpt

```lean
#eval canonical_grav_coupling.toFloat  -- ≈ 0.658541
```
