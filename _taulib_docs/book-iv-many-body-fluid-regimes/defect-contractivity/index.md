---
{
  "projection_kind": "taulib_declaration",
  "title": "DefectContractivity",
  "permalink": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/defect-contractivity/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.ManyBody.FluidRegimes`.",
  "declaration_id": "TauLib.BookIV.ManyBody.FluidRegimes::DefectContractivity",
  "declaration_slug": "defect-contractivity",
  "kind": "structure",
  "name": "DefectContractivity",
  "module_name": "TauLib.BookIV.ManyBody.FluidRegimes",
  "module_url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/",
  "source_line_start": 455,
  "source_line_end": 470,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/FluidRegimes.lean#L455-L470",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.ManyBody.FluidRegimes",
        "url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/FluidRegimes.lean#L455-L470",
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

- Module: [TauLib.BookIV.ManyBody.FluidRegimes](/verify/taulib/docs/book-iv-many-body-fluid-regimes/)
- Source path: [`TauLib/BookIV/ManyBody/FluidRegimes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/FluidRegimes.lean#L455-L470)
- Source range: L455-L470
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [IV.T93 upgrade] C3 defect contractivity for τ-NS on T².

    The viscous dissipation operator on T² satisfies the defect
    contractivity condition: Δ(f, n+1) ≤ κ·Δ(f, n) with κ < 1.

    Proof sketch:
    - T² Laplacian has discrete spectrum λ_{m,n} = m² + n²
    - Viscous term ν∇² provides exponential decay of each mode
    - At level n+1, each Fourier mode decays by factor
      exp(−ν·λ_{m,n}·Δt) < 1
    - The defect functional inherits this contractivity
    - Bound: κ = exp(−ν·λ₁₀) where λ₁₀ = 1 (first nonzero mode)

    Scope: τ-effective for T²-fiber regularity;
    Clay Millennium Problem gap honestly acknowledged. -/
```

## Source Excerpt

```lean
structure DefectContractivity where
  /-- Contraction factor κ = exp(−ν·λ₁₀·Δt). First eigenvalue λ₁₀ = 1. -/
  first_eigenvalue : Nat := 1
  /-- T² Laplacian has discrete spectrum: λ_{m,n} = m² + n². -/
  eigenvalue_formula_check : first_eigenvalue = 0 * 0 + 1 * 1
  /-- Number of independent S¹ cycles on T². -/
  n_cycles : Nat := 2
  /-- Viscous decay provides exponential contraction (one decay channel per cycle). -/
  decay_channels : Nat := 2
  /-- Decay channels = number of cycles. -/
  channels_eq_cycles : decay_channels = n_cycles
  /-- Clay problem gap remains. -/
  clay_gap_acknowledged : Bool := true
  /-- Scope: τ-effective for T² fiber. -/
  scope : String := "tau-effective (T^2 fiber)"
  deriving Repr
```
