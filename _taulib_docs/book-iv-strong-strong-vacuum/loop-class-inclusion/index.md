---
{
  "projection_kind": "taulib_declaration",
  "title": "LoopClassInclusion",
  "permalink": "/verify/taulib/docs/book-iv-strong-strong-vacuum/loop-class-inclusion/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.StrongVacuum`.",
  "declaration_id": "TauLib.BookIV.Strong.StrongVacuum::LoopClassInclusion",
  "declaration_slug": "loop-class-inclusion",
  "kind": "structure",
  "name": "LoopClassInclusion",
  "module_name": "TauLib.BookIV.Strong.StrongVacuum",
  "module_url": "/verify/taulib/docs/book-iv-strong-strong-vacuum/",
  "source_line_start": 143,
  "source_line_end": 150,
  "registry_ids": [
    "IV.P82"
  ],
  "related_registry_items": [
    {
      "id": "IV.P82",
      "title": "Loop class inclusion",
      "url": "/registry/object/IV.P82/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongVacuum.lean#L143-L150",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongVacuum.lean#L143-L150",
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
- Source path: [`TauLib/BookIV/Strong/StrongVacuum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongVacuum.lean#L143-L150)
- Source range: L143-L150
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P82` — Loop class inclusion

## Immediate Comment / Docstring

```lean
/-- [IV.P82] Refinement embedding induces injection L_s[n] into L_s[n+1]. -/
```

## Source Excerpt

```lean
structure LoopClassInclusion where
  /-- Injection under refinement. -/
  injective : Bool := true
  /-- No loops disappear. -/
  no_disappearance : Bool := true
  /-- New loops may appear. -/
  new_loops_possible : Bool := true
  deriving Repr
```
