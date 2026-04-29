---
{
  "projection_kind": "taulib_declaration",
  "title": "crust_fraction_permille",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/crust-fraction-permille/",
  "summary_short": "`def` declaration in `TauLib.BookV.FluidMacro.PhaseTransitions`.",
  "declaration_id": "TauLib.BookV.FluidMacro.PhaseTransitions::crust_fraction_permille",
  "declaration_slug": "crust-fraction-permille",
  "kind": "def",
  "name": "crust_fraction_permille",
  "module_name": "TauLib.BookV.FluidMacro.PhaseTransitions",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/",
  "source_line_start": 435,
  "source_line_end": 435,
  "registry_ids": [
    "V.P190"
  ],
  "related_registry_items": [
    {
      "id": "V.P190",
      "title": "Crust Fraction from Defect-Tuple Crossing",
      "url": "/registry/object/V.P190/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L435-L435",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.FluidMacro.PhaseTransitions",
        "url": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L435-L435",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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

- Module: [TauLib.BookV.FluidMacro.PhaseTransitions](/verify/taulib/docs/book-v-fluid-macro-phase-transitions/)
- Source path: [`TauLib/BookV/FluidMacro/PhaseTransitions.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L435-L435)
- Source range: L435-L435
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.P190` — Crust Fraction from Defect-Tuple Crossing

## Immediate Comment / Docstring

```lean
/-- [V.P190] Crust fraction from defect-tuple crossing.
    ΔR_crust/R_NS ≈ ι_τ ≈ 0.34 (overshoots observed 0.08–0.17).
    Scope: conjectural. -/
```

## Source Excerpt

```lean
def crust_fraction_permille : Nat := 341
```
