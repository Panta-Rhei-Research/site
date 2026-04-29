---
{
  "projection_kind": "taulib_declaration",
  "title": "omega_germs_holomorphic_check",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-yoneda-applied/omega-germs-holomorphic-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.CentralTheorem.YonedaApplied`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.YonedaApplied::omega_germs_holomorphic_check",
  "declaration_slug": "omega-germs-holomorphic-check",
  "kind": "def",
  "name": "omega_germs_holomorphic_check",
  "module_name": "TauLib.BookII.CentralTheorem.YonedaApplied",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-yoneda-applied/",
  "source_line_start": 132,
  "source_line_end": 162,
  "registry_ids": [
    "II.T39"
  ],
  "related_registry_items": [
    {
      "id": "II.T39",
      "title": "Omega-Germs iff Holomorphic Functions",
      "url": "/registry/object/II.T39/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/YonedaApplied.lean#L132-L162",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.CentralTheorem.YonedaApplied",
        "url": "/verify/taulib/docs/book-ii-central-theorem-yoneda-applied/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/YonedaApplied.lean#L132-L162",
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

- Module: [TauLib.BookII.CentralTheorem.YonedaApplied](/verify/taulib/docs/book-ii-central-theorem-yoneda-applied/)
- Source path: [`TauLib/BookII/CentralTheorem/YonedaApplied.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/YonedaApplied.lean#L132-L162)
- Source range: L132-L162
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T39` — Omega-Germs iff Holomorphic Functions

## Immediate Comment / Docstring

```lean
/-- [II.T39] Omega-germs determine holomorphic functions (forward direction).

    Every tower-coherent function (= holomorphic) determines a unique
    omega-germ transformer. Concretely: for a tower-coherent StageFun f,
    the pre-Yoneda image is tower-coherent, and the Code extraction at
    each stage is well-defined.

    Test: for id_stage (tower-coherent by id_coherent),
    - The B/C-sector readings at stage k are reduced values
    - These readings are tower-coherent: reduce(reading at k+1, k) = reading at k
    - Code extraction at stage k matches the reading -/
```

## Source Excerpt

```lean
def omega_germs_holomorphic_check (bound db : TauIdx) : Bool :=
  go 2 1 ((bound + 1) * (db + 1))
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k > db then go (x + 1) 1 (fuel - 1)
    else
      -- id_stage evaluation at (x, k)
      let b_k := id_stage.b_fun x k
      let c_k := id_stage.c_fun x k
      -- id_stage evaluation at (x, k+1)
      let b_k1 := id_stage.b_fun x (k + 1)
      let c_k1 := id_stage.c_fun x (k + 1)
      -- Tower coherence: reduce(f(x, k+1), k) = f(x, k)
      let tc_b := reduce b_k1 k == b_k
      let tc_c := reduce c_k1 k == c_k
      -- Code extraction consistency
      let b_fn : TauIdx -> Int := fun n => (id_stage.b_fun n k : Int)
      let b_code := code_extract b_fn k x
      let code_ok := b_code == (b_k : Int)
      -- Bipolar decomposition: interior_bipolar gives (B, C) sectors
      let p := from_tau_idx (reduce x k)
      let bp := interior_bipolar p
      -- e_plus projection keeps B, e_minus projection keeps C
      let proj_b := SectorPair.mul e_plus_sector bp
      let proj_c := SectorPair.mul e_minus_sector bp
      -- Recovery: proj_b + proj_c = bp
      let recovery_ok := SectorPair.add proj_b proj_c == bp
      tc_b && tc_c && code_ok && recovery_ok && go x (k + 1) (fuel - 1)
  termination_by fuel
```
