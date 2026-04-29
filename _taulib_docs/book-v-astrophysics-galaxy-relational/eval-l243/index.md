---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L243",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-galaxy-relational/eval-l243/",
  "summary_short": "`eval` declaration in `TauLib.BookV.Astrophysics.GalaxyRelational`.",
  "declaration_id": "TauLib.BookV.Astrophysics.GalaxyRelational::#eval:243",
  "declaration_slug": "eval-l243",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.BookV.Astrophysics.GalaxyRelational",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-galaxy-relational/",
  "source_line_start": 243,
  "source_line_end": 243,
  "registry_ids": [
    "V.R169",
    "V.R170",
    "V.R171",
    "V.R172",
    "V.R173"
  ],
  "related_registry_items": [
    {
      "id": "V.R169",
      "title": "No void between galaxies",
      "url": "/registry/object/V.R169/"
    },
    {
      "id": "V.R170",
      "title": "Conjectural scope",
      "url": "/registry/object/V.R170/"
    },
    {
      "id": "V.R171",
      "title": "Filaments are not gravitational wakes",
      "url": "/registry/object/V.R171/"
    },
    {
      "id": "V.R172",
      "title": "Morphology is not destiny",
      "url": "/registry/object/V.R172/"
    },
    {
      "id": "V.R173",
      "title": "Satellite planes and the missing satellite problem",
      "url": "/registry/object/V.R173/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L243-L243",
  "formal_status": "computed",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.GalaxyRelational",
        "url": "/verify/taulib/docs/book-v-astrophysics-galaxy-relational/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L243-L243",
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

- Module: [TauLib.BookV.Astrophysics.GalaxyRelational](/verify/taulib/docs/book-v-astrophysics-galaxy-relational/)
- Source path: [`TauLib/BookV/Astrophysics/GalaxyRelational.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L243-L243)
- Source range: L243-L243
- Kind: `eval`
- Formal status hint: `computed`

## Registry Links

- `V.R169` — No void between galaxies
- `V.R170` — Conjectural scope
- `V.R171` — Filaments are not gravitational wakes
- `V.R172` — Morphology is not destiny
- `V.R173` — Satellite planes and the missing satellite problem

## Immediate Comment / Docstring

```lean
-- ============================================================
-- REMARKS (comment-only)
-- ============================================================

-- [V.R169] No Dark Matter Particle: the τ-framework predicts that
-- no dark matter particle will ever be found in direct detection
-- experiments. The "missing mass" is a readout artifact of applying
-- Newtonian gravity (depth 1) beyond its validity regime.

-- [V.R170] Ellipticals as Relaxed Bundles: elliptical galaxies are
-- relaxed (isotropized) defect bundles that have lost their disk
-- and spiral structure through mergers and dynamical friction.

-- [V.R171] Baryonic Tully-Fisher Preferred: the baryonic (not total)
-- Tully-Fisher relation is tighter because the τ-framework couples
-- rotation to baryonic content, not to any "dark" component.

-- [V.R172] Cluster as Multi-Bundle System: a galaxy cluster is a
-- multi-bundle system whose dynamics involves inter-bundle
-- D-sector couplings — a higher-order readout than single-galaxy
-- dynamics.

-- [V.R173] Dark Matter as Missing Readout Correction: "dark matter"
-- is the name orthodox physics gives to the boundary correction
-- terms it is missing. The correction is real; the particles are not.

-- ============================================================
-- SMOKE TESTS
-- ============================================================
```

## Source Excerpt

```lean
#eval milky_way.morphology       -- BarredSpiral
```
