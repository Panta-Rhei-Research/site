---
{
  "projection_kind": "taulib_declaration",
  "title": "d_squared_zero_tower_check",
  "permalink": "/verify/taulib/docs/book-ii-closure-tau-manifold/d-squared-zero-tower-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Closure.TauManifold`.",
  "declaration_id": "TauLib.BookII.Closure.TauManifold::d_squared_zero_tower_check",
  "declaration_slug": "d-squared-zero-tower-check",
  "kind": "def",
  "name": "d_squared_zero_tower_check",
  "module_name": "TauLib.BookII.Closure.TauManifold",
  "module_url": "/verify/taulib/docs/book-ii-closure-tau-manifold/",
  "source_line_start": 156,
  "source_line_end": 170,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/TauManifold.lean#L156-L170",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Closure.TauManifold",
        "url": "/verify/taulib/docs/book-ii-closure-tau-manifold/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/TauManifold.lean#L156-L170",
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

- Module: [TauLib.BookII.Closure.TauManifold](/verify/taulib/docs/book-ii-closure-tau-manifold/)
- Source path: [`TauLib/BookII/Closure/TauManifold.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/TauManifold.lean#L156-L170)
- Source range: L156-L170
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- d^2 = 0 verified via telescoping: the sum of d_tau f over a full period
    [0, P_k) is 0 for any function f. This is the cyclic telescoping identity:
    sum_{x=0}^{P_k - 1} [f(x+1 mod P_k) - f(x mod P_k)] = 0.

    We verify this for f(y, k) = reduce(y, k) at each stage k. -/
```

## Source Excerpt

```lean
def d_squared_zero_tower_check (db bound : TauIdx) : Bool :=
  go 1 0 ((db + 1) * (bound + 1))
where
  go (k x fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else if x > bound then go (k + 1) 0 (fuel - 1)
    else
      let f_reduce : TauIdx -> TauIdx -> Int := fun y stage => (reduce y stage : Int)
      let pk := primorial k
      if pk == 0 then go k (x + 1) (fuel - 1)
      else
        let df_sum := sum_exterior_deriv f_reduce k 0 pk (pk + 1)
        (df_sum == 0) && go k (x + 1) (fuel - 1)
  termination_by fuel
```
