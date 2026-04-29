---
{
  "projection_kind": "taulib_declaration",
  "title": "mean_field_scaling",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/mean-field-scaling/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.FluidMacro.PhaseTransitions`.",
  "declaration_id": "TauLib.BookV.FluidMacro.PhaseTransitions::mean_field_scaling",
  "declaration_slug": "mean-field-scaling",
  "kind": "theorem",
  "name": "mean_field_scaling",
  "module_name": "TauLib.BookV.FluidMacro.PhaseTransitions",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/",
  "source_line_start": 362,
  "source_line_end": 374,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L362-L374",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L362-L374",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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
- Source path: [`TauLib/BookV/FluidMacro/PhaseTransitions.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L362-L374)
- Source range: L362-L374
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Mean-field scaling relation: α + 2β + γ = 2.
    Verification for mean-field exponents: 0 + 2(1/2) + 1 = 2. -/
```

## Source Excerpt

```lean
theorem mean_field_scaling :
    mean_field_class.exponents.alpha_n * (mean_field_class.exponents.beta_d : Int) *
      (mean_field_class.exponents.gamma_d : Int) +
    2 * (mean_field_class.exponents.beta_n : Int) *
      (mean_field_class.exponents.alpha_d : Int) *
      (mean_field_class.exponents.gamma_d : Int) +
    (mean_field_class.exponents.gamma_n : Int) *
      (mean_field_class.exponents.alpha_d : Int) *
      (mean_field_class.exponents.beta_d : Int) =
    2 * (mean_field_class.exponents.alpha_d : Int) *
      (mean_field_class.exponents.beta_d : Int) *
      (mean_field_class.exponents.gamma_d : Int) := by
  simp [mean_field_class]
```
