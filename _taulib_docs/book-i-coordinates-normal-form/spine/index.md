---
{
  "projection_kind": "taulib_declaration",
  "title": "spine",
  "permalink": "/verify/taulib/docs/book-i-coordinates-normal-form/spine/",
  "summary_short": "`def` declaration in `TauLib.BookI.Coordinates.NormalForm`.",
  "declaration_id": "TauLib.BookI.Coordinates.NormalForm::spine",
  "declaration_slug": "spine",
  "kind": "def",
  "name": "spine",
  "module_name": "TauLib.BookI.Coordinates.NormalForm",
  "module_url": "/verify/taulib/docs/book-i-coordinates-normal-form/",
  "source_line_start": 74,
  "source_line_end": 85,
  "registry_ids": [
    "I.D23"
  ],
  "related_registry_items": [
    {
      "id": "I.D23",
      "title": "Genealogical Decomposition (Spine)",
      "url": "/registry/object/I.D23/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/NormalForm.lean#L74-L85",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Coordinates.NormalForm",
        "url": "/verify/taulib/docs/book-i-coordinates-normal-form/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/NormalForm.lean#L74-L85",
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

- Module: [TauLib.BookI.Coordinates.NormalForm](/verify/taulib/docs/book-i-coordinates-normal-form/)
- Source path: [`TauLib/BookI/Coordinates/NormalForm.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/NormalForm.lean#L74-L85)
- Source range: L74-L85
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `I.D23` — Genealogical Decomposition (Spine)

## Immediate Comment / Docstring

```lean
/-- [I.D23] Iterated greedy peel producing a spine of (A,B,C) triples.
    Fuel-bounded; formal descent proved in the Descent module. -/
```

## Source Excerpt

```lean
def spine (x : TauIdx) : List (TauIdx × TauIdx × TauIdx) :=
  if x ≤ 1 then []
  else go x x
where
  go (x fuel : TauIdx) : List (TauIdx × TauIdx × TauIdx) :=
    if fuel = 0 then []
    else if x ≤ 1 then []
    else
      let (a, b, c, d) := greedy_peel x
      (a, b, c) :: go d (fuel - 1)
  termination_by fuel
  decreasing_by simp_wf; simp only [TauIdx] at *; omega
```
