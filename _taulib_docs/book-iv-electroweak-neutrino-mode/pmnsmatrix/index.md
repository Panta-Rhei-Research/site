---
{
  "projection_kind": "taulib_declaration",
  "title": "PMNSMatrix",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/pmnsmatrix/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.NeutrinoMode`.",
  "declaration_id": "TauLib.BookIV.Electroweak.NeutrinoMode::PMNSMatrix",
  "declaration_slug": "pmnsmatrix",
  "kind": "structure",
  "name": "PMNSMatrix",
  "module_name": "TauLib.BookIV.Electroweak.NeutrinoMode",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/",
  "source_line_start": 211,
  "source_line_end": 224,
  "registry_ids": [
    "IV.D126"
  ],
  "related_registry_items": [
    {
      "id": "IV.D126",
      "title": "PMNS Matrix",
      "url": "/registry/object/IV.D126/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L211-L224",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.NeutrinoMode",
        "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L211-L224",
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

- Module: [TauLib.BookIV.Electroweak.NeutrinoMode](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/)
- Source path: [`TauLib/BookIV/Electroweak/NeutrinoMode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L211-L224)
- Source range: L211-L224
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D126` — PMNS Matrix

## Immediate Comment / Docstring

```lean
/-- [IV.D126] The PMNS (Pontecorvo-Maki-Nakagawa-Sakata) mixing matrix:
    a 3x3 unitary matrix relating flavor eigenstates to mass eigenstates.
    Parameterized by 3 mixing angles and 1 CP-violating phase.
    In the tau-framework, the mixing arises from the mismatch between
    the A-sector coupling basis and the mass eigenstate basis. -/
```

## Source Excerpt

```lean
structure PMNSMatrix where
  /-- Number of mixing angles. -/
  num_angles : Nat
  angles_eq : num_angles = 3
  /-- Number of CP phases (Dirac). -/
  num_cp_phases : Nat
  cp_eq : num_cp_phases = 1
  /-- Matrix dimension (3x3). -/
  dim : Nat
  dim_eq : dim = 3
  /-- Unitarity (structural flag). -/
  unitary : Bool
  unitary_true : unitary = true
  deriving Repr
```
