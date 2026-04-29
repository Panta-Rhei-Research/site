---
{
  "projection_kind": "taulib_declaration",
  "title": "m87_shadow_tau_outer_uas",
  "permalink": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/m87-shadow-tau-outer-uas/",
  "summary_short": "`def` declaration in `TauLib.BookV.Gravity.BHTopoModes`.",
  "declaration_id": "TauLib.BookV.Gravity.BHTopoModes::m87_shadow_tau_outer_uas",
  "declaration_slug": "m87-shadow-tau-outer-uas",
  "kind": "def",
  "name": "m87_shadow_tau_outer_uas",
  "module_name": "TauLib.BookV.Gravity.BHTopoModes",
  "module_url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/",
  "source_line_start": 147,
  "source_line_end": 151,
  "registry_ids": [
    "V.P124"
  ],
  "related_registry_items": [
    {
      "id": "V.P124",
      "title": "T² Shadow Radius vs EHT",
      "url": "/registry/object/V.P124/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L147-L151",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Gravity.BHTopoModes",
        "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L147-L151",
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

- Module: [TauLib.BookV.Gravity.BHTopoModes](/verify/taulib/docs/book-v-gravity-bhtopo-modes/)
- Source path: [`TauLib/BookV/Gravity/BHTopoModes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L147-L151)
- Source range: L147-L151
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.P124` — T² Shadow Radius vs EHT

## Immediate Comment / Docstring

```lean
/-- T² outer torus angular size for M87* [microarcseconds].
    θ_outer = 4πGM/(c²·d) · (rad → μas conversion). [V.P124]
    M87*: M = 6.5×10⁹ M_☉, d = 16.8 Mpc.
    Lab value: 48.00 μas (EHT observed: 42 ± 3 μas). -/
```

## Source Excerpt

```lean
def m87_shadow_tau_outer_uas : Float :=
  let M : Float := 6.5e9 * M_sun
  let d : Float := 16.8 * 3.086e22  -- 16.8 Mpc in meters
  let theta_rad : Float := 4.0 * 3.14159265358979 * G_Newton * M / (c_light ^ 2 * d)
  theta_rad * 206265.0e6  -- convert radians to microarcseconds
```
