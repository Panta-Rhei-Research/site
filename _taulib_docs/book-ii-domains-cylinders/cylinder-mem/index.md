---
{
  "projection_kind": "taulib_declaration",
  "title": "cylinder_mem",
  "permalink": "/verify/taulib/docs/book-ii-domains-cylinders/cylinder-mem/",
  "summary_short": "`def` declaration in `TauLib.BookII.Domains.Cylinders`.",
  "declaration_id": "TauLib.BookII.Domains.Cylinders::cylinder_mem",
  "declaration_slug": "cylinder-mem",
  "kind": "def",
  "name": "cylinder_mem",
  "module_name": "TauLib.BookII.Domains.Cylinders",
  "module_url": "/verify/taulib/docs/book-ii-domains-cylinders/",
  "source_line_start": 36,
  "source_line_end": 37,
  "registry_ids": [
    "II.D09"
  ],
  "related_registry_items": [
    {
      "id": "II.D09",
      "title": "Cylinder Domain",
      "url": "/registry/object/II.D09/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Domains/Cylinders.lean#L36-L37",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Domains.Cylinders",
        "url": "/verify/taulib/docs/book-ii-domains-cylinders/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Domains/Cylinders.lean#L36-L37",
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

- Module: [TauLib.BookII.Domains.Cylinders](/verify/taulib/docs/book-ii-domains-cylinders/)
- Source path: [`TauLib/BookII/Domains/Cylinders.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Domains/Cylinders.lean#L36-L37)
- Source range: L36-L37
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D09` — Cylinder Domain

## Immediate Comment / Docstring

```lean
/-- [II.D09] Stage-k cylinder membership:
    y ∈ C_k(x) iff π_k(y) = π_k(x), i.e., y ≡ x (mod M_k). -/
```

## Source Excerpt

```lean
def cylinder_mem (k center y : TauIdx) : Bool :=
  reduce y k = reduce center k
```
