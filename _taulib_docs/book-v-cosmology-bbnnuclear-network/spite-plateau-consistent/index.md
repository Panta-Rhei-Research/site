---
{
  "projection_kind": "taulib_declaration",
  "title": "spite_plateau_consistent",
  "permalink": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/spite-plateau-consistent/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.BBNNuclearNetwork`.",
  "declaration_id": "TauLib.BookV.Cosmology.BBNNuclearNetwork::spite_plateau_consistent",
  "declaration_slug": "spite-plateau-consistent",
  "kind": "theorem",
  "name": "spite_plateau_consistent",
  "module_name": "TauLib.BookV.Cosmology.BBNNuclearNetwork",
  "module_url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/",
  "source_line_start": 441,
  "source_line_end": 447,
  "registry_ids": [
    "V.P167"
  ],
  "related_registry_items": [
    {
      "id": "V.P167",
      "title": "Spite Plateau Consistency",
      "url": "/registry/object/V.P167/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L441-L447",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.BBNNuclearNetwork",
        "url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L441-L447",
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

- Module: [TauLib.BookV.Cosmology.BBNNuclearNetwork](/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/)
- Source path: [`TauLib/BookV/Cosmology/BBNNuclearNetwork.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L441-L447)
- Source range: L441-L447
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P167` — Spite Plateau Consistency

## Immediate Comment / Docstring

```lean
/-- [V.P167] Including ~15% stellar depletion:
    1.87 × 10⁻¹⁰ × 0.85 ≈ 1.59 × 10⁻¹⁰.
    Spite plateau: (1.6 ± 0.3) × 10⁻¹⁰.
    Using ×10⁻¹² units: 187 × 85 / 100 = 158. Obs = 160 ± 30. -/
```

## Source Excerpt

```lean
theorem spite_plateau_consistent :
    -- Surface depletion: 187 × 85 / 100 = 158 (integer floor of 158.95)
    lithium_resolution.tau_x1e12 * 85 / 100 = 158 ∧
    -- 158 is within [130, 190] = obs ± 1σ
    158 ≥ lithium_resolution.obs_x1e12 - lithium_resolution.obs_unc_x1e12 ∧
    158 ≤ lithium_resolution.obs_x1e12 + lithium_resolution.obs_unc_x1e12 :=
  ⟨by native_decide, by native_decide, by native_decide⟩
```
