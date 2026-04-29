---
{
  "projection_kind": "taulib_declaration",
  "title": "T2EchoFormulas",
  "permalink": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/t2-echo-formulas/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Gravity.BHTopoModes`.",
  "declaration_id": "TauLib.BookV.Gravity.BHTopoModes::T2EchoFormulas",
  "declaration_slug": "t2-echo-formulas",
  "kind": "structure",
  "name": "T2EchoFormulas",
  "module_name": "TauLib.BookV.Gravity.BHTopoModes",
  "module_url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/",
  "source_line_start": 312,
  "source_line_end": 321,
  "registry_ids": [
    "V.D243"
  ],
  "related_registry_items": [
    {
      "id": "V.D243",
      "title": "T² GW Echo Time Formulas with Frequency Bands",
      "url": "/registry/object/V.D243/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L312-L321",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Gravity.BHTopoModes",
        "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L312-L321",
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

- Module: [TauLib.BookV.Gravity.BHTopoModes](/verify/taulib/docs/book-v-gravity-bhtopo-modes/)
- Source path: [`TauLib/BookV/Gravity/BHTopoModes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L312-L321)
- Source range: L312-L321
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D243` — T² GW Echo Time Formulas with Frequency Bands

## Immediate Comment / Docstring

```lean
/-- [V.D243] Structure capturing T² GW echo time formulas.
    t₋/t₊ = ι_τ⁻² ≈ 8.585. Both echoes fall in LIGO band for stellar-mass BHs.
    Ratio stored ×1000 for Nat arithmetic. -/
```

## Source Excerpt

```lean
structure T2EchoFormulas where
  /-- Echo time ratio ×1000 (ι_τ⁻² ≈ 8.585 → 8585). -/
  ratio_x1000 : Nat := 8585
  /-- Number of echo times in LIGO band (inner + outer). -/
  n_ligo_band : Nat := 2
  /-- Number of reference events tested (GW150914). -/
  n_reference_events : Nat := 1
  /-- Ratio exceeds 1000 (i.e., ι_τ⁻² > 1, inner is shorter). -/
  ratio_gt_1000 : ratio_x1000 > 1000
  deriving Repr
```
