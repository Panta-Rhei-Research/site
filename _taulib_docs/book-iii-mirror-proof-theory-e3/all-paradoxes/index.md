---
{
  "projection_kind": "taulib_declaration",
  "title": "all_paradoxes",
  "permalink": "/verify/taulib/docs/book-iii-mirror-proof-theory-e3/all-paradoxes/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Mirror.ProofTheoryE3`.",
  "declaration_id": "TauLib.BookIII.Mirror.ProofTheoryE3::all_paradoxes",
  "declaration_slug": "all-paradoxes",
  "kind": "def",
  "name": "all_paradoxes",
  "module_name": "TauLib.BookIII.Mirror.ProofTheoryE3",
  "module_url": "/verify/taulib/docs/book-iii-mirror-proof-theory-e3/",
  "source_line_start": 96,
  "source_line_end": 107,
  "registry_ids": [
    "III.D73"
  ],
  "related_registry_items": [
    {
      "id": "III.D73",
      "title": "Proof Theory as E₃",
      "url": "/registry/object/III.D73/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L96-L107",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L96-L107",
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
- Source path: [`TauLib/BookIII/Mirror/ProofTheoryE3.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L96-L107)
- Source range: L96-L107
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D73` — Proof Theory as E₃

## Immediate Comment / Docstring

```lean
/-- All four paradoxes as a list. -/
```

## Source Excerpt

```lean
def all_paradoxes : List Paradox :=
  [.Cantor, .Russell, .Goedel, .Turing]

-- ============================================================
-- PROOF THEORY AS E3 [III.D73]
-- ============================================================

/-! **Scope limitation (E3 collapse):** At finite primorial level, the E3
    predicate degenerates to E0 because `reduce` is idempotent. This check
    is vacuous but correctly models the mathematical structure. The E3 layer
    is correctly DEFINED but finite verification is vacuous.
    See audit DASHBOARD.md §E3 Collapse. -/
```
