---
{
  "projection_kind": "taulib_declaration",
  "title": "ClopenLocalization",
  "permalink": "/corpus/taulib/docs/book-iv-quantum-mechanics-address-obstruction/clopen-localization/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.QuantumMechanics.AddressObstruction`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.AddressObstruction::ClopenLocalization",
  "declaration_slug": "clopen-localization",
  "kind": "structure",
  "name": "ClopenLocalization",
  "module_name": "TauLib.BookIV.QuantumMechanics.AddressObstruction",
  "module_url": "/corpus/taulib/docs/book-iv-quantum-mechanics-address-obstruction/",
  "source_line_start": 114,
  "source_line_end": 123,
  "registry_ids": [
    "IV.D71"
  ],
  "related_registry_items": [
    {
      "id": "IV.D71",
      "title": "Clopen Position Localization",
      "url": "/registry/object/IV.D71/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L114-L123",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.QuantumMechanics.AddressObstruction",
        "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-address-obstruction/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L114-L123",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "role": "type/data schema",
      "status": "type/data schema"
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

- Module: [TauLib.BookIV.QuantumMechanics.AddressObstruction](/corpus/taulib/docs/book-iv-quantum-mechanics-address-obstruction/)
- Source path: [`TauLib/BookIV/QuantumMechanics/AddressObstruction.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L114-L123)
- Source range: L114-L123
- Kind: `structure`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- `IV.D71` — Clopen Position Localization

## Immediate Comment / Docstring

```lean
/-- [IV.D71] Clopenly localized state: a state whose position support
    is a clopen (simultaneously closed and open) subset of T^2 of
    diameter at most epsilon. -/
```

## Source Excerpt

```lean
structure ClopenLocalization where
  /-- Localization radius epsilon numerator (scaled). -/
  epsilon_numer : Nat
  /-- Localization radius epsilon denominator. -/
  epsilon_denom : Nat
  /-- Denominator positive. -/
  denom_pos : epsilon_denom > 0
  /-- Epsilon positive. -/
  epsilon_pos : epsilon_numer > 0
  deriving Repr
```
