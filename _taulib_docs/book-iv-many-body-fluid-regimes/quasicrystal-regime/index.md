---
{
  "projection_kind": "taulib_declaration",
  "title": "QuasicrystalRegime",
  "permalink": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/quasicrystal-regime/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.ManyBody.FluidRegimes`.",
  "declaration_id": "TauLib.BookIV.ManyBody.FluidRegimes::QuasicrystalRegime",
  "declaration_slug": "quasicrystal-regime",
  "kind": "structure",
  "name": "QuasicrystalRegime",
  "module_name": "TauLib.BookIV.ManyBody.FluidRegimes",
  "module_url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/",
  "source_line_start": 294,
  "source_line_end": 305,
  "registry_ids": [
    "IV.D237"
  ],
  "related_registry_items": [
    {
      "id": "IV.D237",
      "title": "Quasicrystal regime",
      "url": "/registry/object/IV.D237/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/FluidRegimes.lean#L294-L305",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/FluidRegimes.lean#L294-L305",
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
- Source path: [`TauLib/BookIV/ManyBody/FluidRegimes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/FluidRegimes.lean#L294-L305)
- Source range: L294-L305
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D237` — Quasicrystal regime

## Immediate Comment / Docstring

```lean
/-- [IV.D237] Quasicrystal regime: all four components frozen, but
    theta_0 is an irrational winding number (incommensurate with
    the torus periods). This produces aperiodic long-range order
    without translational symmetry — Penrose-type tilings. -/
```

## Source Excerpt

```lean
structure QuasicrystalRegime where
  /-- Number of frozen tuple components (4 = all). -/
  n_frozen_components : Nat := 4
  /-- Number of incommensurate winding ratios (1 = irrational). -/
  n_incommensurate_ratios : Nat := 1
  /-- Number of translational symmetries (0 = aperiodic). -/
  n_translation_symmetries : Nat := 0
  /-- Number of broken discrete symmetries (1 = translation broken). -/
  n_broken_symmetries : Nat := 1
  /-- All four components frozen. -/
  fully_frozen : n_frozen_components = 4
  deriving Repr
```
