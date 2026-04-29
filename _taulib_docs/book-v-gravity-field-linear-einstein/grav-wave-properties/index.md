---
{
  "projection_kind": "taulib_declaration",
  "title": "grav_wave_properties",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-linear-einstein/grav-wave-properties/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.LinearEinstein`.",
  "declaration_id": "TauLib.BookV.GravityField.LinearEinstein::grav_wave_properties",
  "declaration_slug": "grav-wave-properties",
  "kind": "theorem",
  "name": "grav_wave_properties",
  "module_name": "TauLib.BookV.GravityField.LinearEinstein",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-linear-einstein/",
  "source_line_start": 270,
  "source_line_end": 275,
  "registry_ids": [
    "V.T32"
  ],
  "related_registry_items": [
    {
      "id": "V.T32",
      "title": "Gravitational wave properties",
      "url": "/registry/object/V.T32/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/LinearEinstein.lean#L270-L275",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/LinearEinstein.lean#L270-L275",
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
- Source path: [`TauLib/BookV/GravityField/LinearEinstein.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/LinearEinstein.lean#L270-L275)
- Source range: L270-L275
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T32` — Gravitational wave properties

## Immediate Comment / Docstring

```lean
/-- [V.T32] Gravitational wave properties:
    - Speed: c (null propagation)
    - Polarizations: 2 (plus + cross from T²)
    - Leading multipole: quadrupole (ℓ = 2)
    - Spin: 2 -/
```

## Source Excerpt

```lean
theorem grav_wave_properties :
    canonical_gw.speed_is_c = true ∧
    canonical_gw.polarization_count = 2 ∧
    canonical_gw.leading_multipole = .Quadrupole ∧
    canonical_gw.spin = 2 :=
  ⟨rfl, rfl, rfl, rfl⟩
```
