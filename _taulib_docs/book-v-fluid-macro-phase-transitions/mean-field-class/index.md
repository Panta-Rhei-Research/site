---
{
  "projection_kind": "taulib_declaration",
  "title": "mean_field_class",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/mean-field-class/",
  "summary_short": "`def` declaration in `TauLib.BookV.FluidMacro.PhaseTransitions`.",
  "declaration_id": "TauLib.BookV.FluidMacro.PhaseTransitions::mean_field_class",
  "declaration_slug": "mean-field-class",
  "kind": "def",
  "name": "mean_field_class",
  "module_name": "TauLib.BookV.FluidMacro.PhaseTransitions",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/",
  "source_line_start": 205,
  "source_line_end": 217,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L205-L217",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L205-L217",
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
- Source path: [`TauLib/BookV/FluidMacro/PhaseTransitions.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L205-L217)
- Source range: L205-L217
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Mean-field universality class (d ≥ 4 or infinite-range). -/
```

## Source Excerpt

```lean
def mean_field_class : UniversalityClass where
  spatial_dim := 4
  op_dim := 1
  name := "Mean Field"
  exponents := {
    alpha_n := 0, alpha_d := 1, alpha_d_pos := by omega
    beta_n := 1, beta_d := 2, beta_d_pos := by omega
    gamma_n := 1, gamma_d := 1, gamma_d_pos := by omega
    nu_n := 1, nu_d := 2, nu_d_pos := by omega
    eta_n := 0, eta_d := 1, eta_d_pos := by omega
    delta_n := 3, delta_d := 1, delta_d_pos := by omega
    dim := 4
  }
```
