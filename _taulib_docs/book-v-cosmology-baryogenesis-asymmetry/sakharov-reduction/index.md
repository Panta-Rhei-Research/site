---
{
  "projection_kind": "taulib_declaration",
  "title": "sakharov_reduction",
  "permalink": "/corpus/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/sakharov-reduction/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.BaryogenesisAsymmetry`.",
  "declaration_id": "TauLib.BookV.Cosmology.BaryogenesisAsymmetry::sakharov_reduction",
  "declaration_slug": "sakharov-reduction",
  "kind": "theorem",
  "name": "sakharov_reduction",
  "module_name": "TauLib.BookV.Cosmology.BaryogenesisAsymmetry",
  "module_url": "/corpus/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/",
  "source_line_start": 174,
  "source_line_end": 181,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L174-L181",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.BaryogenesisAsymmetry",
        "url": "/corpus/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L174-L181",
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

- Module: [TauLib.BookV.Cosmology.BaryogenesisAsymmetry](/corpus/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/)
- Source path: [`TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L174-L181)
- Source range: L174-L181
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The three Sakharov conditions reduce the baryogenesis mystery from
    'three unknown mechanisms' to a single open sub-problem
    (the precise ι_τ¹⁵ derivation from holonomy algebra). -/
```

## Source Excerpt

```lean
theorem sakharov_reduction :
    -- B-violation: pre-confinement admits it
    threshold_admissibility.above_confinement = .PreConfinement ∧
    -- Out-of-equilibrium: baryogenesis window is non-empty
    baryogenesis_window.depth_start < baryogenesis_window.depth_end := by
  constructor
  · rfl
  · exact baryogenesis_window.window_nonempty
```
