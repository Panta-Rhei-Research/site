---
{
  "projection_kind": "taulib_declaration",
  "title": "charge_fraction_square",
  "permalink": "/verify/taulib/docs/book-iv-sectors-mode-census/charge-fraction-square/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Sectors.ModeCensus`.",
  "declaration_id": "TauLib.BookIV.Sectors.ModeCensus::charge_fraction_square",
  "declaration_slug": "charge-fraction-square",
  "kind": "theorem",
  "name": "charge_fraction_square",
  "module_name": "TauLib.BookIV.Sectors.ModeCensus",
  "module_url": "/verify/taulib/docs/book-iv-sectors-mode-census/",
  "source_line_start": 129,
  "source_line_end": 129,
  "registry_ids": [
    "IV.P08"
  ],
  "related_registry_items": [
    {
      "id": "IV.P08",
      "title": "Integrability Criterion",
      "url": "/registry/object/IV.P08/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/ModeCensus.lean#L129-L129",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Sectors.ModeCensus",
        "url": "/verify/taulib/docs/book-iv-sectors-mode-census/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/ModeCensus.lean#L129-L129",
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

- Module: [TauLib.BookIV.Sectors.ModeCensus](/verify/taulib/docs/book-iv-sectors-mode-census/)
- Source path: [`TauLib/BookIV/Sectors/ModeCensus.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/ModeCensus.lean#L129-L129)
- Source range: L129-L129
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.P08` — Integrability Criterion

## Immediate Comment / Docstring

```lean
/-- [IV.P08] The charge fraction 11/15 satisfies (11/15)² = 121/225.
    This is the coefficient in the tower formula α = (121/225)·ι_τ⁴. -/
```

## Source Excerpt

```lean
theorem charge_fraction_square : 11 * 11 = (121 : Nat) ∧ 15 * 15 = (225 : Nat) := by omega
```
