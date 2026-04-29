---
{
  "projection_kind": "taulib_declaration",
  "title": "GravConstant",
  "permalink": "/verify/taulib/docs/book-v-gravity-gravitational-constant/grav-constant/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Gravity.GravitationalConstant`.",
  "declaration_id": "TauLib.BookV.Gravity.GravitationalConstant::GravConstant",
  "declaration_slug": "grav-constant",
  "kind": "structure",
  "name": "GravConstant",
  "module_name": "TauLib.BookV.Gravity.GravitationalConstant",
  "module_url": "/verify/taulib/docs/book-v-gravity-gravitational-constant/",
  "source_line_start": 138,
  "source_line_end": 147,
  "registry_ids": [
    "V.D02"
  ],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/GravitationalConstant.lean#L138-L147",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/GravitationalConstant.lean#L138-L147",
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
- Source path: [`TauLib/BookV/Gravity/GravitationalConstant.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/GravitationalConstant.lean#L138-L147)
- Source range: L138-L147
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [V.D02] Gravitational constant G_τ.

    Defined from the minimal mature BH state:
    G_τ := R_min / (2 · M_min)

    Both R and M are readouts of a single surviving scale parameter
    on the stabilized torus vacuum. The factor of 2 comes from the
    canonical Schwarzschild form.

    Properties:
    - Well-defined by refinement coherence beyond maturity horizon
    - G_τ > 0 (positive gravitational coupling)
    - In orthodox units: G = (c³/ℏ) · ι_τ² (sector self-coupling readout) -/
```

## Source Excerpt

```lean
structure GravConstant where
  /-- G_τ numerator. -/
  g_numer : Nat
  /-- G_τ denominator. -/
  g_denom : Nat
  /-- Denominator positive. -/
  denom_pos : g_denom > 0
  /-- G_τ is positive (gravitational attraction). -/
  g_positive : g_numer > 0
  deriving Repr
```
