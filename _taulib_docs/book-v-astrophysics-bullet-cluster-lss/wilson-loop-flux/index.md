---
{
  "projection_kind": "taulib_declaration",
  "title": "WilsonLoopFlux",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-bullet-cluster-lss/wilson-loop-flux/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Astrophysics.BulletClusterLSS`.",
  "declaration_id": "TauLib.BookV.Astrophysics.BulletClusterLSS::WilsonLoopFlux",
  "declaration_slug": "wilson-loop-flux",
  "kind": "structure",
  "name": "WilsonLoopFlux",
  "module_name": "TauLib.BookV.Astrophysics.BulletClusterLSS",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-bullet-cluster-lss/",
  "source_line_start": 263,
  "source_line_end": 272,
  "registry_ids": [
    "V.D291"
  ],
  "related_registry_items": [
    {
      "id": "V.D291",
      "title": "Wilson Loop Magnetic Flux",
      "url": "/registry/object/V.D291/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L263-L272",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L263-L272",
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
- Source path: [`TauLib/BookV/Astrophysics/BulletClusterLSS.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L263-L272)
- Source range: L263-L272
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D291` — Wilson Loop Magnetic Flux

## Immediate Comment / Docstring

```lean
/-- [V.D291] Wilson Loop Magnetic Flux: magnetic flux carried along
    Wilson skeleton edges (filaments), originating from SMBH poloidal
    flux and transported by frozen-flux invariant. -/
```

## Source Excerpt

```lean
structure WilsonLoopFlux where
  /-- Filament name or identifier. -/
  filament : String
  /-- Filament flux (in units of 10⁻¹⁸ Wb). -/
  flux_x18 : Nat
  /-- Flux originates from SMBH (1 = yes). -/
  from_smbh : Nat := 1
  /-- Topologically protected (1 = yes). -/
  topo_protected : Nat := 1
  deriving Repr
```
