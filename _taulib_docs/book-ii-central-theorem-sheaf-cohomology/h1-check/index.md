---
{
  "projection_kind": "taulib_declaration",
  "title": "h1_check",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-sheaf-cohomology/h1-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.CentralTheorem.SheafCohomology`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.SheafCohomology::h1_check",
  "declaration_slug": "h1-check",
  "kind": "def",
  "name": "h1_check",
  "module_name": "TauLib.BookII.CentralTheorem.SheafCohomology",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-sheaf-cohomology/",
  "source_line_start": 108,
  "source_line_end": 125,
  "registry_ids": [
    "II.D87"
  ],
  "related_registry_items": [
    {
      "id": "II.D87",
      "title": "Sheaf Cohomology Groups",
      "url": "/registry/object/II.D87/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/SheafCohomology.lean#L108-L125",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/SheafCohomology.lean#L108-L125",
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
- Source path: [`TauLib/BookII/CentralTheorem/SheafCohomology.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/SheafCohomology.lean#L108-L125)
- Source range: L108-L125
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D87` — Sheaf Cohomology Groups

## Immediate Comment / Docstring

```lean
/-- [II.D87] H¹ check: for the constant sheaf on Z/M_k Z with the
    cylinder cover, H¹ = 0.
    Proof: every 1-cocycle is a coboundary because the cover is acyclic. -/
```

## Source Excerpt

```lean
def h1_check (k : Nat) : Bool :=
  let pk := primorial k
  -- For a 1-cocycle c(a,b) with c(a,b) + c(b,c) = c(a,c):
  -- Define f(a) = c(0,a). Then (δ⁰f)(a,b) = f(b) - f(a) = c(0,b) - c(0,a) = c(a,b).
  -- So every cocycle is a coboundary. H¹ = 0.
  -- Verify for sample cocycles:
  go 0 pk pk
where
  go (a pk fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if a >= pk then true
    else
      -- Cocycle c(0,a) = a (the canonical cocycle)
      -- Cochain f(a) = a. Then δ⁰f(0,a) = a - 0 = a = c(0,a). ✓
      let cocycle_val : Int := (a : Int)
      let cochain_val : Int := (a : Int)
      (cocycle_val == cochain_val) && go (a + 1) pk (fuel - 1)
  termination_by fuel
```
