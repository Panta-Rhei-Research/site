---
{
  "projection_kind": "taulib_declaration",
  "title": "TauHiggsMass",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/tau-higgs-mass/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.TauHiggs2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.TauHiggs2::TauHiggsMass",
  "declaration_slug": "tau-higgs-mass",
  "kind": "structure",
  "name": "TauHiggsMass",
  "module_name": "TauLib.BookIV.Electroweak.TauHiggs2",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/",
  "source_line_start": 84,
  "source_line_end": 93,
  "registry_ids": [
    "IV.D141"
  ],
  "related_registry_items": [
    {
      "id": "IV.D141",
      "title": "τ-Higgs Mass",
      "url": "/registry/object/IV.D141/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L84-L93",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L84-L93",
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
- Source path: [`TauLib/BookIV/Electroweak/TauHiggs2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L84-L93)
- Source range: L84-L93
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D141` — τ-Higgs Mass

## Immediate Comment / Docstring

```lean
/-- [IV.D141] The τ-Higgs mass M_H: determined by the positive
    eigenvalue of the coherence Hessian.

    M_H ≈ 125100 MeV (125.1 GeV).
    Experimental: 125100 ± 140 MeV (ATLAS+CMS combined, 2024).

    In the τ-framework, M_H is a DERIVED quantity from ι_τ and m_n,
    not a free parameter. -/
```

## Source Excerpt

```lean
structure TauHiggsMass where
  /-- Higgs mass in MeV. -/
  mass_MeV : Nat
  /-- Mass is positive. -/
  mass_pos : mass_MeV > 0
  /-- Experimental value in MeV (central). -/
  exp_MeV : Nat := 125100
  /-- Experimental uncertainty in MeV. -/
  exp_unc_MeV : Nat := 140
  deriving Repr
```
