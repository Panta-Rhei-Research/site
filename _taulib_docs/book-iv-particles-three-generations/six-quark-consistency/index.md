---
{
  "projection_kind": "taulib_declaration",
  "title": "SixQuarkConsistency",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/six-quark-consistency/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::SixQuarkConsistency",
  "declaration_slug": "six-quark-consistency",
  "kind": "structure",
  "name": "SixQuarkConsistency",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 2557,
  "source_line_end": 2568,
  "registry_ids": [
    "IV.D377"
  ],
  "related_registry_items": [
    {
      "id": "IV.D377",
      "title": "Six-Quark τ-Chain Mass Table",
      "url": "/registry/object/IV.D377/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2557-L2568",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2557-L2568",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2557-L2568)
- Source range: L2557-L2568
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D377` — Six-Quark τ-Chain Mass Table

## Immediate Comment / Docstring

```lean
/-- [IV.D377] Six-quark τ-chain mass table.
    RMS over 5 well-determined quarks (t,b,c,s,d): 1243 ppm. -/
```

## Source Excerpt

```lean
structure SixQuarkConsistency where
  /-- Number of quarks predicted. -/
  n_quarks : Nat := 6
  /-- Number within 2σ of PDG. -/
  n_within_2sigma : Nat := 5
  /-- RMS ppm over 5 well-determined quarks. -/
  rms_ppm : Nat := 1243
  /-- Correct mass ordering reproduced. -/
  ordering_correct : Nat := 1
  /-- All six quarks present. -/
  complete : n_quarks = 6
  deriving Repr
```
