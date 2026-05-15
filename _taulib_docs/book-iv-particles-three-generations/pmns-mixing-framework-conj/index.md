---
{
  "projection_kind": "taulib_declaration",
  "title": "pmns_mixing_framework_conj",
  "permalink": "/corpus/taulib/docs/book-iv-particles-three-generations/pmns-mixing-framework-conj/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::pmns_mixing_framework_conj",
  "declaration_slug": "pmns-mixing-framework-conj",
  "kind": "theorem",
  "name": "pmns_mixing_framework_conj",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/corpus/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 1166,
  "source_line_end": 1171,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1166-L1171",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.ThreeGenerations",
        "url": "/corpus/taulib/docs/book-iv-particles-three-generations/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1166-L1171",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookIV.Particles.ThreeGenerations](/corpus/taulib/docs/book-iv-particles-three-generations/)
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1166-L1171)
- Source range: L1166-L1171
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `IV.P196` — PMNS Large Mixing from A-Sector Rotation and QLC Complementarity

## Immediate Comment / Docstring

```lean
/-- [IV.P196] Conjunction: 3 angles, 3 σ eigenvectors, 1 A-sector rotation, QLC=45°. -/
```

## Source Excerpt

```lean
theorem pmns_mixing_framework_conj :
    pmns_mixing_framework.n_mixing_angles = 3 ∧
    pmns_mixing_framework.n_sigma_eigenvectors = 3 ∧
    pmns_mixing_framework.n_a_sector_rotations = 1 ∧
    pmns_mixing_framework.qlc_sum_degrees = 45 :=
  ⟨rfl, rfl, rfl, rfl⟩
```
