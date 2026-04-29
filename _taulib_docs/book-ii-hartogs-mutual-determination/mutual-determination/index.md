---
{
  "projection_kind": "taulib_declaration",
  "title": "mutual_determination",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-mutual-determination/mutual-determination/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Hartogs.MutualDetermination`.",
  "declaration_id": "TauLib.BookII.Hartogs.MutualDetermination::mutual_determination",
  "declaration_slug": "mutual-determination",
  "kind": "theorem",
  "name": "mutual_determination",
  "module_name": "TauLib.BookII.Hartogs.MutualDetermination",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-mutual-determination/",
  "source_line_start": 380,
  "source_line_end": 381,
  "registry_ids": [
    "II.T27"
  ],
  "related_registry_items": [
    {
      "id": "II.T27",
      "title": "Mutual Determination (5-Way Equivalence)",
      "url": "/registry/object/II.T27/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/MutualDetermination.lean#L380-L381",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/MutualDetermination.lean#L380-L381",
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
- Source path: [`TauLib/BookII/Hartogs/MutualDetermination.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/MutualDetermination.lean#L380-L381)
- Source range: L380-L381
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.T27` — Mutual Determination (5-Way Equivalence)

## Immediate Comment / Docstring

```lean
-- Mutual Determination Theorem [II.T27]
```

## Source Excerpt

```lean
theorem mutual_determination :
    mutual_determination_check 10 4 = true := by native_decide
```
