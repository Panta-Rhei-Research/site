---
{
  "projection_kind": "taulib_declaration",
  "title": "TorusVacuum",
  "permalink": "/verify/taulib/docs/book-v-gravity-gravitational-constant/torus-vacuum/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Gravity.GravitationalConstant`.",
  "declaration_id": "TauLib.BookV.Gravity.GravitationalConstant::TorusVacuum",
  "declaration_slug": "torus-vacuum",
  "kind": "structure",
  "name": "TorusVacuum",
  "module_name": "TauLib.BookV.Gravity.GravitationalConstant",
  "module_url": "/verify/taulib/docs/book-v-gravity-gravitational-constant/",
  "source_line_start": 74,
  "source_line_end": 91,
  "registry_ids": [
    "V.D01"
  ],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/GravitationalConstant.lean#L74-L91",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Gravity.GravitationalConstant",
        "url": "/verify/taulib/docs/book-v-gravity-gravitational-constant/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/GravitationalConstant.lean#L74-L91",
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

- Module: [TauLib.BookV.Gravity.GravitationalConstant](/verify/taulib/docs/book-v-gravity-gravitational-constant/)
- Source path: [`TauLib/BookV/Gravity/GravitationalConstant.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/GravitationalConstant.lean#L74-L91)
- Source range: L74-L91
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [V.D01] Torus vacuum: the stabilized torus configuration of a
    mature black hole state.

    The shape ratio r/R = ι_τ is fixed by refinement coherence:
    - r = minor radius index (fiber dimension)
    - R = major radius index (base dimension)
    - Only scale (R) remains as free parameter

    The BH topology is a 2-torus T² (NOT a 3-ball). This is the
    unique stabilized topology from τ-NF convergence. -/
```

## Source Excerpt

```lean
structure TorusVacuum where
  /-- Minor radius index numerator (r). -/
  minor_numer : Nat
  /-- Minor radius index denominator. -/
  minor_denom : Nat
  /-- Major radius index numerator (R). -/
  major_numer : Nat
  /-- Major radius index denominator. -/
  major_denom : Nat
  /-- Both denominators positive. -/
  minor_denom_pos : minor_denom > 0
  major_denom_pos : major_denom > 0
  /-- Major radius positive (physical). -/
  major_positive : major_numer > 0
  /-- Shape ratio r/R = ι_τ = iota/iotaD (cross-multiplied). -/
  shape_ratio : minor_numer * major_denom * iotaD =
                iota * minor_denom * major_numer
  deriving Repr
```
