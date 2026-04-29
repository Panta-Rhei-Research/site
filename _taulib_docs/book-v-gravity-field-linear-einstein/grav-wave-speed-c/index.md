---
{
  "projection_kind": "taulib_declaration",
  "title": "grav_wave_speed_c",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-linear-einstein/grav-wave-speed-c/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.LinearEinstein`.",
  "declaration_id": "TauLib.BookV.GravityField.LinearEinstein::grav_wave_speed_c",
  "declaration_slug": "grav-wave-speed-c",
  "kind": "theorem",
  "name": "grav_wave_speed_c",
  "module_name": "TauLib.BookV.GravityField.LinearEinstein",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-linear-einstein/",
  "source_line_start": 287,
  "source_line_end": 288,
  "registry_ids": [
    "V.P14"
  ],
  "related_registry_items": [
    {
      "id": "V.P14",
      "title": "v_mathrmGW",
      "url": "/registry/object/V.P14/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/LinearEinstein.lean#L287-L288",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.LinearEinstein",
        "url": "/verify/taulib/docs/book-v-gravity-field-linear-einstein/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/LinearEinstein.lean#L287-L288",
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

- Module: [TauLib.BookV.GravityField.LinearEinstein](/verify/taulib/docs/book-v-gravity-field-linear-einstein/)
- Source path: [`TauLib/BookV/GravityField/LinearEinstein.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/LinearEinstein.lean#L287-L288)
- Source range: L287-L288
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P14` — v_mathrmGW

## Immediate Comment / Docstring

```lean
/-- [V.P14] Gravitational waves propagate at c.

    GW speed = c follows from null propagation on the base circle τ¹.
    The gravitational wave is a perturbation of the D-sector boundary
    character, and perturbations propagate at the null transport rate.
    Confirmed by LIGO/Virgo GW170817 + GRB 170817A (|Δc/c| < 10⁻¹⁵). -/
```

## Source Excerpt

```lean
theorem grav_wave_speed_c (gw : GravitationalWave) :
    gw.speed_is_c = true := gw.speed_proof
```
