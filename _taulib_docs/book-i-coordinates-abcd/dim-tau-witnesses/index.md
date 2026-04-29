---
{
  "projection_kind": "taulib_declaration",
  "title": "dim_tau_witnesses",
  "permalink": "/verify/taulib/docs/book-i-coordinates-abcd/dim-tau-witnesses/",
  "summary_short": "`def` declaration in `TauLib.BookI.Coordinates.ABCD`.",
  "declaration_id": "TauLib.BookI.Coordinates.ABCD::dim_tau_witnesses",
  "declaration_slug": "dim-tau-witnesses",
  "kind": "def",
  "name": "dim_tau_witnesses",
  "module_name": "TauLib.BookI.Coordinates.ABCD",
  "module_url": "/verify/taulib/docs/book-i-coordinates-abcd/",
  "source_line_start": 120,
  "source_line_end": 126,
  "registry_ids": [
    "I.P08"
  ],
  "related_registry_items": [
    {
      "id": "I.P08",
      "title": "Dimension Theorem (dim_tau = 4)",
      "url": "/registry/object/I.P08/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/ABCD.lean#L120-L126",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Coordinates.ABCD",
        "url": "/verify/taulib/docs/book-i-coordinates-abcd/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/ABCD.lean#L120-L126",
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

- Module: [TauLib.BookI.Coordinates.ABCD](/verify/taulib/docs/book-i-coordinates-abcd/)
- Source path: [`TauLib/BookI/Coordinates/ABCD.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/ABCD.lean#L120-L126)
- Source range: L120-L126
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `I.P08` — Dimension Theorem (dim_tau = 4)

## Immediate Comment / Docstring

```lean
/-- [I.P08] Four-dimensionality witness: exhibit X values where each
    coordinate varies independently. Computable certificate. -/
```

## Source Excerpt

```lean
def dim_tau_witnesses : List (TauIdx × TauIdx × TauIdx × TauIdx × TauIdx) :=
  -- (X, A, B, C, D): examples showing coordinate independence
  [ (12, 3, 1, 1, 4)     -- A = 3
  , (18, 3, 2, 1, 2)     -- same A, different B
  , (16, 2, 1, 3, 1)     -- different A, C = 3
  , (64, 2, 3, 2, 1)     -- same A as 16, different B and C
  ]
```
