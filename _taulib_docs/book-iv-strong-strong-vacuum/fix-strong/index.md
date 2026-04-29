---
{
  "projection_kind": "taulib_declaration",
  "title": "FixStrong",
  "permalink": "/verify/taulib/docs/book-iv-strong-strong-vacuum/fix-strong/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.StrongVacuum`.",
  "declaration_id": "TauLib.BookIV.Strong.StrongVacuum::FixStrong",
  "declaration_slug": "fix-strong",
  "kind": "structure",
  "name": "FixStrong",
  "module_name": "TauLib.BookIV.Strong.StrongVacuum",
  "module_url": "/verify/taulib/docs/book-iv-strong-strong-vacuum/",
  "source_line_start": 324,
  "source_line_end": 333,
  "registry_ids": [
    "IV.D152"
  ],
  "related_registry_items": [
    {
      "id": "IV.D152",
      "title": "Fix(s)",
      "url": "/registry/object/IV.D152/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongVacuum.lean#L324-L333",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongVacuum.lean#L324-L333",
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
- Source path: [`TauLib/BookIV/Strong/StrongVacuum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongVacuum.lean#L324-L333)
- Source range: L324-L333
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D152` — Fix(s)

## Immediate Comment / Docstring

```lean
/-- [IV.D152] Fix(s)[n]: fixed-point subobject of HolEnd_tau(s)[n]
    consisting of endomorphisms commuting with the strong vacuum. -/
```

## Source Excerpt

```lean
structure FixStrong where
  /-- Stage n. -/
  stage : Nat
  /-- Commutes with strong vacuum. -/
  commutes_with_vacuum : Bool := true
  /-- Contains the identity. -/
  contains_id : Bool := true
  /-- Is a subalgebra. -/
  is_subalgebra : Bool := true
  deriving Repr
```
