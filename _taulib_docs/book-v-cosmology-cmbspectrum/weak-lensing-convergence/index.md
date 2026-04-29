---
{
  "projection_kind": "taulib_declaration",
  "title": "WeakLensingConvergence",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/weak-lensing-convergence/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::WeakLensingConvergence",
  "declaration_slug": "weak-lensing-convergence",
  "kind": "structure",
  "name": "WeakLensingConvergence",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 1140,
  "source_line_end": 1145,
  "registry_ids": [
    "V.D273"
  ],
  "related_registry_items": [
    {
      "id": "V.D273",
      "title": "Weak Lensing Convergence from Boundary Holonomy",
      "url": "/registry/object/V.D273/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1140-L1145",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1140-L1145",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1140-L1145)
- Source range: L1140-L1145
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D273` — Weak Lensing Convergence from Boundary Holonomy

## Immediate Comment / Docstring

```lean
/-- [V.D273] Weak Lensing Convergence with Boundary Holonomy.
    κ(θ) = Σ_eff(θ)/Σ_cr where Σ_eff = Σ_b·(1+κ_D/ι_τ²) = Σ_b·6.65.
    Σ_cr = (c²/4πG)·D_S/(D_L·D_LS). -/
```

## Source Excerpt

```lean
structure WeakLensingConvergence where
  /-- Surface density enhancement × 100 = 665. -/
  sigma_enhancement_x100 : Nat := 665
  /-- Same enhancement as 3D mass ratio (1 = yes). -/
  same_as_3d_ratio : Nat := 1
  deriving Repr
```
