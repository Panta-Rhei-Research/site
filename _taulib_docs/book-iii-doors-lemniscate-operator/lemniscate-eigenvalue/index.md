---
{
  "projection_kind": "taulib_declaration",
  "title": "lemniscate_eigenvalue",
  "permalink": "/verify/taulib/docs/book-iii-doors-lemniscate-operator/lemniscate-eigenvalue/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Doors.LemniscateOperator`.",
  "declaration_id": "TauLib.BookIII.Doors.LemniscateOperator::lemniscate_eigenvalue",
  "declaration_slug": "lemniscate-eigenvalue",
  "kind": "def",
  "name": "lemniscate_eigenvalue",
  "module_name": "TauLib.BookIII.Doors.LemniscateOperator",
  "module_url": "/verify/taulib/docs/book-iii-doors-lemniscate-operator/",
  "source_line_start": 43,
  "source_line_end": 43,
  "registry_ids": [
    "III.D28"
  ],
  "related_registry_items": [
    {
      "id": "III.D28",
      "title": "Lemniscate Operator H_L",
      "url": "/registry/object/III.D28/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/LemniscateOperator.lean#L43-L43",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/LemniscateOperator.lean#L43-L43",
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

- Module: [TauLib.BookIII.Doors.LemniscateOperator](/verify/taulib/docs/book-iii-doors-lemniscate-operator/)
- Source path: [`TauLib/BookIII/Doors/LemniscateOperator.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/LemniscateOperator.lean#L43-L43)
- Source range: L43-L43
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D28` — Lemniscate Operator H_L

## Immediate Comment / Docstring

```lean
/-- [III.D28] Lemniscate operator eigenvalue at mode n.
    For L = S¹ ∨ S¹ with unit circumference lobes:
    λ_n = n² (the key spectral property of −d²/dx²).
    The τ-native finite model uses n² directly. -/
```

## Source Excerpt

```lean
def lemniscate_eigenvalue (n : TauIdx) : TauIdx := n * n
```
