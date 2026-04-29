---
{
  "projection_kind": "taulib_declaration",
  "title": "TauReal",
  "permalink": "/verify/taulib/docs/book-i-boundary-constructive-reals/tau-real/",
  "summary_short": "`structure` declaration in `TauLib.BookI.Boundary.ConstructiveReals`.",
  "declaration_id": "TauLib.BookI.Boundary.ConstructiveReals::TauReal",
  "declaration_slug": "tau-real",
  "kind": "structure",
  "name": "TauReal",
  "module_name": "TauLib.BookI.Boundary.ConstructiveReals",
  "module_url": "/verify/taulib/docs/book-i-boundary-constructive-reals/",
  "source_line_start": 136,
  "source_line_end": 138,
  "registry_ids": [
    "I.D84"
  ],
  "related_registry_items": [
    {
      "id": "I.D84",
      "title": "Constructive Reals",
      "url": "/registry/object/I.D84/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ConstructiveReals.lean#L136-L138",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.ConstructiveReals",
        "url": "/verify/taulib/docs/book-i-boundary-constructive-reals/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ConstructiveReals.lean#L136-L138",
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

- Module: [TauLib.BookI.Boundary.ConstructiveReals](/verify/taulib/docs/book-i-boundary-constructive-reals/)
- Source path: [`TauLib/BookI/Boundary/ConstructiveReals.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ConstructiveReals.lean#L136-L138)
- Source range: L136-L138
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `I.D84` — Constructive Reals

## Immediate Comment / Docstring

```lean
/-- [I.D84] TauReal: constructive reals, represented as sequences of
    TauRat approximations.  The sequence need not be Cauchy in the
    definition of the type — the Cauchy condition is carried by the
    separate `TauReal.IsCauchy` predicate, and equivalence is defined
    as Cauchy equivalence regardless of whether the underlying
    sequences themselves are Cauchy. -/
```

## Source Excerpt

```lean
structure TauReal where
  /-- The nth rational approximation. -/
  approx : Nat → TauRat
```
