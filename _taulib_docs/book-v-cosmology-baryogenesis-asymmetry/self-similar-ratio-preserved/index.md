---
{
  "projection_kind": "taulib_declaration",
  "title": "self_similar_ratio_preserved",
  "permalink": "/verify/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/self-similar-ratio-preserved/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.BaryogenesisAsymmetry`.",
  "declaration_id": "TauLib.BookV.Cosmology.BaryogenesisAsymmetry::self_similar_ratio_preserved",
  "declaration_slug": "self-similar-ratio-preserved",
  "kind": "theorem",
  "name": "self_similar_ratio_preserved",
  "module_name": "TauLib.BookV.Cosmology.BaryogenesisAsymmetry",
  "module_url": "/verify/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/",
  "source_line_start": 277,
  "source_line_end": 278,
  "registry_ids": [
    "V.D246"
  ],
  "related_registry_items": [
    {
      "id": "V.D246",
      "title": "Self-Similar NNLO Correction: δ₁=3/175, δ₂=9/700",
      "url": "/registry/object/V.D246/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L277-L278",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L277-L278",
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
- Source path: [`TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L277-L278)
- Source range: L277-L278
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.D246` — Self-Similar NNLO Correction: δ₁=3/175, δ₂=9/700

## Immediate Comment / Docstring

```lean
/-- [V.D246] Self-Similar NNLO Correction.
    δ₁=3/175=dim/(n·W₃(4)²), δ₂=9/700=(3/4)·δ₁. 4/3 ratio preserved. -/
```

## Source Excerpt

```lean
theorem self_similar_ratio_preserved :
    (3 : Rat) / 175 / ((9 : Rat) / 700) = 4 / 3 := by norm_num
```
