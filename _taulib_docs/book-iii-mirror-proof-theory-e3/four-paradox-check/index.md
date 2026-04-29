---
{
  "projection_kind": "taulib_declaration",
  "title": "four_paradox_check",
  "permalink": "/verify/taulib/docs/book-iii-mirror-proof-theory-e3/four-paradox-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Mirror.ProofTheoryE3`.",
  "declaration_id": "TauLib.BookIII.Mirror.ProofTheoryE3::four_paradox_check",
  "declaration_slug": "four-paradox-check",
  "kind": "def",
  "name": "four_paradox_check",
  "module_name": "TauLib.BookIII.Mirror.ProofTheoryE3",
  "module_url": "/verify/taulib/docs/book-iii-mirror-proof-theory-e3/",
  "source_line_start": 236,
  "source_line_end": 240,
  "registry_ids": [
    "III.D75"
  ],
  "related_registry_items": [
    {
      "id": "III.D75",
      "title": "E₂→E₃ Boundary Crossing",
      "url": "/registry/object/III.D75/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L236-L240",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Mirror.ProofTheoryE3",
        "url": "/verify/taulib/docs/book-iii-mirror-proof-theory-e3/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L236-L240",
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

- Module: [TauLib.BookIII.Mirror.ProofTheoryE3](/verify/taulib/docs/book-iii-mirror-proof-theory-e3/)
- Source path: [`TauLib/BookIII/Mirror/ProofTheoryE3.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L236-L240)
- Source range: L236-L240
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D75` — E₂→E₃ Boundary Crossing

## Immediate Comment / Docstring

```lean
/-- [III.D75] Paradox diagnostic: each paradox is a boundary phenomenon.
    At E2 level, the paradoxical construction attempts a move that
    requires E3 self-modelling. The diagnostic verifies:
    1. The paradox operation fails at E2 (forbidden move)
    2. The paradox resolves at E3 (self-model absorbs it)

    Modelled computationally: each paradox corresponds to a specific
    relationship between E2 and E3 layer checks. -/
```

## Source Excerpt

```lean
def four_paradox_check (bound db : TauIdx) : Bool :=
  paradox_single_check .Cantor bound db &&
  paradox_single_check .Russell bound db &&
  paradox_single_check .Goedel bound db &&
  paradox_single_check .Turing bound db
```
