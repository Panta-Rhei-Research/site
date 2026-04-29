---
{
  "projection_kind": "taulib_declaration",
  "title": "he3_in_range",
  "permalink": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/he3-in-range/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.BBNNuclearNetwork`.",
  "declaration_id": "TauLib.BookV.Cosmology.BBNNuclearNetwork::he3_in_range",
  "declaration_slug": "he3-in-range",
  "kind": "theorem",
  "name": "he3_in_range",
  "module_name": "TauLib.BookV.Cosmology.BBNNuclearNetwork",
  "module_url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/",
  "source_line_start": 350,
  "source_line_end": 355,
  "registry_ids": [
    "V.T247"
  ],
  "related_registry_items": [
    {
      "id": "V.T247",
      "title": "He-3/H from τ-native η_B",
      "url": "/registry/object/V.T247/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L350-L355",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L350-L355",
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
- Source path: [`TauLib/BookV/Cosmology/BBNNuclearNetwork.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L350-L355)
- Source range: L350-L355
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T247` — He-3/H from τ-native η_B

## Immediate Comment / Docstring

```lean
/-- [V.T247] ³He/H within observational range (70..150). -/
```

## Source Excerpt

```lean
theorem he3_in_range :
    he3_prediction.he3_x1e7 ≥
      he3_prediction.obs_x1e7 - 2 * he3_prediction.obs_unc_x1e7 ∧
    he3_prediction.he3_x1e7 ≤
      he3_prediction.obs_x1e7 + 2 * he3_prediction.obs_unc_x1e7 :=
  ⟨by native_decide, by native_decide⟩
```
