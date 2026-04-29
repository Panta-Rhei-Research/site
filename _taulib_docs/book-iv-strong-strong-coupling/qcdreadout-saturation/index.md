---
{
  "projection_kind": "taulib_declaration",
  "title": "QCDReadoutSaturation",
  "permalink": "/verify/taulib/docs/book-iv-strong-strong-coupling/qcdreadout-saturation/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.StrongCoupling`.",
  "declaration_id": "TauLib.BookIV.Strong.StrongCoupling::QCDReadoutSaturation",
  "declaration_slug": "qcdreadout-saturation",
  "kind": "structure",
  "name": "QCDReadoutSaturation",
  "module_name": "TauLib.BookIV.Strong.StrongCoupling",
  "module_url": "/verify/taulib/docs/book-iv-strong-strong-coupling/",
  "source_line_start": 196,
  "source_line_end": 203,
  "registry_ids": [
    "IV.P111"
  ],
  "related_registry_items": [
    {
      "id": "IV.P111",
      "title": "Λ_QCD as readout saturation",
      "url": "/registry/object/IV.P111/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongCoupling.lean#L196-L203",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Strong.StrongCoupling",
        "url": "/verify/taulib/docs/book-iv-strong-strong-coupling/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongCoupling.lean#L196-L203",
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

- Module: [TauLib.BookIV.Strong.StrongCoupling](/verify/taulib/docs/book-iv-strong-strong-coupling/)
- Source path: [`TauLib/BookIV/Strong/StrongCoupling.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongCoupling.lean#L196-L203)
- Source range: L196-L203
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P111` — Λ_QCD as readout saturation

## Immediate Comment / Docstring

```lean
/-- [IV.P111] Lambda_QCD is the energy at which the readout functor
    R_C(mu^2) ceases to be injective on the boundary algebra.
    Below this scale, multiple boundary states project to the same
    measured value: confinement at the readout level. -/
```

## Source Excerpt

```lean
structure QCDReadoutSaturation where
  /-- Lambda_QCD is readout saturation point. -/
  saturation_point : Bool := true
  /-- Below saturation: readout non-injective. -/
  non_injective_below : Bool := true
  /-- Interpretation: confinement at readout level. -/
  interpretation : String := "readout-level confinement"
  deriving Repr
```
