---
{
  "projection_kind": "taulib_declaration",
  "title": "measure_compatibility_full",
  "permalink": "/corpus/taulib/docs/book-i-boundary-measure/measure-compatibility-full/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.Measure`.",
  "declaration_id": "TauLib.BookI.Boundary.Measure::measure_compatibility_full",
  "declaration_slug": "measure-compatibility-full",
  "kind": "def",
  "name": "measure_compatibility_full",
  "module_name": "TauLib.BookI.Boundary.Measure",
  "module_url": "/corpus/taulib/docs/book-i-boundary-measure/",
  "source_line_start": 147,
  "source_line_end": 154,
  "registry_ids": [
    "I.P43"
  ],
  "related_registry_items": [
    {
      "id": "I.P43",
      "title": "Measure Compatibility",
      "url": "/registry/object/I.P43/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Measure.lean#L147-L154",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.Measure",
        "url": "/corpus/taulib/docs/book-i-boundary-measure/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Measure.lean#L147-L154",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "data/computed value",
      "status": "data/computed value"
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

- Module: [TauLib.BookI.Boundary.Measure](/corpus/taulib/docs/book-i-boundary-measure/)
- Source path: [`TauLib/BookI/Boundary/Measure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Measure.lean#L147-L154)
- Source range: L147-L154
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- `I.P43` — Measure Compatibility

## Immediate Comment / Docstring

```lean
/-- [I.P43] Full measure compatibility for stages 1..db. -/
```

## Source Excerpt

```lean
def measure_compatibility_full (tms : TowerMeasurableSet) (db : Nat) : Bool :=
  go 1 (db + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k >= db then true
    else measure_compatibility_check tms k && go (k + 1) (fuel - 1)
  termination_by fuel
```
