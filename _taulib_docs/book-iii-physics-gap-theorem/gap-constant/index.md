---
{
  "projection_kind": "taulib_declaration",
  "title": "gap_constant",
  "permalink": "/verify/taulib/docs/book-iii-physics-gap-theorem/gap-constant/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Physics.GapTheorem`.",
  "declaration_id": "TauLib.BookIII.Physics.GapTheorem::gap_constant",
  "declaration_slug": "gap-constant",
  "kind": "def",
  "name": "gap_constant",
  "module_name": "TauLib.BookIII.Physics.GapTheorem",
  "module_url": "/verify/taulib/docs/book-iii-physics-gap-theorem/",
  "source_line_start": 94,
  "source_line_end": 94,
  "registry_ids": [
    "III.D45"
  ],
  "related_registry_items": [
    {
      "id": "III.D45",
      "title": "Gap Constant Γ*",
      "url": "/registry/object/III.D45/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/GapTheorem.lean#L94-L94",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Physics.GapTheorem",
        "url": "/verify/taulib/docs/book-iii-physics-gap-theorem/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/GapTheorem.lean#L94-L94",
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

- Module: [TauLib.BookIII.Physics.GapTheorem](/verify/taulib/docs/book-iii-physics-gap-theorem/)
- Source path: [`TauLib/BookIII/Physics/GapTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/GapTheorem.lean#L94-L94)
- Source range: L94-L94
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D45` — Gap Constant Γ*

## Immediate Comment / Docstring

```lean
/-- [III.D45] Gap constant at level k. For k ≥ 3, this is the minimum
    of B-product and C-product (both positive by strong sector). -/
```

## Source Excerpt

```lean
def gap_constant (k : TauIdx) : TauIdx := tau_gap_at_level k
```
