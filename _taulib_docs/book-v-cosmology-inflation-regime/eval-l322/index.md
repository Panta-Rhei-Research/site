---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L322",
  "permalink": "/verify/taulib/docs/book-v-cosmology-inflation-regime/eval-l322/",
  "summary_short": "`eval` declaration in `TauLib.BookV.Cosmology.InflationRegime`.",
  "declaration_id": "TauLib.BookV.Cosmology.InflationRegime::#eval:322",
  "declaration_slug": "eval-l322",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.BookV.Cosmology.InflationRegime",
  "module_url": "/verify/taulib/docs/book-v-cosmology-inflation-regime/",
  "source_line_start": 322,
  "source_line_end": 322,
  "registry_ids": [
    "V.R214",
    "V.R216"
  ],
  "related_registry_items": [
    {
      "id": "V.R214",
      "title": "Contrast with running couplings",
      "url": "/registry/object/V.R214/"
    },
    {
      "id": "V.R216",
      "title": "Compactness vs. inflation",
      "url": "/registry/object/V.R216/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/InflationRegime.lean#L322-L322",
  "formal_status": "computed",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.InflationRegime",
        "url": "/verify/taulib/docs/book-v-cosmology-inflation-regime/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/InflationRegime.lean#L322-L322",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "eval",
      "status": "computed"
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

- Module: [TauLib.BookV.Cosmology.InflationRegime](/verify/taulib/docs/book-v-cosmology-inflation-regime/)
- Source path: [`TauLib/BookV/Cosmology/InflationRegime.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/InflationRegime.lean#L322-L322)
- Source range: L322-L322
- Kind: `eval`
- Formal status hint: `computed`

## Registry Links

- `V.R214` — Contrast with running couplings
- `V.R216` — Compactness vs. inflation

## Immediate Comment / Docstring

```lean
-- ============================================================
-- REMARKS (comment-only)
-- ============================================================

-- [V.R214] Contrast with running couplings: in the Standard Model,
-- couplings run with energy scale (e.g., asymptotic freedom). In τ,
-- κ_τ is FIXED; what changes is the boundary character magnitude.
-- The "running" is in the boundary character, not the coupling.

-- [V.R216] Compactness vs. inflation: orthodox inflation solves the
-- horizon problem dynamically (rapid expansion stretches a small
-- region), requiring a specific inflaton potential. τ solves it
-- topologically: τ¹ is compact (all at finite distance). The two
-- solutions are structurally different.

-- ============================================================
-- SMOKE TESTS
-- ============================================================
```

## Source Excerpt

```lean
#eval canonical_efolds.efolds_times_10    -- 600
```
