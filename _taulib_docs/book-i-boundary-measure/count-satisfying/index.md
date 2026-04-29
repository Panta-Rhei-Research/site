---
{
  "projection_kind": "taulib_declaration",
  "title": "count_satisfying",
  "permalink": "/verify/taulib/docs/book-i-boundary-measure/count-satisfying/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.Measure`.",
  "declaration_id": "TauLib.BookI.Boundary.Measure::count_satisfying",
  "declaration_slug": "count-satisfying",
  "kind": "def",
  "name": "count_satisfying",
  "module_name": "TauLib.BookI.Boundary.Measure",
  "module_url": "/verify/taulib/docs/book-i-boundary-measure/",
  "source_line_start": 51,
  "source_line_end": 57,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Measure.lean#L51-L57",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Measure.lean#L51-L57",
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
- Source path: [`TauLib/BookI/Boundary/Measure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Measure.lean#L51-L57)
- Source range: L51-L57
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `I.D95` — τ-Measure Space

## Immediate Comment / Docstring

```lean
/-- [I.D95] Count elements of a predicate-defined subset of Z/M_k Z.
    count_satisfying p k = |{x ∈ [0, M_k) : p(x) = true}|. -/
```

## Source Excerpt

```lean
def count_satisfying (p : Nat → Bool) (k : Nat) : Nat :=
  go 0 (primorial k) 0
where
  go (x bound acc : Nat) : Nat :=
    if x >= bound then acc
    else go (x + 1) bound (if p x then acc + 1 else acc)
  termination_by bound - x
```
