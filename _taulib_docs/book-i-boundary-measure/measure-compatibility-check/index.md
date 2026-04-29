---
{
  "projection_kind": "taulib_declaration",
  "title": "measure_compatibility_check",
  "permalink": "/verify/taulib/docs/book-i-boundary-measure/measure-compatibility-check/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.Measure`.",
  "declaration_id": "TauLib.BookI.Boundary.Measure::measure_compatibility_check",
  "declaration_slug": "measure-compatibility-check",
  "kind": "def",
  "name": "measure_compatibility_check",
  "module_name": "TauLib.BookI.Boundary.Measure",
  "module_url": "/verify/taulib/docs/book-i-boundary-measure/",
  "source_line_start": 139,
  "source_line_end": 144,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Measure.lean#L139-L144",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Measure.lean#L139-L144",
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
- Source path: [`TauLib/BookI/Boundary/Measure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Measure.lean#L139-L144)
- Source range: L139-L144
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `I.P43` — Measure Compatibility

## Immediate Comment / Docstring

```lean
/-- [I.P43] Measure compatibility check: the measure of a tower-measurable
    set at stage k+1 (projected down) equals the measure at stage k.
    Formally: count_{k+1}(S_{k+1}) / M_{k+1} = count_k(S_k) / M_k
    i.e., count_{k+1}(S_{k+1}) * M_k = count_k(S_k) * M_{k+1}. -/
```

## Source Excerpt

```lean
def measure_compatibility_check (tms : TowerMeasurableSet) (k : Nat) : Bool :=
  let pk := primorial k
  let pk1 := primorial (k + 1)
  let ck := count_satisfying (tms.predicate k) k
  let ck1 := count_satisfying (tms.predicate (k + 1)) (k + 1)
  ck1 * pk == ck * pk1
```
