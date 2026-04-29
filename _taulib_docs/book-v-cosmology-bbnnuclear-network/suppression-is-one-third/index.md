---
{
  "projection_kind": "taulib_declaration",
  "title": "suppression_is_one_third",
  "permalink": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/suppression-is-one-third/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.BBNNuclearNetwork`.",
  "declaration_id": "TauLib.BookV.Cosmology.BBNNuclearNetwork::suppression_is_one_third",
  "declaration_slug": "suppression-is-one-third",
  "kind": "theorem",
  "name": "suppression_is_one_third",
  "module_name": "TauLib.BookV.Cosmology.BBNNuclearNetwork",
  "module_url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/",
  "source_line_start": 254,
  "source_line_end": 256,
  "registry_ids": [
    "V.T243"
  ],
  "related_registry_items": [
    {
      "id": "V.T243",
      "title": "Suppression = 1/dim(τ³) = 1/3",
      "url": "/registry/object/V.T243/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L254-L256",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L254-L256",
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
- Source path: [`TauLib/BookV/Cosmology/BBNNuclearNetwork.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L254-L256)
- Source range: L254-L256
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T243` — Suppression = 1/dim(τ³) = 1/3

## Immediate Comment / Docstring

```lean
/-- [V.T243] S_{⁷Be} = 1/3 exactly. -/
```

## Source Excerpt

```lean
theorem suppression_is_one_third :
    be7_suppression.supp_num = 1 ∧ be7_suppression.supp_den = 3 :=
  ⟨rfl, rfl⟩
```
