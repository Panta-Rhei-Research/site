---
{
  "projection_kind": "taulib_declaration",
  "title": "PowerSpectrumData",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-bullet-cluster-lss/power-spectrum-data/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Astrophysics.BulletClusterLSS`.",
  "declaration_id": "TauLib.BookV.Astrophysics.BulletClusterLSS::PowerSpectrumData",
  "declaration_slug": "power-spectrum-data",
  "kind": "structure",
  "name": "PowerSpectrumData",
  "module_name": "TauLib.BookV.Astrophysics.BulletClusterLSS",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-bullet-cluster-lss/",
  "source_line_start": 189,
  "source_line_end": 198,
  "registry_ids": [
    "V.D143"
  ],
  "related_registry_items": [
    {
      "id": "V.D143",
      "title": "Topological Lensing Signature",
      "url": "/registry/object/V.D143/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L189-L198",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.BulletClusterLSS",
        "url": "/verify/taulib/docs/book-v-astrophysics-bullet-cluster-lss/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L189-L198",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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

- Module: [TauLib.BookV.Astrophysics.BulletClusterLSS](/verify/taulib/docs/book-v-astrophysics-bullet-cluster-lss/)
- Source path: [`TauLib/BookV/Astrophysics/BulletClusterLSS.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L189-L198)
- Source range: L189-L198
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D143` — Topological Lensing Signature

## Immediate Comment / Docstring

```lean
/-- [V.D143] Power spectrum data: the matter power spectrum P(k)
    encoding the amplitude of density fluctuations at each scale k. -/
```

## Source Excerpt

```lean
structure PowerSpectrumData where
  /-- Spectral index n_s (scaled × 1000). -/
  spectral_index_scaled : Nat
  /-- σ₈: amplitude at 8 Mpc/h (scaled × 1000). -/
  sigma8_scaled : Nat
  /-- BAO peak position (h/Mpc, scaled × 1000). -/
  bao_peak_scaled : Nat
  /-- Whether the spectrum is consistent with Planck. -/
  planck_consistent : Bool := true
  deriving Repr
```
