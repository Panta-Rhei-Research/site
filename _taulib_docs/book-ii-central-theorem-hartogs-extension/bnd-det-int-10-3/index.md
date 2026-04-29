---
{
  "projection_kind": "taulib_declaration",
  "title": "bnd_det_int_10_3",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-hartogs-extension/bnd-det-int-10-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.CentralTheorem.HartogsExtension`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.HartogsExtension::bnd_det_int_10_3",
  "declaration_slug": "bnd-det-int-10-3",
  "kind": "theorem",
  "name": "bnd_det_int_10_3",
  "module_name": "TauLib.BookII.CentralTheorem.HartogsExtension",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-hartogs-extension/",
  "source_line_start": 345,
  "source_line_end": 346,
  "registry_ids": [
    "II.T37"
  ],
  "related_registry_items": [
    {
      "id": "II.T37",
      "title": "Hartogs Extension Uniqueness",
      "url": "/registry/object/II.T37/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/HartogsExtension.lean#L345-L346",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.CentralTheorem.HartogsExtension",
        "url": "/verify/taulib/docs/book-ii-central-theorem-hartogs-extension/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/HartogsExtension.lean#L345-L346",
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

- Module: [TauLib.BookII.CentralTheorem.HartogsExtension](/verify/taulib/docs/book-ii-central-theorem-hartogs-extension/)
- Source path: [`TauLib/BookII/CentralTheorem/HartogsExtension.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/HartogsExtension.lean#L345-L346)
- Source range: L345-L346
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.T37` — Hartogs Extension Uniqueness

## Immediate Comment / Docstring

```lean
-- Boundary determines interior [II.T37]
```

## Source Excerpt

```lean
theorem bnd_det_int_10_3 :
    boundary_determines_interior_check 10 3 = true := by native_decide
```
