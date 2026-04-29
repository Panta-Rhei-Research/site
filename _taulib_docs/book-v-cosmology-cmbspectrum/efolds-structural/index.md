---
{
  "projection_kind": "taulib_declaration",
  "title": "EfoldsStructural",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/efolds-structural/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::EfoldsStructural",
  "declaration_slug": "efolds-structural",
  "kind": "structure",
  "name": "EfoldsStructural",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 520,
  "source_line_end": 539,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L520-L539",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L520-L539",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L520-L539)
- Source range: L520-L539
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [V.T196 upgrade] N_e = dim(τ³) × W₅(3) = 3 × 19 = 57.

    The number of e-folds is determined by:
    - dim(τ³) = 3: independent directions in the fiber
    - W₅(3) = 19: the [5,3] Window modulus from CF(ι_τ⁻¹)
    - Each dimension traverses W₅(3) independent winding modes
      before the first complex structure (hadronic threshold)

    This gives n_s = 1 − 2/N_e = 1 − 2/57 = 0.96491
    vs Planck 0.9649 ± 0.0042 (deviation +13 ppm).

    Wave 14A upgrade: exit condition formalized. Inflation ends when
    boundary characters cross the threshold ladder (ch48). The exit
    is structural (cooling function), not fine-tuned (inflaton potential).
    Scope: conjectural → τ-effective. -/
```

## Source Excerpt

```lean
structure EfoldsStructural where
  /-- τ³ dimension. -/
  tau3_dim : Nat := 3
  /-- W₅(3) window modulus. -/
  w53 : Nat := 19
  /-- N_e = dim × W₅(3). -/
  n_e : Nat := 57
  /-- N_e = dim × window. -/
  decomp : n_e = tau3_dim * w53
  /-- n_s deviation from Planck in ppm (+13). -/
  ns_deviation_ppm : Nat := 13
  /-- Exit condition: 1 = threshold crossing (ch48). -/
  exit_condition : Nat := 1
  /-- a₃ = 13 from CF(ι_τ⁻¹), source of W₅(3). -/
  cf_a3 : Nat := 13
  /-- a₄ = 3 from CF(ι_τ⁻¹). -/
  cf_a4 : Nat := 3
  /-- W₅(3) = a₃ + a₄ + 1 = 13 + 5 + 1 = 19. -/
  window_decomp : w53 = cf_a3 + 5 + 1
  deriving Repr
```
