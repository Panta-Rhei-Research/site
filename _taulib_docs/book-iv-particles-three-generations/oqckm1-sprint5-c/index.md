---
{
  "projection_kind": "taulib_declaration",
  "title": "OQCKM1Sprint5C",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/oqckm1-sprint5-c/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::OQCKM1Sprint5C",
  "declaration_slug": "oqckm1-sprint5-c",
  "kind": "structure",
  "name": "OQCKM1Sprint5C",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 1316,
  "source_line_end": 1327,
  "registry_ids": [
    "IV.R407"
  ],
  "related_registry_items": [
    {
      "id": "IV.R407",
      "title": "OQ-CKM1 Status after Sprint 5C: rho_bar Derived, A Improved, eta_bar Open",
      "url": "/registry/object/IV.R407/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1316-L1327",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.ThreeGenerations",
        "url": "/verify/taulib/docs/book-iv-particles-three-generations/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1316-L1327",
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

- Module: [TauLib.BookIV.Particles.ThreeGenerations](/verify/taulib/docs/book-iv-particles-three-generations/)
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1316-L1327)
- Source range: L1316-L1327
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.R407` — OQ-CKM1 Status after Sprint 5C: rho_bar Derived, A Improved, eta_bar Open

## Immediate Comment / Docstring

```lean
/-- [IV.R407] OQ-CKM1 status structure after Sprint 5C (formalized). -/
```

## Source Excerpt

```lean
structure OQCKM1Sprint5C where
  /-- Number of resolved Wolfenstein parameters (λ_C, ρ̄, A). -/
  n_resolved : Nat := 3
  /-- Number of open Wolfenstein parameters (η̄). -/
  n_open : Nat := 1
  /-- Total Wolfenstein parameters. -/
  n_total : Nat := 4
  /-- λ_C deviation from PDG in ppm. -/
  lambda_deviation_ppm : Nat := 2327
  /-- ρ̄ deviation from PDG in ppm. -/
  rho_deviation_ppm : Nat := 975
  deriving Repr
```
