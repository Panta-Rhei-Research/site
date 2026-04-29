---
{
  "projection_kind": "taulib_declaration",
  "title": "bao_from_boundary",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-bullet-cluster-lss/bao-from-boundary/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.BulletClusterLSS`.",
  "declaration_id": "TauLib.BookV.Astrophysics.BulletClusterLSS::bao_from_boundary",
  "declaration_slug": "bao-from-boundary",
  "kind": "theorem",
  "name": "bao_from_boundary",
  "module_name": "TauLib.BookV.Astrophysics.BulletClusterLSS",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-bullet-cluster-lss/",
  "source_line_start": 180,
  "source_line_end": 181,
  "registry_ids": [
    "V.T98"
  ],
  "related_registry_items": [
    {
      "id": "V.T98",
      "title": "Cosmic Web from Holonomy Loops",
      "url": "/registry/object/V.T98/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L180-L181",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L180-L181",
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

- Module: [TauLib.BookV.Astrophysics.BulletClusterLSS](/verify/taulib/docs/book-v-astrophysics-bullet-cluster-lss/)
- Source path: [`TauLib/BookV/Astrophysics/BulletClusterLSS.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L180-L181)
- Source range: L180-L181
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T98` — Cosmic Web from Holonomy Loops

## Immediate Comment / Docstring

```lean
/-- [V.T98] BAO from primordial boundary spectrum: baryon acoustic
    oscillations at ~150 Mpc are frozen sound waves from the
    pre-recombination boundary character spectrum.

    The BAO scale is set by the sound horizon at recombination:
        r_s = ∫₀^{t_rec} c_s(t) dt / (1+z_rec)

    In the τ-framework, this is a readout of the primordial
    defect-density oscillation wavelength at the recombination
    boundary-data surface. -/
```

## Source Excerpt

```lean
theorem bao_from_boundary :
    bao_scale = 150 := rfl
```
