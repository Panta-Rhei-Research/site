---
{
  "projection_kind": "taulib_declaration",
  "title": "GRCoupling",
  "permalink": "/verify/taulib/docs/book-v-gravity-einstein-equation/grcoupling/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Gravity.EinsteinEquation`.",
  "declaration_id": "TauLib.BookV.Gravity.EinsteinEquation::GRCoupling",
  "declaration_slug": "grcoupling",
  "kind": "structure",
  "name": "GRCoupling",
  "module_name": "TauLib.BookV.Gravity.EinsteinEquation",
  "module_url": "/verify/taulib/docs/book-v-gravity-einstein-equation/",
  "source_line_start": 147,
  "source_line_end": 158,
  "registry_ids": [
    "V.D05"
  ],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/EinsteinEquation.lean#L147-L158",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Gravity.EinsteinEquation",
        "url": "/verify/taulib/docs/book-v-gravity-einstein-equation/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/EinsteinEquation.lean#L147-L158",
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

- Module: [TauLib.BookV.Gravity.EinsteinEquation](/verify/taulib/docs/book-v-gravity-einstein-equation/)
- Source path: [`TauLib/BookV/Gravity/EinsteinEquation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/EinsteinEquation.lean#L147-L158)
- Source range: L147-L158
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [V.D05] GR coupling κ_τ: the unique unpolarized coupling constant
    in the tau-Einstein equation.

    Properties:
    - σ-fixed (unpolarized, crossing-point mediator)
    - Unique by field cancellation at canonical carrier x*
    - Determined entirely by ι_τ (No Knobs)

    The gravity sector self-coupling κ(D;1) = 1 − ι_τ is the
    sector-level expression. The Einstein coupling κ_τ relates
    curvature to total matter character. -/
```

## Source Excerpt

```lean
structure GRCoupling where
  /-- κ_τ numerator. -/
  kappa_numer : Nat
  /-- κ_τ denominator. -/
  kappa_denom : Nat
  /-- Denominator positive. -/
  denom_pos : kappa_denom > 0
  /-- κ_τ is σ-fixed (unpolarized). -/
  sigma_fixed : Bool := true
  /-- κ_τ is unique (no other coupling satisfies the universal property). -/
  is_unique : Bool := true
  deriving Repr
```
