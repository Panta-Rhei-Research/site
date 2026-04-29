---
{
  "projection_kind": "taulib_declaration",
  "title": "ew_prediction_table",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/ew-prediction-table/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Electroweak.EWSynthesis`.",
  "declaration_id": "TauLib.BookIV.Electroweak.EWSynthesis::ew_prediction_table",
  "declaration_slug": "ew-prediction-table",
  "kind": "def",
  "name": "ew_prediction_table",
  "module_name": "TauLib.BookIV.Electroweak.EWSynthesis",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/",
  "source_line_start": 145,
  "source_line_end": 155,
  "registry_ids": [
    "IV.T66"
  ],
  "related_registry_items": [
    {
      "id": "IV.T66",
      "title": "Electroweak Prediction Table",
      "url": "/registry/object/IV.T66/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWSynthesis.lean#L145-L155",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.EWSynthesis",
        "url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWSynthesis.lean#L145-L155",
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

- Module: [TauLib.BookIV.Electroweak.EWSynthesis](/verify/taulib/docs/book-iv-electroweak-ewsynthesis/)
- Source path: [`TauLib/BookIV/Electroweak/EWSynthesis.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWSynthesis.lean#L145-L155)
- Source range: L145-L155
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.T66` — Electroweak Prediction Table

## Immediate Comment / Docstring

```lean
/-- [IV.T66] The nine EW quantities determined by ι_τ and m_n. -/
```

## Source Excerpt

```lean
def ew_prediction_table : List EWSynthesisPrediction := [
  ⟨"M_W", 80379, 1, 80377, 1, 25⟩,
  ⟨"M_Z", 91188, 1, 91188, 1, 2⟩,
  ⟨"M_H", 125100, 1, 125100, 1, 1100⟩,
  ⟨"v_EW", 246200, 1, 246220, 1, 80⟩,
  ⟨"sin2_theta_W", 2249, 10000, 2312, 10000, 27000⟩,
  ⟨"alpha_EM", 7247, 1000000, 7297, 1000000, 6900⟩,
  ⟨"y_top", 995000, 1000000, 995000, 1000000, 500⟩,
  ⟨"y_bottom", 24000, 1000000, 24000, 1000000, 2000⟩,
  ⟨"y_electron", 3, 1000000, 3, 1000000, 25⟩
]
```
