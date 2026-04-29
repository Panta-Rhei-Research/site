---
{
  "projection_kind": "taulib_declaration",
  "title": "idx_add_injective",
  "permalink": "/verify/taulib/docs/book-i-denotation-arithmetic/idx-add-injective/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Denotation.Arithmetic`.",
  "declaration_id": "TauLib.BookI.Denotation.Arithmetic::idx_add_injective",
  "declaration_slug": "idx-add-injective",
  "kind": "theorem",
  "name": "idx_add_injective",
  "module_name": "TauLib.BookI.Denotation.Arithmetic",
  "module_url": "/verify/taulib/docs/book-i-denotation-arithmetic/",
  "source_line_start": 197,
  "source_line_end": 201,
  "registry_ids": [
    "I.P05"
  ],
  "related_registry_items": [
    {
      "id": "I.P05",
      "title": "Tetration Injectivity",
      "url": "/registry/object/I.P05/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Arithmetic.lean#L197-L201",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Denotation.Arithmetic",
        "url": "/verify/taulib/docs/book-i-denotation-arithmetic/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Arithmetic.lean#L197-L201",
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

- Module: [TauLib.BookI.Denotation.Arithmetic](/verify/taulib/docs/book-i-denotation-arithmetic/)
- Source path: [`TauLib/BookI/Denotation/Arithmetic.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Arithmetic.lean#L197-L201)
- Source range: L197-L201
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.P05` — Tetration Injectivity

## Immediate Comment / Docstring

```lean
/-- [I.P05] Addition is injective in the second argument. -/
```

## Source Excerpt

```lean
theorem idx_add_injective (n : TauIdx) : Function.Injective (idx_add n) := by
  intro a b h
  have h3 : n + a = n + b := by
    rw [← idx_add_eq_nat_add, ← idx_add_eq_nat_add]; exact h
  exact Tau.Orbit.add_injective n h3
```
