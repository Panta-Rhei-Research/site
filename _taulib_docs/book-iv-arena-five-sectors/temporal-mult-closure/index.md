---
{
  "projection_kind": "taulib_declaration",
  "title": "temporal_mult_closure",
  "permalink": "/verify/taulib/docs/book-iv-arena-five-sectors/temporal-mult-closure/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Arena.FiveSectors`.",
  "declaration_id": "TauLib.BookIV.Arena.FiveSectors::temporal_mult_closure",
  "declaration_slug": "temporal-mult-closure",
  "kind": "theorem",
  "name": "temporal_mult_closure",
  "module_name": "TauLib.BookIV.Arena.FiveSectors",
  "module_url": "/verify/taulib/docs/book-iv-arena-five-sectors/",
  "source_line_start": 98,
  "source_line_end": 101,
  "registry_ids": [
    "IV.P154"
  ],
  "related_registry_items": [
    {
      "id": "IV.P154",
      "title": "Temporal Multiplicative Closure",
      "url": "/registry/object/IV.P154/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/FiveSectors.lean#L98-L101",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Arena.FiveSectors",
        "url": "/verify/taulib/docs/book-iv-arena-five-sectors/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/FiveSectors.lean#L98-L101",
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

- Module: [TauLib.BookIV.Arena.FiveSectors](/verify/taulib/docs/book-iv-arena-five-sectors/)
- Source path: [`TauLib/BookIV/Arena/FiveSectors.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/FiveSectors.lean#L98-L101)
- Source range: L98-L101
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.P154` — Temporal Multiplicative Closure

## Immediate Comment / Docstring

```lean
/-- [IV.P154] Temporal multiplicative closure: κ(A)·κ(D) < 1/4 (strict AM-GM).
    Since κ(A) + κ(D) = 1 and κ(A) ≠ κ(D), strict inequality holds. -/
```

## Source Excerpt

```lean
theorem temporal_mult_closure :
    kappa_AD.numer * (kappa_AA.denom * kappa_DD.denom) =
    kappa_AA.numer * kappa_DD.numer * kappa_AD.denom :=
  Tau.BookIV.Sectors.temporal_multiplicative
```
