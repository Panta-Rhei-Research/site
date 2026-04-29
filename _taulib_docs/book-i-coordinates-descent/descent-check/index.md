---
{
  "projection_kind": "taulib_declaration",
  "title": "descent_check",
  "permalink": "/verify/taulib/docs/book-i-coordinates-descent/descent-check/",
  "summary_short": "`def` declaration in `TauLib.BookI.Coordinates.Descent`.",
  "declaration_id": "TauLib.BookI.Coordinates.Descent::descent_check",
  "declaration_slug": "descent-check",
  "kind": "def",
  "name": "descent_check",
  "module_name": "TauLib.BookI.Coordinates.Descent",
  "module_url": "/verify/taulib/docs/book-i-coordinates-descent/",
  "source_line_start": 49,
  "source_line_end": 54,
  "registry_ids": [
    "I.L04"
  ],
  "related_registry_items": [
    {
      "id": "I.L04",
      "title": "Strict Remainder Descent",
      "url": "/registry/object/I.L04/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Descent.lean#L49-L54",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Coordinates.Descent",
        "url": "/verify/taulib/docs/book-i-coordinates-descent/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Descent.lean#L49-L54",
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

- Module: [TauLib.BookI.Coordinates.Descent](/verify/taulib/docs/book-i-coordinates-descent/)
- Source path: [`TauLib/BookI/Coordinates/Descent.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Descent.lean#L49-L54)
- Source range: L49-L54
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `I.L04` — Strict Remainder Descent

## Immediate Comment / Docstring

```lean
/-- [I.L04] Check that greedy_peel remainder D < X for X ≥ 2.
    Also checks T(A,B,C) * D = X (reconstruction). -/
```

## Source Excerpt

```lean
def descent_check (x : TauIdx) : Bool :=
  if x ≤ 1 then true
  else
    let (a, b, c, d) := greedy_peel x
    let t := tower_atom a b c
    (t * d == x) && (d < x)
```
