---
{
  "projection_kind": "taulib_declaration",
  "title": "GalaxyBenchmark",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/galaxy-benchmark/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Astrophysics.RotationCurves`.",
  "declaration_id": "TauLib.BookV.Astrophysics.RotationCurves::GalaxyBenchmark",
  "declaration_slug": "galaxy-benchmark",
  "kind": "structure",
  "name": "GalaxyBenchmark",
  "module_name": "TauLib.BookV.Astrophysics.RotationCurves",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/",
  "source_line_start": 374,
  "source_line_end": 389,
  "registry_ids": [
    "V.D258"
  ],
  "related_registry_items": [
    {
      "id": "V.D258",
      "title": "20-Galaxy Benchmark Table",
      "url": "/registry/object/V.D258/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L374-L389",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L374-L389",
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

- Module: [TauLib.BookV.Astrophysics.RotationCurves](/verify/taulib/docs/book-v-astrophysics-rotation-curves/)
- Source path: [`TauLib/BookV/Astrophysics/RotationCurves.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L374-L389)
- Source range: L374-L389
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D258` — 20-Galaxy Benchmark Table

## Immediate Comment / Docstring

```lean
/-- [V.D258] 20-Galaxy Benchmark: systematic test of V.T85 across
    the galaxy mass spectrum from dwarfs (DDO 154, 5×10⁷ M☉) to
    giant spirals (NGC 2841, 9×10¹⁰ M☉).

    Results (V.T85, Planck H₀):
    - RMS scatter: 0.067 dex (20 galaxies, zero free parameters)
    - Mean offset: −0.043 dex (systematic underprediction ~10%)
    - BTFR slope: 3.991 (theory: 4.000)
    - No mass-dependent systematic (correlation r = +0.21) -/
```

## Source Excerpt

```lean
structure GalaxyBenchmark where
  /-- Number of galaxies in benchmark. -/
  n_galaxies : Nat
  /-- RMS scatter in dex (log₁₀(v_pred/v_obs)), scaled ×10000. -/
  rms_scatter_x10000 : Nat
  /-- Mean offset in dex, scaled ×10000 (negative = underprediction). -/
  mean_offset_x10000 : Nat
  /-- BTFR slope ×1000. -/
  btfr_slope_x1000 : Nat
  /-- Mass-correlation coefficient ×10000 (unsigned). -/
  mass_corr_x10000 : Nat
  /-- 20 galaxies tested. -/
  sufficient_sample : n_galaxies ≥ 20
  /-- RMS scatter below 0.10 dex. -/
  low_scatter : rms_scatter_x10000 < 1000
  deriving Repr
```
