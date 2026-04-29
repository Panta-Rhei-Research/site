---
{
  "projection_kind": "taulib_declaration",
  "title": "ErrorCancellationStructural",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/error-cancellation-structural/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::ErrorCancellationStructural",
  "declaration_slug": "error-cancellation-structural",
  "kind": "structure",
  "name": "ErrorCancellationStructural",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 574,
  "source_line_end": 581,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L574-L581",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.CMBSpectrum",
        "url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L574-L581",
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

- Module: [TauLib.BookV.Cosmology.CMBSpectrum](/verify/taulib/docs/book-v-cosmology-cmbspectrum/)
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L574-L581)
- Source range: L574-L581
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [V.T191 upgrade] Error cancellation is structural.

    ℓ₁ ∝ ω_m^{−a} · ω_b^{b} where a ≈ 0.25, b ≈ 0.13.
    The errors: ω_b at −1.2%, ω_m at +4.1%.
    Product: (−1.2%)^0.13 × (+4.1%)^{−0.25} ≈ 1.
    This is structural: the M3h baseline holonomy formula
    has ω_b undershoot compensating ω_m overshoot in the
    Friedmann integral for the sound horizon.

    Wave 8C finding: correcting ω_m alone BREAKS cancellation.
    NLO must shift both η_B and holonomy ratio together. -/
```

## Source Excerpt

```lean
structure ErrorCancellationStructural where
  /-- Number of structural constraints (coupled NLO + Friedmann integral). -/
  n_structural_constraints : Nat := 2
  /-- Number of compensating error terms (ω_b undershoot + ω_m overshoot). -/
  n_compensating_terms : Nat := 2
  /-- Number of coupled NLO parameters (η_B + holonomy ratio). -/
  n_coupled_params : Nat := 2
  deriving Repr
```
