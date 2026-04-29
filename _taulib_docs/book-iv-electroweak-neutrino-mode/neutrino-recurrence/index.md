---
{
  "projection_kind": "taulib_declaration",
  "title": "NeutrinoRecurrence",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/neutrino-recurrence/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.NeutrinoMode`.",
  "declaration_id": "TauLib.BookIV.Electroweak.NeutrinoMode::NeutrinoRecurrence",
  "declaration_slug": "neutrino-recurrence",
  "kind": "structure",
  "name": "NeutrinoRecurrence",
  "module_name": "TauLib.BookIV.Electroweak.NeutrinoMode",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/",
  "source_line_start": 286,
  "source_line_end": 299,
  "registry_ids": [
    "IV.D127"
  ],
  "related_registry_items": [
    {
      "id": "IV.D127",
      "title": "τ-Hypercharge",
      "url": "/registry/object/IV.D127/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L286-L299",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.NeutrinoMode",
        "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L286-L299",
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

- Module: [TauLib.BookIV.Electroweak.NeutrinoMode](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/)
- Source path: [`TauLib/BookIV/Electroweak/NeutrinoMode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L286-L299)
- Source range: L286-L299
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D127` — τ-Hypercharge

## Immediate Comment / Docstring

```lean
/-- [IV.D127] σ-Polarity Neutrino Recurrence Model.
    The three neutrino mass modes arise from a σ-equivariant 3×3 matrix
    M = [[a, b, 0], [b, c, b], [0, b, a]]
    where a = ι_τ^p (lobe self-coupling), b = ι_τ^q (lobe-mediator coupling),
    c = ι_τ^r (mediator self-coupling).

    The eigenvalues of M give three mass modes:
    λ₁ = a (σ-odd mode: past-shifted vs future-shifted)
    λ₂,₃ = (a+c)/2 ∓ √((a-c)²/4 + 2b²) (σ-even modes)

    Physical origin: U_ω eigenmodes from σ-polarity structure
    on L = S¹∨S¹ — two lobes (χ₊, χ₋) plus σ-fixed crossing mediator
    produce a third-order recurrence with three mass eigenmodes
    (past-shifted, now/σ-fixed, future-shifted).

    Best-fit parameters: (p,q,r) = (3.7, 4.8, 2.8)
    giving Δm²₃₁/Δm²₂₁ ≈ 32.8 (PDG: 32.6) and Σm_ν ≈ 0.089 eV.

    This supersedes the equal-spacing model (exponents 13,14,15) which
    gave Σ = 0.635 eV (5× too heavy) and ratio ≈ 9.58 (wrong). -/
```

## Source Excerpt

```lean
structure NeutrinoRecurrence where
  /-- Lobe self-coupling exponent: a = ι_τ^p. -/
  p_lobe : Nat
  /-- Lobe-mediator coupling exponent: b = ι_τ^q. -/
  q_coupling : Nat
  /-- Mediator self-coupling exponent: c = ι_τ^r. -/
  r_mediator : Nat
  /-- σ-equivariance: matrix is [[a,b,0],[b,c,b],[0,b,a]]. -/
  sigma_equivariant : Bool
  sigma_true : sigma_equivariant = true
  /-- Three eigenvalues (structural). -/
  num_modes : Nat
  modes_eq : num_modes = 3
  deriving Repr
```
