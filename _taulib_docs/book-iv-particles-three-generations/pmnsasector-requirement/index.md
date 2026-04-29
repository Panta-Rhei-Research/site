---
{
  "projection_kind": "taulib_declaration",
  "title": "PMNSASectorRequirement",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/pmnsasector-requirement/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::PMNSASectorRequirement",
  "declaration_slug": "pmnsasector-requirement",
  "kind": "structure",
  "name": "PMNSASectorRequirement",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 813,
  "source_line_end": 820,
  "registry_ids": [
    "IV.T153"
  ],
  "related_registry_items": [
    {
      "id": "IV.T153",
      "title": "PMNS Large Mixing Requires A-Sector Flavor Rotation Beyond σ-Matrix",
      "url": "/registry/object/IV.T153/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L813-L820",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L813-L820",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L813-L820)
- Source range: L813-L820
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T153` — PMNS Large Mixing Requires A-Sector Flavor Rotation Beyond σ-Matrix

## Immediate Comment / Docstring

```lean
/-- [IV.T153] PMNS requires A-sector rotation structure. -/
```

## Source Excerpt

```lean
structure PMNSASectorRequirement where
  /-- Number of shared eigenvectors from σ-polarity (→ PMNS bare = identity). -/
  n_shared_eigenvectors : Nat := 3
  /-- Number of A-sector (π-generator) rotations needed. -/
  n_a_sector_rotations : Nat := 1
  /-- Number of candidate coupling scales (κ_D = 1−ι_τ). -/
  n_coupling_scales : Nat := 1
  deriving Repr
```
