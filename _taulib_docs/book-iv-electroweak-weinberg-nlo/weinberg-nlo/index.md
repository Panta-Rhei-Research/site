---
{
  "projection_kind": "taulib_declaration",
  "title": "WeinbergNLO",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-weinberg-nlo/weinberg-nlo/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.WeinbergNLO`.",
  "declaration_id": "TauLib.BookIV.Electroweak.WeinbergNLO::WeinbergNLO",
  "declaration_slug": "weinberg-nlo",
  "kind": "structure",
  "name": "WeinbergNLO",
  "module_name": "TauLib.BookIV.Electroweak.WeinbergNLO",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-weinberg-nlo/",
  "source_line_start": 50,
  "source_line_end": 56,
  "registry_ids": [
    "IV.D334"
  ],
  "related_registry_items": [
    {
      "id": "IV.D334",
      "title": "NLO Weinberg Correction",
      "url": "/registry/object/IV.D334/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L50-L56",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L50-L56",
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

- Module: [TauLib.BookIV.Electroweak.WeinbergNLO](/verify/taulib/docs/book-iv-electroweak-weinberg-nlo/)
- Source path: [`TauLib/BookIV/Electroweak/WeinbergNLO.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L50-L56)
- Source range: L50-L56
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D334` — NLO Weinberg Correction

## Immediate Comment / Docstring

```lean
/-- [IV.D334] The NLO Weinberg correction packages the CF window data.
    - nlo_num = W₃(4) = 5 (numerator of 5/7)
    - nlo_den = W₃(3) − 2·W₃(4) = 7 (denominator of 5/7)
    - nlo_exp = 3 = a₄ = dim(τ³) (exponent of ι in NLO term) -/
```

## Source Excerpt

```lean
structure WeinbergNLO where
  nlo_num : Nat
  nlo_den : Nat
  nlo_exp : Nat
  hnum : nlo_num = windowSum cf_head 3 4
  hden : nlo_den = windowSum cf_head 3 3 - 2 * windowSum cf_head 3 4
  hexp : nlo_exp = cf_head.getD 4 0
```
