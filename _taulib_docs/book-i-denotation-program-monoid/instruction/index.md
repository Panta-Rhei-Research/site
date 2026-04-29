---
{
  "projection_kind": "taulib_declaration",
  "title": "Instruction",
  "permalink": "/verify/taulib/docs/book-i-denotation-program-monoid/instruction/",
  "summary_short": "`inductive` declaration in `TauLib.BookI.Denotation.ProgramMonoid`.",
  "declaration_id": "TauLib.BookI.Denotation.ProgramMonoid::Instruction",
  "declaration_slug": "instruction",
  "kind": "inductive",
  "name": "Instruction",
  "module_name": "TauLib.BookI.Denotation.ProgramMonoid",
  "module_url": "/verify/taulib/docs/book-i-denotation-program-monoid/",
  "source_line_start": 37,
  "source_line_end": 43,
  "registry_ids": [
    "I.D14"
  ],
  "related_registry_items": [
    {
      "id": "I.D14",
      "title": "Program Monoid",
      "url": "/registry/object/I.D14/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/ProgramMonoid.lean#L37-L43",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Denotation.ProgramMonoid",
        "url": "/verify/taulib/docs/book-i-denotation-program-monoid/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/ProgramMonoid.lean#L37-L43",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
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

- Module: [TauLib.BookI.Denotation.ProgramMonoid](/verify/taulib/docs/book-i-denotation-program-monoid/)
- Source path: [`TauLib/BookI/Denotation/ProgramMonoid.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/ProgramMonoid.lean#L37-L43)
- Source range: L37-L43
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `I.D14` — Program Monoid

## Immediate Comment / Docstring

```lean
/-- [I.D14] The two instruction types. -/
```

## Source Excerpt

```lean
inductive Instruction : Type where
  | rho_inst : Instruction
  | sigma_inst : Generator → Generator → Instruction
  deriving DecidableEq, Repr

/-- A program is a finite sequence of instructions. -/
abbrev Program := List Instruction
```
