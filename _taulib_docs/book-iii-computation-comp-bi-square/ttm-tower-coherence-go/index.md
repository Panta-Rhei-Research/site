---
{
  "projection_kind": "taulib_declaration",
  "title": "ttm_tower_coherence_go",
  "permalink": "/verify/taulib/docs/book-iii-computation-comp-bi-square/ttm-tower-coherence-go/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Computation.CompBiSquare`.",
  "declaration_id": "TauLib.BookIII.Computation.CompBiSquare::ttm_tower_coherence_go",
  "declaration_slug": "ttm-tower-coherence-go",
  "kind": "def",
  "name": "ttm_tower_coherence_go",
  "module_name": "TauLib.BookIII.Computation.CompBiSquare",
  "module_url": "/verify/taulib/docs/book-iii-computation-comp-bi-square/",
  "source_line_start": 78,
  "source_line_end": 91,
  "registry_ids": [
    "III.D56"
  ],
  "related_registry_items": [
    {
      "id": "III.D56",
      "title": "Computational Bi-Square",
      "url": "/registry/object/III.D56/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/CompBiSquare.lean#L78-L91",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Computation.CompBiSquare",
        "url": "/verify/taulib/docs/book-iii-computation-comp-bi-square/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/CompBiSquare.lean#L78-L91",
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

- Module: [TauLib.BookIII.Computation.CompBiSquare](/verify/taulib/docs/book-iii-computation-comp-bi-square/)
- Source path: [`TauLib/BookIII/Computation/CompBiSquare.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/CompBiSquare.lean#L78-L91)
- Source range: L78-L91
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D56` — Computational Bi-Square

## Immediate Comment / Docstring

```lean
/-- [III.D56] TTM tower coherence: result at depth k+1 reduces mod p_k
    to result at depth k. -/
```

## Source Excerpt

```lean
def ttm_tower_coherence_go (x k bound db fuel : Nat) : Bool :=
  if fuel = 0 then true
  else if x > bound then true
  else if k >= db then ttm_tower_coherence_go (x + 1) 1 bound db (fuel - 1)
  else
    let pk := primorial k
    let pk1 := primorial (k + 1)
    if pk == 0 || pk1 == 0 then ttm_tower_coherence_go x (k + 1) bound db (fuel - 1)
    else
      let cfg_k := ttm_run (TTMConfig.mk 0 (x % pk) 1 k) 4
      let cfg_k1 := ttm_run (TTMConfig.mk 0 (x % pk1) 1 (k + 1)) 4
      let coherent := cfg_k1.reg_a % pk == cfg_k.reg_a
      coherent && ttm_tower_coherence_go x (k + 1) bound db (fuel - 1)
termination_by fuel
```
