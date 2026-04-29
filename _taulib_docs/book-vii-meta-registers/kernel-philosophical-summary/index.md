---
{
  "projection_kind": "taulib_declaration",
  "title": "KernelPhilosophicalSummary",
  "permalink": "/verify/taulib/docs/book-vii-meta-registers/kernel-philosophical-summary/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Meta.Registers`.",
  "declaration_id": "TauLib.BookVII.Meta.Registers::KernelPhilosophicalSummary",
  "declaration_slug": "kernel-philosophical-summary",
  "kind": "structure",
  "name": "KernelPhilosophicalSummary",
  "module_name": "TauLib.BookVII.Meta.Registers",
  "module_url": "/verify/taulib/docs/book-vii-meta-registers/",
  "source_line_start": 576,
  "source_line_end": 583,
  "registry_ids": [
    "VII.D24"
  ],
  "related_registry_items": [
    {
      "id": "VII.D24",
      "title": "τ-Kernel Philosophical Summary",
      "url": "/registry/object/VII.D24/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L576-L583",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Meta.Registers",
        "url": "/verify/taulib/docs/book-vii-meta-registers/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L576-L583",
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

- Module: [TauLib.BookVII.Meta.Registers](/verify/taulib/docs/book-vii-meta-registers/)
- Source path: [`TauLib/BookVII/Meta/Registers.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L576-L583)
- Source range: L576-L583
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.D24` — τ-Kernel Philosophical Summary

## Immediate Comment / Docstring

```lean
/-- [VII.D24] τ-Kernel Philosophical Summary (ch17). The τ kernel as
    ontological foundation: 5 generators {α, π, π′, π″, ω} and
    7 axioms K0–K6 provide the complete structural basis.
    No external ontological commitments needed. -/
```

## Source Excerpt

```lean
structure KernelPhilosophicalSummary where
  /-- 5 generators. -/
  generator_count : Nat := 5
  /-- 7 axioms. -/
  axiom_count : Nat := 9
  /-- Ontologically self-sufficient. -/
  self_sufficient : Bool := true
  deriving Repr
```
