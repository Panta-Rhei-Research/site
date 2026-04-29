---
{
  "projection_kind": "taulib_declaration",
  "title": "ns_level",
  "permalink": "/verify/taulib/docs/book-iii-doors-master-schema/ns-level/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Doors.MasterSchema`.",
  "declaration_id": "TauLib.BookIII.Doors.MasterSchema::ns_level",
  "declaration_slug": "ns-level",
  "kind": "theorem",
  "name": "ns_level",
  "module_name": "TauLib.BookIII.Doors.MasterSchema",
  "module_url": "/verify/taulib/docs/book-iii-doors-master-schema/",
  "source_line_start": 185,
  "source_line_end": 185,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/MasterSchema.lean#L185-L185",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/MasterSchema.lean#L185-L185",
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

- Module: [TauLib.BookIII.Doors.MasterSchema](/verify/taulib/docs/book-iii-doors-master-schema/)
- Source path: [`TauLib/BookIII/Doors/MasterSchema.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/MasterSchema.lean#L185-L185)
- Source range: L185-L185
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T23` — Master Schema Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T23] Structural: NS is at E₁. -/
```

## Source Excerpt

```lean
theorem ns_level : problem_level .NS = .E1 := rfl
```
