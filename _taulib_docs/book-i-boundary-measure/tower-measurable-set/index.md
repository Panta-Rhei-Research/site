---
{
  "projection_kind": "taulib_declaration",
  "title": "TowerMeasurableSet",
  "permalink": "/verify/taulib/docs/book-i-boundary-measure/tower-measurable-set/",
  "summary_short": "`structure` declaration in `TauLib.BookI.Boundary.Measure`.",
  "declaration_id": "TauLib.BookI.Boundary.Measure::TowerMeasurableSet",
  "declaration_slug": "tower-measurable-set",
  "kind": "structure",
  "name": "TowerMeasurableSet",
  "module_name": "TauLib.BookI.Boundary.Measure",
  "module_url": "/verify/taulib/docs/book-i-boundary-measure/",
  "source_line_start": 79,
  "source_line_end": 80,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Measure.lean#L79-L80",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Measure.lean#L79-L80",
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

- Module: [TauLib.BookI.Boundary.Measure](/verify/taulib/docs/book-i-boundary-measure/)
- Source path: [`TauLib/BookI/Boundary/Measure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Measure.lean#L79-L80)
- Source range: L79-L80
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `I.D96` — Tower σ-Algebra

## Immediate Comment / Docstring

```lean
/-- [I.D96] A tower-measurable set is a family of predicates, one per stage,
    that are compatible under the reduction map. -/
```

## Source Excerpt

```lean
structure TowerMeasurableSet where
  predicate : Nat → Nat → Bool  -- predicate(k, x) = whether x ∈ S_k
```
