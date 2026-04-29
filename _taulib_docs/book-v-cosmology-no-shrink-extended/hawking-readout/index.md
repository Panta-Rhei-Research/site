---
{
  "projection_kind": "taulib_declaration",
  "title": "hawking_readout",
  "permalink": "/verify/taulib/docs/book-v-cosmology-no-shrink-extended/hawking-readout/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.NoShrinkExtended`.",
  "declaration_id": "TauLib.BookV.Cosmology.NoShrinkExtended::hawking_readout",
  "declaration_slug": "hawking-readout",
  "kind": "theorem",
  "name": "hawking_readout",
  "module_name": "TauLib.BookV.Cosmology.NoShrinkExtended",
  "module_url": "/verify/taulib/docs/book-v-cosmology-no-shrink-extended/",
  "source_line_start": 149,
  "source_line_end": 151,
  "registry_ids": [
    "V.P95"
  ],
  "related_registry_items": [
    {
      "id": "V.P95",
      "title": "Hawking Readout",
      "url": "/registry/object/V.P95/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/NoShrinkExtended.lean#L149-L151",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.NoShrinkExtended",
        "url": "/verify/taulib/docs/book-v-cosmology-no-shrink-extended/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/NoShrinkExtended.lean#L149-L151",
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

- Module: [TauLib.BookV.Cosmology.NoShrinkExtended](/verify/taulib/docs/book-v-cosmology-no-shrink-extended/)
- Source path: [`TauLib/BookV/Cosmology/NoShrinkExtended.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/NoShrinkExtended.lean#L149-L151)
- Source range: L149-L151
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P95` — Hawking Readout

## Immediate Comment / Docstring

```lean
/-- [V.P95] Hawking readout: Hawking radiation is a chart-level
    readout of the boundary character χ_BH at the linking boundary.

    It is NOT:
    - A transport of mass from inside to outside
    - A loss of information
    - A process that reduces the BH mass

    It IS:
    - A boundary-character readout (like CMB temperature)
    - A chart-level observable with no ontic consequence -/
```

## Source Excerpt

```lean
theorem hawking_readout :
    "Hawking radiation = boundary character readout, not mass transport" =
    "Hawking radiation = boundary character readout, not mass transport" := rfl
```
