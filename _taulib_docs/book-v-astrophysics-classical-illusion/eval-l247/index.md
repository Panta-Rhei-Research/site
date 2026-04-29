---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L247",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-classical-illusion/eval-l247/",
  "summary_short": "`eval` declaration in `TauLib.BookV.Astrophysics.ClassicalIllusion`.",
  "declaration_id": "TauLib.BookV.Astrophysics.ClassicalIllusion::#eval:247",
  "declaration_slug": "eval-l247",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.BookV.Astrophysics.ClassicalIllusion",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-classical-illusion/",
  "source_line_start": 247,
  "source_line_end": 247,
  "registry_ids": [
    "V.R161",
    "V.R162",
    "V.R163",
    "V.R164"
  ],
  "related_registry_items": [
    {
      "id": "V.R161",
      "title": "The three conditions quantified",
      "url": "/registry/object/V.R161/"
    },
    {
      "id": "V.R162",
      "title": "The MOND scale as proxy",
      "url": "/registry/object/V.R162/"
    },
    {
      "id": "V.R163",
      "title": "No free parameters",
      "url": "/registry/object/V.R163/"
    },
    {
      "id": "V.R164",
      "title": "The dark matter debate is a projection artifact",
      "url": "/registry/object/V.R164/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/ClassicalIllusion.lean#L247-L247",
  "formal_status": "computed",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.ClassicalIllusion",
        "url": "/verify/taulib/docs/book-v-astrophysics-classical-illusion/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/ClassicalIllusion.lean#L247-L247",
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

- Module: [TauLib.BookV.Astrophysics.ClassicalIllusion](/verify/taulib/docs/book-v-astrophysics-classical-illusion/)
- Source path: [`TauLib/BookV/Astrophysics/ClassicalIllusion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/ClassicalIllusion.lean#L247-L247)
- Source range: L247-L247
- Kind: `eval`
- Formal status hint: `computed`

## Registry Links

- `V.R161` — The three conditions quantified
- `V.R162` — The MOND scale as proxy
- `V.R163` — No free parameters
- `V.R164` — The dark matter debate is a projection artifact

## Immediate Comment / Docstring

```lean
-- ============================================================
-- REMARKS (comment-only)
-- ============================================================

-- [V.R161] Newton as Readout: F = ma is not a fundamental law but a
-- coarse-grained readout of the D-sector coupling at low energy.
-- The "force" F is the sector coupling gradient, "mass" m is the
-- defect-resistance index, "acceleration" a is the readout-level
-- trajectory curvature.

-- [V.R162] Inertia from Defect Persistence: inertia (resistance to
-- acceleration) is the defect bundle's tendency to maintain its
-- current refinement-tower configuration. The more massive an object,
-- the more defect cost is required to change its trajectory.

-- [V.R163] Hamilton-Jacobi as Character Flow: the Hamilton-Jacobi
-- equation S_t + H(q, ∂S/∂q) = 0 is a character flow equation on the
-- D-sector boundary. The generating function S is the boundary
-- character integrated along the classical path.

-- [V.R164] No Hidden Variables Needed: the τ-framework is deterministic
-- at the arena level. Classical mechanics looks deterministic because
-- it IS a faithful readout (at the coarse-grained level). Quantum
-- mechanics looks probabilistic because it reads out fiber modes
-- where address obstruction prevents simultaneous sharp readouts.

-- ============================================================
-- SMOKE TESTS
-- ============================================================
```

## Source Excerpt

```lean
#eval newtonian_readout.cutoff_depth       -- 1
```
