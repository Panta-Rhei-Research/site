---
{
  "projection_kind": "taulib_declaration",
  "title": "JarlskogInvariant",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/jarlskog-invariant/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::JarlskogInvariant",
  "declaration_slug": "jarlskog-invariant",
  "kind": "structure",
  "name": "JarlskogInvariant",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 2576,
  "source_line_end": 2587,
  "registry_ids": [
    "IV.T195"
  ],
  "related_registry_items": [
    {
      "id": "IV.T195",
      "title": "Jarlskog Invariant from τ-CKM at −35000 ppm",
      "url": "/registry/object/IV.T195/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2576-L2587",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2576-L2587",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2576-L2587)
- Source range: L2576-L2587
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T195` — Jarlskog Invariant from τ-CKM at −35000 ppm

## Immediate Comment / Docstring

```lean
/-- [IV.T195] Jarlskog invariant from τ-CKM.
    J(τ) = 2.97 × 10⁻⁵ vs PDG (3.08 ± 0.15) × 10⁻⁵.
    At -35000 ppm, within 0.7σ. -/
```

## Source Excerpt

```lean
structure JarlskogInvariant where
  /-- J (×10⁷ for integer). -/
  j_x1e7 : Nat := 297
  /-- PDG J (×10⁷). -/
  j_pdg_x1e7 : Nat := 308
  /-- Deviation ppm. -/
  deviation_ppm : Int := -35000
  /-- Within 1σ. -/
  within_1sigma : Nat := 1
  /-- Number of free parameters. -/
  free_params : Nat := 0
  deriving Repr
```
