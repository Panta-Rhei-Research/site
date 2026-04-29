---
{
  "projection_kind": "taulib_declaration",
  "title": "MassDerivationLayer2",
  "permalink": "/verify/taulib/docs/book-v-coda-calibration-chain/mass-derivation-layer2/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Coda.CalibrationChain`.",
  "declaration_id": "TauLib.BookV.Coda.CalibrationChain::MassDerivationLayer2",
  "declaration_slug": "mass-derivation-layer2",
  "kind": "structure",
  "name": "MassDerivationLayer2",
  "module_name": "TauLib.BookV.Coda.CalibrationChain",
  "module_url": "/verify/taulib/docs/book-v-coda-calibration-chain/",
  "source_line_start": 51,
  "source_line_end": 64,
  "registry_ids": [
    "V.T156"
  ],
  "related_registry_items": [
    {
      "id": "V.T156",
      "title": "Mass Derivations --- Layer 2",
      "url": "/registry/object/V.T156/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/CalibrationChain.lean#L51-L64",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Coda.CalibrationChain",
        "url": "/verify/taulib/docs/book-v-coda-calibration-chain/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/CalibrationChain.lean#L51-L64",
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

- Module: [TauLib.BookV.Coda.CalibrationChain](/verify/taulib/docs/book-v-coda-calibration-chain/)
- Source path: [`TauLib/BookV/Coda/CalibrationChain.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/CalibrationChain.lean#L51-L64)
- Source range: L51-L64
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T156` — Mass Derivations --- Layer 2

## Immediate Comment / Docstring

```lean
/-- [V.T156] Mass derivations — Layer 2.
    Derives m_e, m_P, and G from m_n and Layer 1 outputs:
    - m_e = m_n / R (R from τ³ mass ratio)
    - m_P = m_n / √α_G (α_G from G-α bridge)
    - G = (c³/ℏ) · ι_τ² (direct from master constant)

    The layer structure:
    Layer 0: ι_τ = 2/(π+e) (master constant, from axioms)
    Layer 1: α_G = α¹⁸ · √3 · (1 − (3/π)α) (G-α bridge)
    Layer 2: m_e, m_P, G (this theorem)
    Anchor: m_n (single dimensionful input) -/
```

## Source Excerpt

```lean
structure MassDerivationLayer2 where
  /-- Number of derived masses. -/
  n_derived : Nat
  /-- Three masses derived. -/
  derived_eq : n_derived = 3
  /-- Number of layers in the cascade. -/
  n_layers : Nat
  /-- Three layers (0, 1, 2). -/
  layers_eq : n_layers = 3
  /-- Single anchor (m_n). -/
  single_anchor : Bool := true
  /-- Zero additional free parameters. -/
  zero_additional_params : Bool := true
  deriving Repr
```
