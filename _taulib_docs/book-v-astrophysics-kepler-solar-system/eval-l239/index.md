---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L239",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/eval-l239/",
  "summary_short": "`eval` declaration in `TauLib.BookV.Astrophysics.KeplerSolarSystem`.",
  "declaration_id": "TauLib.BookV.Astrophysics.KeplerSolarSystem::#eval:239",
  "declaration_slug": "eval-l239",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.BookV.Astrophysics.KeplerSolarSystem",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/",
  "source_line_start": 239,
  "source_line_end": 239,
  "registry_ids": [
    "V.R165",
    "V.R166",
    "V.R167",
    "V.R168"
  ],
  "related_registry_items": [
    {
      "id": "V.R165",
      "title": "Second law is deeper than the first",
      "url": "/registry/object/V.R165/"
    },
    {
      "id": "V.R166",
      "title": "Kepler as theorem, not phenomenology",
      "url": "/registry/object/V.R166/"
    },
    {
      "id": "V.R167",
      "title": "All three tests pass with zero fitting",
      "url": "/registry/object/V.R167/"
    },
    {
      "id": "V.R168",
      "title": "Heliophysics as readout of H_partial[omega",
      "url": "/registry/object/V.R168/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/KeplerSolarSystem.lean#L239-L239",
  "formal_status": "computed",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.KeplerSolarSystem",
        "url": "/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/KeplerSolarSystem.lean#L239-L239",
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

- Module: [TauLib.BookV.Astrophysics.KeplerSolarSystem](/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/)
- Source path: [`TauLib/BookV/Astrophysics/KeplerSolarSystem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/KeplerSolarSystem.lean#L239-L239)
- Source range: L239-L239
- Kind: `eval`
- Formal status hint: `computed`

## Registry Links

- `V.R165` — Second law is deeper than the first
- `V.R166` — Kepler as theorem, not phenomenology
- `V.R167` — All three tests pass with zero fitting
- `V.R168` — Heliophysics as readout of H_partial[omega

## Immediate Comment / Docstring

```lean
-- ============================================================
-- REMARKS (comment-only)
-- ============================================================

-- [V.R165] Perihelion Precession as Post-Newtonian: Mercury's
-- 43"/century precession is the depth-2 correction to the D-sector
-- coupling. It is NOT a separate "relativistic" effect but the
-- next term in the refinement tower expansion.

-- [V.R166] Roche Limit as Defect Threshold: the Roche limit is the
-- distance at which the tidal defect cost exceeds the internal
-- cohesion budget of an extended object. Below this distance,
-- the object is disrupted.

-- [V.R167] Bode's Law as Approximate Readout: the Titius-Bode law
-- is an approximate pattern in the refinement tower, not a deep
-- structural feature. It works approximately because the D-sector
-- coupling has approximate scale invariance at depth 1.

-- [V.R168] Tidal Locking as Defect Equilibrium: tidal locking
-- (e.g. Moon always showing one face) is the defect-equilibrium
-- state where the tidal dissipation cost is minimized.

-- ============================================================
-- SMOKE TESTS
-- ============================================================
```

## Source Excerpt

```lean
#eval earth_orbit.semimajor_axis      -- 1000
```
