---
{
  "projection_kind": "taulib_declaration",
  "title": "remark_nnlo_precision",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-weinberg-nlo/remark-nnlo-precision/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Electroweak.WeinbergNLO`.",
  "declaration_id": "TauLib.BookIV.Electroweak.WeinbergNLO::remark_nnlo_precision",
  "declaration_slug": "remark-nnlo-precision",
  "kind": "def",
  "name": "remark_nnlo_precision",
  "module_name": "TauLib.BookIV.Electroweak.WeinbergNLO",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-weinberg-nlo/",
  "source_line_start": 282,
  "source_line_end": 284,
  "registry_ids": [
    "IV.R393"
  ],
  "related_registry_items": [
    {
      "id": "IV.R393",
      "title": "NNLO Precision Summary",
      "url": "/registry/object/IV.R393/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L282-L284",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.WeinbergNLO",
        "url": "/verify/taulib/docs/book-iv-electroweak-weinberg-nlo/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L282-L284",
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

- Module: [TauLib.BookIV.Electroweak.WeinbergNLO](/verify/taulib/docs/book-iv-electroweak-weinberg-nlo/)
- Source path: [`TauLib/BookIV/Electroweak/WeinbergNLO.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L282-L284)
- Source range: L282-L284
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.R393` — NNLO Precision Summary

## Immediate Comment / Docstring

```lean
/-- [IV.R393] NNLO precision summary.
    sin²θ_W: −0.7 ppm (NNLO);  M_W: −0.4 ppm (NLO);  α_s: +43 ppm (NLO).
    All from W₃(4)=5 as universal NLO modulus. -/
```

## Source Excerpt

```lean
def remark_nnlo_precision : String :=
  "NNLO precision: sin2W at -0.7 ppm (NNLO), M_W at -0.4 ppm (NLO), " ++
  "alpha_s at +43 ppm (NLO). W_3(4)=5 is universal NLO modulus."
```
