---
{
  "projection_kind": "taulib_declaration",
  "title": "exec_nil",
  "permalink": "/corpus/taulib/docs/book-i-denotation-program-monoid/exec-nil/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Denotation.ProgramMonoid`.",
  "declaration_id": "TauLib.BookI.Denotation.ProgramMonoid::exec_nil",
  "declaration_slug": "exec-nil",
  "kind": "theorem",
  "name": "exec_nil",
  "module_name": "TauLib.BookI.Denotation.ProgramMonoid",
  "module_url": "/corpus/taulib/docs/book-i-denotation-program-monoid/",
  "source_line_start": 117,
  "source_line_end": 118,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/ProgramMonoid.lean#L117-L118",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/ProgramMonoid.lean#L117-L118",
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
- Source path: [`TauLib/BookI/Denotation/ProgramMonoid.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/ProgramMonoid.lean#L117-L118)
- Source range: L117-L118
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The empty program is the identity. -/
```

## Source Excerpt

```lean
theorem exec_nil (x : TauObj) : execProgram [] x = x := by
  simp [execProgram]
```
