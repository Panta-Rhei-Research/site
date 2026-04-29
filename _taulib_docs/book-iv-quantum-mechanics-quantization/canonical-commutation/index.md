---
{
  "projection_kind": "taulib_declaration",
  "title": "CanonicalCommutation",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-quantization/canonical-commutation/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.QuantumMechanics.Quantization`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.Quantization::CanonicalCommutation",
  "declaration_slug": "canonical-commutation",
  "kind": "structure",
  "name": "CanonicalCommutation",
  "module_name": "TauLib.BookIV.QuantumMechanics.Quantization",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantization/",
  "source_line_start": 161,
  "source_line_end": 170,
  "registry_ids": [
    "IV.T21"
  ],
  "related_registry_items": [
    {
      "id": "IV.T21",
      "title": "Canonical Commutation Relation",
      "url": "/registry/object/IV.T21/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Quantization.lean#L161-L170",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.QuantumMechanics.Quantization",
        "url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantization/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Quantization.lean#L161-L170",
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

- Module: [TauLib.BookIV.QuantumMechanics.Quantization](/verify/taulib/docs/book-iv-quantum-mechanics-quantization/)
- Source path: [`TauLib/BookIV/QuantumMechanics/Quantization.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Quantization.lean#L161-L170)
- Source range: L161-L170
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T21` — Canonical Commutation Relation

## Immediate Comment / Docstring

```lean
/-- [IV.T21] Canonical commutation relation: [X_hat, P_hat] = i * hbar_tau.

    In tau-units, hbar_tau = 1/4 (the unique sigma-equivariant crossing-point
    mediator, as established in PlanckCharacter.lean).

    This commutation relation is a THEOREM derived from the CR-structure
    on tau^3, not a postulate of quantum mechanics.

    We encode hbar_tau = 1/4 as the pair (1, 4). -/
```

## Source Excerpt

```lean
structure CanonicalCommutation where
  /-- hbar_tau numerator. -/
  hbar_numer : Nat
  /-- hbar_tau denominator. -/
  hbar_denom : Nat
  /-- Denominator positive. -/
  denom_pos : hbar_denom > 0
  /-- hbar_tau = 1/4 in tau-units. -/
  is_quarter : hbar_numer = 1 ∧ hbar_denom = 4
  deriving Repr
```
