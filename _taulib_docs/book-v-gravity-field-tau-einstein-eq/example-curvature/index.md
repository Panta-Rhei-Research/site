---
{
  "projection_kind": "taulib_declaration",
  "title": "example_curvature",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-tau-einstein-eq/example-curvature/",
  "summary_short": "`def` declaration in `TauLib.BookV.GravityField.TauEinsteinEq`.",
  "declaration_id": "TauLib.BookV.GravityField.TauEinsteinEq::example_curvature",
  "declaration_slug": "example-curvature",
  "kind": "def",
  "name": "example_curvature",
  "module_name": "TauLib.BookV.GravityField.TauEinsteinEq",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-tau-einstein-eq/",
  "source_line_start": 271,
  "source_line_end": 276,
  "registry_ids": [
    "V.R65",
    "V.R67",
    "V.R68"
  ],
  "related_registry_items": [
    {
      "id": "V.R65",
      "title": "The GR coupling kappa_tau --- V.D05",
      "url": "/registry/object/V.R65/"
    },
    {
      "id": "V.R67",
      "title": "Singularities are chart artifacts",
      "url": "/registry/object/V.R67/"
    },
    {
      "id": "V.R68",
      "title": "No admissible refinement without compensation",
      "url": "/registry/object/V.R68/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauEinsteinEq.lean#L271-L276",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.TauEinsteinEq",
        "url": "/verify/taulib/docs/book-v-gravity-field-tau-einstein-eq/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauEinsteinEq.lean#L271-L276",
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

- Module: [TauLib.BookV.GravityField.TauEinsteinEq](/verify/taulib/docs/book-v-gravity-field-tau-einstein-eq/)
- Source path: [`TauLib/BookV/GravityField/TauEinsteinEq.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauEinsteinEq.lean#L271-L276)
- Source range: L271-L276
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.R65` — The GR coupling kappa_tau --- V.D05
- `V.R67` — Singularities are chart artifacts
- `V.R68` — No admissible refinement without compensation

## Immediate Comment / Docstring

```lean
-- ============================================================
-- [V.R65] κ_τ UNIQUENESS
-- ============================================================

-- [V.R65] κ_τ is the unique unpolarized coupling constant in the
-- τ-Einstein equation. Uniqueness follows from field cancellation:
-- any two couplings satisfying the Einstein identity must agree
-- at the canonical carrier x* where T^mat ≠ 0.

-- ============================================================
-- [V.R67] SINGULARITIES AS CHART ARTIFACTS
-- ============================================================

-- [V.R67] Orthodox GR singularities (Schwarzschild, Kerr, Big Bang)
-- are artifacts of the chart readout functor, NOT features of the
-- τ-ontology. The boundary-character identity R^H = κ_τ · T^mat
-- is everywhere well-defined in H_∂[n]. "Singular" = chart breakdown.

-- ============================================================
-- [V.R68] MATTER-CURVATURE COUPLING
-- ============================================================

-- [V.R68] The coupling between matter and curvature in the
-- τ-framework is NOT mediated by a metric — it is a direct
-- identity between boundary characters. "Geometry bends" is a
-- readout metaphor; ontologically, holonomy defects change.

-- ============================================================
-- SMOKE TESTS
-- ============================================================

-- Example curvature character
```

## Source Excerpt

```lean
def example_curvature : CurvatureCharH where
  defect_numer := 658541    -- κ_τ times some matter value
  defect_denom := 1000000
  denom_pos := by omega
  depth := 10
  depth_pos := by omega
```
