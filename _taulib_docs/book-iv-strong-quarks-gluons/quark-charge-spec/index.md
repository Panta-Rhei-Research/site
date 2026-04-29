---
{
  "projection_kind": "taulib_declaration",
  "title": "QuarkChargeSpec",
  "permalink": "/verify/taulib/docs/book-iv-strong-quarks-gluons/quark-charge-spec/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.QuarksGluons`.",
  "declaration_id": "TauLib.BookIV.Strong.QuarksGluons::QuarkChargeSpec",
  "declaration_slug": "quark-charge-spec",
  "kind": "structure",
  "name": "QuarkChargeSpec",
  "module_name": "TauLib.BookIV.Strong.QuarksGluons",
  "module_url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/",
  "source_line_start": 78,
  "source_line_end": 85,
  "registry_ids": [
    "IV.P113"
  ],
  "related_registry_items": [
    {
      "id": "IV.P113",
      "title": "Quark electric charges",
      "url": "/registry/object/IV.P113/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/QuarksGluons.lean#L78-L85",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Strong.QuarksGluons",
        "url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/QuarksGluons.lean#L78-L85",
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

- Module: [TauLib.BookIV.Strong.QuarksGluons](/verify/taulib/docs/book-iv-strong-quarks-gluons/)
- Source path: [`TauLib/BookIV/Strong/QuarksGluons.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/QuarksGluons.lean#L78-L85)
- Source range: L78-L85
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P113` — Quark electric charges

## Immediate Comment / Docstring

```lean
/-- [IV.P113] Quark electric charges from the ternary structure:
    - d-type (n equiv 1 mod 3): Q = -1/3 e
    - u-type (n equiv 2 mod 3): Q = +2/3 e

    Charges are given as (numerator, denominator) pairs. -/
```

## Source Excerpt

```lean
structure QuarkChargeSpec where
  /-- Quark type. -/
  quark_type : QuarkType
  /-- Charge numerator. -/
  charge_numer : Int
  /-- Charge denominator. -/
  charge_denom : Nat := 3
  deriving Repr
```
