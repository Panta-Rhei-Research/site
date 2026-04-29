---
{
  "projection_kind": "taulib_declaration",
  "title": "NoDist",
  "permalink": "/verify/taulib/docs/book-vi-sectors-absence/no-dist/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Sectors.Absence`.",
  "declaration_id": "TauLib.BookVI.Sectors.Absence::NoDist",
  "declaration_slug": "no-dist",
  "kind": "structure",
  "name": "NoDist",
  "module_name": "TauLib.BookVI.Sectors.Absence",
  "module_url": "/verify/taulib/docs/book-vi-sectors-absence/",
  "source_line_start": 24,
  "source_line_end": 27,
  "registry_ids": [
    "VI.D21"
  ],
  "related_registry_items": [
    {
      "id": "VI.D21",
      "title": "NoDist",
      "url": "/registry/object/VI.D21/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Sectors/Absence.lean#L24-L27",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Sectors.Absence",
        "url": "/verify/taulib/docs/book-vi-sectors-absence/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Sectors/Absence.lean#L24-L27",
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

- Module: [TauLib.BookVI.Sectors.Absence](/verify/taulib/docs/book-vi-sectors-absence/)
- Source path: [`TauLib/BookVI/Sectors/Absence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Sectors/Absence.lean#L24-L27)
- Source range: L24-L27
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D21` — NoDist

## Immediate Comment / Docstring

```lean
/-- [VI.D21] NoDist: system fails τ-Distinction. -/
```

## Source Excerpt

```lean
structure NoDist where
  conditions_failed : Nat
  at_least_one : conditions_failed ≥ 1
  deriving Repr
```
