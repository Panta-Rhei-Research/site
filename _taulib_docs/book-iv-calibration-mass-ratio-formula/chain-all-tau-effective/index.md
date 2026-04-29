---
{
  "projection_kind": "taulib_declaration",
  "title": "chain_all_tau_effective",
  "permalink": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/chain-all-tau-effective/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Calibration.MassRatioFormula`.",
  "declaration_id": "TauLib.BookIV.Calibration.MassRatioFormula::chain_all_tau_effective",
  "declaration_slug": "chain-all-tau-effective",
  "kind": "theorem",
  "name": "chain_all_tau_effective",
  "module_name": "TauLib.BookIV.Calibration.MassRatioFormula",
  "module_url": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/",
  "source_line_start": 366,
  "source_line_end": 368,
  "registry_ids": [
    "IV.P07"
  ],
  "related_registry_items": [
    {
      "id": "IV.P07",
      "title": "All Links Tau-Effective",
      "url": "/registry/object/IV.P07/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/MassRatioFormula.lean#L366-L368",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/MassRatioFormula.lean#L366-L368",
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

- Module: [TauLib.BookIV.Calibration.MassRatioFormula](/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/)
- Source path: [`TauLib/BookIV/Calibration/MassRatioFormula.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/MassRatioFormula.lean#L366-L368)
- Source range: L366-L368
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.P07` — All Links Tau-Effective

## Immediate Comment / Docstring

```lean
/-- [IV.P07] ALL 10 links are tau-effective. Zero conjectural ingredients. -/
```

## Source Excerpt

```lean
theorem chain_all_tau_effective :
    r_derivation_chain.all (fun l => l.scope == "tau-effective") = true := by
  native_decide
```
