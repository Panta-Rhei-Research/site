---
{
  "projection_kind": "taulib_declaration",
  "title": "LiftProperties",
  "permalink": "/verify/taulib/docs/book-iv-strong-strong-vacuum/lift-properties/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.StrongVacuum`.",
  "declaration_id": "TauLib.BookIV.Strong.StrongVacuum::LiftProperties",
  "declaration_slug": "lift-properties",
  "kind": "structure",
  "name": "LiftProperties",
  "module_name": "TauLib.BookIV.Strong.StrongVacuum",
  "module_url": "/verify/taulib/docs/book-iv-strong-strong-vacuum/",
  "source_line_start": 371,
  "source_line_end": 380,
  "registry_ids": [
    "IV.P87"
  ],
  "related_registry_items": [
    {
      "id": "IV.P87",
      "title": "Properties of the canonical strong lift",
      "url": "/registry/object/IV.P87/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongVacuum.lean#L371-L380",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Strong.StrongVacuum",
        "url": "/verify/taulib/docs/book-iv-strong-strong-vacuum/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongVacuum.lean#L371-L380",
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

- Module: [TauLib.BookIV.Strong.StrongVacuum](/verify/taulib/docs/book-iv-strong-strong-vacuum/)
- Source path: [`TauLib/BookIV/Strong/StrongVacuum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongVacuum.lean#L371-L380)
- Source range: L371-L380
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P87` — Properties of the canonical strong lift

## Immediate Comment / Docstring

```lean
/-- [IV.P87] Properties of the canonical strong lift:
    exists for all n >= 3, unique, truncation coherent, computable. -/
```

## Source Excerpt

```lean
structure LiftProperties where
  /-- Exists for all stages >= 3. -/
  exists_all_stages : Bool := true
  /-- Unique after NF tie-breaking. -/
  unique : Bool := true
  /-- Truncation coherent: Lift_{s,n+1}|_n = Lift_{s,n}. -/
  truncation_coherent : Bool := true
  /-- Computable from boundary holonomy data. -/
  computable : Bool := true
  deriving Repr
```
