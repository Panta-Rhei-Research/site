---
{
  "projection_kind": "taulib_declaration",
  "title": "higgs_mass_nlo_formula_n6",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-mass-nlo-formula-n6/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Electroweak.TauHiggs2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.TauHiggs2::higgs_mass_nlo_formula_n6",
  "declaration_slug": "higgs-mass-nlo-formula-n6",
  "kind": "def",
  "name": "higgs_mass_nlo_formula_n6",
  "module_name": "TauLib.BookIV.Electroweak.TauHiggs2",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/",
  "source_line_start": 397,
  "source_line_end": 398,
  "registry_ids": [
    "IV.R399"
  ],
  "related_registry_items": [
    {
      "id": "IV.R399",
      "title": "Open: omega Self-Energy Correction and Coefficient-6 Identification",
      "url": "/registry/object/IV.R399/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L397-L398",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L397-L398",
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
- Source path: [`TauLib/BookIV/Electroweak/TauHiggs2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L397-L398)
- Source range: L397-L398
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.R399` — Open: omega Self-Energy Correction and Coefficient-6 Identification

## Immediate Comment / Docstring

```lean
/-- [IV.R399] Bonus formula with n=6 coefficient (68 ppm, structural meaning open).
    (4 − ι_τ³/(1 − 6κ_ω))/κ_ω = 133.315 vs PDG 133.306 → +68 ppm.
    Coefficient 6 not yet identified structurally. -/
```

## Source Excerpt

```lean
def higgs_mass_nlo_formula_n6 : String :=
  "m_H/m_n = (4 - iota_tau^3 / (1 - 6*kappa_omega)) / kappa_omega = 133.315  [+68 ppm, conjectural]"
```
