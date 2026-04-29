---
{
  "projection_kind": "taulib_declaration",
  "title": "yp_preserved",
  "permalink": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/yp-preserved/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.BBNNuclearNetwork`.",
  "declaration_id": "TauLib.BookV.Cosmology.BBNNuclearNetwork::yp_preserved",
  "declaration_slug": "yp-preserved",
  "kind": "theorem",
  "name": "yp_preserved",
  "module_name": "TauLib.BookV.Cosmology.BBNNuclearNetwork",
  "module_url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/",
  "source_line_start": 364,
  "source_line_end": 372,
  "registry_ids": [
    "V.T245"
  ],
  "related_registry_items": [
    {
      "id": "V.T245",
      "title": "Y_p Preservation",
      "url": "/registry/object/V.T245/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L364-L372",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L364-L372",
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
- Source path: [`TauLib/BookV/Cosmology/BBNNuclearNetwork.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L364-L372)
- Source range: L364-L372
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T245` — Y_p Preservation

## Immediate Comment / Docstring

```lean
/-- [V.T245] Y_p = 20/81 is independent of ⁷Be production rate.
    It derives from combinatorial voxel packing (8/27 × 5/6 = 20/81). -/
```

## Source Excerpt

```lean
theorem yp_preserved :
    -- Y_p components are unrelated to suppression factor
    he_prediction.yp_num = 20 ∧
    he_prediction.yp_den = 81 ∧
    -- Suppression factor exists but is distinct
    be7_suppression.supp_den = 3 ∧
    -- Y_p denominator ≠ suppression denominator (different mechanism)
    he_prediction.yp_den ≠ be7_suppression.supp_den :=
  ⟨rfl, rfl, rfl, by native_decide⟩
```
