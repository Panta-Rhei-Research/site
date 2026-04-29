---
{
  "projection_kind": "taulib_declaration",
  "title": "level_coherence_check",
  "permalink": "/verify/taulib/docs/book-iii-hinge-hinge-theorem/level-coherence-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Hinge.HingeTheorem`.",
  "declaration_id": "TauLib.BookIII.Hinge.HingeTheorem::level_coherence_check",
  "declaration_slug": "level-coherence-check",
  "kind": "def",
  "name": "level_coherence_check",
  "module_name": "TauLib.BookIII.Hinge.HingeTheorem",
  "module_url": "/verify/taulib/docs/book-iii-hinge-hinge-theorem/",
  "source_line_start": 121,
  "source_line_end": 142,
  "registry_ids": [
    "III.T41"
  ],
  "related_registry_items": [
    {
      "id": "III.T41",
      "title": "Hinge Theorem",
      "url": "/registry/object/III.T41/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/HingeTheorem.lean#L121-L142",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Hinge.HingeTheorem",
        "url": "/verify/taulib/docs/book-iii-hinge-hinge-theorem/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/HingeTheorem.lean#L121-L142",
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

- Module: [TauLib.BookIII.Hinge.HingeTheorem](/verify/taulib/docs/book-iii-hinge-hinge-theorem/)
- Source path: [`TauLib/BookIII/Hinge/HingeTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/HingeTheorem.lean#L121-L142)
- Source range: L121-L142
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T41` — Hinge Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T41] Level coherence check: sector products at level k+1
    extend those at level k (divisibility). -/
```

## Source Excerpt

```lean
def level_coherence_check (db : TauIdx) : Bool :=
  go 1 db (db + 1)
where
  go (k db fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k >= db then true
    else
      let b_k := split_zeta_b k
      let b_k1 := split_zeta_b (k + 1)
      let c_k := split_zeta_c k
      let c_k1 := split_zeta_c (k + 1)
      -- Extension: products at k+1 are divisible by products at k
      let b_ext := if b_k > 0 then b_k1 % b_k == 0 else true
      let c_ext := if c_k > 0 then c_k1 % c_k == 0 else true
      b_ext && c_ext && go (k + 1) db (fuel - 1)
  termination_by fuel

/-! **Scope limitation (E3 collapse):** At finite primorial level, the E3
    predicate degenerates to E0 because `reduce` is idempotent. This check
    is vacuous but correctly models the mathematical structure. The E3 layer
    is correctly DEFINED but finite verification is vacuous.
    See audit DASHBOARD.md §E3 Collapse. -/
```
