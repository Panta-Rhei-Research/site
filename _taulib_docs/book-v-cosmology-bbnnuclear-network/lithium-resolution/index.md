---
{
  "projection_kind": "taulib_declaration",
  "title": "LithiumResolution",
  "permalink": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/lithium-resolution/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.BBNNuclearNetwork`.",
  "declaration_id": "TauLib.BookV.Cosmology.BBNNuclearNetwork::LithiumResolution",
  "declaration_slug": "lithium-resolution",
  "kind": "structure",
  "name": "LithiumResolution",
  "module_name": "TauLib.BookV.Cosmology.BBNNuclearNetwork",
  "module_url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/",
  "source_line_start": 270,
  "source_line_end": 285,
  "registry_ids": [
    "V.T244"
  ],
  "related_registry_items": [
    {
      "id": "V.T244",
      "title": "Li-7 Resolution",
      "url": "/registry/object/V.T244/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L270-L285",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.BBNNuclearNetwork",
        "url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L270-L285",
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

- Module: [TauLib.BookV.Cosmology.BBNNuclearNetwork](/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/)
- Source path: [`TauLib/BookV/Cosmology/BBNNuclearNetwork.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L270-L285)
- Source range: L270-L285
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T244` — Li-7 Resolution

## Immediate Comment / Docstring

```lean
/-- [V.T244] Lithium-7 resolution: SBBN value × (1/3) → within 0.9σ.
    SBBN: ⁷Li/H = 562 × 10⁻¹² (i.e. 5.62 × 10⁻¹⁰).
    τ-BBN: 562/3 = 187 × 10⁻¹² (i.e. 1.87 × 10⁻¹⁰).
    Spite plateau: 160 ± 30 × 10⁻¹². Deviation: +0.9σ. -/
```

## Source Excerpt

```lean
structure LithiumResolution where
  /-- SBBN prediction (×10⁻¹²). -/
  sbbn_x1e12 : Nat := 562
  /-- Suppression factor denominator. -/
  suppression_den : Nat := 3
  /-- τ-BBN prediction (×10⁻¹²). -/
  tau_x1e12 : Nat := 187
  /-- τ-BBN = SBBN / suppression_den (integer floor). -/
  tau_from_sbbn : tau_x1e12 = sbbn_x1e12 / suppression_den
  /-- Observed Spite plateau midpoint (×10⁻¹²). -/
  obs_x1e12 : Nat := 160
  /-- Observed uncertainty (×10⁻¹²). -/
  obs_unc_x1e12 : Nat := 30
  /-- τ-BBN within observed range (160 − 30 = 130, 160 + 90 = 250). -/
  within_range : tau_x1e12 > obs_x1e12 - obs_unc_x1e12
  deriving Repr
```
