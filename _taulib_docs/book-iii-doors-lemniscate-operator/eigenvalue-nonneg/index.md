---
{
  "projection_kind": "taulib_declaration",
  "title": "eigenvalue_nonneg",
  "permalink": "/verify/taulib/docs/book-iii-doors-lemniscate-operator/eigenvalue-nonneg/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Doors.LemniscateOperator`.",
  "declaration_id": "TauLib.BookIII.Doors.LemniscateOperator::eigenvalue_nonneg",
  "declaration_slug": "eigenvalue-nonneg",
  "kind": "theorem",
  "name": "eigenvalue_nonneg",
  "module_name": "TauLib.BookIII.Doors.LemniscateOperator",
  "module_url": "/verify/taulib/docs/book-iii-doors-lemniscate-operator/",
  "source_line_start": 203,
  "source_line_end": 204,
  "registry_ids": [
    "III.T17"
  ],
  "related_registry_items": [
    {
      "id": "III.T17",
      "title": "Self-Adjointness of H_L",
      "url": "/registry/object/III.T17/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/LemniscateOperator.lean#L203-L204",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Doors.LemniscateOperator",
        "url": "/verify/taulib/docs/book-iii-doors-lemniscate-operator/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/LemniscateOperator.lean#L203-L204",
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

- Module: [TauLib.BookIII.Doors.LemniscateOperator](/verify/taulib/docs/book-iii-doors-lemniscate-operator/)
- Source path: [`TauLib/BookIII/Doors/LemniscateOperator.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/LemniscateOperator.lean#L203-L204)
- Source range: L203-L204
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T17` — Self-Adjointness of H_L

## Immediate Comment / Docstring

```lean
/-- [III.T17] Structural: all eigenvalues are non-negative. -/
```

## Source Excerpt

```lean
theorem eigenvalue_nonneg (n : Nat) :
    lemniscate_eigenvalue n ≥ 0 := Nat.zero_le _
```
