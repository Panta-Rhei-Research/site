---
{
  "projection_kind": "taulib_declaration",
  "title": "all_formulas_positive",
  "permalink": "/verify/taulib/docs/book-iv-sectors-coupling-formulas/all-formulas-positive/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Sectors.CouplingFormulas`.",
  "declaration_id": "TauLib.BookIV.Sectors.CouplingFormulas::all_formulas_positive",
  "declaration_slug": "all-formulas-positive",
  "kind": "theorem",
  "name": "all_formulas_positive",
  "module_name": "TauLib.BookIV.Sectors.CouplingFormulas",
  "module_url": "/verify/taulib/docs/book-iv-sectors-coupling-formulas/",
  "source_line_start": 248,
  "source_line_end": 257,
  "registry_ids": [
    "IV.P01"
  ],
  "related_registry_items": [
    {
      "id": "IV.P01",
      "title": "All Couplings Positive",
      "url": "/registry/object/IV.P01/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/CouplingFormulas.lean#L248-L257",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Sectors.CouplingFormulas",
        "url": "/verify/taulib/docs/book-iv-sectors-coupling-formulas/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/CouplingFormulas.lean#L248-L257",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookIV.Sectors.CouplingFormulas](/verify/taulib/docs/book-iv-sectors-coupling-formulas/)
- Source path: [`TauLib/BookIV/Sectors/CouplingFormulas.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/CouplingFormulas.lean#L248-L257)
- Source range: L248-L257
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.P01` — All Couplings Positive

## Immediate Comment / Docstring

```lean
/-- [IV.P01] All 10 coupling numerators are positive.
    Since all denominators are positive by construction,
    all coupling values are strictly positive. -/
```

## Source Excerpt

```lean
theorem all_formulas_positive :
    kappa_DD.numer > 0 ∧ kappa_AA.numer > 0 ∧
    kappa_BB.numer > 0 ∧ kappa_CC.numer > 0 ∧
    kappa_AB.numer > 0 ∧ kappa_AC.numer > 0 ∧
    kappa_AD.numer > 0 ∧ kappa_BC.numer > 0 ∧
    kappa_BD.numer > 0 ∧ kappa_CD.numer > 0 := by
  simp [kappa_DD, kappa_AA, kappa_BB, kappa_CC,
        kappa_AB, kappa_AC, kappa_AD, kappa_BC, kappa_BD, kappa_CD,
        iota, oneMinusIota, onePlusIota, iotaD,
        iota_tau_numer, iota_tau_denom]
```
