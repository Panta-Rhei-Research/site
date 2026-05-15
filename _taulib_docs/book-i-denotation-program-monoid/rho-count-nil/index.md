---
{
  "projection_kind": "taulib_declaration",
  "title": "rho_count_nil",
  "permalink": "/corpus/taulib/docs/book-i-denotation-program-monoid/rho-count-nil/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Denotation.ProgramMonoid`.",
  "declaration_id": "TauLib.BookI.Denotation.ProgramMonoid::rho_count_nil",
  "declaration_slug": "rho-count-nil",
  "kind": "theorem",
  "name": "rho_count_nil",
  "module_name": "TauLib.BookI.Denotation.ProgramMonoid",
  "module_url": "/corpus/taulib/docs/book-i-denotation-program-monoid/",
  "source_line_start": 152,
  "source_line_end": 154,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/ProgramMonoid.lean#L152-L154",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/ProgramMonoid.lean#L152-L154",
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
- Source path: [`TauLib/BookI/Denotation/ProgramMonoid.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/ProgramMonoid.lean#L152-L154)
- Source range: L152-L154
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The rho count of the empty program is 0. -/
```

## Source Excerpt

```lean
theorem rho_count_nil : countRho [] = 0 := rfl

end Tau.Denotation
```
