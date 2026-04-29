---
{
  "projection_kind": "taulib_declaration",
  "title": "h0_nonconstant_check",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-sheaf-cohomology/h0-nonconstant-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.CentralTheorem.SheafCohomology`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.SheafCohomology::h0_nonconstant_check",
  "declaration_slug": "h0-nonconstant-check",
  "kind": "def",
  "name": "h0_nonconstant_check",
  "module_name": "TauLib.BookII.CentralTheorem.SheafCohomology",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-sheaf-cohomology/",
  "source_line_start": 149,
  "source_line_end": 156,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/SheafCohomology.lean#L149-L156",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/SheafCohomology.lean#L149-L156",
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
- Source path: [`TauLib/BookII/CentralTheorem/SheafCohomology.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/SheafCohomology.lean#L149-L156)
- Source range: L149-L156
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T55` — H⁰ = Global Sections

## Immediate Comment / Docstring

```lean
/-- [II.T55] Non-constant functions are NOT global sections. -/
```

## Source Excerpt

```lean
def h0_nonconstant_check (k : Nat) : Bool :=
  let pk := primorial k
  if pk <= 1 then true
  else
    -- The identity function f(x) = x is not constant
    let f : Nat → Int := fun x => (x : Int)
    -- δ⁰f(0,1) = f(1) - f(0) = 1 ≠ 0
    cech_coboundary_0 f k 0 1 != 0
```
