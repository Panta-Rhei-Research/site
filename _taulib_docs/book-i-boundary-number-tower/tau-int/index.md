---
{
  "projection_kind": "taulib_declaration",
  "title": "TauInt",
  "permalink": "/verify/taulib/docs/book-i-boundary-number-tower/tau-int/",
  "summary_short": "`structure` declaration in `TauLib.BookI.Boundary.NumberTower`.",
  "declaration_id": "TauLib.BookI.Boundary.NumberTower::TauInt",
  "declaration_slug": "tau-int",
  "kind": "structure",
  "name": "TauInt",
  "module_name": "TauLib.BookI.Boundary.NumberTower",
  "module_url": "/verify/taulib/docs/book-i-boundary-number-tower/",
  "source_line_start": 50,
  "source_line_end": 53,
  "registry_ids": [
    "I.D14"
  ],
  "related_registry_items": [
    {
      "id": "I.D14",
      "title": "Program Monoid",
      "url": "/registry/object/I.D14/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/NumberTower.lean#L50-L53",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/NumberTower.lean#L50-L53",
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
- Source path: [`TauLib/BookI/Boundary/NumberTower.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/NumberTower.lean#L50-L53)
- Source range: L50-L53
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `I.D14` — Program Monoid

## Immediate Comment / Docstring

```lean
/-- [I.D14] Formal difference representation of integers earned from TauIdx.
    The pair (pos, neg) represents the integer pos - neg. -/
```

## Source Excerpt

```lean
structure TauInt where
  pos : TauIdx
  neg : TauIdx
  deriving DecidableEq, Repr
```
