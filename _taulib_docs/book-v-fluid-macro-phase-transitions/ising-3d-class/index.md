---
{
  "projection_kind": "taulib_declaration",
  "title": "ising_3d_class",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/ising-3d-class/",
  "summary_short": "`def` declaration in `TauLib.BookV.FluidMacro.PhaseTransitions`.",
  "declaration_id": "TauLib.BookV.FluidMacro.PhaseTransitions::ising_3d_class",
  "declaration_slug": "ising-3d-class",
  "kind": "def",
  "name": "ising_3d_class",
  "module_name": "TauLib.BookV.FluidMacro.PhaseTransitions",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/",
  "source_line_start": 220,
  "source_line_end": 233,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L220-L233",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L220-L233",
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
- Source path: [`TauLib/BookV/FluidMacro/PhaseTransitions.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L220-L233)
- Source range: L220-L233
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- 3D Ising universality class (d=3, n=1). -/
```

## Source Excerpt

```lean
def ising_3d_class : UniversalityClass where
  spatial_dim := 3
  op_dim := 1
  name := "3D Ising"
  exponents := {
    -- Approximate: α ≈ 0.11, β ≈ 0.326, γ ≈ 1.237, ν ≈ 0.630, η ≈ 0.036, δ ≈ 4.79
    alpha_n := 11, alpha_d := 100, alpha_d_pos := by omega
    beta_n := 326, beta_d := 1000, beta_d_pos := by omega
    gamma_n := 1237, gamma_d := 1000, gamma_d_pos := by omega
    nu_n := 630, nu_d := 1000, nu_d_pos := by omega
    eta_n := 36, eta_d := 1000, eta_d_pos := by omega
    delta_n := 479, delta_d := 100, delta_d_pos := by omega
    dim := 3
  }
```
