---
{
  "projection_kind": "taulib_declaration",
  "title": "GWSignalData",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-binary-mergers-gw/gwsignal-data/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Astrophysics.BinaryMergersGW`.",
  "declaration_id": "TauLib.BookV.Astrophysics.BinaryMergersGW::GWSignalData",
  "declaration_slug": "gwsignal-data",
  "kind": "structure",
  "name": "GWSignalData",
  "module_name": "TauLib.BookV.Astrophysics.BinaryMergersGW",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-binary-mergers-gw/",
  "source_line_start": 96,
  "source_line_end": 116,
  "registry_ids": [
    "V.D134"
  ],
  "related_registry_items": [
    {
      "id": "V.D134",
      "title": "GW Boundary-Character Wave",
      "url": "/registry/object/V.D134/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L96-L116",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.BinaryMergersGW",
        "url": "/verify/taulib/docs/book-v-astrophysics-binary-mergers-gw/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L96-L116",
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

- Module: [TauLib.BookV.Astrophysics.BinaryMergersGW](/verify/taulib/docs/book-v-astrophysics-binary-mergers-gw/)
- Source path: [`TauLib/BookV/Astrophysics/BinaryMergersGW.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L96-L116)
- Source range: L96-L116
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D134` — GW Boundary-Character Wave

## Immediate Comment / Docstring

```lean
/-- [V.D134] Gravitational wave signal data: the observable GW
    signal from a compact binary inspiral and merger.

    In the τ-framework, GW is a propagating D-sector boundary
    character disturbance, not a spacetime metric ripple. -/
```

## Source Excerpt

```lean
structure GWSignalData where
  /-- Binary type. -/
  binary_type : BinarySystemType
  /-- Component mass 1 (tenths of solar mass). -/
  mass1 : Nat
  /-- Component mass 2 (tenths of solar mass). -/
  mass2 : Nat
  /-- Both masses positive. -/
  mass1_pos : mass1 > 0
  mass2_pos : mass2 > 0
  /-- mass1 >= mass2 by convention. -/
  mass_ordered : mass1 ≥ mass2
  /-- Luminosity distance (Mpc). -/
  distance_mpc : Nat
  /-- Distance positive. -/
  distance_pos : distance_mpc > 0
  /-- Peak frequency (Hz). -/
  peak_freq_hz : Nat
  /-- Peak strain (scaled, 10⁻²¹ × 100). -/
  peak_strain_scaled : Nat
  deriving Repr
```
