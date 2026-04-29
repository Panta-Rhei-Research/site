---
{
  "projection_kind": "taulib_declaration",
  "title": "sakharov_from_sigma",
  "permalink": "/verify/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/sakharov-from-sigma-l230/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.BaryogenesisAsymmetry`.",
  "declaration_id": "TauLib.BookV.Cosmology.BaryogenesisAsymmetry::sakharov_from_sigma",
  "declaration_slug": "sakharov-from-sigma-l230",
  "kind": "theorem",
  "name": "sakharov_from_sigma",
  "module_name": "TauLib.BookV.Cosmology.BaryogenesisAsymmetry",
  "module_url": "/verify/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/",
  "source_line_start": 230,
  "source_line_end": 237,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L230-L237",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.BaryogenesisAsymmetry",
        "url": "/verify/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L230-L237",
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

- Module: [TauLib.BookV.Cosmology.BaryogenesisAsymmetry](/verify/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/)
- Source path: [`TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L230-L237)
- Source range: L230-L237
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- All 3 Sakharov conditions met from σ-involution:
    B-violation window [2,3], CP from 3 generations, 3 conditions total. -/
```

## Source Excerpt

```lean
theorem sakharov_from_sigma :
    sakharov_from_sigma_data.baryogenesis_depth_start = 2 ∧
    sakharov_from_sigma_data.baryogenesis_depth_end = 3 ∧
    sakharov_from_sigma_data.n_generations_for_cp = 3 ∧
    sakharov_from_sigma_data.n_conditions = 3 ∧
    sakharov_from_sigma_data.baryogenesis_depth_start <
      sakharov_from_sigma_data.baryogenesis_depth_end :=
  ⟨rfl, rfl, rfl, rfl, sakharov_from_sigma_data.window_nonempty⟩
```
