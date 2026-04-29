---
{
  "projection_kind": "taulib_declaration",
  "title": "cech_coboundary_sq_zero_check",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-sheaf-cohomology/cech-coboundary-sq-zero-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.CentralTheorem.SheafCohomology`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.SheafCohomology::cech_coboundary_sq_zero_check",
  "declaration_slug": "cech-coboundary-sq-zero-check",
  "kind": "def",
  "name": "cech_coboundary_sq_zero_check",
  "module_name": "TauLib.BookII.CentralTheorem.SheafCohomology",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-sheaf-cohomology/",
  "source_line_start": 63,
  "source_line_end": 88,
  "registry_ids": [
    "II.D86"
  ],
  "related_registry_items": [
    {
      "id": "II.D86",
      "title": "Čech Complex",
      "url": "/registry/object/II.D86/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/SheafCohomology.lean#L63-L88",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.CentralTheorem.SheafCohomology",
        "url": "/verify/taulib/docs/book-ii-central-theorem-sheaf-cohomology/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/SheafCohomology.lean#L63-L88",
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

- Module: [TauLib.BookII.CentralTheorem.SheafCohomology](/verify/taulib/docs/book-ii-central-theorem-sheaf-cohomology/)
- Source path: [`TauLib/BookII/CentralTheorem/SheafCohomology.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/SheafCohomology.lean#L63-L88)
- Source range: L63-L88
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D86` — Čech Complex

## Immediate Comment / Docstring

```lean
/-- [II.D86] Check δ² = 0 for the Čech complex.
    δ¹(δ⁰ f)(a,b,c) = δ⁰f(b,c) - δ⁰f(a,c) + δ⁰f(a,b)
    = (f(c)-f(b)) - (f(c)-f(a)) + (f(b)-f(a)) = 0. -/
```

## Source Excerpt

```lean
def cech_coboundary_sq_zero_check (k : Nat) : Bool :=
  let pk := primorial k
  go_a 0 pk pk
where
  go_a (a pk fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if a >= pk then true
    else go_b a 0 pk pk && go_a (a + 1) pk (fuel - 1)
  termination_by fuel
  go_b (a b pk fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if b >= pk then true
    else go_c a b 0 pk pk && go_b a (b + 1) pk (fuel - 1)
  termination_by fuel
  go_c (a b c pk fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if c >= pk then true
    else
      -- Use the identity function as test cochain
      let f : Nat → Int := fun x => (x : Int)
      let d01 := cech_coboundary_0 f pk b c
      let d02 := cech_coboundary_0 f pk a c
      let d03 := cech_coboundary_0 f pk a b
      -- δ¹(δ⁰f)(a,b,c) = d01 - d02 + d03 = 0
      (d01 - d02 + d03 == 0) && go_c a b (c + 1) pk (fuel - 1)
  termination_by fuel
```
