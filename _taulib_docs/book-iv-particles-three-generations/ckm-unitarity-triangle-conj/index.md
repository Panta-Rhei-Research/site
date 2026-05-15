---
{
  "projection_kind": "taulib_declaration",
  "title": "ckm_unitarity_triangle_conj",
  "permalink": "/corpus/taulib/docs/book-iv-particles-three-generations/ckm-unitarity-triangle-conj/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::ckm_unitarity_triangle_conj",
  "declaration_slug": "ckm-unitarity-triangle-conj",
  "kind": "theorem",
  "name": "ckm_unitarity_triangle_conj",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/corpus/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 1357,
  "source_line_end": 1362,
  "registry_ids": [
    "IV.P198"
  ],
  "related_registry_items": [
    {
      "id": "IV.P198",
      "title": "CKM Unitarity Triangle Angles from tau-Framework",
      "url": "/registry/object/IV.P198/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1357-L1362",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1357-L1362",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1357-L1362)
- Source range: L1357-L1362
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `IV.P198` — CKM Unitarity Triangle Angles from tau-Framework

## Immediate Comment / Docstring

```lean
/-- [IV.P198] Conjunction: 3 angles, sum 180°, β and γ values. -/
```

## Source Excerpt

```lean
theorem ckm_unitarity_triangle_conj :
    ckm_unitarity_triangle.n_angles = 3 ∧
    ckm_unitarity_triangle.angle_sum_degrees = 180 ∧
    ckm_unitarity_triangle.beta_deg_x100 = 2248 ∧
    ckm_unitarity_triangle.gamma_deg_x100 = 6544 :=
  ⟨rfl, rfl, rfl, rfl⟩
```
