---
{
  "projection_kind": "taulib_declaration",
  "title": "sector_decomp_5",
  "permalink": "/verify/taulib/docs/book-iii-sectors-decomposition/sector-decomp-5/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Sectors.Decomposition`.",
  "declaration_id": "TauLib.BookIII.Sectors.Decomposition::sector_decomp_5",
  "declaration_slug": "sector-decomp-5",
  "kind": "theorem",
  "name": "sector_decomp_5",
  "module_name": "TauLib.BookIII.Sectors.Decomposition",
  "module_url": "/verify/taulib/docs/book-iii-sectors-decomposition/",
  "source_line_start": 182,
  "source_line_end": 183,
  "registry_ids": [
    "III.D13"
  ],
  "related_registry_items": [
    {
      "id": "III.D13",
      "title": "4+1 Sector Decomposition",
      "url": "/registry/object/III.D13/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/Decomposition.lean#L182-L183",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Sectors.Decomposition",
        "url": "/verify/taulib/docs/book-iii-sectors-decomposition/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/Decomposition.lean#L182-L183",
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

- Module: [TauLib.BookIII.Sectors.Decomposition](/verify/taulib/docs/book-iii-sectors-decomposition/)
- Source path: [`TauLib/BookIII/Sectors/Decomposition.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/Decomposition.lean#L182-L183)
- Source range: L182-L183
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.D13` — 4+1 Sector Decomposition

## Immediate Comment / Docstring

```lean
-- ============================================================
-- FORMAL VERIFICATION (native_decide)
-- ============================================================

-- Sector decomposition [III.D13]
```

## Source Excerpt

```lean
theorem sector_decomp_5 :
    sector_decomposition_check 5 = true := by native_decide
```
