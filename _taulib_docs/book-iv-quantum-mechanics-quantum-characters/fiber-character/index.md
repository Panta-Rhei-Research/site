---
{
  "projection_kind": "taulib_declaration",
  "title": "FiberCharacter",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/fiber-character/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.QuantumMechanics.QuantumCharacters`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.QuantumCharacters::FiberCharacter",
  "declaration_slug": "fiber-character",
  "kind": "structure",
  "name": "FiberCharacter",
  "module_name": "TauLib.BookIV.QuantumMechanics.QuantumCharacters",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/",
  "source_line_start": 77,
  "source_line_end": 84,
  "registry_ids": [
    "IV.D56"
  ],
  "related_registry_items": [
    {
      "id": "IV.D56",
      "title": "Character Variety of T²",
      "url": "/registry/object/IV.D56/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean#L77-L84",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean#L77-L84",
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
- Source path: [`TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean#L77-L84)
- Source range: L77-L84
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D56` — Character Variety of T²

## Immediate Comment / Docstring

```lean
/-- [IV.D56] Character variety Char(T^2) = U(1) x U(1) = T^2.
    The admissible quantum characters are those restricted to
    the CR-admissible sublattice Lambda_CR.

    A FiberCharacter is a character mode together with its
    CR-admissibility proof. -/
```

## Source Excerpt

```lean
structure FiberCharacter where
  /-- The underlying (m,n) address. -/
  mode : CharacterMode
  /-- Must be CR-admissible: m + n even. -/
  admissible : cr_admissible mode

instance : Repr FiberCharacter where
  reprPrec fc _ := s!"FiberCharacter({fc.mode.m}, {fc.mode.n})"
```
