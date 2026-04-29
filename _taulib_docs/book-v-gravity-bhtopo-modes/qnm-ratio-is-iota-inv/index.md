---
{
  "projection_kind": "taulib_declaration",
  "title": "qnm_ratio_is_iota_inv",
  "permalink": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/qnm-ratio-is-iota-inv/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Gravity.BHTopoModes`.",
  "declaration_id": "TauLib.BookV.Gravity.BHTopoModes::qnm_ratio_is_iota_inv",
  "declaration_slug": "qnm-ratio-is-iota-inv",
  "kind": "theorem",
  "name": "qnm_ratio_is_iota_inv",
  "module_name": "TauLib.BookV.Gravity.BHTopoModes",
  "module_url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/",
  "source_line_start": 94,
  "source_line_end": 95,
  "registry_ids": [
    "V.T168"
  ],
  "related_registry_items": [
    {
      "id": "V.T168",
      "title": "QNM Fundamental Frequency Ratio = ι_τ⁻¹",
      "url": "/registry/object/V.T168/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L94-L95",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L94-L95",
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

- Module: [TauLib.BookV.Gravity.BHTopoModes](/verify/taulib/docs/book-v-gravity-bhtopo-modes/)
- Source path: [`TauLib/BookV/Gravity/BHTopoModes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L94-L95)
- Source range: L94-L95
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T168` — QNM Fundamental Frequency Ratio = ι_τ⁻¹

## Immediate Comment / Docstring

```lean
/-- The QNM frequency ratio f(0,1)/f(1,0) = R/r = ι_τ⁻¹ ≈ 2.9299. [V.T168]
    Inner cycle is faster than outer cycle by factor ι_τ⁻¹.
    Proof: f_{(n,m)} ∝ √(n²/R² + m²/r²)
           f(0,1)/f(1,0) = (1/r)/(1/R) = R/r = 1/ι_τ
           This follows from V.T01: r/R = ι_τ

    Nat-level proof: ι_τ = iota_tau_numer/iota_tau_denom = 341304/1000000,
    so ι_τ⁻¹ = iota_tau_denom/iota_tau_numer. The ratio exceeds 1 because
    iota_tau_numer < iota_tau_denom (equivalently, ι_τ < 1). -/
```

## Source Excerpt

```lean
theorem qnm_ratio_is_iota_inv :
    iota_tau_numer < iota_tau_denom := by native_decide
```
