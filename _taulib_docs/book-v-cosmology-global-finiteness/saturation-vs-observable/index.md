---
{
  "projection_kind": "taulib_declaration",
  "title": "saturation_vs_observable",
  "permalink": "/verify/taulib/docs/book-v-cosmology-global-finiteness/saturation-vs-observable/",
  "summary_short": "`def` declaration in `TauLib.BookV.Cosmology.GlobalFiniteness`.",
  "declaration_id": "TauLib.BookV.Cosmology.GlobalFiniteness::saturation_vs_observable",
  "declaration_slug": "saturation-vs-observable",
  "kind": "def",
  "name": "saturation_vs_observable",
  "module_name": "TauLib.BookV.Cosmology.GlobalFiniteness",
  "module_url": "/verify/taulib/docs/book-v-cosmology-global-finiteness/",
  "source_line_start": 252,
  "source_line_end": 254,
  "registry_ids": [
    "V.R235"
  ],
  "related_registry_items": [
    {
      "id": "V.R235",
      "title": "Saturation radius vs. observable universe",
      "url": "/registry/object/V.R235/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/GlobalFiniteness.lean#L252-L254",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.GlobalFiniteness",
        "url": "/verify/taulib/docs/book-v-cosmology-global-finiteness/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/GlobalFiniteness.lean#L252-L254",
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

- Module: [TauLib.BookV.Cosmology.GlobalFiniteness](/verify/taulib/docs/book-v-cosmology-global-finiteness/)
- Source path: [`TauLib/BookV/Cosmology/GlobalFiniteness.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/GlobalFiniteness.lean#L252-L254)
- Source range: L252-L254
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.R235` — Saturation radius vs. observable universe

## Immediate Comment / Docstring

```lean
/-- [V.R235] Saturation radius vs. observable universe: R_sat is
    structural (property of τ³); observable universe is chart-level.
    R_sat may be larger or smaller than the observable universe
    depending on calibration. -/
```

## Source Excerpt

```lean
def saturation_vs_observable : Prop :=
  "R_sat is structural (tau^3), observable universe is chart-level" =
  "R_sat is structural (tau^3), observable universe is chart-level"
```
