---
{
  "projection_kind": "taulib_declaration",
  "title": "paradox_move_injective",
  "permalink": "/verify/taulib/docs/book-iii-mirror-proof-theory-e3/paradox-move-injective/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Mirror.ProofTheoryE3`.",
  "declaration_id": "TauLib.BookIII.Mirror.ProofTheoryE3::paradox_move_injective",
  "declaration_slug": "paradox-move-injective",
  "kind": "theorem",
  "name": "paradox_move_injective",
  "module_name": "TauLib.BookIII.Mirror.ProofTheoryE3",
  "module_url": "/verify/taulib/docs/book-iii-mirror-proof-theory-e3/",
  "source_line_start": 367,
  "source_line_end": 374,
  "registry_ids": [
    "III.T48"
  ],
  "related_registry_items": [
    {
      "id": "III.T48",
      "title": "Four Paradox Diagnostic",
      "url": "/registry/object/III.T48/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L367-L374",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L367-L374",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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
- Source path: [`TauLib/BookIII/Mirror/ProofTheoryE3.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L367-L374)
- Source range: L367-L374
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T48` — Four Paradox Diagnostic

## Immediate Comment / Docstring

```lean
/-- [III.T48] Structural: each paradox maps to a unique forbidden move. -/
```

## Source Excerpt

```lean
theorem paradox_move_injective :
    Paradox.Cantor.forbidden_move_idx ≠ Paradox.Russell.forbidden_move_idx ∧
    Paradox.Cantor.forbidden_move_idx ≠ Paradox.Goedel.forbidden_move_idx ∧
    Paradox.Cantor.forbidden_move_idx ≠ Paradox.Turing.forbidden_move_idx ∧
    Paradox.Russell.forbidden_move_idx ≠ Paradox.Goedel.forbidden_move_idx ∧
    Paradox.Russell.forbidden_move_idx ≠ Paradox.Turing.forbidden_move_idx ∧
    Paradox.Goedel.forbidden_move_idx ≠ Paradox.Turing.forbidden_move_idx := by
  exact ⟨by decide, by decide, by decide, by decide, by decide, by decide⟩
```
