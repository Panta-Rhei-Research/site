---
{
  "projection_kind": "taulib_declaration",
  "title": "full_mutual_determination",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-mutual-determination/full-mutual-determination/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Hartogs.MutualDetermination`.",
  "declaration_id": "TauLib.BookII.Hartogs.MutualDetermination::full_mutual_determination",
  "declaration_slug": "full-mutual-determination",
  "kind": "theorem",
  "name": "full_mutual_determination",
  "module_name": "TauLib.BookII.Hartogs.MutualDetermination",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-mutual-determination/",
  "source_line_start": 388,
  "source_line_end": 391,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/MutualDetermination.lean#L388-L391",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.MutualDetermination",
        "url": "/verify/taulib/docs/book-ii-hartogs-mutual-determination/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/MutualDetermination.lean#L388-L391",
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

- Module: [TauLib.BookII.Hartogs.MutualDetermination](/verify/taulib/docs/book-ii-hartogs-mutual-determination/)
- Source path: [`TauLib/BookII/Hartogs/MutualDetermination.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/MutualDetermination.lean#L388-L391)
- Source range: L388-L391
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
-- Full mutual determination
```

## Source Excerpt

```lean
theorem full_mutual_determination :
    full_mutual_determination_check 10 4 = true := by native_decide

end Tau.BookII.Hartogs
```
