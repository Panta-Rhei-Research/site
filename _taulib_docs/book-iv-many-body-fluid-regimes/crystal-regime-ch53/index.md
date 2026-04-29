---
{
  "projection_kind": "taulib_declaration",
  "title": "CrystalRegimeCh53",
  "permalink": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/crystal-regime-ch53/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.ManyBody.FluidRegimes`.",
  "declaration_id": "TauLib.BookIV.ManyBody.FluidRegimes::CrystalRegimeCh53",
  "declaration_slug": "crystal-regime-ch53",
  "kind": "structure",
  "name": "CrystalRegimeCh53",
  "module_name": "TauLib.BookIV.ManyBody.FluidRegimes",
  "module_url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/",
  "source_line_start": 245,
  "source_line_end": 254,
  "registry_ids": [
    "IV.D235"
  ],
  "related_registry_items": [
    {
      "id": "IV.D235",
      "title": "Crystal regime",
      "url": "/registry/object/IV.D235/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/FluidRegimes.lean#L245-L254",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/FluidRegimes.lean#L245-L254",
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
- Source path: [`TauLib/BookIV/ManyBody/FluidRegimes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/FluidRegimes.lean#L245-L254)
- Source range: L245-L254
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D235` — Crystal regime

## Immediate Comment / Docstring

```lean
/-- [IV.D235] Crystal regime (ch53 formulation): mu ~ 0 (locked),
    nu ~ 0 (locked), kappa ~ 0 (rigid lattice), theta = theta_0 fixed.
    Atoms locked in periodic arrangement. -/
```

## Source Excerpt

```lean
structure CrystalRegimeCh53 where
  /-- Number of arrested tuple components (4 = all). -/
  n_arrested_components : Nat := 4
  /-- Number of lattice generators on T² (2 = periodic). -/
  n_lattice_generators : Nat := 2
  /-- Theta degrees of freedom (0 = fixed). -/
  theta_degrees_freedom : Nat := 0
  /-- All four tuple components arrested. -/
  fully_arrested : n_arrested_components = 4
  deriving Repr
```
