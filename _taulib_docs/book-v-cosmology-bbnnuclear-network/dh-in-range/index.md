---
{
  "projection_kind": "taulib_declaration",
  "title": "dh_in_range",
  "permalink": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/dh-in-range/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.BBNNuclearNetwork`.",
  "declaration_id": "TauLib.BookV.Cosmology.BBNNuclearNetwork::dh_in_range",
  "declaration_slug": "dh-in-range",
  "kind": "theorem",
  "name": "dh_in_range",
  "module_name": "TauLib.BookV.Cosmology.BBNNuclearNetwork",
  "module_url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/",
  "source_line_start": 323,
  "source_line_end": 328,
  "registry_ids": [
    "V.P166"
  ],
  "related_registry_items": [
    {
      "id": "V.P166",
      "title": "D/H Observational Consistency",
      "url": "/registry/object/V.P166/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L323-L328",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L323-L328",
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
- Source path: [`TauLib/BookV/Cosmology/BBNNuclearNetwork.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L323-L328)
- Source range: L323-L328
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P166` — D/H Observational Consistency

## Immediate Comment / Docstring

```lean
/-- [V.P166] D/H within 3σ range (obs ± 3·unc = 253 ± 9, range 244..262). -/
```

## Source Excerpt

```lean
theorem dh_in_range :
    deuterium_prediction.dh_x1e7 ≥
      deuterium_prediction.obs_x1e7 - 3 * deuterium_prediction.obs_unc_x1e7 ∧
    deuterium_prediction.dh_x1e7 ≤
      deuterium_prediction.obs_x1e7 + 3 * deuterium_prediction.obs_unc_x1e7 :=
  ⟨by native_decide, by native_decide⟩
```
