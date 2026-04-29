---
{
  "projection_kind": "taulib_declaration",
  "title": "countable_additivity_check",
  "permalink": "/verify/taulib/docs/book-i-boundary-measure/countable-additivity-check/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.Measure`.",
  "declaration_id": "TauLib.BookI.Boundary.Measure::countable_additivity_check",
  "declaration_slug": "countable-additivity-check",
  "kind": "def",
  "name": "countable_additivity_check",
  "module_name": "TauLib.BookI.Boundary.Measure",
  "module_url": "/verify/taulib/docs/book-i-boundary-measure/",
  "source_line_start": 123,
  "source_line_end": 129,
  "registry_ids": [
    "I.T49"
  ],
  "related_registry_items": [
    {
      "id": "I.T49",
      "title": "Countable Additivity",
      "url": "/registry/object/I.T49/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Measure.lean#L123-L129",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Measure.lean#L123-L129",
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
- Source path: [`TauLib/BookI/Boundary/Measure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Measure.lean#L123-L129)
- Source range: L123-L129
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `I.T49` — Countable Additivity

## Immediate Comment / Docstring

```lean
/-- [I.T49] Additivity check: if p ∩ q = ∅, then |p ∪ q| = |p| + |q|. -/
```

## Source Excerpt

```lean
def countable_additivity_check (p q : Nat → Bool) (k : Nat) : Bool :=
  if disjoint_check p q k then
    let cp := count_satisfying p k
    let cq := count_satisfying q k
    let cpq := count_satisfying (fun x => p x || q x) k
    cpq == cp + cq
  else true  -- precondition not met, vacuously true
```
