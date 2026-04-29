---
{
  "projection_kind": "taulib_declaration",
  "title": "canonical_nu_decoupling",
  "permalink": "/verify/taulib/docs/book-v-temporal-boundary-data/canonical-nu-decoupling/",
  "summary_short": "`def` declaration in `TauLib.BookV.Temporal.BoundaryData`.",
  "declaration_id": "TauLib.BookV.Temporal.BoundaryData::canonical_nu_decoupling",
  "declaration_slug": "canonical-nu-decoupling",
  "kind": "def",
  "name": "canonical_nu_decoupling",
  "module_name": "TauLib.BookV.Temporal.BoundaryData",
  "module_url": "/verify/taulib/docs/book-v-temporal-boundary-data/",
  "source_line_start": 183,
  "source_line_end": 185,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/BoundaryData.lean#L183-L185",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Temporal.BoundaryData",
        "url": "/verify/taulib/docs/book-v-temporal-boundary-data/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/BoundaryData.lean#L183-L185",
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

- Module: [TauLib.BookV.Temporal.BoundaryData](/verify/taulib/docs/book-v-temporal-boundary-data/)
- Source path: [`TauLib/BookV/Temporal/BoundaryData.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/BoundaryData.lean#L183-L185)
- Source range: L183-L185
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Canonical neutrino decoupling depth. -/
```

## Source Excerpt

```lean
def canonical_nu_decoupling : NeutrinoDecoupling where
  depth := 200
  depth_pos := by omega
```
