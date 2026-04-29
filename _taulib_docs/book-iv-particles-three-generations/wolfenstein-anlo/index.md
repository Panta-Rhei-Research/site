---
{
  "projection_kind": "taulib_declaration",
  "title": "WolfensteinANLO",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/wolfenstein-anlo/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::WolfensteinANLO",
  "declaration_slug": "wolfenstein-anlo",
  "kind": "structure",
  "name": "WolfensteinANLO",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 2789,
  "source_line_end": 2804,
  "registry_ids": [
    "IV.D381"
  ],
  "related_registry_items": [
    {
      "id": "IV.D381",
      "title": "Wolfenstein A NLO: Confinement Correction",
      "url": "/registry/object/IV.D381/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2789-L2804",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2789-L2804",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2789-L2804)
- Source range: L2789-L2804
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D381` — Wolfenstein A NLO: Confinement Correction

## Immediate Comment / Docstring

```lean
/-- [IV.D381] Wolfenstein A NLO: confinement correction.
    A_NLO = A_LO·(1-ι_τ³) = 0.7925 at +3109 ppm. -/
```

## Source Excerpt

```lean
structure WolfensteinANLO where
  /-- A_LO (×10000). -/
  a_lo_x10000 : Nat := 8253
  /-- A_NLO (×10000). -/
  a_nlo_x10000 : Nat := 7925
  /-- PDG A (×10000). -/
  a_pdg_x10000 : Nat := 7900
  /-- LO deviation ppm. -/
  lo_ppm : Int := 44642
  /-- NLO deviation ppm. -/
  nlo_ppm : Int := 3109
  /-- Improvement factor. -/
  improvement : Nat := 14
  /-- Correction is ι_τ^dim(τ³). -/
  correction_exponent : Nat := 3
  deriving Repr
```
