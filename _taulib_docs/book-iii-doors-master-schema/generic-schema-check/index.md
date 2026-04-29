---
{
  "projection_kind": "taulib_declaration",
  "title": "generic_schema_check",
  "permalink": "/verify/taulib/docs/book-iii-doors-master-schema/generic-schema-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Doors.MasterSchema`.",
  "declaration_id": "TauLib.BookIII.Doors.MasterSchema::generic_schema_check",
  "declaration_slug": "generic-schema-check",
  "kind": "def",
  "name": "generic_schema_check",
  "module_name": "TauLib.BookIII.Doors.MasterSchema",
  "module_url": "/verify/taulib/docs/book-iii-doors-master-schema/",
  "source_line_start": 100,
  "source_line_end": 102,
  "registry_ids": [
    "III.T23"
  ],
  "related_registry_items": [
    {
      "id": "III.T23",
      "title": "Master Schema Theorem",
      "url": "/registry/object/III.T23/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/MasterSchema.lean#L100-L102",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Doors.MasterSchema",
        "url": "/verify/taulib/docs/book-iii-doors-master-schema/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/MasterSchema.lean#L100-L102",
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

- Module: [TauLib.BookIII.Doors.MasterSchema](/verify/taulib/docs/book-iii-doors-master-schema/)
- Source path: [`TauLib/BookIII/Doors/MasterSchema.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/MasterSchema.lean#L100-L102)
- Source range: L100-L102
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T23` — Master Schema Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T23] Generic E₁/E₂ schema: uses the full MD infrastructure
    at the appropriate enrichment level. The specific content for NS, YM,
    Hodge, BSD, Langlands, P vs NP is developed in Parts V-VII.
    At this level we verify the template is available. -/
```

## Source Excerpt

```lean
def generic_schema_check (bound db : TauIdx) : Bool :=
  -- The MD template works at every enrichment level
  mutual_det_check bound db
```
