---
{
  "projection_kind": "taulib_declaration",
  "title": "NearHorizonBField",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-ehtreread/near-horizon-bfield/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Astrophysics.EHTReread`.",
  "declaration_id": "TauLib.BookV.Astrophysics.EHTReread::NearHorizonBField",
  "declaration_slug": "near-horizon-bfield",
  "kind": "structure",
  "name": "NearHorizonBField",
  "module_name": "TauLib.BookV.Astrophysics.EHTReread",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-ehtreread/",
  "source_line_start": 585,
  "source_line_end": 596,
  "registry_ids": [
    "V.D288"
  ],
  "related_registry_items": [
    {
      "id": "V.D288",
      "title": "Near-Horizon B-Field",
      "url": "/registry/object/V.D288/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L585-L596",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L585-L596",
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
- Source path: [`TauLib/BookV/Astrophysics/EHTReread.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L585-L596)
- Source range: L585-L596
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D288` — Near-Horizon B-Field

## Immediate Comment / Docstring

```lean
/-- [V.D288] Near-Horizon B-Field: equipartition magnetic field at photon sphere.
    B_tor/B_pol = ι_τ⁻¹ ≈ 2.93, mass-independent zero-parameter prediction. -/
```

## Source Excerpt

```lean
structure NearHorizonBField where
  /-- Source name. -/
  source : String
  /-- Total equipartition field (Gauss × 100). -/
  b_eq_x100 : Nat
  /-- Toroidal component (Gauss × 100). -/
  b_tor_x100 : Nat
  /-- Poloidal component (Gauss × 100). -/
  b_pol_x100 : Nat
  /-- Field ratio × 1000 (should be ≈ 2930). -/
  ratio_x1000 : Nat := 2930
  deriving Repr
```
