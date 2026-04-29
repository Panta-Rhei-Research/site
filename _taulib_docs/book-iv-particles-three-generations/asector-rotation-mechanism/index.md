---
{
  "projection_kind": "taulib_declaration",
  "title": "ASectorRotationMechanism",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/asector-rotation-mechanism/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::ASectorRotationMechanism",
  "declaration_slug": "asector-rotation-mechanism",
  "kind": "structure",
  "name": "ASectorRotationMechanism",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 2280,
  "source_line_end": 2293,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2280-L2293",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2280-L2293",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2280-L2293)
- Source range: L2280-L2293
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [IV.T162/T174/T175 upgrade] A-sector rotation mechanism.

    The π-generator (A-sector, weak force) acts on the 3-generation
    structure via the polarity matrix. The rotation angle on the
    base cycle g₃ is determined by κ(A;1) = ι_τ.

    Key equation: sin(θ_A) = κ_ω = ι_τ/(1+ι_τ)
    This is the A-sector crossing amplitude normalized by
    the full holonomy.

    Physical: sin(θ₂₃)_LO = 1/(1+ι_τ) is "one full A-sector
    traversal" — the natural output of the π-generator rotation.

    NLO: sin(θ₂₃) = (1−ι_τ⁵)/(1+ι_τ) at +8604 ppm.
    The ι_τ⁵ correction is the W₃(4)-order Window correction. -/
```

## Source Excerpt

```lean
structure ASectorRotationMechanism where
  /-- π-generator index in {α,π,γ,η,ω}: 2nd generator. -/
  pi_generator_index : Nat := 2
  /-- LO deviation from PDG in ppm. -/
  lo_deviation_ppm : Nat := 18012
  /-- NLO deviation from PDG in ppm. -/
  nlo_deviation_ppm : Nat := 8604
  /-- Window exponent W₃(4) in NLO correction. -/
  nlo_window_exp : Nat := 5
  /-- Number of mixing matrices bridged (CKM + PMNS). -/
  n_matrices_bridged : Nat := 2
  /-- Polarity matrix dimension (3×3). -/
  polarity_dim : Nat := 3
  deriving Repr
```
