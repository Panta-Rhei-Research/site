---
{
  "projection_kind": "taulib_declaration",
  "title": "GravitationalWave",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-linear-einstein/gravitational-wave/",
  "summary_short": "`structure` declaration in `TauLib.BookV.GravityField.LinearEinstein`.",
  "declaration_id": "TauLib.BookV.GravityField.LinearEinstein::GravitationalWave",
  "declaration_slug": "gravitational-wave",
  "kind": "structure",
  "name": "GravitationalWave",
  "module_name": "TauLib.BookV.GravityField.LinearEinstein",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-linear-einstein/",
  "source_line_start": 133,
  "source_line_end": 150,
  "registry_ids": [
    "V.D53"
  ],
  "related_registry_items": [
    {
      "id": "V.D53",
      "title": "Gravitational wave in tau-framework",
      "url": "/registry/object/V.D53/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/LinearEinstein.lean#L133-L150",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/LinearEinstein.lean#L133-L150",
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

- Module: [TauLib.BookV.GravityField.LinearEinstein](/verify/taulib/docs/book-v-gravity-field-linear-einstein/)
- Source path: [`TauLib/BookV/GravityField/LinearEinstein.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/LinearEinstein.lean#L133-L150)
- Source range: L133-L150
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D53` — Gravitational wave in tau-framework

## Immediate Comment / Docstring

```lean
/-- [V.D53] Gravitational wave: propagating solution of the
    linearized τ-Einstein equation.

    Properties determined by τ³ structure:
    - Speed: c (null propagation, from base circle τ¹)
    - Polarizations: 2 (plus + cross, from fiber T²)
    - Leading multipole: quadrupole (ℓ = 2)
    - Spin: 2 (from tensor structure of h_μν perturbation) -/
```

## Source Excerpt

```lean
structure GravitationalWave where
  /-- Propagation speed is c (light speed). -/
  speed_is_c : Bool
  /-- Must propagate at c. -/
  speed_proof : speed_is_c = true
  /-- Number of polarization modes. -/
  polarization_count : Nat
  /-- Exactly 2 polarizations. -/
  two_polarizations : polarization_count = 2
  /-- Leading radiation pattern. -/
  leading_multipole : RadiationPattern
  /-- Leading order is quadrupole. -/
  is_quadrupole : leading_multipole = .Quadrupole
  /-- Spin of the gravitational wave (= 2). -/
  spin : Nat
  /-- Spin is 2. -/
  spin_is_two : spin = 2
  deriving Repr
```
