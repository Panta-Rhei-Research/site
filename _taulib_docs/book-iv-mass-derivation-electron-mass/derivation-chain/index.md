---
{
  "projection_kind": "taulib_declaration",
  "title": "derivation_chain",
  "permalink": "/verify/taulib/docs/book-iv-mass-derivation-electron-mass/derivation-chain/",
  "summary_short": "`def` declaration in `TauLib.BookIV.MassDerivation.ElectronMass`.",
  "declaration_id": "TauLib.BookIV.MassDerivation.ElectronMass::derivation_chain",
  "declaration_slug": "derivation-chain",
  "kind": "def",
  "name": "derivation_chain",
  "module_name": "TauLib.BookIV.MassDerivation.ElectronMass",
  "module_url": "/verify/taulib/docs/book-iv-mass-derivation-electron-mass/",
  "source_line_start": 48,
  "source_line_end": 59,
  "registry_ids": [
    "IV.T117"
  ],
  "related_registry_items": [
    {
      "id": "IV.T117",
      "title": "Derivation Chain Complete --- IV.T15",
      "url": "/registry/object/IV.T117/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/ElectronMass.lean#L48-L59",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.MassDerivation.ElectronMass",
        "url": "/verify/taulib/docs/book-iv-mass-derivation-electron-mass/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/ElectronMass.lean#L48-L59",
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

- Module: [TauLib.BookIV.MassDerivation.ElectronMass](/verify/taulib/docs/book-iv-mass-derivation-electron-mass/)
- Source path: [`TauLib/BookIV/MassDerivation/ElectronMass.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/ElectronMass.lean#L48-L59)
- Source range: L48-L59
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.T117` — Derivation Chain Complete --- IV.T15

## Immediate Comment / Docstring

```lean
/-- [IV.T117] The complete 10-link chain from K₀-K₆ to m_e. -/
```

## Source Excerpt

```lean
def derivation_chain : List ChainLink := [
  ⟨1,  "τ³ = τ¹ ×_f T² fibration (Axiom K5)",      .Established⟩,
  ⟨2,  "Hodge Laplacian Δ on T² with shape ι_τ",    .Established⟩,
  ⟨3,  "Breathing operator B = Δ⁻¹|_{T²}",          .Established⟩,
  ⟨4,  "Spectral factorization Λ_{n,k₁,k₂}",       .TauEffective⟩,
  ⟨5,  "Epstein zeta Z(s; iι_τ) at s=4",            .TauEffective⟩,
  ⟨6,  "√3 from lemniscate three-fold |1−ω|",       .TauEffective⟩,
  ⟨7,  "R₀ = ι_τ^(-7) − √3·ι_τ^(-2)",              .TauEffective⟩,
  ⟨8,  "π³α² holonomy correction (3 circles)",       .TauEffective⟩,
  ⟨9,  "R₁ = ι_τ^(-7) − (√3+π³α²)·ι_τ^(-2)",       .TauEffective⟩,
  ⟨10, "m_e = m_n/R₁ (electron mass from anchor)",   .TauEffective⟩
]
```
