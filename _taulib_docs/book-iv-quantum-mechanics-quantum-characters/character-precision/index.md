---
{
  "projection_kind": "taulib_declaration",
  "title": "CharacterPrecision",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/character-precision/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.QuantumMechanics.QuantumCharacters`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.QuantumCharacters::CharacterPrecision",
  "declaration_slug": "character-precision",
  "kind": "structure",
  "name": "CharacterPrecision",
  "module_name": "TauLib.BookIV.QuantumMechanics.QuantumCharacters",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/",
  "source_line_start": 120,
  "source_line_end": 131,
  "registry_ids": [
    "IV.D57"
  ],
  "related_registry_items": [
    {
      "id": "IV.D57",
      "title": "Address Precision (ch17)",
      "url": "/registry/object/IV.D57/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean#L120-L131",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.QuantumMechanics.QuantumCharacters",
        "url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean#L120-L131",
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

- Module: [TauLib.BookIV.QuantumMechanics.QuantumCharacters](/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/)
- Source path: [`TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean#L120-L131)
- Source range: L120-L131
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D57` — Address Precision (ch17)

## Immediate Comment / Docstring

```lean
/-- [IV.D57] Address precision at a specific character: delta(psi, (m0,n0))
    = |c_{m0,n0}|^2 in [0,1]. Same concept as IV.D53 but specifically
    tied to a FiberCharacter. -/
```

## Source Excerpt

```lean
structure CharacterPrecision where
  /-- The target character. -/
  target : FiberCharacter
  /-- Precision numerator (|c|^2 scaled). -/
  numer : Nat
  /-- Precision denominator. -/
  denom : Nat
  /-- Denominator positive. -/
  denom_pos : denom > 0
  /-- Precision in [0,1]: numer <= denom. -/
  numer_le : numer ≤ denom
  deriving Repr
```
