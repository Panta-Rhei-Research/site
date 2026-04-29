---
{
  "projection_kind": "taulib_declaration",
  "title": "ParadoxWitness",
  "permalink": "/verify/taulib/docs/book-iii-mirror-e3-witness/paradox-witness/",
  "summary_short": "`inductive` declaration in `TauLib.BookIII.Mirror.E3Witness`.",
  "declaration_id": "TauLib.BookIII.Mirror.E3Witness::ParadoxWitness",
  "declaration_slug": "paradox-witness",
  "kind": "inductive",
  "name": "ParadoxWitness",
  "module_name": "TauLib.BookIII.Mirror.E3Witness",
  "module_url": "/verify/taulib/docs/book-iii-mirror-e3-witness/",
  "source_line_start": 106,
  "source_line_end": 111,
  "registry_ids": [
    "III.D86"
  ],
  "related_registry_items": [
    {
      "id": "III.D86",
      "title": "Paradox Absorption Map",
      "url": "/registry/object/III.D86/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/E3Witness.lean#L106-L111",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Mirror.E3Witness",
        "url": "/verify/taulib/docs/book-iii-mirror-e3-witness/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/E3Witness.lean#L106-L111",
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

- Module: [TauLib.BookIII.Mirror.E3Witness](/verify/taulib/docs/book-iii-mirror-e3-witness/)
- Source path: [`TauLib/BookIII/Mirror/E3Witness.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/E3Witness.lean#L106-L111)
- Source range: L106-L111
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `III.D86` — Paradox Absorption Map

## Immediate Comment / Docstring

```lean
/-- [III.D86] Paradox type (mirrors ProofTheoryE3). -/
```

## Source Excerpt

```lean
inductive ParadoxWitness where
  | cantor : ParadoxWitness    -- diagonal overflow
  | russell : ParadoxWitness   -- self-membership
  | goedel : ParadoxWitness    -- self-reference
  | turing : ParadoxWitness    -- halting
  deriving Repr, DecidableEq, BEq
```
