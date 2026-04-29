---
{
  "projection_kind": "taulib_declaration",
  "title": "HiggsSelfCoupling",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-self-coupling/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.TauHiggs2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.TauHiggs2::HiggsSelfCoupling",
  "declaration_slug": "higgs-self-coupling",
  "kind": "structure",
  "name": "HiggsSelfCoupling",
  "module_name": "TauLib.BookIV.Electroweak.TauHiggs2",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/",
  "source_line_start": 641,
  "source_line_end": 656,
  "registry_ids": [
    "IV.D376"
  ],
  "related_registry_items": [
    {
      "id": "IV.D376",
      "title": "Higgs Self-Coupling from τ-Chain",
      "url": "/registry/object/IV.D376/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L641-L656",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.TauHiggs2",
        "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L641-L656",
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

- Module: [TauLib.BookIV.Electroweak.TauHiggs2](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/)
- Source path: [`TauLib/BookIV/Electroweak/TauHiggs2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L641-L656)
- Source range: L641-L656
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D376` — Higgs Self-Coupling from τ-Chain

## Immediate Comment / Docstring

```lean
/-- [IV.D376] Higgs self-coupling from τ-chain.

    λ_H = m_H(τ)² / (2·v_EW²) = 0.12928 at +16 ppm.
    Inherits precision from IV.T166 (m_H at +8 ppm);
    λ_H deviation ≈ 2 × m_H deviation since λ ∝ m².
    Coherence functional curvature at ω-crossing equilibrium. -/
```

## Source Excerpt

```lean
structure HiggsSelfCoupling where
  /-- λ_H (×100000 for integer: 12928). -/
  lambda_x1e5 : Nat := 12928
  /-- SM λ from PDG m_H (×100000). -/
  lambda_sm_x1e5 : Nat := 12928
  /-- Deviation in ppm. -/
  deviation_ppm : Int := 16
  /-- Inherited from n=7 Higgs mass. -/
  higgs_mass_ppm : Nat := 8
  /-- λ deviation ≈ 2 × m_H deviation. -/
  doubled_mass_ppm : Bool := true
  /-- No standalone formula found. -/
  standalone_formula : Bool := false
  /-- Number of free parameters. -/
  free_params : Nat := 0
  deriving Repr
```
