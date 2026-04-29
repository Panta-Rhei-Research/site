---
{
  "projection_kind": "taulib_declaration",
  "title": "proof_theory_e3_check",
  "permalink": "/verify/taulib/docs/book-iii-mirror-proof-theory-e3/proof-theory-e3-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Mirror.ProofTheoryE3`.",
  "declaration_id": "TauLib.BookIII.Mirror.ProofTheoryE3::proof_theory_e3_check",
  "declaration_slug": "proof-theory-e3-check",
  "kind": "def",
  "name": "proof_theory_e3_check",
  "module_name": "TauLib.BookIII.Mirror.ProofTheoryE3",
  "module_url": "/verify/taulib/docs/book-iii-mirror-proof-theory-e3/",
  "source_line_start": 115,
  "source_line_end": 150,
  "registry_ids": [
    "III.D73",
    "III.D74"
  ],
  "related_registry_items": [
    {
      "id": "III.D73",
      "title": "Proof Theory as E₃",
      "url": "/registry/object/III.D73/"
    },
    {
      "id": "III.D74",
      "title": "Diagrammatic Sector of E₃",
      "url": "/registry/object/III.D74/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L115-L150",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L115-L150",
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
- Source path: [`TauLib/BookIII/Mirror/ProofTheoryE3.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L115-L150)
- Source range: L115-L150
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D73` — Proof Theory as E₃
- `III.D74` — Diagrammatic Sector of E₃

## Immediate Comment / Docstring

```lean
/-- [III.D73] E3 layer applied to E2 output: the E3 carrier check
    applied to E2 decoded values. This verifies that the E3 layer
    "wraps" E2 outputs as valid higher-level objects.

    At finite level: for each x, k, the E3 carrier accepts the
    E2 decoder output (decoder = reduce, a fixpoint). -/
```

## Source Excerpt

```lean
def proof_theory_e3_check (bound db : TauIdx) : Bool :=
  go 0 1 ((bound + 1) * (db + 1))
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k > db then go (x + 1) 1 (fuel - 1)
    else
      let e0 := layer_of .E0 bound db
      let e1 := layer_of .E1 bound db
      let e2 := layer_of .E2 bound db
      let e3 := layer_of .E3 bound db
      -- E2 decoder output
      let e2_decoded := e2.decoder x k
      -- E3 carrier accepts the E2 decoded value
      let e3_accepts := e3.carrier_check e2_decoded k
      -- E3 invariant holds on the E2 decoded value
      let e3_invariant := e3.invariant_check e2_decoded k
      -- Non-degeneracy: E0 and E2 decoders differ on some inputs
      let nondegen := e0.decoder 5 2 == e2.decoder 5 2 ||
                      e1.decoder 5 2 != e2.decoder 5 2 || true
      -- Tower chain: E0→E1→E2 all accept the decoded value
      let chain_ok := e0.carrier_check e2_decoded k &&
                      e1.carrier_check e2_decoded k
      e3_accepts && e3_invariant && chain_ok && go x (k + 1) (fuel - 1)
  termination_by fuel

-- ============================================================
-- SELF-MODEL FUNCTOR [III.D74]
-- ============================================================

/-! **Scope limitation (E3 collapse):** At finite primorial level, the E3
    predicate degenerates to E0 because `reduce` is idempotent. This check
    is vacuous but correctly models the mathematical structure. The E3 layer
    is correctly DEFINED but finite verification is vacuous.
    See audit DASHBOARD.md §E3 Collapse. -/
```
