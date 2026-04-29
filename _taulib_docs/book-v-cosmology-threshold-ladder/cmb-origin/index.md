---
{
  "projection_kind": "taulib_declaration",
  "title": "CmbOrigin",
  "permalink": "/verify/taulib/docs/book-v-cosmology-threshold-ladder/cmb-origin/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.ThresholdLadder`.",
  "declaration_id": "TauLib.BookV.Cosmology.ThresholdLadder::CmbOrigin",
  "declaration_slug": "cmb-origin",
  "kind": "structure",
  "name": "CmbOrigin",
  "module_name": "TauLib.BookV.Cosmology.ThresholdLadder",
  "module_url": "/verify/taulib/docs/book-v-cosmology-threshold-ladder/",
  "source_line_start": 257,
  "source_line_end": 264,
  "registry_ids": [
    "V.P92"
  ],
  "related_registry_items": [
    {
      "id": "V.P92",
      "title": "CMB Origin",
      "url": "/registry/object/V.P92/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/ThresholdLadder.lean#L257-L264",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.ThresholdLadder",
        "url": "/verify/taulib/docs/book-v-cosmology-threshold-ladder/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/ThresholdLadder.lean#L257-L264",
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

- Module: [TauLib.BookV.Cosmology.ThresholdLadder](/verify/taulib/docs/book-v-cosmology-threshold-ladder/)
- Source path: [`TauLib/BookV/Cosmology/ThresholdLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/ThresholdLadder.lean#L257-L264)
- Source range: L257-L264
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.P92` — CMB Origin

## Immediate Comment / Docstring

```lean
/-- [V.P92] CMB origin: the CMB is the photon readout of the
    last-scattering surface at the photon decoupling threshold L_γ.

    Temperature T_CMB ≈ 2.725 K. The last-scattering surface is
    at redshift z ≈ 1100 in chart-level readout coordinates.

    In τ, the CMB is a boundary-character snapshot of the B-sector
    at L_γ depth. -/
```

## Source Excerpt

```lean
structure CmbOrigin where
  /-- CMB temperature × 1000 (in mK). -/
  temp_mK : Nat
  /-- Redshift of last scattering × 10. -/
  redshift_times_10 : Nat
  /-- Temperature is ~ 2725 mK. -/
  temp_range : temp_mK > 2700 ∧ temp_mK < 2750
  deriving Repr
```
