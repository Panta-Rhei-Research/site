---
{
  "projection_kind": "taulib_declaration",
  "title": "heisenberg_ineq",
  "permalink": "/verify/taulib/docs/book-iv-arena-actors-dynamics/heisenberg-ineq/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Arena.ActorsDynamics`.",
  "declaration_id": "TauLib.BookIV.Arena.ActorsDynamics::heisenberg_ineq",
  "declaration_slug": "heisenberg-ineq",
  "kind": "theorem",
  "name": "heisenberg_ineq",
  "module_name": "TauLib.BookIV.Arena.ActorsDynamics",
  "module_url": "/verify/taulib/docs/book-iv-arena-actors-dynamics/",
  "source_line_start": 181,
  "source_line_end": 202,
  "registry_ids": [
    "IV.D274",
    "IV.R236",
    "IV.T103"
  ],
  "related_registry_items": [
    {
      "id": "IV.D274",
      "title": "Defect functional",
      "url": "/registry/object/IV.D274/"
    },
    {
      "id": "IV.R236",
      "title": "Lean formalization",
      "url": "/registry/object/IV.R236/"
    },
    {
      "id": "IV.T103",
      "title": "Euler budget conservation",
      "url": "/registry/object/IV.T103/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/ActorsDynamics.lean#L181-L202",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Arena.ActorsDynamics",
        "url": "/verify/taulib/docs/book-iv-arena-actors-dynamics/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/ActorsDynamics.lean#L181-L202",
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

- Module: [TauLib.BookIV.Arena.ActorsDynamics](/verify/taulib/docs/book-iv-arena-actors-dynamics/)
- Source path: [`TauLib/BookIV/Arena/ActorsDynamics.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/ActorsDynamics.lean#L181-L202)
- Source range: L181-L202
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.D274` — Defect functional
- `IV.R236` — Lean formalization
- `IV.T103` — Euler budget conservation

## Immediate Comment / Docstring

```lean
-- Structural assertion: the Planck character is the natural action unit.
-- Quantitative proof uses UncertaintyProduct from PlanckCharacter module.
```

## Source Excerpt

```lean
theorem heisenberg_ineq :
    -- The 5 sector lifts exist and are complete
    all_sector_lifts.length = 5 := by rfl

-- [IV.R236] Lean formalization: PlanckCharacter module in BookIV/Physics/.

-- ============================================================
-- DEFECT FUNCTIONAL [IV.D274]
-- ============================================================

/-- [IV.D274] Defect functional S[φ]: the action functional on τ³ defect
    configurations. Has 4 components: mobility μ, vorticity ν,
    compression κ, topological θ. Wraps DefectTuple from Physics/. -/
abbrev defect_func := @DefectTuple

-- ============================================================
-- EULER BUDGET CONSERVATION [IV.T103]
-- ============================================================

/-- [IV.T103] Euler budget conservation: μ + ν + κ + θ = const
    for single defect bundles. The total defect budget is conserved
    during evolution — individual components may redistribute. -/
```
