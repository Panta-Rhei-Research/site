---
{
  "projection_kind": "taulib_declaration",
  "title": "h0_global_sections",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-sheaf-cohomology/h0-global-sections/",
  "summary_short": "`def` declaration in `TauLib.BookII.CentralTheorem.SheafCohomology`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.SheafCohomology::h0_global_sections",
  "declaration_slug": "h0-global-sections",
  "kind": "def",
  "name": "h0_global_sections",
  "module_name": "TauLib.BookII.CentralTheorem.SheafCohomology",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-sheaf-cohomology/",
  "source_line_start": 96,
  "source_line_end": 103,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/SheafCohomology.lean#L96-L103",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/SheafCohomology.lean#L96-L103",
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
- Source path: [`TauLib/BookII/CentralTheorem/SheafCohomology.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/SheafCohomology.lean#L96-L103)
- Source range: L96-L103
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D87` — Sheaf Cohomology Groups

## Immediate Comment / Docstring

```lean
/-- [II.D87] H⁰ = global sections: count cochains f with δ⁰f = 0,
    i.e., f(a) = f(b) for all a,b (constant functions). -/
```

## Source Excerpt

```lean
def h0_global_sections (k : Nat) : Nat :=
  let pk := primorial k
  -- A global section is a constant function on Z/M_k Z.
  -- The number of distinct constant functions = M_k
  -- (one for each value in Z/M_k Z as codomain).
  -- But as a group, H⁰(ℤ) ≅ ℤ, rank 1.
  -- We return the rank.
  if pk > 0 then 1 else 0
```
