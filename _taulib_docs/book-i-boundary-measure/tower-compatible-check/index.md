---
{
  "projection_kind": "taulib_declaration",
  "title": "tower_compatible_check",
  "permalink": "/verify/taulib/docs/book-i-boundary-measure/tower-compatible-check/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.Measure`.",
  "declaration_id": "TauLib.BookI.Boundary.Measure::tower_compatible_check",
  "declaration_slug": "tower-compatible-check",
  "kind": "def",
  "name": "tower_compatible_check",
  "module_name": "TauLib.BookI.Boundary.Measure",
  "module_url": "/verify/taulib/docs/book-i-boundary-measure/",
  "source_line_start": 84,
  "source_line_end": 94,
  "registry_ids": [
    "I.D96"
  ],
  "related_registry_items": [
    {
      "id": "I.D96",
      "title": "Tower σ-Algebra",
      "url": "/registry/object/I.D96/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Measure.lean#L84-L94",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.Measure",
        "url": "/verify/taulib/docs/book-i-boundary-measure/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Measure.lean#L84-L94",
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

- Module: [TauLib.BookI.Boundary.Measure](/verify/taulib/docs/book-i-boundary-measure/)
- Source path: [`TauLib/BookI/Boundary/Measure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Measure.lean#L84-L94)
- Source range: L84-L94
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `I.D96` — Tower σ-Algebra

## Immediate Comment / Docstring

```lean
/-- [I.D96] Check tower compatibility at stages k and k+1:
    x satisfies S_{k+1} implies reduce(x, k) satisfies S_k. -/
```

## Source Excerpt

```lean
def tower_compatible_check (tms : TowerMeasurableSet) (k : Nat) : Bool :=
  go 0 (primorial (k + 1))
where
  go (x bound : Nat) : Bool :=
    if x >= bound then true
    else
      let ok := if tms.predicate (k + 1) x then
        tms.predicate k (x % primorial k)
      else true
      ok && go (x + 1) bound
  termination_by bound - x
```
