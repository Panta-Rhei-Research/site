---
{
  "projection_kind": "taulib_declaration",
  "title": "HiggsLambdaFalsification",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-lambda-falsification/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.TauHiggs2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.TauHiggs2::HiggsLambdaFalsification",
  "declaration_slug": "higgs-lambda-falsification",
  "kind": "structure",
  "name": "HiggsLambdaFalsification",
  "module_name": "TauLib.BookIV.Electroweak.TauHiggs2",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/",
  "source_line_start": 670,
  "source_line_end": 679,
  "registry_ids": [
    "IV.P220"
  ],
  "related_registry_items": [
    {
      "id": "IV.P220",
      "title": "HL-LHC and FCC-hh Falsification Window",
      "url": "/registry/object/IV.P220/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L670-L679",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L670-L679",
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
- Source path: [`TauLib/BookIV/Electroweak/TauHiggs2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L670-L679)
- Source range: L670-L679
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P220` — HL-LHC and FCC-hh Falsification Window

## Immediate Comment / Docstring

```lean
/-- [IV.P220] HL-LHC / FCC-hh sensitivity vs τ-SM gap.
    HL-LHC: 50% precision → cannot see 0.0016% gap.
    FCC-hh: 3-5% precision → still cannot see 0.0016% gap. -/
```

## Source Excerpt

```lean
structure HiggsLambdaFalsification where
  /-- τ-SM gap in ppm. -/
  tau_sm_gap_ppm : Nat := 16
  /-- HL-LHC precision (percent ×10). -/
  hllhc_precision_pct_x10 : Nat := 500
  /-- FCC-hh precision (percent ×10). -/
  fcc_precision_pct_x10 : Nat := 40
  /-- Neither can discriminate. -/
  discriminating : Bool := false
  deriving Repr
```
