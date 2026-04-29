---
{
  "projection_kind": "taulib_declaration",
  "title": "AddressPrecision",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-craddress-space/address-precision/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.QuantumMechanics.CRAddressSpace`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.CRAddressSpace::AddressPrecision",
  "declaration_slug": "address-precision",
  "kind": "structure",
  "name": "AddressPrecision",
  "module_name": "TauLib.BookIV.QuantumMechanics.CRAddressSpace",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-craddress-space/",
  "source_line_start": 138,
  "source_line_end": 149,
  "registry_ids": [
    "IV.D53"
  ],
  "related_registry_items": [
    {
      "id": "IV.D53",
      "title": "Address Precision (ch16)",
      "url": "/registry/object/IV.D53/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L138-L149",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L138-L149",
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
- Source path: [`TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L138-L149)
- Source range: L138-L149
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D53` — Address Precision (ch16)

## Immediate Comment / Docstring

```lean
/-- [IV.D53] Address precision P(f) = sup |f_hat_{m,n}|^2 in (0,1].
    How sharply a state f is localized at a particular address.
    Represented as a scaled rational (numer, denom). -/
```

## Source Excerpt

```lean
structure AddressPrecision where
  /-- Precision numerator (scaled). -/
  numer : Nat
  /-- Precision denominator. -/
  denom : Nat
  /-- Denominator positive. -/
  denom_pos : denom > 0
  /-- Precision in (0,1]: numer > 0. -/
  numer_pos : numer > 0
  /-- Precision in (0,1]: numer <= denom. -/
  numer_le_denom : numer ≤ denom
  deriving Repr
```
