---
{
  "projection_kind": "taulib_declaration",
  "title": "paradox_single_check",
  "permalink": "/verify/taulib/docs/book-iii-mirror-proof-theory-e3/paradox-single-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Mirror.ProofTheoryE3`.",
  "declaration_id": "TauLib.BookIII.Mirror.ProofTheoryE3::paradox_single_check",
  "declaration_slug": "paradox-single-check",
  "kind": "def",
  "name": "paradox_single_check",
  "module_name": "TauLib.BookIII.Mirror.ProofTheoryE3",
  "module_url": "/verify/taulib/docs/book-iii-mirror-proof-theory-e3/",
  "source_line_start": 212,
  "source_line_end": 226,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L212-L226",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L212-L226",
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
- Source path: [`TauLib/BookIII/Mirror/ProofTheoryE3.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L212-L226)
- Source range: L212-L226
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Check a single paradox: it arises at E2 and resolves at E3. -/
```

## Source Excerpt

```lean
def paradox_single_check (p : Paradox) (bound db : TauIdx) : Bool :=
  -- The paradox arises at E2
  let arises_at_e2 := p.level == .E2
  -- The paradox resolves at E3
  let resolves_at_e3 := p.resolution_level == .E3
  -- The forbidden move index is unique (each maps to different move)
  let unique_move := p.forbidden_move_idx < 4
  -- E3 is strictly above E2 (gap exists for the paradox to live in)
  let gap := EnrLevel.lt .E2 .E3
  -- Distinguishing: this paradox's index differs from all others
  let distinct := all_paradoxes.all (fun q =>
    p == q || p.forbidden_move_idx != q.forbidden_move_idx)
  -- Paradox index matches its toNat (bijection with [0..3])
  let bijective := p.forbidden_move_idx == p.toNat
  arises_at_e2 && resolves_at_e3 && unique_move && gap && distinct && bijective
```
