---
{
  "projection_kind": "taulib_declaration",
  "title": "VacuumExistenceUniqueness",
  "permalink": "/verify/taulib/docs/book-iv-strong-strong-vacuum/vacuum-existence-uniqueness/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.StrongVacuum`.",
  "declaration_id": "TauLib.BookIV.Strong.StrongVacuum::VacuumExistenceUniqueness",
  "declaration_slug": "vacuum-existence-uniqueness",
  "kind": "structure",
  "name": "VacuumExistenceUniqueness",
  "module_name": "TauLib.BookIV.Strong.StrongVacuum",
  "module_url": "/verify/taulib/docs/book-iv-strong-strong-vacuum/",
  "source_line_start": 247,
  "source_line_end": 254,
  "registry_ids": [
    "IV.P85"
  ],
  "related_registry_items": [
    {
      "id": "IV.P85",
      "title": "Existence and uniqueness at each stage",
      "url": "/registry/object/IV.P85/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongVacuum.lean#L247-L254",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongVacuum.lean#L247-L254",
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
- Source path: [`TauLib/BookIV/Strong/StrongVacuum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongVacuum.lean#L247-L254)
- Source range: L247-L254
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P85` — Existence and uniqueness at each stage

## Immediate Comment / Docstring

```lean
/-- [IV.P85] Existence and uniqueness at each stage:
    exists (finite nonempty domain), unique (NFMin), computable. -/
```

## Source Excerpt

```lean
structure VacuumExistenceUniqueness where
  /-- Existence from finiteness + nonemptiness. -/
  exists_ : Bool := true
  /-- Uniqueness from NFMin tie-breaking. -/
  unique : Bool := true
  /-- Computable from boundary holonomy data. -/
  computable : Bool := true
  deriving Repr
```
