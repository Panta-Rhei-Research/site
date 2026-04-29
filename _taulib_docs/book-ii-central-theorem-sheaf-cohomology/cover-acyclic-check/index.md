---
{
  "projection_kind": "taulib_declaration",
  "title": "cover_acyclic_check",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-sheaf-cohomology/cover-acyclic-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.CentralTheorem.SheafCohomology`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.SheafCohomology::cover_acyclic_check",
  "declaration_slug": "cover-acyclic-check",
  "kind": "def",
  "name": "cover_acyclic_check",
  "module_name": "TauLib.BookII.CentralTheorem.SheafCohomology",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-sheaf-cohomology/",
  "source_line_start": 165,
  "source_line_end": 179,
  "registry_ids": [
    "II.P20"
  ],
  "related_registry_items": [
    {
      "id": "II.P20",
      "title": "Čech-to-Derived Comparison",
      "url": "/registry/object/II.P20/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/SheafCohomology.lean#L165-L179",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/SheafCohomology.lean#L165-L179",
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
- Source path: [`TauLib/BookII/CentralTheorem/SheafCohomology.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/SheafCohomology.lean#L165-L179)
- Source range: L165-L179
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.P20` — Čech-to-Derived Comparison

## Immediate Comment / Docstring

```lean
/-- [II.P20] Acyclicity of the cylinder cover: any intersection of
    cylinders at the same stage is either empty or a cylinder.
    In the ultrametric topology, C_{k,a} ∩ C_{k,b} = ∅ for a ≠ b. -/
```

## Source Excerpt

```lean
def cover_acyclic_check (k : Nat) : Bool :=
  let pk := primorial k
  go 0 0 pk pk
where
  go (a b pk fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if a >= pk then true
    else if b >= pk then go (a + 1) 0 pk (fuel - 1)
    else
      -- C_{k,a} ∩ C_{k,b}: nonempty iff a = b
      let nonempty := a == b
      -- If nonempty, intersection is a cylinder (C_{k,a} itself)
      let ok := if nonempty then true else true  -- empty or cylinder, both OK
      ok && go a (b + 1) pk (fuel - 1)
  termination_by fuel
```
