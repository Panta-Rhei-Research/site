---
{
  "projection_kind": "taulib_declaration",
  "title": "defect_entropy_reaches_zero",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/defect-entropy-reaches-zero/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Thermodynamics.EntropySplitting`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.EntropySplitting::defect_entropy_reaches_zero",
  "declaration_slug": "defect-entropy-reaches-zero",
  "kind": "theorem",
  "name": "defect_entropy_reaches_zero",
  "module_name": "TauLib.BookV.Thermodynamics.EntropySplitting",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/",
  "source_line_start": 202,
  "source_line_end": 204,
  "registry_ids": [
    "V.C06"
  ],
  "related_registry_items": [
    {
      "id": "V.C06",
      "title": "Defect entropy reaches zero",
      "url": "/registry/object/V.C06/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L202-L204",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Thermodynamics.EntropySplitting",
        "url": "/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L202-L204",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookV.Thermodynamics.EntropySplitting](/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/)
- Source path: [`TauLib/BookV/Thermodynamics/EntropySplitting.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L202-L204)
- Source range: L202-L204
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.C06` — Defect entropy reaches zero

## Immediate Comment / Docstring

```lean
/-- [V.C06] Defect entropy reaches zero with exponentially fast
    convergence: S_def(n) <= (1 - iota_tau)^n S_def(0).

    Since (1 - iota_tau) < 1, this converges to zero.
    The rate is controlled by the gravitational coupling. -/
```

## Source Excerpt

```lean
theorem defect_entropy_reaches_zero :
    "S_def(n) <= (1-iota)^n S_def(0) -> 0 as n -> inf" =
    "S_def(n) <= (1-iota)^n S_def(0) -> 0 as n -> inf" := rfl
```
