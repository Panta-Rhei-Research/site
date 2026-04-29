---
{
  "projection_kind": "taulib_declaration",
  "title": "combined_ratio_43",
  "permalink": "/verify/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/combined-ratio-43/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.BaryogenesisAsymmetry`.",
  "declaration_id": "TauLib.BookV.Cosmology.BaryogenesisAsymmetry::combined_ratio_43",
  "declaration_slug": "combined-ratio-43",
  "kind": "theorem",
  "name": "combined_ratio_43",
  "module_name": "TauLib.BookV.Cosmology.BaryogenesisAsymmetry",
  "module_url": "/verify/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/",
  "source_line_start": 290,
  "source_line_end": 291,
  "registry_ids": [
    "V.P134"
  ],
  "related_registry_items": [
    {
      "id": "V.P134",
      "title": "Self-Similar 4/3 Ratio Preservation under NNLO",
      "url": "/registry/object/V.P134/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L290-L291",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.BaryogenesisAsymmetry",
        "url": "/verify/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L290-L291",
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

- Module: [TauLib.BookV.Cosmology.BaryogenesisAsymmetry](/verify/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/)
- Source path: [`TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L290-L291)
- Source range: L290-L291
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P134` — Self-Similar 4/3 Ratio Preservation under NNLO

## Immediate Comment / Docstring

```lean
/-- [V.P134] Self-Similar 4/3 Ratio Preservation.
    Combined (203/175)/(609/700) = 4/3 exactly. -/
```

## Source Excerpt

```lean
theorem combined_ratio_43 :
    (203 : Rat) / 175 / (609 / 700) = 4 / 3 := by norm_num
```
