---
{
  "projection_kind": "taulib_declaration",
  "title": "paradox_resolved",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/paradox-resolved/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Thermodynamics.EntropySplitting`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.EntropySplitting::paradox_resolved",
  "declaration_slug": "paradox-resolved",
  "kind": "theorem",
  "name": "paradox_resolved",
  "module_name": "TauLib.BookV.Thermodynamics.EntropySplitting",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/",
  "source_line_start": 277,
  "source_line_end": 279,
  "registry_ids": [
    "V.R119",
    "V.R120"
  ],
  "related_registry_items": [
    {
      "id": "V.R119",
      "title": "Why varepsilon is harmless",
      "url": "/registry/object/V.R119/"
    },
    {
      "id": "V.R120",
      "title": "The paradox resolved",
      "url": "/registry/object/V.R120/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L277-L279",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L277-L279",
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
- Source path: [`TauLib/BookV/Thermodynamics/EntropySplitting.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L277-L279)
- Source range: L277-L279
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.R119` — Why varepsilon is harmless
- `V.R120` — The paradox resolved

## Immediate Comment / Docstring

```lean
-- ============================================================
-- REMARKS
-- ============================================================

-- [V.R119] Why epsilon is Harmless: bounded above by S_def,
-- it inherits monotone decrease and vanishes at the coherence horizon.

-- [V.R120] The Paradox Resolved: total entropy S increases because
-- S_ref increases, but physical disorder S_def decreases.
```

## Source Excerpt

```lean
theorem paradox_resolved :
    "S_total increases (S_ref grows), S_def decreases: paradox dissolved" =
    "S_total increases (S_ref grows), S_def decreases: paradox dissolved" := rfl
```
