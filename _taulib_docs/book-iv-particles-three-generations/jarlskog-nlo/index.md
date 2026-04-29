---
{
  "projection_kind": "taulib_declaration",
  "title": "JarlskogNLO",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/jarlskog-nlo/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::JarlskogNLO",
  "declaration_slug": "jarlskog-nlo",
  "kind": "structure",
  "name": "JarlskogNLO",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 2810,
  "source_line_end": 2827,
  "registry_ids": [
    "IV.T198"
  ],
  "related_registry_items": [
    {
      "id": "IV.T198",
      "title": "Jarlskog NLO at +2624 ppm",
      "url": "/registry/object/IV.T198/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2810-L2827",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2810-L2827",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2810-L2827)
- Source range: L2810-L2827
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T198` — Jarlskog NLO at +2624 ppm

## Immediate Comment / Docstring

```lean
/-- [IV.T198] Jarlskog NLO at +2624 ppm.
    J_NLO = J_LO·(1+ι_τ³) = 3.088×10⁻⁵. -/
```

## Source Excerpt

```lean
structure JarlskogNLO where
  /-- J_NLO (×10⁷). -/
  j_nlo_x1e7 : Nat := 309
  /-- J_LO (×10⁷). -/
  j_lo_x1e7 : Nat := 297
  /-- PDG J (×10⁷). -/
  j_pdg_x1e7 : Nat := 308
  /-- LO deviation ppm. -/
  lo_ppm : Int := -35714
  /-- NLO deviation ppm. -/
  nlo_ppm : Int := 2624
  /-- Improvement factor (×10). -/
  improvement_x10 : Nat := 136
  /-- Correction exponent = dim(τ³). -/
  correction_exponent : Nat := 3
  /-- Sign duality: A gets (1-δ), J gets (1+δ). -/
  sign_duality : Bool := true
  deriving Repr
```
