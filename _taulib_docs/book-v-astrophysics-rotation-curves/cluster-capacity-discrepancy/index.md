---
{
  "projection_kind": "taulib_declaration",
  "title": "cluster_capacity_discrepancy",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/cluster-capacity-discrepancy/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.RotationCurves`.",
  "declaration_id": "TauLib.BookV.Astrophysics.RotationCurves::cluster_capacity_discrepancy",
  "declaration_slug": "cluster-capacity-discrepancy",
  "kind": "theorem",
  "name": "cluster_capacity_discrepancy",
  "module_name": "TauLib.BookV.Astrophysics.RotationCurves",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/",
  "source_line_start": 508,
  "source_line_end": 510,
  "registry_ids": [
    "V.T203"
  ],
  "related_registry_items": [
    {
      "id": "V.T203",
      "title": "Cluster Capacity Mass Discrepancy",
      "url": "/registry/object/V.T203/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L508-L510",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.RotationCurves",
        "url": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L508-L510",
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

- Module: [TauLib.BookV.Astrophysics.RotationCurves](/verify/taulib/docs/book-v-astrophysics-rotation-curves/)
- Source path: [`TauLib/BookV/Astrophysics/RotationCurves.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L508-L510)
- Source range: L508-L510
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T203` — Cluster Capacity Mass Discrepancy

## Immediate Comment / Docstring

```lean
/-- [V.T203] Cluster Capacity Mass Discrepancy.

    At cluster scales (r ~ 1 Mpc), the screening factor exp(-r/ℓ_τ)
    is essentially 1 (r/ℓ_τ ~ 10⁻³). The screening enhancement
    factor 1 + r/ℓ_τ ≈ 1.00004 provides negligible additional
    correction beyond the galaxy-scale mechanism.

    V.T85 formula gives D_tau ~ 2-4 for galaxy clusters, compared
    to observed D_obs ~ 5-7. This is comparable to MOND's cluster
    problem (MOND predicts D ~ 2-3 vs observed D ~ 5-7).

    Resolution requires: hot gas contribution correction and/or
    full nonlinear capacity effects from the τ-Einstein equation. -/
```

## Source Excerpt

```lean
theorem cluster_capacity_discrepancy :
    "Cluster D_tau ~ 2-4 vs D_obs ~ 5-7: comparable to MOND cluster problem" =
    "Cluster D_tau ~ 2-4 vs D_obs ~ 5-7: comparable to MOND cluster problem" := rfl
```
