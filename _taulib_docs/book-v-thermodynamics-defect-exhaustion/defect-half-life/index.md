---
{
  "projection_kind": "taulib_declaration",
  "title": "DefectHalfLife",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/defect-half-life/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Thermodynamics.DefectExhaustion`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.DefectExhaustion::DefectHalfLife",
  "declaration_slug": "defect-half-life",
  "kind": "structure",
  "name": "DefectHalfLife",
  "module_name": "TauLib.BookV.Thermodynamics.DefectExhaustion",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/",
  "source_line_start": 235,
  "source_line_end": 244,
  "registry_ids": [
    "V.D90"
  ],
  "related_registry_items": [
    {
      "id": "V.D90",
      "title": "Defect half-life",
      "url": "/registry/object/V.D90/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L235-L244",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Thermodynamics.DefectExhaustion",
        "url": "/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L235-L244",
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

- Module: [TauLib.BookV.Thermodynamics.DefectExhaustion](/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/)
- Source path: [`TauLib/BookV/Thermodynamics/DefectExhaustion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L235-L244)
- Source range: L235-L244
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D90` — Defect half-life

## Immediate Comment / Docstring

```lean
/-- [V.D90] Defect half-life: the number of orbit steps for the
    defect count to halve.

    n_{1/2} = ln(2) / (-ln(1 - iota_tau)) ~ 1.66 orbit steps

    Universal: does not depend on defect type, sector, or regime.
    Controlled entirely by the gravitational self-coupling. -/
```

## Source Excerpt

```lean
structure DefectHalfLife where
  /-- Half-life numerator (scaled by 100 for integer arithmetic). -/
  half_life_numer : Nat
  /-- Half-life denominator. -/
  half_life_denom : Nat
  /-- Denominator positive. -/
  denom_pos : half_life_denom > 0
  /-- Whether the half-life is universal (regime-independent). -/
  is_universal : Bool := true
  deriving Repr
```
