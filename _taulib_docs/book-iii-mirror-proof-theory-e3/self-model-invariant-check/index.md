---
{
  "projection_kind": "taulib_declaration",
  "title": "self_model_invariant_check",
  "permalink": "/verify/taulib/docs/book-iii-mirror-proof-theory-e3/self-model-invariant-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Mirror.ProofTheoryE3`.",
  "declaration_id": "TauLib.BookIII.Mirror.ProofTheoryE3::self_model_invariant_check",
  "declaration_slug": "self-model-invariant-check",
  "kind": "def",
  "name": "self_model_invariant_check",
  "module_name": "TauLib.BookIII.Mirror.ProofTheoryE3",
  "module_url": "/verify/taulib/docs/book-iii-mirror-proof-theory-e3/",
  "source_line_start": 180,
  "source_line_end": 209,
  "registry_ids": [
    "III.D74",
    "III.D75"
  ],
  "related_registry_items": [
    {
      "id": "III.D74",
      "title": "Diagrammatic Sector of E₃",
      "url": "/registry/object/III.D74/"
    },
    {
      "id": "III.D75",
      "title": "E₂→E₃ Boundary Crossing",
      "url": "/registry/object/III.D75/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L180-L209",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L180-L209",
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
- Source path: [`TauLib/BookIII/Mirror/ProofTheoryE3.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L180-L209)
- Source range: L180-L209
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D74` — Diagrammatic Sector of E₃
- `III.D75` — E₂→E₃ Boundary Crossing

## Immediate Comment / Docstring

```lean
/-- [III.D74] Self-model functor preserves invariants: E2 invariant
    implies E3 invariant on the functor image. -/
```

## Source Excerpt

```lean
def self_model_invariant_check (bound db : TauIdx) : Bool :=
  go 0 1 ((bound + 1) * (db + 1))
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k > db then go (x + 1) 1 (fuel - 1)
    else
      let e2 := layer_of .E2 bound db
      let e3 := layer_of .E3 bound db
      -- If E2 invariant holds...
      let inv_ok := if e2.invariant_check x k then
        -- ...then E3 invariant also holds
        e3.invariant_check x k
      else
        -- Else branch: E2 invariant fails → test E0 invariant separately
        let e0 := layer_of .E0 bound db
        e0.invariant_check x k
      inv_ok && go x (k + 1) (fuel - 1)
  termination_by fuel

-- ============================================================
-- FOUR PARADOX DIAGNOSTIC [III.D75]
-- ============================================================

/-! **Scope limitation (E3 collapse):** At finite primorial level, the E3
    predicate degenerates to E0 because `reduce` is idempotent. This check
    is vacuous but correctly models the mathematical structure. The E3 layer
    is correctly DEFINED but finite verification is vacuous.
    See audit DASHBOARD.md §E3 Collapse. -/
```
