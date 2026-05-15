---
{
  "projection_kind": "taulib_declaration",
  "title": "MasterSchemaEntry",
  "permalink": "/corpus/taulib/docs/book-iii-doors-master-schema/master-schema-entry/",
  "summary_short": "`structure` declaration in `TauLib.BookIII.Doors.MasterSchema`.",
  "declaration_id": "TauLib.BookIII.Doors.MasterSchema::MasterSchemaEntry",
  "declaration_slug": "master-schema-entry",
  "kind": "structure",
  "name": "MasterSchemaEntry",
  "module_name": "TauLib.BookIII.Doors.MasterSchema",
  "module_url": "/corpus/taulib/docs/book-iii-doors-master-schema/",
  "source_line_start": 76,
  "source_line_end": 80,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/MasterSchema.lean#L76-L80",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Doors.MasterSchema",
        "url": "/corpus/taulib/docs/book-iii-doors-master-schema/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/MasterSchema.lean#L76-L80",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "role": "type/data schema",
      "status": "type/data schema"
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

- Module: [TauLib.BookIII.Doors.MasterSchema](/corpus/taulib/docs/book-iii-doors-master-schema/)
- Source path: [`TauLib/BookIII/Doors/MasterSchema.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/MasterSchema.lean#L76-L80)
- Source range: L76-L80
- Kind: `structure`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- `III.T23` — Master Schema Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T23] Master Schema entry: each problem has a Mutual Determination
    instance (B ↔ I ↔ S) at its enrichment level. The finite check verifies
    that the MD infrastructure is available at the required level. -/
```

## Source Excerpt

```lean
structure MasterSchemaEntry where
  problem : MillenniumProblem
  level : EnrLevel
  part : TauIdx
  md_check : TauIdx → TauIdx → Bool  -- the MD check for this problem
```
