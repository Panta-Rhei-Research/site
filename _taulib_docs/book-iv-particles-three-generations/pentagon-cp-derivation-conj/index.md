---
{
  "projection_kind": "taulib_declaration",
  "title": "pentagon_cp_derivation_conj",
  "permalink": "/corpus/taulib/docs/book-iv-particles-three-generations/pentagon-cp-derivation-conj/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::pentagon_cp_derivation_conj",
  "declaration_slug": "pentagon-cp-derivation-conj",
  "kind": "theorem",
  "name": "pentagon_cp_derivation_conj",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/corpus/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 1500,
  "source_line_end": 1504,
  "registry_ids": [
    "IV.P200"
  ],
  "related_registry_items": [
    {
      "id": "IV.P200",
      "title": "CP Violation from ω-Period Pentagon: Pentagon-Angle Derivation",
      "url": "/registry/object/IV.P200/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1500-L1504",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1500-L1504",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1500-L1504)
- Source range: L1500-L1504
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `IV.P200` — CP Violation from ω-Period Pentagon: Pentagon-Angle Derivation

## Immediate Comment / Docstring

```lean
/-- [IV.P200] Conjunction: 5 generators, ρ̄ denom multiplier, 72° step. -/
```

## Source Excerpt

```lean
theorem pentagon_cp_derivation_conj :
    pentagon_cp_data.n_generators = 5 ∧
    pentagon_cp_data.rho_bar_denom_multiplier = 2 ∧
    pentagon_cp_data.step_angle_degrees = 72 :=
  ⟨rfl, rfl, rfl⟩
```
