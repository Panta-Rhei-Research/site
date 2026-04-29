---
{
  "projection_kind": "taulib_declaration",
  "title": "SchwarzschildRelation",
  "permalink": "/verify/taulib/docs/book-v-gravity-schwarzschild/schwarzschild-relation/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Gravity.Schwarzschild`.",
  "declaration_id": "TauLib.BookV.Gravity.Schwarzschild::SchwarzschildRelation",
  "declaration_slug": "schwarzschild-relation",
  "kind": "structure",
  "name": "SchwarzschildRelation",
  "module_name": "TauLib.BookV.Gravity.Schwarzschild",
  "module_url": "/verify/taulib/docs/book-v-gravity-schwarzschild/",
  "source_line_start": 113,
  "source_line_end": 128,
  "registry_ids": [
    "V.D08"
  ],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/Schwarzschild.lean#L113-L128",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Gravity.Schwarzschild",
        "url": "/verify/taulib/docs/book-v-gravity-schwarzschild/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/Schwarzschild.lean#L113-L128",
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

- Module: [TauLib.BookV.Gravity.Schwarzschild](/verify/taulib/docs/book-v-gravity-schwarzschild/)
- Source path: [`TauLib/BookV/Gravity/Schwarzschild.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/Schwarzschild.lean#L113-L128)
- Source range: L113-L128
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [V.D08] Tau-Schwarzschild relation: R_n(x) = 2 · G_τ · M_n(x).

    Linear coupling between major radius index and mass index,
    arising from the single surviving scale degree of freedom
    on the stabilized torus vacuum.

    BH topology is T² (not S²) — only scale remains as free parameter.

    Cross-multiplied form:
    radius_numer · mass_denom · g_denom =
    2 · g_numer · mass_numer · radius_denom -/
```

## Source Excerpt

```lean
structure SchwarzschildRelation where
  /-- Major radius index numerator R_n(x). -/
  radius_numer : Nat
  /-- Major radius index denominator. -/
  radius_denom : Nat
  /-- Radius denominator positive. -/
  radius_denom_pos : radius_denom > 0
  /-- The BH mass index. -/
  mass : BHMassIndex
  /-- The gravitational constant. -/
  g_tau : GravConstant
  /-- The Schwarzschild identity: R = 2 G_τ M (cross-multiplied). -/
  schwarzschild_identity :
    radius_numer * mass.mass_denom * g_tau.g_denom =
    2 * g_tau.g_numer * mass.mass_numer * radius_denom
  deriving Repr
```
