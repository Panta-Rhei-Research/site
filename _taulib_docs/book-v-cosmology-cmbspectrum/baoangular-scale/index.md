---
{
  "projection_kind": "taulib_declaration",
  "title": "BAOAngularScale",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/baoangular-scale/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::BAOAngularScale",
  "declaration_slug": "baoangular-scale",
  "kind": "structure",
  "name": "BAOAngularScale",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 1202,
  "source_line_end": 1209,
  "registry_ids": [
    "V.D275"
  ],
  "related_registry_items": [
    {
      "id": "V.D275",
      "title": "BAO Angular Scale from τ-Native d_A",
      "url": "/registry/object/V.D275/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1202-L1209",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.CMBSpectrum",
        "url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1202-L1209",
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

- Module: [TauLib.BookV.Cosmology.CMBSpectrum](/verify/taulib/docs/book-v-cosmology-cmbspectrum/)
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1202-L1209)
- Source range: L1202-L1209
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D275` — BAO Angular Scale from τ-Native d_A

## Immediate Comment / Docstring

```lean
/-- [V.D275] BAO Angular Scale from τ-Native d_A.
    θ_BAO(z) = r_s/d_A(z). At z=0.5: d_A/r_s=8.85.
    Consistent with DESI DR1 to <310 ppm. -/
```

## Source Excerpt

```lean
structure BAOAngularScale where
  /-- r_s in Mpc × 10 = 1471. -/
  r_s_x10 : Nat := 1471
  /-- d_A/r_s at z=0.5 × 100 = 885. -/
  dA_rs_z05_x100 : Nat := 885
  /-- d_A/r_s at z=1.0 × 100 = 1157. -/
  dA_rs_z10_x100 : Nat := 1157
  deriving Repr
```
