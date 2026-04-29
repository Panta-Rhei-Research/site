---
{
  "projection_kind": "taulib_declaration",
  "title": "SchrodingerEquation",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-measurement/schrodinger-equation/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.QuantumMechanics.Measurement`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.Measurement::SchrodingerEquation",
  "declaration_slug": "schrodinger-equation",
  "kind": "structure",
  "name": "SchrodingerEquation",
  "module_name": "TauLib.BookIV.QuantumMechanics.Measurement",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-measurement/",
  "source_line_start": 180,
  "source_line_end": 191,
  "registry_ids": [
    "IV.T28"
  ],
  "related_registry_items": [
    {
      "id": "IV.T28",
      "title": "Schrödinger Equation",
      "url": "/registry/object/IV.T28/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Measurement.lean#L180-L191",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.QuantumMechanics.Measurement",
        "url": "/verify/taulib/docs/book-iv-quantum-mechanics-measurement/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Measurement.lean#L180-L191",
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

- Module: [TauLib.BookIV.QuantumMechanics.Measurement](/verify/taulib/docs/book-iv-quantum-mechanics-measurement/)
- Source path: [`TauLib/BookIV/QuantumMechanics/Measurement.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Measurement.lean#L180-L191)
- Source range: L180-L191
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T28` — Schrödinger Equation

## Immediate Comment / Docstring

```lean
/-- [IV.T28] Schrodinger equation: iℏ_τ ∂ψ/∂t = H_∞ ψ.

    H_∞ = ι_τ² Δ_Hodge is the breathing operator on T².
    This equation is DERIVED from holomorphic flow on the CR-address
    lattice, not postulated. The ι_τ² prefactor is the inverse of
    the breathing operator B = (1/ι_τ²)·Δ⁻¹|_{T²}.

    The iota-squared coefficient:
    - iota_sq_numer = ι² numerator (from SectorParameters)
    - iota_sq_denom = ι² denominator -/
```

## Source Excerpt

```lean
structure SchrodingerEquation where
  /-- H_∞ coefficient numerator: ι_τ². -/
  hamiltonian_coeff_numer : Nat
  /-- H_∞ coefficient denominator. -/
  hamiltonian_coeff_denom : Nat
  /-- Denominator positive. -/
  denom_pos : hamiltonian_coeff_denom > 0
  /-- The equation is derived (not postulated). -/
  is_derived : Bool := true
  /-- The Hamiltonian is H_∞ = ι_τ² Δ_Hodge. -/
  operator_name : String := "H_∞ = ι_τ² Δ_Hodge"
  deriving Repr
```
