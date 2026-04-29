---
{
  "projection_kind": "taulib_declaration",
  "title": "noise_dominance",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/noise-dominance/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Thermodynamics.EntropySplitting`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.EntropySplitting::noise_dominance",
  "declaration_slug": "noise-dominance",
  "kind": "theorem",
  "name": "noise_dominance",
  "module_name": "TauLib.BookV.Thermodynamics.EntropySplitting",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/",
  "source_line_start": 283,
  "source_line_end": 285,
  "registry_ids": [
    "V.R121"
  ],
  "related_registry_items": [
    {
      "id": "V.R121",
      "title": "The 99.99% that is noise",
      "url": "/registry/object/V.R121/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L283-L285",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Thermodynamics.EntropySplitting",
        "url": "/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L283-L285",
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

- Module: [TauLib.BookV.Thermodynamics.EntropySplitting](/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/)
- Source path: [`TauLib/BookV/Thermodynamics/EntropySplitting.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L283-L285)
- Source range: L283-L285
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.R121` — The 99.99% that is noise

## Immediate Comment / Docstring

```lean
-- [V.R121] The 99.99% That is Noise: at late orbit depths, virtually
-- all entropy is refinement entropy (label count, not disorder).
```

## Source Excerpt

```lean
theorem noise_dominance :
    "At late depths: S_def/S -> 0 exponentially, S ~ S_ref" =
    "At late depths: S_def/S -> 0 exponentially, S ~ S_ref" := rfl
```
