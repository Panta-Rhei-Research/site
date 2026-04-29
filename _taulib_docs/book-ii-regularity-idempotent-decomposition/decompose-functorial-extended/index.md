---
{
  "projection_kind": "taulib_declaration",
  "title": "decompose_functorial_extended",
  "permalink": "/verify/taulib/docs/book-ii-regularity-idempotent-decomposition/decompose-functorial-extended/",
  "summary_short": "`def` declaration in `TauLib.BookII.Regularity.IdempotentDecomposition`.",
  "declaration_id": "TauLib.BookII.Regularity.IdempotentDecomposition::decompose_functorial_extended",
  "declaration_slug": "decompose-functorial-extended",
  "kind": "def",
  "name": "decompose_functorial_extended",
  "module_name": "TauLib.BookII.Regularity.IdempotentDecomposition",
  "module_url": "/verify/taulib/docs/book-ii-regularity-idempotent-decomposition/",
  "source_line_start": 228,
  "source_line_end": 255,
  "registry_ids": [
    "II.P10"
  ],
  "related_registry_items": [
    {
      "id": "II.P10",
      "title": "Functions as Tau-Objects",
      "url": "/registry/object/II.P10/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/IdempotentDecomposition.lean#L228-L255",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Regularity.IdempotentDecomposition",
        "url": "/verify/taulib/docs/book-ii-regularity-idempotent-decomposition/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/IdempotentDecomposition.lean#L228-L255",
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

- Module: [TauLib.BookII.Regularity.IdempotentDecomposition](/verify/taulib/docs/book-ii-regularity-idempotent-decomposition/)
- Source path: [`TauLib/BookII/Regularity/IdempotentDecomposition.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/IdempotentDecomposition.lean#L228-L255)
- Source range: L228-L255
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.P10` — Functions as Tau-Objects

## Immediate Comment / Docstring

```lean
/-- [II.P10] Extended functoriality: test with multiple endomorphism pairs. -/
```

## Source Excerpt

```lean
def decompose_functorial_extended (bound db : TauIdx) : Bool :=
  go 2 1 ((bound + 1) * (db + 1))
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k > db then go (x + 1) 1 (fuel - 1)
    else
      -- Test pair 1: chi_minus and id
      let f1 := chi_minus_stage
      let g1 := id_stage
      let comp1 := StageFun.comp f1 g1
      let (comp1_b, comp1_c) := stagefun_decompose comp1
      let (f1_b, f1_c) := stagefun_decompose f1
      let (g1_b, g1_c) := stagefun_decompose g1
      let ok1 := comp1_b.b_fun x k == (StageFun.comp f1_b g1_b).b_fun x k &&
                 comp1_c.c_fun x k == (StageFun.comp f1_c g1_c).c_fun x k
      -- Test pair 2: id and chi_plus
      let f2 := id_stage
      let g2 := chi_plus_stage
      let comp2 := StageFun.comp f2 g2
      let (comp2_b, comp2_c) := stagefun_decompose comp2
      let (f2_b, f2_c) := stagefun_decompose f2
      let (g2_b, g2_c) := stagefun_decompose g2
      let ok2 := comp2_b.b_fun x k == (StageFun.comp f2_b g2_b).b_fun x k &&
                 comp2_c.c_fun x k == (StageFun.comp f2_c g2_c).c_fun x k
      ok1 && ok2 && go x (k + 1) (fuel - 1)
  termination_by fuel
```
