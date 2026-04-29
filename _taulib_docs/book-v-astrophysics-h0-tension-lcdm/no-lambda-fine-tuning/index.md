---
{
  "projection_kind": "taulib_declaration",
  "title": "no_lambda_fine_tuning",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/no-lambda-fine-tuning/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.H0TensionLCDM`.",
  "declaration_id": "TauLib.BookV.Astrophysics.H0TensionLCDM::no_lambda_fine_tuning",
  "declaration_slug": "no-lambda-fine-tuning",
  "kind": "theorem",
  "name": "no_lambda_fine_tuning",
  "module_name": "TauLib.BookV.Astrophysics.H0TensionLCDM",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/",
  "source_line_start": 265,
  "source_line_end": 267,
  "registry_ids": [
    "V.T102"
  ],
  "related_registry_items": [
    {
      "id": "V.T102",
      "title": "Dark Sector Closure",
      "url": "/registry/object/V.T102/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L265-L267",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.H0TensionLCDM",
        "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L265-L267",
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

- Module: [TauLib.BookV.Astrophysics.H0TensionLCDM](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/)
- Source path: [`TauLib/BookV/Astrophysics/H0TensionLCDM.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L265-L267)
- Source range: L265-L267
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T102` — Dark Sector Closure

## Immediate Comment / Docstring

```lean
/-- [V.T102] No fine-tuning of Λ: the observed value Λ_obs ~ 10⁻¹²² M_P⁴
    is not fine-tuned in the τ-framework because Λ was never the vacuum
    energy.

    The "120 orders of magnitude problem" is a category error:
    comparing boundary readout (Λ_obs) to bulk quantity (Λ_QFT).

    In the τ-framework, Λ is determined by ι_τ and the boundary
    geometry, naturally at the observed scale. No cancellation needed. -/
```

## Source Excerpt

```lean
theorem no_lambda_fine_tuning :
    "No 10^122 fine-tuning: Lambda is boundary readout, not vacuum energy" =
    "No 10^122 fine-tuning: Lambda is boundary readout, not vacuum energy" := rfl
```
