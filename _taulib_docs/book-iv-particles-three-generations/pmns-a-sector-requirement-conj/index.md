---
{
  "projection_kind": "taulib_declaration",
  "title": "pmns_a_sector_requirement_conj",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/pmns-a-sector-requirement-conj/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::pmns_a_sector_requirement_conj",
  "declaration_slug": "pmns-a-sector-requirement-conj",
  "kind": "theorem",
  "name": "pmns_a_sector_requirement_conj",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 826,
  "source_line_end": 830,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L826-L830",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L826-L830",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L826-L830)
- Source range: L826-L830
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T153` — PMNS Large Mixing Requires A-Sector Flavor Rotation Beyond σ-Matrix

## Immediate Comment / Docstring

```lean
/-- [IV.T153] Conjunction: 3 shared eigenvectors, 1 A-sector rotation, 1 coupling scale. -/
```

## Source Excerpt

```lean
theorem pmns_a_sector_requirement_conj :
    pmns_a_sector_requirement.n_shared_eigenvectors = 3 ∧
    pmns_a_sector_requirement.n_a_sector_rotations = 1 ∧
    pmns_a_sector_requirement.n_coupling_scales = 1 :=
  ⟨rfl, rfl, rfl⟩
```
