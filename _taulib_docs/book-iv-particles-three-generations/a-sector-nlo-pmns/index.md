---
{
  "projection_kind": "taulib_declaration",
  "title": "a_sector_nlo_pmns",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/a-sector-nlo-pmns/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::a_sector_nlo_pmns",
  "declaration_slug": "a-sector-nlo-pmns",
  "kind": "def",
  "name": "a_sector_nlo_pmns",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 1827,
  "source_line_end": 1829,
  "registry_ids": [
    "IV.D365"
  ],
  "related_registry_items": [
    {
      "id": "IV.D365",
      "title": "A-Sector NLO PMNS Rotation",
      "url": "/registry/object/IV.D365/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1827-L1829",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1827-L1829",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1827-L1829)
- Source range: L1827-L1829
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.D365` — A-Sector NLO PMNS Rotation

## Immediate Comment / Docstring

```lean
/-- [IV.D365] A-Sector NLO PMNS Rotation.
    The σ-polarity matrix is shared by M_ℓ and M_ν (same eigenvectors),
    so bare PMNS ≈ identity. All mixing from A-sector (π-generator) rotation.
    NLO: sin(θ₂₃) = (1−ι_τ⁵)/(1+ι_τ), with W₃(4)=5. -/
```

## Source Excerpt

```lean
def a_sector_nlo_pmns : String :=
  "A-sector NLO PMNS rotation: sin(θ₂₃)_NLO = (1-ι_τ^5)/(1+ι_τ). " ++
  "Bare PMNS ≈ identity from shared σ-matrix eigenvectors."
```
