---
{
  "projection_kind": "taulib_declaration",
  "title": "holographic_check",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-central-theorem/holographic-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.CentralTheorem.CentralTheorem`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.CentralTheorem::holographic_check",
  "declaration_slug": "holographic-check",
  "kind": "def",
  "name": "holographic_check",
  "module_name": "TauLib.BookII.CentralTheorem.CentralTheorem",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-central-theorem/",
  "source_line_start": 298,
  "source_line_end": 326,
  "registry_ids": [
    "II.C01"
  ],
  "related_registry_items": [
    {
      "id": "II.C01",
      "title": "Holographic Principle",
      "url": "/registry/object/II.C01/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L298-L326",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L298-L326",
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
- Source path: [`TauLib/BookII/CentralTheorem/CentralTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L298-L326)
- Source range: L298-L326
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.C01` — Holographic Principle

## Immediate Comment / Docstring

```lean
/-- [II.C01] Holographic principle check:
    boundary-to-interior and interior-to-boundary are mutual inverses.

    The boundary data (spectral algebra element on L) completely
    determines the interior data (holomorphic function on tau^3),
    and conversely.

    Test: for the identity function:
    - Extract boundary data at stage k
    - Reconstruct interior via BndLift (= reduce to stage k+1)
    - Restrict back to boundary at stage k
    - Result matches original boundary data -/
```

## Source Excerpt

```lean
def holographic_check (db bound : TauIdx) : Bool :=
  go 1 2 ((db + 1) * (bound + 1))
where
  go (k x fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k >= db then true
    else if x > bound then go (k + 1) 2 (fuel - 1)
    else
      -- Boundary data at stage k: (reduce(x, k), reduce(x, k))
      let bdry_b := reduce x k
      let bdry_c := reduce x k
      -- Interior reconstruction: BndLift to stage k+1
      let interior := bndlift x k
      -- Back to boundary: reduce interior to stage k
      let back_b := reduce interior k
      let back_c := reduce interior k
      -- Round-trip: boundary -> interior -> boundary = id
      let rt_ok := back_b == bdry_b && back_c == bdry_c
      -- Also verify the bipolar structure is preserved
      let bp_bdry := interior_bipolar (from_tau_idx bdry_b)
      let bp_back := interior_bipolar (from_tau_idx back_b)
      let bp_ok := bp_bdry == bp_back
      -- Code/Decode round-trip at the boundary level
      let code_fn : TauIdx -> Int := fun n => (reduce n k : Int)
      let code_val := code_extract code_fn k x
      let decode_val := decode_reconstruct code_fn k x
      let cd_ok := code_val == decode_val
      rt_ok && bp_ok && cd_ok && go k (x + 1) (fuel - 1)
  termination_by fuel
```
