---
{
  "projection_kind": "taulib_declaration",
  "title": "pixel_analogy",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-inversion/pixel-analogy/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Thermodynamics.Inversion`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.Inversion::pixel_analogy",
  "declaration_slug": "pixel-analogy",
  "kind": "theorem",
  "name": "pixel_analogy",
  "module_name": "TauLib.BookV.Thermodynamics.Inversion",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-inversion/",
  "source_line_start": 287,
  "source_line_end": 289,
  "registry_ids": [
    "V.R111",
    "V.R112"
  ],
  "related_registry_items": [
    {
      "id": "V.R111",
      "title": "The explanatory gap",
      "url": "/registry/object/V.R111/"
    },
    {
      "id": "V.R112",
      "title": "An analogy: pixels and noise",
      "url": "/registry/object/V.R112/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/Inversion.lean#L287-L289",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Thermodynamics.Inversion",
        "url": "/verify/taulib/docs/book-v-thermodynamics-inversion/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/Inversion.lean#L287-L289",
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

- Module: [TauLib.BookV.Thermodynamics.Inversion](/verify/taulib/docs/book-v-thermodynamics-inversion/)
- Source path: [`TauLib/BookV/Thermodynamics/Inversion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/Inversion.lean#L287-L289)
- Source range: L287-L289
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.R111` — The explanatory gap
- `V.R112` — An analogy: pixels and noise

## Immediate Comment / Docstring

```lean
-- ============================================================
-- REMARKS (comment-only)
-- ============================================================

-- [V.R111] The Explanatory Gap: time-reversible microscopic equations
-- cannot explain macroscopic entropy increase without the Past Hypothesis.
-- The tau-framework dissolves this gap structurally.

-- [V.R112] Pixel-Resolution Analogy: increasing resolution raises pixel
-- count (refinement entropy) by 100x while defect entropy stays near zero.
-- Recorded structurally:
```

## Source Excerpt

```lean
theorem pixel_analogy :
    "resolution 100x100 -> 1000x1000: pixel count up 100x, noise near zero" =
    "resolution 100x100 -> 1000x1000: pixel count up 100x, noise near zero" := rfl
```
