---
{
  "projection_kind": "taulib_declaration",
  "title": "CharacterMode",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-craddress-space/character-mode/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.QuantumMechanics.CRAddressSpace`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.CRAddressSpace::CharacterMode",
  "declaration_slug": "character-mode",
  "kind": "structure",
  "name": "CharacterMode",
  "module_name": "TauLib.BookIV.QuantumMechanics.CRAddressSpace",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-craddress-space/",
  "source_line_start": 115,
  "source_line_end": 129,
  "registry_ids": [
    "IV.D51",
    "IV.D52"
  ],
  "related_registry_items": [
    {
      "id": "IV.D51",
      "title": "Character Modes",
      "url": "/registry/object/IV.D51/"
    },
    {
      "id": "IV.D52",
      "title": "CR-Address",
      "url": "/registry/object/IV.D52/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L115-L129",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.QuantumMechanics.CRAddressSpace",
        "url": "/verify/taulib/docs/book-iv-quantum-mechanics-craddress-space/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L115-L129",
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

- Module: [TauLib.BookIV.QuantumMechanics.CRAddressSpace](/verify/taulib/docs/book-iv-quantum-mechanics-craddress-space/)
- Source path: [`TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L115-L129)
- Source range: L115-L129
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D51` — Character Modes
- `IV.D52` — CR-Address

## Immediate Comment / Docstring

```lean
/-- [IV.D51] Character mode chi_{m,n}(theta_gamma, theta_eta) =
    exp(i(m*theta_gamma + n*theta_eta)) for (m,n) in Z^2.
    The Fourier mode on T^2 fiber. -/
```

## Source Excerpt

```lean
structure CharacterMode where
  /-- Winding number along gamma-circle. -/
  m : Int
  /-- Winding number along eta-circle. -/
  n : Int
  deriving Repr, DecidableEq, BEq

-- ============================================================
-- CR-ADDRESS [IV.D52]
-- ============================================================

/-- [IV.D52] CR-address: a pair (m, n) in Z^2 identifying a specific
    character mode on T^2. The address encodes the "quantum numbers"
    of a state on the fiber torus. -/
abbrev CRAddress := CharacterMode
```
