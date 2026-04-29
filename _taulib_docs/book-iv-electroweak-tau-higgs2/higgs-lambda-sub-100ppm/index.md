---
{
  "projection_kind": "taulib_declaration",
  "title": "higgs_lambda_sub_100ppm",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-lambda-sub-100ppm/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.TauHiggs2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.TauHiggs2::higgs_lambda_sub_100ppm",
  "declaration_slug": "higgs-lambda-sub-100ppm",
  "kind": "theorem",
  "name": "higgs_lambda_sub_100ppm",
  "module_name": "TauLib.BookIV.Electroweak.TauHiggs2",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/",
  "source_line_start": 662,
  "source_line_end": 665,
  "registry_ids": [
    "IV.T194"
  ],
  "related_registry_items": [
    {
      "id": "IV.T194",
      "title": "τ-Chain Higgs Self-Coupling at +16 ppm",
      "url": "/registry/object/IV.T194/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L662-L665",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L662-L665",
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

- Module: [TauLib.BookIV.Electroweak.TauHiggs2](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/)
- Source path: [`TauLib/BookIV/Electroweak/TauHiggs2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L662-L665)
- Source range: L662-L665
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T194` — τ-Chain Higgs Self-Coupling at +16 ppm

## Immediate Comment / Docstring

```lean
/-- [IV.T194] τ-chain λ_H at +16 ppm.
    No planned collider can distinguish τ from SM (gap = 0.0016%). -/
```

## Source Excerpt

```lean
theorem higgs_lambda_sub_100ppm :
    higgs_self_coupling.deviation_ppm < 100 ∧
    higgs_self_coupling.deviation_ppm > 0 := by
  constructor <;> native_decide
```
