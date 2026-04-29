---
{
  "projection_kind": "taulib_declaration",
  "title": "VirusNoDist",
  "permalink": "/verify/taulib/docs/book-vi-sectors-absence/virus-no-dist/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Sectors.Absence`.",
  "declaration_id": "TauLib.BookVI.Sectors.Absence::VirusNoDist",
  "declaration_slug": "virus-no-dist",
  "kind": "structure",
  "name": "VirusNoDist",
  "module_name": "TauLib.BookVI.Sectors.Absence",
  "module_url": "/verify/taulib/docs/book-vi-sectors-absence/",
  "source_line_start": 37,
  "source_line_end": 41,
  "registry_ids": [
    "VI.T15"
  ],
  "related_registry_items": [
    {
      "id": "VI.T15",
      "title": "Virus NoDist",
      "url": "/registry/object/VI.T15/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Sectors/Absence.lean#L37-L41",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Sectors/Absence.lean#L37-L41",
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
- Source path: [`TauLib/BookVI/Sectors/Absence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Sectors/Absence.lean#L37-L41)
- Source range: L37-L41
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.T15` — Virus NoDist

## Immediate Comment / Docstring

```lean
/-- [VI.T15] Virus NoDist: fails 3/5 distinction conditions outside host. -/
```

## Source Excerpt

```lean
structure VirusNoDist where
  conditions_failed : Nat
  three_fail : conditions_failed = 3
  host_dependent : Bool := true
  deriving Repr
```
