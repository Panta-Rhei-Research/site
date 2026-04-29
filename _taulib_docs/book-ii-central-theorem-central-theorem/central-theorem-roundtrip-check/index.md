---
{
  "projection_kind": "taulib_declaration",
  "title": "central_theorem_roundtrip_check",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-central-theorem/central-theorem-roundtrip-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.CentralTheorem.CentralTheorem`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.CentralTheorem::central_theorem_roundtrip_check",
  "declaration_slug": "central-theorem-roundtrip-check",
  "kind": "def",
  "name": "central_theorem_roundtrip_check",
  "module_name": "TauLib.BookII.CentralTheorem.CentralTheorem",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-central-theorem/",
  "source_line_start": 229,
  "source_line_end": 260,
  "registry_ids": [
    "II.T40"
  ],
  "related_registry_items": [
    {
      "id": "II.T40",
      "title": "Central Theorem",
      "url": "/registry/object/II.T40/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L229-L260",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.CentralTheorem.CentralTheorem",
        "url": "/verify/taulib/docs/book-ii-central-theorem-central-theorem/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L229-L260",
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

- Module: [TauLib.BookII.CentralTheorem.CentralTheorem](/verify/taulib/docs/book-ii-central-theorem-central-theorem/)
- Source path: [`TauLib/BookII/CentralTheorem/CentralTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L229-L260)
- Source range: L229-L260
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T40` — Central Theorem

## Immediate Comment / Docstring

```lean
/-- [II.T40] Central Theorem round-trip check:
    forward . inverse = id AND inverse . forward = id.

    Direction 1 (forward . inverse = id):
    Start with a holomorphic function f = id_stage.
    - Inverse: extract boundary data b_fn(n) = reduce(n, k), c_fn(n) = reduce(n, k)
    - Forward: reconstruct hol function from boundary data
    - Result: spectral_to_hol(b_fn, c_fn, x, k) = (reduce(x,k), reduce(x,k))
      = id_stage evaluation

    Direction 2 (inverse . forward = id):
    Start with spectral data b_fn = c_fn = identity.
    - Forward: construct holomorphic function
    - Inverse: extract boundary data
    - Result: same as original spectral data -/
```

## Source Excerpt

```lean
def central_theorem_roundtrip_check (db bound : TauIdx) : Bool :=
  go 1 2 ((db + 1) * (bound + 1))
where
  go (k x fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else if x > bound then go (k + 1) 2 (fuel - 1)
    else
      -- Direction 1: forward . inverse = id (with squaring function)
      -- Holomorphic: sq_stage (non-trivial, exercises mul_mod)
      let sq_stage : StageFun := ⟨fun n k' => reduce (n * n) k', fun n k' => reduce (n * n) k'⟩
      let hol_val := hol_to_spectral sq_stage x k
      -- Extract boundary data from squaring function
      let b_fn : TauIdx -> Int := fun n => (sq_stage.b_fun n k : Int)
      let c_fn : TauIdx -> Int := fun n => (sq_stage.c_fun n k : Int)
      -- Reconstruct: spectral_to_hol applies b_fn to reduce(x,k),
      -- which gives reduce((reduce(x,k))², k) ≠ id in general
      let reconstructed := spectral_to_hol b_fn c_fn x k
      let dir1_ok := reconstructed == hol_val
      -- Direction 2: inverse . forward = id
      -- Spectral data: identity
      let sa_b : TauIdx -> Int := fun n => (n : Int)
      let sa_c : TauIdx -> Int := fun n => (n : Int)
      -- Forward: construct holomorphic
      let fwd := spectral_to_hol sa_b sa_c x k
      -- Inverse: extract boundary data at reduced point
      let rx := reduce x k
      let inv_b := sa_b rx
      let inv_c := sa_c rx
      let dir2_ok := fwd.b_sector == inv_b && fwd.c_sector == inv_c
      dir1_ok && dir2_ok && go k (x + 1) (fuel - 1)
  termination_by fuel
```
