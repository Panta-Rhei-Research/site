---
{
  "projection_kind": "taulib_declaration",
  "title": "GeometricContraction",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-inversion/geometric-contraction/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Thermodynamics.Inversion`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.Inversion::GeometricContraction",
  "declaration_slug": "geometric-contraction",
  "kind": "structure",
  "name": "GeometricContraction",
  "module_name": "TauLib.BookV.Thermodynamics.Inversion",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-inversion/",
  "source_line_start": 186,
  "source_line_end": 197,
  "registry_ids": [
    "V.L02"
  ],
  "related_registry_items": [
    {
      "id": "V.L02",
      "title": "Geometric contraction of defect support",
      "url": "/registry/object/V.L02/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/Inversion.lean#L186-L197",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Thermodynamics.Inversion",
        "url": "/verify/taulib/docs/book-v-thermodynamics-inversion/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/Inversion.lean#L186-L197",
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

- Module: [TauLib.BookV.Thermodynamics.Inversion](/verify/taulib/docs/book-v-thermodynamics-inversion/)
- Source path: [`TauLib/BookV/Thermodynamics/Inversion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/Inversion.lean#L186-L197)
- Source range: L186-L197
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.L02` — Geometric contraction of defect support

## Immediate Comment / Docstring

```lean
/-- [V.L02] Geometric contraction of defect support.

    If a_{n+1} <= (1 - iota_tau) * a_n, then:
    (i)  a_n <= (1 - iota_tau)^n * a_0
    (ii) sum_{n>=0} a_n <= a_0 / iota_tau (finite)
    (iii) a_n -> 0

    The contraction factor is the gravitational coupling. -/
```

## Source Excerpt

```lean
structure GeometricContraction where
  /-- Initial defect count a_0. -/
  a_0 : Nat
  /-- The contraction factor numerator (1 - iota_tau). -/
  factor_numer : Nat := contraction_numer
  /-- The contraction factor denominator. -/
  factor_denom : Nat := contraction_denom
  /-- Denominator positive. -/
  denom_pos : factor_denom > 0 := by simp [contraction_denom, iota_tau_denom]
  /-- Factor is strictly contractive. -/
  is_contractive : factor_numer < factor_denom
  deriving Repr
```
