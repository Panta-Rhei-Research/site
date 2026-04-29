---
{
  "projection_kind": "taulib_declaration",
  "title": "SpaceCharacter",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/space-character/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.QuantumMechanics.QuantumCharacters`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.QuantumCharacters::SpaceCharacter",
  "declaration_slug": "space-character",
  "kind": "structure",
  "name": "SpaceCharacter",
  "module_name": "TauLib.BookIV.QuantumMechanics.QuantumCharacters",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/",
  "source_line_start": 43,
  "source_line_end": 50,
  "registry_ids": [
    "IV.D55"
  ],
  "related_registry_items": [
    {
      "id": "IV.D55",
      "title": "Character on a Space",
      "url": "/registry/object/IV.D55/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean#L43-L50",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean#L43-L50",
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
- Source path: [`TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean#L43-L50)
- Source range: L43-L50
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D55` — Character on a Space

## Immediate Comment / Docstring

```lean
/-- [IV.D55] Character on a path-connected space X: a group
    homomorphism pi_1(X) -> U(1). For T^2, pi_1 = Z^2, so a
    character is determined by an image pair (m, n) in Z^2.
    This is the abstract definition. -/
```

## Source Excerpt

```lean
structure SpaceCharacter where
  /-- Dimension of the fundamental group (rank of pi_1). -/
  pi1_rank : Nat
  /-- The character is determined by this many integers. -/
  param_count : Nat
  /-- Number of parameters equals pi_1 rank. -/
  param_eq : param_count = pi1_rank
  deriving Repr
```
