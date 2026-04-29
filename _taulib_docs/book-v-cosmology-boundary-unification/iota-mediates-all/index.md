---
{
  "projection_kind": "taulib_declaration",
  "title": "iota_mediates_all",
  "permalink": "/verify/taulib/docs/book-v-cosmology-boundary-unification/iota-mediates-all/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.BoundaryUnification`.",
  "declaration_id": "TauLib.BookV.Cosmology.BoundaryUnification::iota_mediates_all",
  "declaration_slug": "iota-mediates-all",
  "kind": "theorem",
  "name": "iota_mediates_all",
  "module_name": "TauLib.BookV.Cosmology.BoundaryUnification",
  "module_url": "/verify/taulib/docs/book-v-cosmology-boundary-unification/",
  "source_line_start": 220,
  "source_line_end": 221,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BoundaryUnification.lean#L220-L221",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.BoundaryUnification",
        "url": "/verify/taulib/docs/book-v-cosmology-boundary-unification/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BoundaryUnification.lean#L220-L221",
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

- Module: [TauLib.BookV.Cosmology.BoundaryUnification](/verify/taulib/docs/book-v-cosmology-boundary-unification/)
- Source path: [`TauLib/BookV/Cosmology/BoundaryUnification.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BoundaryUnification.lean#L220-L221)
- Source range: L220-L221
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- 10 couplings total. -/
```

## Source Excerpt

```lean
theorem iota_mediates_all :
    all_couplings.length = 10 := by native_decide
```
