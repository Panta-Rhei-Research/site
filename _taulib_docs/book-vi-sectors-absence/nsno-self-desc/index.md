---
{
  "projection_kind": "taulib_declaration",
  "title": "NSNoSelfDesc",
  "permalink": "/verify/taulib/docs/book-vi-sectors-absence/nsno-self-desc/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Sectors.Absence`.",
  "declaration_id": "TauLib.BookVI.Sectors.Absence::NSNoSelfDesc",
  "declaration_slug": "nsno-self-desc",
  "kind": "structure",
  "name": "NSNoSelfDesc",
  "module_name": "TauLib.BookVI.Sectors.Absence",
  "module_url": "/verify/taulib/docs/book-vi-sectors-absence/",
  "source_line_start": 53,
  "source_line_end": 57,
  "registry_ids": [
    "VI.L06"
  ],
  "related_registry_items": [
    {
      "id": "VI.L06",
      "title": "NS-NoSelfDesc",
      "url": "/registry/object/VI.L06/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Sectors/Absence.lean#L53-L57",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Sectors/Absence.lean#L53-L57",
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
- Source path: [`TauLib/BookVI/Sectors/Absence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Sectors/Absence.lean#L53-L57)
- Source range: L53-L57
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.L06` — NS-NoSelfDesc

## Immediate Comment / Docstring

```lean
/-- [VI.L06] NS-NoSelfDesc: 5/5 distinction, fails SelfDesc. -/
```

## Source Excerpt

```lean
structure NSNoSelfDesc where
  distinction_passed : Nat
  all_five : distinction_passed = 5
  selfdesc_fails : Bool := true
  deriving Repr
```
