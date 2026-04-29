---
{
  "projection_kind": "taulib_declaration",
  "title": "threshold_exists",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-tovphase-boundary/threshold-exists/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.TOVPhaseBoundary`.",
  "declaration_id": "TauLib.BookV.GravityField.TOVPhaseBoundary::threshold_exists",
  "declaration_slug": "threshold-exists",
  "kind": "theorem",
  "name": "threshold_exists",
  "module_name": "TauLib.BookV.GravityField.TOVPhaseBoundary",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-tovphase-boundary/",
  "source_line_start": 204,
  "source_line_end": 205,
  "registry_ids": [
    "V.T46"
  ],
  "related_registry_items": [
    {
      "id": "V.T46",
      "title": "Structural Threshold --- Forced Topology Relaxation",
      "url": "/registry/object/V.T46/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVPhaseBoundary.lean#L204-L205",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.TOVPhaseBoundary",
        "url": "/verify/taulib/docs/book-v-gravity-field-tovphase-boundary/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVPhaseBoundary.lean#L204-L205",
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

- Module: [TauLib.BookV.GravityField.TOVPhaseBoundary](/verify/taulib/docs/book-v-gravity-field-tovphase-boundary/)
- Source path: [`TauLib/BookV/GravityField/TOVPhaseBoundary.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVPhaseBoundary.lean#L204-L205)
- Source range: L204-L205
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T46` — Structural Threshold --- Forced Topology Relaxation

## Immediate Comment / Docstring

```lean
/-- [V.T46] Threshold existence: the coherence horizon M_n* exists.
    Follows from tension monotonicity + T^2 branch being bounded. -/
```

## Source Excerpt

```lean
theorem threshold_exists (h : CoherenceHorizon) :
    h.mass_numer > 0 := h.mass_positive
```
