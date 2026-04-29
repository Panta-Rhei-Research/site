---
{
  "projection_kind": "taulib_declaration",
  "title": "cech_derived_comparison_check",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-sheaf-cohomology/cech-derived-comparison-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.CentralTheorem.SheafCohomology`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.SheafCohomology::cech_derived_comparison_check",
  "declaration_slug": "cech-derived-comparison-check",
  "kind": "def",
  "name": "cech_derived_comparison_check",
  "module_name": "TauLib.BookII.CentralTheorem.SheafCohomology",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-sheaf-cohomology/",
  "source_line_start": 184,
  "source_line_end": 187,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/SheafCohomology.lean#L184-L187",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/SheafCohomology.lean#L184-L187",
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
- Source path: [`TauLib/BookII/CentralTheorem/SheafCohomology.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/SheafCohomology.lean#L184-L187)
- Source range: L184-L187
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.P20` — Čech-to-Derived Comparison

## Immediate Comment / Docstring

```lean
/-- [II.P20] Čech-to-derived comparison: on an acyclic cover,
    Čech cohomology = derived functor cohomology.
    Verify: H⁰ = Γ(X, F) and H¹ = 0 (acyclic). -/
```

## Source Excerpt

```lean
def cech_derived_comparison_check (k : Nat) : Bool :=
  h0_equals_global_check k &&
  h1_check k &&
  cover_acyclic_check k
```
