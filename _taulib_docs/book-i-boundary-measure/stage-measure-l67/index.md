---
{
  "projection_kind": "taulib_declaration",
  "title": "stage_measure",
  "permalink": "/verify/taulib/docs/book-i-boundary-measure/stage-measure-l67/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.Measure`.",
  "declaration_id": "TauLib.BookI.Boundary.Measure::stage_measure",
  "declaration_slug": "stage-measure-l67",
  "kind": "def",
  "name": "stage_measure",
  "module_name": "TauLib.BookI.Boundary.Measure",
  "module_url": "/verify/taulib/docs/book-i-boundary-measure/",
  "source_line_start": 67,
  "source_line_end": 71,
  "registry_ids": [
    "I.D95"
  ],
  "related_registry_items": [
    {
      "id": "I.D95",
      "title": "τ-Measure Space",
      "url": "/registry/object/I.D95/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Measure.lean#L67-L71",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Measure.lean#L67-L71",
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
- Source path: [`TauLib/BookI/Boundary/Measure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Measure.lean#L67-L71)
- Source range: L67-L71
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `I.D95` — τ-Measure Space

## Immediate Comment / Docstring

```lean
/-- [I.D95] Compute the stage-k measure of a predicate-defined subset. -/
```

## Source Excerpt

```lean
def stage_measure (p : Nat → Bool) (k : Nat) : StageMeasure :=
  let pk := primorial k
  let count := count_satisfying p k
  { numerator := count
  , denominator := pk }
```
