---
{
  "projection_kind": "taulib_declaration",
  "title": "silent_count",
  "permalink": "/verify/taulib/docs/book-iv-sectors-mode-census/silent-count/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Sectors.ModeCensus`.",
  "declaration_id": "TauLib.BookIV.Sectors.ModeCensus::silent_count",
  "declaration_slug": "silent-count",
  "kind": "theorem",
  "name": "silent_count",
  "module_name": "TauLib.BookIV.Sectors.ModeCensus",
  "module_url": "/verify/taulib/docs/book-iv-sectors-mode-census/",
  "source_line_start": 117,
  "source_line_end": 117,
  "registry_ids": [
    "IV.T16"
  ],
  "related_registry_items": [
    {
      "id": "IV.T16",
      "title": "CR Parity Constraint",
      "url": "/registry/object/IV.T16/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/ModeCensus.lean#L117-L117",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/ModeCensus.lean#L117-L117",
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
- Source path: [`TauLib/BookIV/Sectors/ModeCensus.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/ModeCensus.lean#L117-L117)
- Source range: L117-L117
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T16` — CR Parity Constraint

## Immediate Comment / Docstring

```lean
/-- [IV.T16] Number of EM-silent modes = 4. -/
```

## Source Excerpt

```lean
theorem silent_count : silentModes.length = 4 := by native_decide
```
