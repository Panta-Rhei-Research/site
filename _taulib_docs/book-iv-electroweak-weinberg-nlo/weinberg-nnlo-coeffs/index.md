---
{
  "projection_kind": "taulib_declaration",
  "title": "weinberg_nnlo_coeffs",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-weinberg-nlo/weinberg-nnlo-coeffs/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Electroweak.WeinbergNLO`.",
  "declaration_id": "TauLib.BookIV.Electroweak.WeinbergNLO::weinberg_nnlo_coeffs",
  "declaration_slug": "weinberg-nnlo-coeffs",
  "kind": "def",
  "name": "weinberg_nnlo_coeffs",
  "module_name": "TauLib.BookIV.Electroweak.WeinbergNLO",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-weinberg-nlo/",
  "source_line_start": 223,
  "source_line_end": 224,
  "registry_ids": [
    "IV.D337"
  ],
  "related_registry_items": [
    {
      "id": "IV.D337",
      "title": "sin²θ_W NNLO Formula",
      "url": "/registry/object/IV.D337/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L223-L224",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L223-L224",
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
- Source path: [`TauLib/BookIV/Electroweak/WeinbergNLO.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L223-L224)
- Source range: L223-L224
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.D337` — sin²θ_W NNLO Formula

## Immediate Comment / Docstring

```lean
/-- [IV.D337] NNLO Weinberg angle: ι(1−ι)·(1 + (5/7)·ι³ + (1/18)·ι⁶)
    at −0.7 ppm from PDG MS-bar 0.23122.
    Coefficients: NLO_num=5=W₃(4), NLO_den=7, NNLO_num=1, NNLO_den=18=W₄(3). -/
```

## Source Excerpt

```lean
def weinberg_nnlo_coeffs : Nat × Nat × Nat × Nat :=
  (5, 7, 1, 18)  -- (NLO_num, NLO_den, NNLO_num, NNLO_den)
```
