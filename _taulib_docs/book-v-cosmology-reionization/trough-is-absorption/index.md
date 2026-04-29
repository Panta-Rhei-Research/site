---
{
  "projection_kind": "taulib_declaration",
  "title": "trough_is_absorption",
  "permalink": "/verify/taulib/docs/book-v-cosmology-reionization/trough-is-absorption/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.Reionization`.",
  "declaration_id": "TauLib.BookV.Cosmology.Reionization::trough_is_absorption",
  "declaration_slug": "trough-is-absorption",
  "kind": "theorem",
  "name": "trough_is_absorption",
  "module_name": "TauLib.BookV.Cosmology.Reionization",
  "module_url": "/verify/taulib/docs/book-v-cosmology-reionization/",
  "source_line_start": 87,
  "source_line_end": 104,
  "registry_ids": [
    "V.P189",
    "V.R470"
  ],
  "related_registry_items": [
    {
      "id": "V.P189",
      "title": "EDGES/HERA/SKA Predictions",
      "url": "/registry/object/V.P189/"
    },
    {
      "id": "V.R470",
      "title": "V.OP9 Status: PARTIAL-IMPROVED",
      "url": "/registry/object/V.R470/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/Reionization.lean#L87-L104",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.Reionization",
        "url": "/verify/taulib/docs/book-v-cosmology-reionization/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/Reionization.lean#L87-L104",
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

- Module: [TauLib.BookV.Cosmology.Reionization](/verify/taulib/docs/book-v-cosmology-reionization/)
- Source path: [`TauLib/BookV/Cosmology/Reionization.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/Reionization.lean#L87-L104)
- Source range: L87-L104
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P189` — EDGES/HERA/SKA Predictions
- `V.R470` — V.OP9 Status: PARTIAL-IMPROVED

## Immediate Comment / Docstring

```lean
/-- The trough prediction is an absorption signal (negative). -/
```

## Source Excerpt

```lean
theorem trough_is_absorption : absorption_trough_z17_mK < 0 := by decide

-- ============================================================
-- REMARKS (comment-only)
-- ============================================================

-- [V.P189] EDGES/HERA/SKA Predictions:
-- EDGES: −500 mK reported, 2.4× deeper than τ-prediction. Unconfirmed.
-- HERA: sensitivity ~10 mK at z=8–12; τ predicts transition at z=8.
-- SKA: 21cm power spectrum at z=15–25 probes dark-ages signal.
-- Falsification: confirmed trough > 300 mK below τ-prediction.

-- [V.R470] V.OP9 Status: PARTIAL-IMPROVED.
-- Brightness temperature formula uses exclusively τ-native inputs.
-- Remaining gap: spin coupling function x_α(z) requires
-- astrophysical modelling beyond τ-framework's current scope.

end Tau.BookV.Cosmology
```
