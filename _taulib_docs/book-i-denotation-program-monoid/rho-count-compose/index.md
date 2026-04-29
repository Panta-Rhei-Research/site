---
{
  "projection_kind": "taulib_declaration",
  "title": "rho_count_compose",
  "permalink": "/verify/taulib/docs/book-i-denotation-program-monoid/rho-count-compose/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Denotation.ProgramMonoid`.",
  "declaration_id": "TauLib.BookI.Denotation.ProgramMonoid::rho_count_compose",
  "declaration_slug": "rho-count-compose",
  "kind": "theorem",
  "name": "rho_count_compose",
  "module_name": "TauLib.BookI.Denotation.ProgramMonoid",
  "module_url": "/verify/taulib/docs/book-i-denotation-program-monoid/",
  "source_line_start": 136,
  "source_line_end": 149,
  "registry_ids": [
    "I.L02"
  ],
  "related_registry_items": [
    {
      "id": "I.L02",
      "title": "NF-Confluence",
      "url": "/registry/object/I.L02/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/ProgramMonoid.lean#L136-L149",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/ProgramMonoid.lean#L136-L149",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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
- Source path: [`TauLib/BookI/Denotation/ProgramMonoid.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/ProgramMonoid.lean#L136-L149)
- Source range: L136-L149
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.L02` — NF-Confluence

## Immediate Comment / Docstring

```lean
/-- [I.L02] Normal form confluence: the rho count of a composed program
    is the sum of the individual rho counts. -/
```

## Source Excerpt

```lean
theorem rho_count_compose (p q : Program) :
    countRho (Program.compose p q) = countRho p + countRho q := by
  induction p with
  | nil => simp [Program.compose, countRho]
  | cons i rest ih =>
    simp only [Program.compose, List.cons_append]
    cases i with
    | rho_inst =>
      simp only [countRho]
      have : countRho (rest ++ q) = countRho rest + countRho q := ih
      omega
    | sigma_inst s t =>
      simp only [countRho]
      exact ih
```
