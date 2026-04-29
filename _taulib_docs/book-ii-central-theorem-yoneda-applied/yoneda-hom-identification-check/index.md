---
{
  "projection_kind": "taulib_declaration",
  "title": "yoneda_hom_identification_check",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-yoneda-applied/yoneda-hom-identification-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.CentralTheorem.YonedaApplied`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.YonedaApplied::yoneda_hom_identification_check",
  "declaration_slug": "yoneda-hom-identification-check",
  "kind": "def",
  "name": "yoneda_hom_identification_check",
  "module_name": "TauLib.BookII.CentralTheorem.YonedaApplied",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-yoneda-applied/",
  "source_line_start": 89,
  "source_line_end": 115,
  "registry_ids": [
    "II.L14"
  ],
  "related_registry_items": [
    {
      "id": "II.L14",
      "title": "Yoneda Application",
      "url": "/registry/object/II.L14/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/YonedaApplied.lean#L89-L115",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/YonedaApplied.lean#L89-L115",
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
- Source path: [`TauLib/BookII/CentralTheorem/YonedaApplied.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/YonedaApplied.lean#L89-L115)
- Source range: L89-L115
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.L14` — Yoneda Application

## Immediate Comment / Docstring

```lean
/-- [II.L14] Yoneda hom identification check: for test functions f,
    verify that the Hom-object representation (via hom_stage from pre-Yoneda)
    is consistent with the Code/Decode representation.

    For f = chi_plus_stage (B-sector projection):
    - preyoneda gives f(reduce(x, k)) = reduce(x, k) in B, 0 in C
    - Code/Decode round-trip on the B-channel recovers the same value

    For f = chi_minus_stage:
    - preyoneda gives 0 in B, reduce(x, k) in C
    - Code/Decode round-trip on the C-channel recovers the same value -/
```

## Source Excerpt

```lean
def yoneda_hom_identification_check (bound db : TauIdx) : Bool :=
  go 2 1 ((bound + 1) * (db + 1))
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k > db then go (x + 1) 1 (fuel - 1)
    else
      -- chi_plus hom stage: B = reduce(x, k), C = 0
      let b_val := chi_plus_stage.b_fun (reduce x k) k
      let c_val := chi_plus_stage.c_fun (reduce x k) k
      -- Code on B-channel
      let b_fn : TauIdx -> Int := fun n => (chi_plus_stage.b_fun n k : Int)
      let b_code := code_extract b_fn k x
      -- The B-channel code should match the direct evaluation
      let b_ok := b_code == (b_val : Int)
      -- C-channel should be 0
      let c_ok := c_val == 0
      -- chi_minus hom stage: B = 0, C = reduce(x, k)
      let b2_val := chi_minus_stage.b_fun (reduce x k) k
      let c2_val := chi_minus_stage.c_fun (reduce x k) k
      let c_fn : TauIdx -> Int := fun n => (chi_minus_stage.c_fun n k : Int)
      let c_code := code_extract c_fn k x
      let b2_ok := b2_val == 0
      let c2_ok := c_code == (c2_val : Int)
      b_ok && c_ok && b2_ok && c2_ok && go x (k + 1) (fuel - 1)
  termination_by fuel
```
