---
{
  "projection_kind": "taulib_declaration",
  "title": "clusterScreeningEnhancement",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/cluster-screening-enhancement/",
  "summary_short": "`def` declaration in `TauLib.BookV.Astrophysics.RotationCurves`.",
  "declaration_id": "TauLib.BookV.Astrophysics.RotationCurves::clusterScreeningEnhancement",
  "declaration_slug": "cluster-screening-enhancement",
  "kind": "def",
  "name": "clusterScreeningEnhancement",
  "module_name": "TauLib.BookV.Astrophysics.RotationCurves",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/",
  "source_line_start": 529,
  "source_line_end": 532,
  "registry_ids": [
    "V.D261"
  ],
  "related_registry_items": [
    {
      "id": "V.D261",
      "title": "Cluster-Scale Screening Enhancement",
      "url": "/registry/object/V.D261/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L529-L532",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L529-L532",
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

- Module: [TauLib.BookV.Astrophysics.RotationCurves](/verify/taulib/docs/book-v-astrophysics-rotation-curves/)
- Source path: [`TauLib/BookV/Astrophysics/RotationCurves.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L529-L532)
- Source range: L529-L532
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.D261` — Cluster-Scale Screening Enhancement

## Immediate Comment / Docstring

```lean
/-- [V.D261] Cluster-Scale Screening Enhancement.

    For a point mass M at radius r, the screening enhancement is:
      1 + r/ℓ_τ where ℓ_τ = c/(H₀·√(1−ι_τ)) ≈ 5.5 Mpc.

    At cluster scales (r_c ~ 200 kpc):
      Enhancement = 1 + 200 kpc / 5.5 Mpc ≈ 1.00004
    At galaxy scales (r ~ 10 kpc):
      Enhancement = 1 + 10 kpc / 5.5 Mpc ≈ 1.000002

    Both are essentially unity — the screening factor does NOT
    provide additional correction at cluster scales. The capacity
    mechanism has the same cluster problem as MOND. -/
```

## Source Excerpt

```lean
def clusterScreeningEnhancement : String :=
  "Screening enhancement 1+r/ell_tau ~ 1.00004 at cluster scales. " ++
  "No additional correction beyond galaxy-scale mechanism. " ++
  "Cluster problem comparable to MOND: D_tau ~ 2-4 vs D_obs ~ 5-7."
```
