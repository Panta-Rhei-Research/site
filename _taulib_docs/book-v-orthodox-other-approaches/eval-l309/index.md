---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L309",
  "permalink": "/verify/taulib/docs/book-v-orthodox-other-approaches/eval-l309/",
  "summary_short": "`eval` declaration in `TauLib.BookV.Orthodox.OtherApproaches`.",
  "declaration_id": "TauLib.BookV.Orthodox.OtherApproaches::#eval:309",
  "declaration_slug": "eval-l309",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.BookV.Orthodox.OtherApproaches",
  "module_url": "/verify/taulib/docs/book-v-orthodox-other-approaches/",
  "source_line_start": 309,
  "source_line_end": 309,
  "registry_ids": [
    "V.R278",
    "V.R279",
    "V.R280",
    "V.R284",
    "V.R285",
    "V.R286"
  ],
  "related_registry_items": [
    {
      "id": "V.R278",
      "title": "LQG's genuine contribution",
      "url": "/registry/object/V.R278/"
    },
    {
      "id": "V.R279",
      "title": "The residual manifold in LQG",
      "url": "/registry/object/V.R279/"
    },
    {
      "id": "V.R280",
      "title": "Four echoes, one architecture",
      "url": "/registry/object/V.R280/"
    },
    {
      "id": "V.R284",
      "title": "Twistors as shadow",
      "url": "/registry/object/V.R284/"
    },
    {
      "id": "V.R285",
      "title": "The two relevant directions",
      "url": "/registry/object/V.R285/"
    },
    {
      "id": "V.R286",
      "title": "Verlinde's rotation curves",
      "url": "/registry/object/V.R286/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/OtherApproaches.lean#L309-L309",
  "formal_status": "computed",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Orthodox.OtherApproaches",
        "url": "/verify/taulib/docs/book-v-orthodox-other-approaches/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/OtherApproaches.lean#L309-L309",
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

- Module: [TauLib.BookV.Orthodox.OtherApproaches](/verify/taulib/docs/book-v-orthodox-other-approaches/)
- Source path: [`TauLib/BookV/Orthodox/OtherApproaches.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/OtherApproaches.lean#L309-L309)
- Source range: L309-L309
- Kind: `eval`
- Formal status hint: `computed`

## Registry Links

- `V.R278` — LQG's genuine contribution
- `V.R279` — The residual manifold in LQG
- `V.R280` — Four echoes, one architecture
- `V.R284` — Twistors as shadow
- `V.R285` — The two relevant directions
- `V.R286` — Verlinde's rotation curves

## Immediate Comment / Docstring

```lean
-- [V.R278] LQG's genuine contribution: spin networks capture the
-- combinatorial structure of the boundary algebra at finite depth.
-- The Barbero-Immirzi parameter is the price of starting from GR
-- rather than from the boundary.

-- [V.R279] The residual manifold in LQG: LQG quantizes GR on a
-- manifold, inheriting the manifold as background structure. tau
-- has no residual manifold; the manifold is a readout.

-- [V.R280] Four echoes, one architecture: string theory (fiber),
-- LQG (discrete combinatorics), CDT (emergent geometry), causal
-- sets (discrete causality) each echo one aspect of tau^3.

-- [V.R284] Twistors as shadow: Penrose's twistor program captures
-- the null structure of spacetime, which in tau is the base circle
-- readout. Twistors are the shadow of the base tau^1.

-- [V.R285] The two relevant directions: only base (temporal) and
-- fiber (spatial) matter. The 6-7 extra string dimensions are an
-- artifact of starting from the wrong fiber.

-- [V.R286] Verlinde's rotation curves: emergent gravity from
-- entropy matches the defect-entropy mechanism in tau. Verlinde's
-- approach is a partial echo of the entropy splitting.

-- ============================================================
-- SMOKE TESTS
-- ============================================================
```

## Source Excerpt

```lean
#eval string_comparison.has_landscape     -- true
```
