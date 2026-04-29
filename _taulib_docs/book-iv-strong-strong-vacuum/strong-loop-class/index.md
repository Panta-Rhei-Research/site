---
{
  "projection_kind": "taulib_declaration",
  "title": "StrongLoopClass",
  "permalink": "/verify/taulib/docs/book-iv-strong-strong-vacuum/strong-loop-class/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.StrongVacuum`.",
  "declaration_id": "TauLib.BookIV.Strong.StrongVacuum::StrongLoopClass",
  "declaration_slug": "strong-loop-class",
  "kind": "structure",
  "name": "StrongLoopClass",
  "module_name": "TauLib.BookIV.Strong.StrongVacuum",
  "module_url": "/verify/taulib/docs/book-iv-strong-strong-vacuum/",
  "source_line_start": 116,
  "source_line_end": 127,
  "registry_ids": [
    "IV.D145"
  ],
  "related_registry_items": [
    {
      "id": "IV.D145",
      "title": "Strong loop class",
      "url": "/registry/object/IV.D145/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongVacuum.lean#L116-L127",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongVacuum.lean#L116-L127",
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
- Source path: [`TauLib/BookIV/Strong/StrongVacuum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongVacuum.lean#L116-L127)
- Source range: L116-L127
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D145` — Strong loop class

## Immediate Comment / Docstring

```lean
/-- [IV.D145] The strong loop class L_s[n] at primorial stage n:
    the subset of loops in H_partial[n] satisfying eta-support,
    gap-class membership, and nonzero contraction defect conditions. -/
```

## Source Excerpt

```lean
structure StrongLoopClass where
  /-- Primorial stage. -/
  stage : Nat
  /-- Minimum stage for nonemptiness. -/
  min_stage : Nat := 3
  /-- Number of loops (finite at each stage). -/
  loop_count : Nat
  /-- Loops have eta-support. -/
  eta_supported : Bool := true
  /-- Loops are gap-class members. -/
  gap_class : Bool := true
  deriving Repr
```
