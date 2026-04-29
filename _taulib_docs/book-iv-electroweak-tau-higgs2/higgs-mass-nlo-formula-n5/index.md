---
{
  "projection_kind": "taulib_declaration",
  "title": "higgs_mass_nlo_formula_n5",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-mass-nlo-formula-n5/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Electroweak.TauHiggs2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.TauHiggs2::higgs_mass_nlo_formula_n5",
  "declaration_slug": "higgs-mass-nlo-formula-n5",
  "kind": "def",
  "name": "higgs_mass_nlo_formula_n5",
  "module_name": "TauLib.BookIV.Electroweak.TauHiggs2",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/",
  "source_line_start": 391,
  "source_line_end": 392,
  "registry_ids": [
    "IV.D348"
  ],
  "related_registry_items": [
    {
      "id": "IV.D348",
      "title": "Higgs Mass omega-Sector Formula",
      "url": "/registry/object/IV.D348/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L391-L392",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L391-L392",
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

- Module: [TauLib.BookIV.Electroweak.TauHiggs2](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/)
- Source path: [`TauLib/BookIV/Electroweak/TauHiggs2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L391-L392)
- Source range: L391-L392
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.D348` — Higgs Mass omega-Sector Formula

## Immediate Comment / Docstring

```lean
/-- [IV.D348] The Higgs NLO mass formula using n=5 = W₃(4) window correction.
    m_H/m_n = (4 − ι_τ³/(1 − 5κ_ω))/κ_ω ≈ 133.372, deviation +493 ppm from PDG.
    Structural motivation: W₃(4)=5 is the Window Universality modulus (IV.T140)
    governing all three EW NLO corrections. -/
```

## Source Excerpt

```lean
def higgs_mass_nlo_formula_n5 : String :=
  "m_H/m_n = (4 - iota_tau^3 / (1 - 5*kappa_omega)) / kappa_omega = 133.372  [+493 ppm, tau-effective]"
```
