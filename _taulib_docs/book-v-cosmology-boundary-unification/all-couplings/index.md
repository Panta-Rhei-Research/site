---
{
  "projection_kind": "taulib_declaration",
  "title": "all_couplings",
  "permalink": "/verify/taulib/docs/book-v-cosmology-boundary-unification/all-couplings/",
  "summary_short": "`def` declaration in `TauLib.BookV.Cosmology.BoundaryUnification`.",
  "declaration_id": "TauLib.BookV.Cosmology.BoundaryUnification::all_couplings",
  "declaration_slug": "all-couplings",
  "kind": "def",
  "name": "all_couplings",
  "module_name": "TauLib.BookV.Cosmology.BoundaryUnification",
  "module_url": "/verify/taulib/docs/book-v-cosmology-boundary-unification/",
  "source_line_start": 205,
  "source_line_end": 217,
  "registry_ids": [
    "V.P104"
  ],
  "related_registry_items": [
    {
      "id": "V.P104",
      "title": "iota_tau mediates all ten couplings",
      "url": "/registry/object/V.P104/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BoundaryUnification.lean#L205-L217",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.BoundaryUnification",
        "url": "/verify/taulib/docs/book-v-cosmology-boundary-unification/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BoundaryUnification.lean#L205-L217",
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

- Module: [TauLib.BookV.Cosmology.BoundaryUnification](/verify/taulib/docs/book-v-cosmology-boundary-unification/)
- Source path: [`TauLib/BookV/Cosmology/BoundaryUnification.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BoundaryUnification.lean#L205-L217)
- Source range: L205-L217
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.P104` — iota_tau mediates all ten couplings

## Immediate Comment / Docstring

```lean
/-- [V.P104] ι_τ mediates all ten couplings: every coupling constant
    in τ is a rational function of ι_τ = 2/(π+e).

    4 self-couplings + 6 cross-couplings = 10 total.
    Plus the closing identity (α_G from α¹⁸) = 11th relation. -/
```

## Source Excerpt

```lean
def all_couplings : List CouplingEntry :=
  [ -- Self-couplings
    { name := "kappa(D;1) = 1 - iota", kind := .SelfCoupling, value_times_1e6 := 658541 },
    { name := "kappa(A;2) = iota^2/(1-iota)", kind := .SelfCoupling, value_times_1e6 := 177062 },
    { name := "kappa(B;1) = iota/(1-iota)", kind := .SelfCoupling, value_times_1e6 := 518601 },
    { name := "kappa(C;3) = iota^3/(1-iota)", kind := .SelfCoupling, value_times_1e6 := 60435 },
    -- Cross-couplings (placeholder representative values)
    { name := "kappa(D,A)", kind := .CrossCoupling, value_times_1e6 := 224900 },
    { name := "kappa(D,B)", kind := .CrossCoupling, value_times_1e6 := 341304 },
    { name := "kappa(D,C)", kind := .CrossCoupling, value_times_1e6 := 116594 },
    { name := "kappa(A,B)", kind := .CrossCoupling, value_times_1e6 := 177062 },
    { name := "kappa(A,C)", kind := .CrossCoupling, value_times_1e6 := 60435 },
    { name := "kappa(B,C)", kind := .CrossCoupling, value_times_1e6 := 177062 } ]
```
