---
{
  "projection_kind": "taulib_declaration",
  "title": "MaxwellEquations",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/maxwell-equations/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.TauMaxwell`.",
  "declaration_id": "TauLib.BookIV.Electroweak.TauMaxwell::MaxwellEquations",
  "declaration_slug": "maxwell-equations",
  "kind": "structure",
  "name": "MaxwellEquations",
  "module_name": "TauLib.BookIV.Electroweak.TauMaxwell",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/",
  "source_line_start": 263,
  "source_line_end": 271,
  "registry_ids": [
    "IV.T44"
  ],
  "related_registry_items": [
    {
      "id": "IV.T44",
      "title": "Complete tau-Maxwell System",
      "url": "/registry/object/IV.T44/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauMaxwell.lean#L263-L271",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.TauMaxwell",
        "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauMaxwell.lean#L263-L271",
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

- Module: [TauLib.BookIV.Electroweak.TauMaxwell](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/)
- Source path: [`TauLib/BookIV/Electroweak/TauMaxwell.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauMaxwell.lean#L263-L271)
- Source range: L263-L271
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T44` — Complete tau-Maxwell System

## Immediate Comment / Docstring

```lean
/-- [IV.T44] All four Maxwell equations assembled:
    (1) div B = 0, (2) curl E = -∂B/∂t [from dF=0],
    (3) div E = ρ/ε₀, (4) curl B = μ₀J + μ₀ε₀ ∂E/∂t [from d*F=*J].
    Total: 2 + 2 = 4 equations. -/
```

## Source Excerpt

```lean
structure MaxwellEquations where
  /-- Bianchi identity (homogeneous pair). -/
  bianchi : BianchiIdentity
  /-- Source equation (inhomogeneous pair). -/
  source : SourceEquation
  /-- Total equation count. -/
  total_count : Nat
  total_eq : total_count = bianchi.maxwell_count + source.maxwell_count
  deriving Repr
```
