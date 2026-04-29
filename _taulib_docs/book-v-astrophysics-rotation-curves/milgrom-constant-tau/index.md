---
{
  "projection_kind": "taulib_declaration",
  "title": "milgromConstantTau",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/milgrom-constant-tau/",
  "summary_short": "`def` declaration in `TauLib.BookV.Astrophysics.RotationCurves`.",
  "declaration_id": "TauLib.BookV.Astrophysics.RotationCurves::milgromConstantTau",
  "declaration_slug": "milgrom-constant-tau",
  "kind": "def",
  "name": "milgromConstantTau",
  "module_name": "TauLib.BookV.Astrophysics.RotationCurves",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/",
  "source_line_start": 227,
  "source_line_end": 229,
  "registry_ids": [
    "V.D232"
  ],
  "related_registry_items": [
    {
      "id": "V.D232",
      "title": "Milgrom Constant from tau",
      "url": "/registry/object/V.D232/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L227-L229",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L227-L229",
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
- Source path: [`TauLib/BookV/Astrophysics/RotationCurves.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L227-L229)
- Source range: L227-L229
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.D232` — Milgrom Constant from tau

## Immediate Comment / Docstring

```lean
/-- [V.D232] The Milgrom constant a₀ from the master constant and Hubble rate.
    a₀ = c · H₀ · ι_τ / 2.

    Numerical results (from rotation_curves_lab.py, 50-digit precision):
    - H₀ = 67.4 km/s/Mpc (CMB/Planck): a₀ = 1.118×10⁻¹⁰ m/s²  (-6.9% from MOND)
    - H₀ = 73.0 km/s/Mpc (local/SH0ES): a₀ = 1.211×10⁻¹⁰ m/s²  (+0.9% from MOND)

    The factor ι_τ/2 reflects the two-lobe structure of the τ-boundary L = S¹∨S¹.
    Each lobe contributes c·H₀·ι_τ/4 to the effective acceleration scale. -/
```

## Source Excerpt

```lean
def milgromConstantTau : String :=
  "a_0 = c * H_0 * iota_tau / 2 (connects galactic and cosmic scales, " ++
  "0.9% from MOND with local H_0=73.0 km/s/Mpc)"
```
