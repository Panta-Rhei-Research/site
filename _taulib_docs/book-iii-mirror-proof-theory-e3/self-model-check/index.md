---
{
  "projection_kind": "taulib_declaration",
  "title": "self_model_check",
  "permalink": "/verify/taulib/docs/book-iii-mirror-proof-theory-e3/self-model-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Mirror.ProofTheoryE3`.",
  "declaration_id": "TauLib.BookIII.Mirror.ProofTheoryE3::self_model_check",
  "declaration_slug": "self-model-check",
  "kind": "def",
  "name": "self_model_check",
  "module_name": "TauLib.BookIII.Mirror.ProofTheoryE3",
  "module_url": "/verify/taulib/docs/book-iii-mirror-proof-theory-e3/",
  "source_line_start": 158,
  "source_line_end": 176,
  "registry_ids": [
    "III.D74"
  ],
  "related_registry_items": [
    {
      "id": "III.D74",
      "title": "Diagrammatic Sector of E₃",
      "url": "/registry/object/III.D74/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L158-L176",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L158-L176",
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
- Source path: [`TauLib/BookIII/Mirror/ProofTheoryE3.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L158-L176)
- Source range: L158-L176
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D74` — Diagrammatic Sector of E₃

## Immediate Comment / Docstring

```lean
/-- [III.D74] Self-model functor: E2 -> E3. Takes E2 objects (codes
    with operational closure) and produces E3 objects (self-modelling
    codes). The functor applies the E3 predicate to E2 carriers.

    Verified by: if E2 carrier + predicate hold, then E3 carrier +
    predicate hold on the E2 decoded value. -/
```

## Source Excerpt

```lean
def self_model_check (bound db : TauIdx) : Bool :=
  go 0 1 ((bound + 1) * (db + 1))
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k > db then go (x + 1) 1 (fuel - 1)
    else
      let e2 := layer_of .E2 bound db
      let e3 := layer_of .E3 bound db
      -- If x is a valid E2 object...
      let is_e2 := e2.carrier_check x k && e2.predicate_check x k
      -- ...then the self-model functor produces a valid E3 object
      let functor_ok := if is_e2 then
        let decoded := e2.decoder x k
        e3.carrier_check decoded k && e3.predicate_check decoded k
      else true
      functor_ok && go x (k + 1) (fuel - 1)
  termination_by fuel
```
