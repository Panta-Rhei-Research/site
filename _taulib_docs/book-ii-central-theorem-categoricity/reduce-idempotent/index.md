---
{
  "projection_kind": "taulib_declaration",
  "title": "reduce_idempotent",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-categoricity/reduce-idempotent/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.CentralTheorem.Categoricity`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.Categoricity::reduce_idempotent",
  "declaration_slug": "reduce-idempotent",
  "kind": "theorem",
  "name": "reduce_idempotent",
  "module_name": "TauLib.BookII.CentralTheorem.Categoricity",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-categoricity/",
  "source_line_start": 363,
  "source_line_end": 365,
  "registry_ids": [
    "II.T42"
  ],
  "related_registry_items": [
    {
      "id": "II.T42",
      "title": "Categoricity",
      "url": "/registry/object/II.T42/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/Categoricity.lean#L363-L365",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.CentralTheorem.Categoricity",
        "url": "/verify/taulib/docs/book-ii-central-theorem-categoricity/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/Categoricity.lean#L363-L365",
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

- Module: [TauLib.BookII.CentralTheorem.Categoricity](/verify/taulib/docs/book-ii-central-theorem-categoricity/)
- Source path: [`TauLib/BookII/CentralTheorem/Categoricity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/Categoricity.lean#L363-L365)
- Source range: L363-L365
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.T42` — Categoricity

## Immediate Comment / Docstring

```lean
/-- [II.T42] Reduction is idempotent: reduce(reduce(x, k), k) = reduce(x, k).
    This is the formal statement that the primorial tower has no ambiguity. -/
```

## Source Excerpt

```lean
theorem reduce_idempotent (x k : TauIdx) :
    reduce (reduce x k) k = reduce x k :=
  reduction_compat x (Nat.le_refl k)
```
