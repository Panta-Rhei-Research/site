---
{
  "projection_kind": "taulib_declaration",
  "title": "compose_assoc",
  "permalink": "/corpus/taulib/docs/book-i-denotation-program-monoid/compose-assoc/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Denotation.ProgramMonoid`.",
  "declaration_id": "TauLib.BookI.Denotation.ProgramMonoid::compose_assoc",
  "declaration_slug": "compose-assoc",
  "kind": "theorem",
  "name": "compose_assoc",
  "module_name": "TauLib.BookI.Denotation.ProgramMonoid",
  "module_url": "/corpus/taulib/docs/book-i-denotation-program-monoid/",
  "source_line_start": 93,
  "source_line_end": 95,
  "registry_ids": [
    "I.T03"
  ],
  "related_registry_items": [
    {
      "id": "I.T03",
      "title": "Composition Associativity",
      "url": "/registry/object/I.T03/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/ProgramMonoid.lean#L93-L95",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Denotation.ProgramMonoid",
        "url": "/corpus/taulib/docs/book-i-denotation-program-monoid/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/ProgramMonoid.lean#L93-L95",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookI.Denotation.ProgramMonoid](/corpus/taulib/docs/book-i-denotation-program-monoid/)
- Source path: [`TauLib/BookI/Denotation/ProgramMonoid.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/ProgramMonoid.lean#L93-L95)
- Source range: L93-L95
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `I.T03` — Composition Associativity

## Immediate Comment / Docstring

```lean
/-- [I.T03] Composition is associative. -/
```

## Source Excerpt

```lean
theorem compose_assoc (p q r : Program) :
    Program.compose (Program.compose p q) r = Program.compose p (Program.compose q r) := by
  simp [Program.compose, List.append_assoc]
```
