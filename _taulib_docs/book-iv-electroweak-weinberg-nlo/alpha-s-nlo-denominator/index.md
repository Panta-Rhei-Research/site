---
{
  "projection_kind": "taulib_declaration",
  "title": "alpha_s_nlo_denominator",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-weinberg-nlo/alpha-s-nlo-denominator/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.WeinbergNLO`.",
  "declaration_id": "TauLib.BookIV.Electroweak.WeinbergNLO::alpha_s_nlo_denominator",
  "declaration_slug": "alpha-s-nlo-denominator",
  "kind": "theorem",
  "name": "alpha_s_nlo_denominator",
  "module_name": "TauLib.BookIV.Electroweak.WeinbergNLO",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-weinberg-nlo/",
  "source_line_start": 262,
  "source_line_end": 263,
  "registry_ids": [
    "IV.D339"
  ],
  "related_registry_items": [
    {
      "id": "IV.D339",
      "title": "alpha_s NLO Formula",
      "url": "/registry/object/IV.D339/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L262-L263",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L262-L263",
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

- Module: [TauLib.BookIV.Electroweak.WeinbergNLO](/verify/taulib/docs/book-iv-electroweak-weinberg-nlo/)
- Source path: [`TauLib/BookIV/Electroweak/WeinbergNLO.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L262-L263)
- Source range: L262-L263
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.D339` — alpha_s NLO Formula

## Immediate Comment / Docstring

```lean
/-- [IV.D339] The α_s NLO denominator is W₃(4) = 5.
    Formula: α_s = 2κ(C;3)·(1 − ι²/W₃(4)).
    The SAME W₃(4) = 5 appears as denominator here (with negative sign). -/
```

## Source Excerpt

```lean
theorem alpha_s_nlo_denominator :
    windowSum cf_head 3 4 = 5 := w3_at_4
```
