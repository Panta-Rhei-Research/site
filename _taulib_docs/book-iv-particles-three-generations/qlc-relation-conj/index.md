---
{
  "projection_kind": "taulib_declaration",
  "title": "qlc_relation_conj",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/qlc-relation-conj/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::qlc_relation_conj",
  "declaration_slug": "qlc-relation-conj",
  "kind": "theorem",
  "name": "qlc_relation_conj",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 877,
  "source_line_end": 881,
  "registry_ids": [
    "IV.P189"
  ],
  "related_registry_items": [
    {
      "id": "IV.P189",
      "title": "Quark-Lepton Complementarity: θ₁₂+θ_C ≈ π/4 from Fiber-Base Duality",
      "url": "/registry/object/IV.P189/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L877-L881",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L877-L881",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L877-L881)
- Source range: L877-L881
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.P189` — Quark-Lepton Complementarity: θ₁₂+θ_C ≈ π/4 from Fiber-Base Duality

## Immediate Comment / Docstring

```lean
/-- [IV.P189] Conjunction: target 45°, deviation ≤ 3%, 1 A-sector rotation. -/
```

## Source Excerpt

```lean
theorem qlc_relation_conj :
    qlc_relation_data.target_degrees = 45 ∧
    qlc_relation_data.deviation_pct_x10 = 30 ∧
    qlc_relation_data.n_a_sector_rotations = 1 :=
  ⟨rfl, rfl, rfl⟩
```
