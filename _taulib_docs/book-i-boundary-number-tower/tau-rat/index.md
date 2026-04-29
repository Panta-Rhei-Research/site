---
{
  "projection_kind": "taulib_declaration",
  "title": "TauRat",
  "permalink": "/verify/taulib/docs/book-i-boundary-number-tower/tau-rat/",
  "summary_short": "`structure` declaration in `TauLib.BookI.Boundary.NumberTower`.",
  "declaration_id": "TauLib.BookI.Boundary.NumberTower::TauRat",
  "declaration_slug": "tau-rat",
  "kind": "structure",
  "name": "TauRat",
  "module_name": "TauLib.BookI.Boundary.NumberTower",
  "module_url": "/verify/taulib/docs/book-i-boundary-number-tower/",
  "source_line_start": 273,
  "source_line_end": 277,
  "registry_ids": [
    "I.D15"
  ],
  "related_registry_items": [
    {
      "id": "I.D15",
      "title": "Three-Level Equality",
      "url": "/registry/object/I.D15/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/NumberTower.lean#L273-L277",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.NumberTower",
        "url": "/verify/taulib/docs/book-i-boundary-number-tower/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/NumberTower.lean#L273-L277",
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

- Module: [TauLib.BookI.Boundary.NumberTower](/verify/taulib/docs/book-i-boundary-number-tower/)
- Source path: [`TauLib/BookI/Boundary/NumberTower.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/NumberTower.lean#L273-L277)
- Source range: L273-L277
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `I.D15` — Three-Level Equality

## Immediate Comment / Docstring

```lean
/-- [I.D15] Formal fraction representation of rationals earned from TauIdx.
    The pair (num, den) with den > 0 represents num / den. -/
```

## Source Excerpt

```lean
structure TauRat where
  num : TauInt
  den : TauIdx
  den_pos : den > 0
  deriving Repr
```
