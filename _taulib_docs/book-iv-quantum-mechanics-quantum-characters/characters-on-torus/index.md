---
{
  "projection_kind": "taulib_declaration",
  "title": "characters_on_torus",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/characters-on-torus/",
  "summary_short": "`def` declaration in `TauLib.BookIV.QuantumMechanics.QuantumCharacters`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.QuantumCharacters::characters_on_torus",
  "declaration_slug": "characters-on-torus",
  "kind": "def",
  "name": "characters_on_torus",
  "module_name": "TauLib.BookIV.QuantumMechanics.QuantumCharacters",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/",
  "source_line_start": 58,
  "source_line_end": 61,
  "registry_ids": [
    "IV.P11"
  ],
  "related_registry_items": [
    {
      "id": "IV.P11",
      "title": "Characters on T²",
      "url": "/registry/object/IV.P11/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean#L58-L61",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean#L58-L61",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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
- Source path: [`TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean#L58-L61)
- Source range: L58-L61
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.P11` — Characters on T²

## Immediate Comment / Docstring

```lean
/-- [IV.P11] A character on T^2 is determined by a pair (m,n) in Z^2,
    since pi_1(T^2) = Z^2 has rank 2. -/
```

## Source Excerpt

```lean
def characters_on_torus : SpaceCharacter where
  pi1_rank := 2
  param_count := 2
  param_eq := rfl
```
