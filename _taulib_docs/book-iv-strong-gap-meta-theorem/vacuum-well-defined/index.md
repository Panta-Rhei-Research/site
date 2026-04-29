---
{
  "projection_kind": "taulib_declaration",
  "title": "VacuumWellDefined",
  "permalink": "/verify/taulib/docs/book-iv-strong-gap-meta-theorem/vacuum-well-defined/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.GapMetaTheorem`.",
  "declaration_id": "TauLib.BookIV.Strong.GapMetaTheorem::VacuumWellDefined",
  "declaration_slug": "vacuum-well-defined",
  "kind": "structure",
  "name": "VacuumWellDefined",
  "module_name": "TauLib.BookIV.Strong.GapMetaTheorem",
  "module_url": "/verify/taulib/docs/book-iv-strong-gap-meta-theorem/",
  "source_line_start": 94,
  "source_line_end": 101,
  "registry_ids": [
    "IV.P97"
  ],
  "related_registry_items": [
    {
      "id": "IV.P97",
      "title": "Well-definedness",
      "url": "/registry/object/IV.P97/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/GapMetaTheorem.lean#L94-L101",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Strong.GapMetaTheorem",
        "url": "/verify/taulib/docs/book-iv-strong-gap-meta-theorem/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/GapMetaTheorem.lean#L94-L101",
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

- Module: [TauLib.BookIV.Strong.GapMetaTheorem](/verify/taulib/docs/book-iv-strong-gap-meta-theorem/)
- Source path: [`TauLib/BookIV/Strong/GapMetaTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/GapMetaTheorem.lean#L94-L101)
- Source range: L94-L101
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P97` — Well-definedness

## Immediate Comment / Docstring

```lean
/-- [IV.P97] Well-definedness: vacuum exists (finite nonempty),
    is unique (lex total order), and computable (exhaustive search). -/
```

## Source Excerpt

```lean
structure VacuumWellDefined where
  /-- Existence. -/
  exists_ : Bool := true
  /-- Uniqueness. -/
  unique : Bool := true
  /-- Computability. -/
  computable : Bool := true
  deriving Repr
```
