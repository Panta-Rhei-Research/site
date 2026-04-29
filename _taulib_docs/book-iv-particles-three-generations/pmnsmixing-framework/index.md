---
{
  "projection_kind": "taulib_declaration",
  "title": "PMNSMixingFramework",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/pmnsmixing-framework/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::PMNSMixingFramework",
  "declaration_slug": "pmnsmixing-framework",
  "kind": "structure",
  "name": "PMNSMixingFramework",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 1148,
  "source_line_end": 1159,
  "registry_ids": [
    "IV.P196"
  ],
  "related_registry_items": [
    {
      "id": "IV.P196",
      "title": "PMNS Large Mixing from A-Sector Rotation and QLC Complementarity",
      "url": "/registry/object/IV.P196/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1148-L1159",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1148-L1159",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1148-L1159)
- Source range: L1148-L1159
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P196` — PMNS Large Mixing from A-Sector Rotation and QLC Complementarity

## Immediate Comment / Docstring

```lean
/-- [IV.P196] PMNS large mixing framework structure. -/
```

## Source Excerpt

```lean
structure PMNSMixingFramework where
  /-- Number of PMNS mixing angles. -/
  n_mixing_angles : Nat
  /-- Three mixing angles. -/
  angles_eq : n_mixing_angles = 3
  /-- Number of σ-polarity shared eigenvectors (bare PMNS → near-identity). -/
  n_sigma_eigenvectors : Nat := 3
  /-- Number of A-sector rotations. -/
  n_a_sector_rotations : Nat := 1
  /-- QLC complementarity sum (degrees): θ₁₂+θ_C ≈ 45°. -/
  qlc_sum_degrees : Nat := 45
  deriving Repr
```
