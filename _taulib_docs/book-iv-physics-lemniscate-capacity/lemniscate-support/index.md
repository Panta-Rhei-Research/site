---
{
  "projection_kind": "taulib_declaration",
  "title": "LemniscateSupport",
  "permalink": "/verify/taulib/docs/book-iv-physics-lemniscate-capacity/lemniscate-support/",
  "summary_short": "`inductive` declaration in `TauLib.BookIV.Physics.LemniscateCapacity`.",
  "declaration_id": "TauLib.BookIV.Physics.LemniscateCapacity::LemniscateSupport",
  "declaration_slug": "lemniscate-support",
  "kind": "inductive",
  "name": "LemniscateSupport",
  "module_name": "TauLib.BookIV.Physics.LemniscateCapacity",
  "module_url": "/verify/taulib/docs/book-iv-physics-lemniscate-capacity/",
  "source_line_start": 69,
  "source_line_end": 73,
  "registry_ids": [
    "IV.D42"
  ],
  "related_registry_items": [
    {
      "id": "IV.D42",
      "title": "Lemniscate Three-Fold",
      "url": "/registry/object/IV.D42/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/LemniscateCapacity.lean#L69-L73",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Physics.LemniscateCapacity",
        "url": "/verify/taulib/docs/book-iv-physics-lemniscate-capacity/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/LemniscateCapacity.lean#L69-L73",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
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

- Module: [TauLib.BookIV.Physics.LemniscateCapacity](/verify/taulib/docs/book-iv-physics-lemniscate-capacity/)
- Source path: [`TauLib/BookIV/Physics/LemniscateCapacity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/LemniscateCapacity.lean#L69-L73)
- Source range: L69-L73
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `IV.D42` — Lemniscate Three-Fold

## Immediate Comment / Docstring

```lean
/-- [IV.D42] The three distinguished supports on L = S¹ ∨ S¹. -/
```

## Source Excerpt

```lean
inductive LemniscateSupport
  | Lobe1     -- First S¹ component (χ₊-sector)
  | Lobe2     -- Second S¹ component (χ₋-sector)
  | Crossing  -- Wedge point where lobes meet
  deriving Repr, DecidableEq
```
