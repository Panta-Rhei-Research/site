---
{
  "projection_kind": "taulib_declaration",
  "title": "sector_distribution_sum",
  "permalink": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/sector-distribution-sum/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.BBNNuclearNetwork`.",
  "declaration_id": "TauLib.BookV.Cosmology.BBNNuclearNetwork::sector_distribution_sum",
  "declaration_slug": "sector-distribution-sum",
  "kind": "theorem",
  "name": "sector_distribution_sum",
  "module_name": "TauLib.BookV.Cosmology.BBNNuclearNetwork",
  "module_url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/",
  "source_line_start": 199,
  "source_line_end": 201,
  "registry_ids": [
    "V.T242"
  ],
  "related_registry_items": [
    {
      "id": "V.T242",
      "title": "Sector Distribution {1,4,7}",
      "url": "/registry/object/V.T242/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L199-L201",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L199-L201",
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
- Source path: [`TauLib/BookV/Cosmology/BBNNuclearNetwork.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L199-L201)
- Source range: L199-L201
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T242` — Sector Distribution {1,4,7}

## Immediate Comment / Docstring

```lean
/-- [V.T242] Sector distribution sums to 12. -/
```

## Source Excerpt

```lean
theorem sector_distribution_sum :
    sector_count .A + sector_count .B + sector_count .C = 12 := by
  native_decide
```
