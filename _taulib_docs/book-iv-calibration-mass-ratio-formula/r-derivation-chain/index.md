---
{
  "projection_kind": "taulib_declaration",
  "title": "r_derivation_chain",
  "permalink": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/r-derivation-chain/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Calibration.MassRatioFormula`.",
  "declaration_id": "TauLib.BookIV.Calibration.MassRatioFormula::r_derivation_chain",
  "declaration_slug": "r-derivation-chain",
  "kind": "def",
  "name": "r_derivation_chain",
  "module_name": "TauLib.BookIV.Calibration.MassRatioFormula",
  "module_url": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/",
  "source_line_start": 349,
  "source_line_end": 360,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/MassRatioFormula.lean#L349-L360",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Calibration.MassRatioFormula",
        "url": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/MassRatioFormula.lean#L349-L360",
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

- Module: [TauLib.BookIV.Calibration.MassRatioFormula](/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/)
- Source path: [`TauLib/BookIV/Calibration/MassRatioFormula.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/MassRatioFormula.lean#L349-L360)
- Source range: L349-L360
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The complete 10-link derivation chain. -/
```

## Source Excerpt

```lean
def r_derivation_chain : List RDerivationLink := [
  ⟨1, "τ³ = τ¹ ×_f T² fibration (Axiom K5)", "tau-effective"⟩,
  ⟨2, "Hodge Laplacian Δ on T² with shape ι_τ", "tau-effective"⟩,
  ⟨3, "Breathing operator B = Δ⁻¹|_{T²}", "tau-effective"⟩,
  ⟨4, "Spectral factorization Λ_{n,k₁,k₂}", "tau-effective"⟩,
  ⟨5, "Epstein zeta Z(s; iι_τ) at s=4", "tau-effective"⟩,
  ⟨6, "√3 from lemniscate three-fold |1−ω|", "tau-effective"⟩,
  ⟨7, "R₀ = ι_τ^(-7) − √3·ι_τ^(-2)", "tau-effective"⟩,
  ⟨8, "π³α² holonomy correction (3 circles)", "tau-effective"⟩,
  ⟨9, "R₁ = ι_τ^(-7) − (√3+π³α²)·ι_τ^(-2)", "tau-effective"⟩,
  ⟨10, "m_e = m_n/R₁ (electron mass from anchor)", "tau-effective"⟩
]
```
