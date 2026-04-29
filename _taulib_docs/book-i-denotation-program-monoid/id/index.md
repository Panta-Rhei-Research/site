---
{
  "projection_kind": "taulib_declaration",
  "title": "NormalForm.id",
  "permalink": "/verify/taulib/docs/book-i-denotation-program-monoid/id/",
  "summary_short": "`def` declaration in `TauLib.BookI.Denotation.ProgramMonoid`.",
  "declaration_id": "TauLib.BookI.Denotation.ProgramMonoid::NormalForm.id",
  "declaration_slug": "id",
  "kind": "def",
  "name": "NormalForm.id",
  "module_name": "TauLib.BookI.Denotation.ProgramMonoid",
  "module_url": "/verify/taulib/docs/book-i-denotation-program-monoid/",
  "source_line_start": 71,
  "source_line_end": 73,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/ProgramMonoid.lean#L71-L73",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/ProgramMonoid.lean#L71-L73",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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
- Source path: [`TauLib/BookI/Denotation/ProgramMonoid.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/ProgramMonoid.lean#L71-L73)
- Source range: L71-L73
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The identity normal form. -/
```

## Source Excerpt

```lean
def NormalForm.id : NormalForm where
  seedMap := fun g => g
  rhoCount := 0
```
