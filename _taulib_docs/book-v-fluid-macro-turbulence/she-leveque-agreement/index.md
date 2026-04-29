---
{
  "projection_kind": "taulib_declaration",
  "title": "SheLevequeAgreement",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-turbulence/she-leveque-agreement/",
  "summary_short": "`structure` declaration in `TauLib.BookV.FluidMacro.Turbulence`.",
  "declaration_id": "TauLib.BookV.FluidMacro.Turbulence::SheLevequeAgreement",
  "declaration_slug": "she-leveque-agreement",
  "kind": "structure",
  "name": "SheLevequeAgreement",
  "module_name": "TauLib.BookV.FluidMacro.Turbulence",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-turbulence/",
  "source_line_start": 339,
  "source_line_end": 352,
  "registry_ids": [
    "V.T249"
  ],
  "related_registry_items": [
    {
      "id": "V.T249",
      "title": "Intermittency Exponent Agreement",
      "url": "/registry/object/V.T249/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/Turbulence.lean#L339-L352",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.FluidMacro.Turbulence",
        "url": "/verify/taulib/docs/book-v-fluid-macro-turbulence/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/Turbulence.lean#L339-L352",
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

- Module: [TauLib.BookV.FluidMacro.Turbulence](/verify/taulib/docs/book-v-fluid-macro-turbulence/)
- Source path: [`TauLib/BookV/FluidMacro/Turbulence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/Turbulence.lean#L339-L352)
- Source range: L339-L352
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T249` — Intermittency Exponent Agreement

## Immediate Comment / Docstring

```lean
/-- [V.T249] She-Leveque exponent agreement with experiment.

    Verification at p=2,4,6,8:
    | p | ζ_p (S-L) | ζ_p (expt) | Error  |
    |---|-----------|------------|--------|
    | 2 | 0.696     | 0.70±0.01  | −0.6%  |
    | 4 | 1.280     | 1.28±0.02  |  0.0%  |
    | 6 | 1.778     | 1.77±0.04  | +0.5%  |
    | 8 | 2.211     | 2.21±0.07  |  0.0%  |

    All within experimental error for p ≤ 12. -/
```

## Source Excerpt

```lean
structure SheLevequeAgreement where
  /-- ζ₂ × 1000 (S-L prediction). -/
  zeta2_x1000 : Nat := 696
  /-- ζ₄ × 1000. -/
  zeta4_x1000 : Nat := 1280
  /-- ζ₆ × 1000. -/
  zeta6_x1000 : Nat := 1778
  /-- ζ₈ × 1000. -/
  zeta8_x1000 : Nat := 2211
  /-- Maximum relative error × 10000 (for p ≤ 12). -/
  max_error_x10000 : Nat := 100
  /-- Error < 1% for p ≤ 12. -/
  sub_percent : max_error_x10000 ≤ 100 := by omega
  deriving Repr
```
