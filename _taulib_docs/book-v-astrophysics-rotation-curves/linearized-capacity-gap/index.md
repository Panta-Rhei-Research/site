---
{
  "projection_kind": "taulib_declaration",
  "title": "linearizedCapacityGap",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/linearized-capacity-gap/",
  "summary_short": "`def` declaration in `TauLib.BookV.Astrophysics.RotationCurves`.",
  "declaration_id": "TauLib.BookV.Astrophysics.RotationCurves::linearizedCapacityGap",
  "declaration_slug": "linearized-capacity-gap",
  "kind": "def",
  "name": "linearizedCapacityGap",
  "module_name": "TauLib.BookV.Astrophysics.RotationCurves",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/",
  "source_line_start": 448,
  "source_line_end": 451,
  "registry_ids": [
    "V.D259"
  ],
  "related_registry_items": [
    {
      "id": "V.D259",
      "title": "Linearized Capacity Gap",
      "url": "/registry/object/V.D259/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L448-L451",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L448-L451",
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
- Source path: [`TauLib/BookV/Astrophysics/RotationCurves.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L448-L451)
- Source range: L448-L451
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.D259` — Linearized Capacity Gap

## Immediate Comment / Docstring

```lean
/-- [V.D259] The linearized capacity gap.

    v_T85 / v_screen = (c²·ℓ_τ/(2·G·M))^{1/4} ≈ 2000 (NGC 3198)
    The c² factor in V.T85 does NOT emerge from the linearized PDE.
    Resolution: full nonlinear τ-Einstein metric coupling provides c².
    V.P67 scope remains conjectural pending nonlinear PDE solution. -/
```

## Source Excerpt

```lean
def linearizedCapacityGap : String :=
  "v_T85/v_screen = (c^2*ell_tau/(2GM))^(1/4) ~ 2000. " ++
  "c^2 enters through metric coupling, not scalar perturbation. " ++
  "Full nonlinear tau-Einstein PDE is the key open problem."
```
