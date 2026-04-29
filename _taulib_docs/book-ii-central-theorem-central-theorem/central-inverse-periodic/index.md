---
{
  "projection_kind": "taulib_declaration",
  "title": "central_inverse_periodic",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-central-theorem/central-inverse-periodic/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.CentralTheorem.CentralTheorem`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.CentralTheorem::central_inverse_periodic",
  "declaration_slug": "central-inverse-periodic",
  "kind": "theorem",
  "name": "central_inverse_periodic",
  "module_name": "TauLib.BookII.CentralTheorem.CentralTheorem",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-central-theorem/",
  "source_line_start": 432,
  "source_line_end": 434,
  "registry_ids": [
    "II.T40"
  ],
  "related_registry_items": [
    {
      "id": "II.T40",
      "title": "Central Theorem",
      "url": "/registry/object/II.T40/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L432-L434",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.CentralTheorem.CentralTheorem",
        "url": "/verify/taulib/docs/book-ii-central-theorem-central-theorem/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L432-L434",
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

- Module: [TauLib.BookII.CentralTheorem.CentralTheorem](/verify/taulib/docs/book-ii-central-theorem-central-theorem/)
- Source path: [`TauLib/BookII/CentralTheorem/CentralTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L432-L434)
- Source range: L432-L434
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.T40` — Central Theorem

## Immediate Comment / Docstring

```lean
/-- [II.T40] Central Theorem inverse: holomorphic restriction is periodic.
    reduce(x + P_k, k) = reduce(x, k) ensures the boundary restriction
    is well-defined on Z/P_kZ. -/
```

## Source Excerpt

```lean
theorem central_inverse_periodic (x k : TauIdx) :
    reduce (x + primorial k) k = reduce x k := by
  simp [reduce, Nat.add_mod_right]
```
