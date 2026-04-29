---
{
  "projection_kind": "taulib_declaration",
  "title": "Paradox",
  "permalink": "/verify/taulib/docs/book-iii-mirror-proof-theory-e3/paradox/",
  "summary_short": "`inductive` declaration in `TauLib.BookIII.Mirror.ProofTheoryE3`.",
  "declaration_id": "TauLib.BookIII.Mirror.ProofTheoryE3::Paradox",
  "declaration_slug": "paradox",
  "kind": "inductive",
  "name": "Paradox",
  "module_name": "TauLib.BookIII.Mirror.ProofTheoryE3",
  "module_url": "/verify/taulib/docs/book-iii-mirror-proof-theory-e3/",
  "source_line_start": 55,
  "source_line_end": 60,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L55-L60",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L55-L60",
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

- Module: [TauLib.BookIII.Mirror.ProofTheoryE3](/verify/taulib/docs/book-iii-mirror-proof-theory-e3/)
- Source path: [`TauLib/BookIII/Mirror/ProofTheoryE3.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L55-L60)
- Source range: L55-L60
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `III.D75` — E₂→E₃ Boundary Crossing

## Immediate Comment / Docstring

```lean
/-- [III.D75] The four classical paradoxes, each arising at a
    specific boundary in the enrichment tower. -/
```

## Source Excerpt

```lean
inductive Paradox where
  | Cantor : Paradox
  | Russell : Paradox
  | Goedel : Paradox
  | Turing : Paradox
  deriving Repr, DecidableEq, BEq
```
