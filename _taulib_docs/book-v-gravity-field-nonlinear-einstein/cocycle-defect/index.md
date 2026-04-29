---
{
  "projection_kind": "taulib_declaration",
  "title": "CocycleDefect",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-nonlinear-einstein/cocycle-defect/",
  "summary_short": "`structure` declaration in `TauLib.BookV.GravityField.NonlinearEinstein`.",
  "declaration_id": "TauLib.BookV.GravityField.NonlinearEinstein::CocycleDefect",
  "declaration_slug": "cocycle-defect",
  "kind": "structure",
  "name": "CocycleDefect",
  "module_name": "TauLib.BookV.GravityField.NonlinearEinstein",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-nonlinear-einstein/",
  "source_line_start": 90,
  "source_line_end": 99,
  "registry_ids": [
    "V.D54"
  ],
  "related_registry_items": [
    {
      "id": "V.D54",
      "title": "Cocycle defect",
      "url": "/registry/object/V.D54/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/NonlinearEinstein.lean#L90-L99",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/NonlinearEinstein.lean#L90-L99",
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

- Module: [TauLib.BookV.GravityField.NonlinearEinstein](/verify/taulib/docs/book-v-gravity-field-nonlinear-einstein/)
- Source path: [`TauLib/BookV/GravityField/NonlinearEinstein.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/NonlinearEinstein.lean#L90-L99)
- Source range: L90-L99
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D54` — Cocycle defect

## Immediate Comment / Docstring

```lean
/-- [V.D54] Cocycle defect: deviation of a candidate solution from
    the exact cocycle condition in the Einstein identity.

    At each NF step, the defect decreases. At the fixed point
    S_ω, the cocycle defect is zero.

    defect(S_k) ≥ defect(S_{k+1}) ≥ 0 -/
```

## Source Excerpt

```lean
structure CocycleDefect where
  /-- Defect numerator (scaled). -/
  defect_numer : Nat
  /-- Defect denominator. -/
  defect_denom : Nat
  /-- Denominator positive. -/
  denom_pos : defect_denom > 0
  /-- Iteration step at which this defect was measured. -/
  step : Nat
  deriving Repr
```
