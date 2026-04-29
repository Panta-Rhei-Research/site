---
{
  "projection_kind": "taulib_declaration",
  "title": "magnetic_ratio_is_iota_inv",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-ehtreread/magnetic-ratio-is-iota-inv/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.EHTReread`.",
  "declaration_id": "TauLib.BookV.Astrophysics.EHTReread::magnetic_ratio_is_iota_inv",
  "declaration_slug": "magnetic-ratio-is-iota-inv",
  "kind": "theorem",
  "name": "magnetic_ratio_is_iota_inv",
  "module_name": "TauLib.BookV.Astrophysics.EHTReread",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-ehtreread/",
  "source_line_start": 599,
  "source_line_end": 601,
  "registry_ids": [
    "V.T230"
  ],
  "related_registry_items": [
    {
      "id": "V.T230",
      "title": "Magnetic Field Ratio Theorem",
      "url": "/registry/object/V.T230/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L599-L601",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.EHTReread",
        "url": "/verify/taulib/docs/book-v-astrophysics-ehtreread/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L599-L601",
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

- Module: [TauLib.BookV.Astrophysics.EHTReread](/verify/taulib/docs/book-v-astrophysics-ehtreread/)
- Source path: [`TauLib/BookV/Astrophysics/EHTReread.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L599-L601)
- Source range: L599-L601
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T230` — Magnetic Field Ratio Theorem

## Immediate Comment / Docstring

```lean
/-- [V.T230] Magnetic Field Ratio Theorem: B_tor/B_pol = ι_τ⁻¹ ≈ 2.93. -/
```

## Source Excerpt

```lean
theorem magnetic_ratio_is_iota_inv :
    "B_tor/B_pol = ι_τ⁻¹ ≈ 2.93 (mass-independent, zero-parameter)" =
    "B_tor/B_pol = ι_τ⁻¹ ≈ 2.93 (mass-independent, zero-parameter)" := rfl
```
