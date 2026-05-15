---
{
  "projection_kind": "taulib_declaration",
  "title": "tau_measure_check",
  "permalink": "/corpus/taulib/docs/book-i-boundary-measure/tau-measure-check/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.Measure`.",
  "declaration_id": "TauLib.BookI.Boundary.Measure::tau_measure_check",
  "declaration_slug": "tau-measure-check",
  "kind": "def",
  "name": "tau_measure_check",
  "module_name": "TauLib.BookI.Boundary.Measure",
  "module_url": "/corpus/taulib/docs/book-i-boundary-measure/",
  "source_line_start": 226,
  "source_line_end": 227,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Measure.lean#L226-L227",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Measure.lean#L226-L227",
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
- Source path: [`TauLib/BookI/Boundary/Measure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Measure.lean#L226-L227)
- Source range: L226-L227
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- `I.D95` — τ-Measure Space

## Immediate Comment / Docstring

```lean
/-- [I.D95] Validate a τ-measure space: all sets tower-compatible. -/
```

## Source Excerpt

```lean
def tau_measure_check (tms : TauMeasureSpace) : Bool :=
  tms.measurable_sets.all (fun s => sigma_algebra_check s tms.max_stage)
```
