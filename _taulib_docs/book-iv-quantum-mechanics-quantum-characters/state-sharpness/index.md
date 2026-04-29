---
{
  "projection_kind": "taulib_declaration",
  "title": "StateSharpness",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/state-sharpness/",
  "summary_short": "`inductive` declaration in `TauLib.BookIV.QuantumMechanics.QuantumCharacters`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.QuantumCharacters::StateSharpness",
  "declaration_slug": "state-sharpness",
  "kind": "inductive",
  "name": "StateSharpness",
  "module_name": "TauLib.BookIV.QuantumMechanics.QuantumCharacters",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/",
  "source_line_start": 207,
  "source_line_end": 212,
  "registry_ids": [
    "IV.D59"
  ],
  "related_registry_items": [
    {
      "id": "IV.D59",
      "title": "Sharp and Spread States",
      "url": "/registry/object/IV.D59/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean#L207-L212",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean#L207-L212",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
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
- Source path: [`TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean#L207-L212)
- Source range: L207-L212
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `IV.D59` — Sharp and Spread States

## Immediate Comment / Docstring

```lean
/-- [IV.D59] A state is sharp at address (m0,n0) if its precision is
    close to 1, and spread if the precision is distributed across many modes. -/
```

## Source Excerpt

```lean
inductive StateSharpness where
  /-- Precision concentrated at one address. -/
  | Sharp
  /-- Precision distributed across many addresses. -/
  | Spread
  deriving Repr, DecidableEq, BEq
```
