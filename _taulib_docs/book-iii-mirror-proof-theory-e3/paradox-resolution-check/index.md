---
{
  "projection_kind": "taulib_declaration",
  "title": "paradox_resolution_check",
  "permalink": "/verify/taulib/docs/book-iii-mirror-proof-theory-e3/paradox-resolution-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Mirror.ProofTheoryE3`.",
  "declaration_id": "TauLib.BookIII.Mirror.ProofTheoryE3::paradox_resolution_check",
  "declaration_slug": "paradox-resolution-check",
  "kind": "def",
  "name": "paradox_resolution_check",
  "module_name": "TauLib.BookIII.Mirror.ProofTheoryE3",
  "module_url": "/verify/taulib/docs/book-iii-mirror-proof-theory-e3/",
  "source_line_start": 266,
  "source_line_end": 277,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L266-L277",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L266-L277",
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
- Source path: [`TauLib/BookIII/Mirror/ProofTheoryE3.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L266-L277)
- Source range: L266-L277
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T48` — Four Paradox Diagnostic

## Immediate Comment / Docstring

```lean
/-- [III.T48] Paradox resolution: all four paradoxes are resolved by
    the enrichment tower. Each paradox is a boundary phenomenon between
    E2 and E3, and the E3 self-modelling absorbs the paradoxical move.

    Verified computationally:
    1. All four paradoxes are diagnosed (arise at E2)
    2. All four resolve at E3 (self-model functor absorbs them)
    3. The E3 layer is self-consistent (invariant is idempotent)
    4. Forbidden moves are distinct (no two paradoxes are the same) -/
```

## Source Excerpt

```lean
def paradox_resolution_check (bound db : TauIdx) : Bool :=
  -- Part 1: All paradoxes diagnosed
  let diagnosed := four_paradox_check bound db
  -- Part 2: E3 self-modelling absorbs all (proof theory wraps E2)
  let absorbed := proof_theory_e3_check bound db
  -- Part 3: Self-model functor works (E2 -> E3 is well-defined)
  let functor := self_model_check bound db
  -- Part 4: E3 invariants preserved
  let invariants := self_model_invariant_check bound db
  -- Part 5: All forbidden moves distinct
  let distinct := forbidden_moves_distinct
  diagnosed && absorbed && functor && invariants && distinct
```
