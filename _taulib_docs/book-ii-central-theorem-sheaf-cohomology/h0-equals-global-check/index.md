---
{
  "projection_kind": "taulib_declaration",
  "title": "h0_equals_global_check",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-sheaf-cohomology/h0-equals-global-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.CentralTheorem.SheafCohomology`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.SheafCohomology::h0_equals_global_check",
  "declaration_slug": "h0-equals-global-check",
  "kind": "def",
  "name": "h0_equals_global_check",
  "module_name": "TauLib.BookII.CentralTheorem.SheafCohomology",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-sheaf-cohomology/",
  "source_line_start": 134,
  "source_line_end": 146,
  "registry_ids": [
    "II.T55"
  ],
  "related_registry_items": [
    {
      "id": "II.T55",
      "title": "H⁰ = Global Sections",
      "url": "/registry/object/II.T55/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/SheafCohomology.lean#L134-L146",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/SheafCohomology.lean#L134-L146",
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
- Source path: [`TauLib/BookII/CentralTheorem/SheafCohomology.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/SheafCohomology.lean#L134-L146)
- Source range: L134-L146
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T55` — H⁰ = Global Sections

## Immediate Comment / Docstring

```lean
/-- [II.T55] Verify that H⁰ equals global sections:
    a 0-cochain f is a global section iff f is constant on Z/M_k Z.
    We check: the constant function 1 is in ker(δ⁰). -/
```

## Source Excerpt

```lean
def h0_equals_global_check (k : Nat) : Bool :=
  let pk := primorial k
  let const_one : Nat → Int := fun _ => 1
  go 0 0 pk pk const_one k
where
  go (a b pk fuel : Nat) (f : Nat → Int) (k : Nat) : Bool :=
    if fuel = 0 then true
    else if a >= pk then true
    else if b >= pk then go (a + 1) 0 pk (fuel - 1) f k
    else
      let delta := cech_coboundary_0 f k a b
      (delta == 0) && go a (b + 1) pk (fuel - 1) f k
  termination_by fuel
```
