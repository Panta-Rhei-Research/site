---
{
  "projection_kind": "taulib_declaration",
  "title": "FiniteAtEveryLevel",
  "permalink": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/finite-at-every-level/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.ManyBody.FluidRegimes`.",
  "declaration_id": "TauLib.BookIV.ManyBody.FluidRegimes::FiniteAtEveryLevel",
  "declaration_slug": "finite-at-every-level",
  "kind": "structure",
  "name": "FiniteAtEveryLevel",
  "module_name": "TauLib.BookIV.ManyBody.FluidRegimes",
  "module_url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/",
  "source_line_start": 116,
  "source_line_end": 127,
  "registry_ids": [
    "IV.P140"
  ],
  "related_registry_items": [
    {
      "id": "IV.P140",
      "title": "Finite at every primorial level",
      "url": "/registry/object/IV.P140/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/FluidRegimes.lean#L116-L127",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.ManyBody.FluidRegimes",
        "url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/FluidRegimes.lean#L116-L127",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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

- Module: [TauLib.BookIV.ManyBody.FluidRegimes](/verify/taulib/docs/book-iv-many-body-fluid-regimes/)
- Source path: [`TauLib/BookIV/ManyBody/FluidRegimes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/FluidRegimes.lean#L116-L127)
- Source range: L116-L127
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P140` — Finite at every primorial level

## Immediate Comment / Docstring

```lean
/-- [IV.P140] At every primorial level n, the defect-tuple components satisfy
    |mu_n|, |nu_n|, |kappa_n|, |theta_n| <= M * Prim(n)^{1/2} for a
    uniform constant M. This is unconditional finiteness at every finite stage,
    the structural prerequisite for well-defined evolution. -/
```

## Source Excerpt

```lean
structure FiniteAtEveryLevel where
  /-- Bound: M * Prim(n)^{1/2}. -/
  bound_type : String := "M * Prim(n)^{1/2}"
  /-- Number of uniform bounding constants (1 = constant M). -/
  n_bound_constants : Nat := 1
  /-- Number of excluded stages (0 = every stage). -/
  n_excluded_stages : Nat := 0
  /-- Number of regularity assumptions required (0 = unconditional). -/
  n_assumptions : Nat := 0
  /-- Every stage is covered: none excluded. -/
  covers_all : n_excluded_stages = 0
  deriving Repr
```
