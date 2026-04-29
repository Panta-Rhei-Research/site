---
{
  "projection_kind": "taulib_declaration",
  "title": "higgs_as_holonomy",
  "permalink": "/verify/taulib/docs/book-iv-strong-gap-meta-theorem/higgs-as-holonomy/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Strong.GapMetaTheorem`.",
  "declaration_id": "TauLib.BookIV.Strong.GapMetaTheorem::higgs_as_holonomy",
  "declaration_slug": "higgs-as-holonomy",
  "kind": "def",
  "name": "higgs_as_holonomy",
  "module_name": "TauLib.BookIV.Strong.GapMetaTheorem",
  "module_url": "/verify/taulib/docs/book-iv-strong-gap-meta-theorem/",
  "source_line_start": 274,
  "source_line_end": 276,
  "registry_ids": [
    "IV.P99"
  ],
  "related_registry_items": [
    {
      "id": "IV.P99",
      "title": "Higgs sector as τ-holonomy sector",
      "url": "/registry/object/IV.P99/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/GapMetaTheorem.lean#L274-L276",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Strong.GapMetaTheorem",
        "url": "/verify/taulib/docs/book-iv-strong-gap-meta-theorem/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/GapMetaTheorem.lean#L274-L276",
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

- Module: [TauLib.BookIV.Strong.GapMetaTheorem](/verify/taulib/docs/book-iv-strong-gap-meta-theorem/)
- Source path: [`TauLib/BookIV/Strong/GapMetaTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/GapMetaTheorem.lean#L274-L276)
- Source range: L274-L276
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.P99` — Higgs sector as τ-holonomy sector

## Immediate Comment / Docstring

```lean
/-- [IV.P99] The Higgs sector as a tau-holonomy sector. -/
```

## Source Excerpt

```lean
def higgs_as_holonomy : HolonomySector where
  sector := .Omega
  activation_depth := 2
```
