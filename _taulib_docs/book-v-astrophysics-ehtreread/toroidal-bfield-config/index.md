---
{
  "projection_kind": "taulib_declaration",
  "title": "ToroidalBFieldConfig",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-ehtreread/toroidal-bfield-config/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Astrophysics.EHTReread`.",
  "declaration_id": "TauLib.BookV.Astrophysics.EHTReread::ToroidalBFieldConfig",
  "declaration_slug": "toroidal-bfield-config",
  "kind": "structure",
  "name": "ToroidalBFieldConfig",
  "module_name": "TauLib.BookV.Astrophysics.EHTReread",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-ehtreread/",
  "source_line_start": 519,
  "source_line_end": 531,
  "registry_ids": [
    "V.D284"
  ],
  "related_registry_items": [
    {
      "id": "V.D284",
      "title": "Toroidal B-Field Configuration",
      "url": "/registry/object/V.D284/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L519-L531",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.EHTReread",
        "url": "/verify/taulib/docs/book-v-astrophysics-ehtreread/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L519-L531",
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

- Module: [TauLib.BookV.Astrophysics.EHTReread](/verify/taulib/docs/book-v-astrophysics-ehtreread/)
- Source path: [`TauLib/BookV/Astrophysics/EHTReread.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L519-L531)
- Source range: L519-L531
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D284` — Toroidal B-Field Configuration

## Immediate Comment / Docstring

```lean
/-- [V.D284] Toroidal B-Field Configuration: magnetic field geometry
    on T² black hole. Toroidal component dominates by factor ι_τ⁻¹ ≈ 2.93.
    Field ratio is mass-independent, set by torus aspect ratio. -/
```

## Source Excerpt

```lean
structure ToroidalBFieldConfig where
  /-- Toroidal field strength (Gauss × 100). -/
  b_tor_x100 : Nat
  /-- Poloidal field strength (Gauss × 100). -/
  b_pol_x100 : Nat
  /-- Field ratio B_tor/B_pol × 1000. Should be ≈ 2930. -/
  field_ratio_x1000 : Nat := 2930
  /-- Toroidal dominates poloidal. -/
  tor_gt_pol : b_tor_x100 > b_pol_x100
  deriving Repr

instance : Inhabited ToroidalBFieldConfig :=
  ⟨⟨2930, 1000, 2930, by omega⟩⟩
```
