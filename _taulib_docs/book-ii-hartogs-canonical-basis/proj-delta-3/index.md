---
{
  "projection_kind": "taulib_declaration",
  "title": "proj_delta_3",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-canonical-basis/proj-delta-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Hartogs.CanonicalBasis`.",
  "declaration_id": "TauLib.BookII.Hartogs.CanonicalBasis::proj_delta_3",
  "declaration_slug": "proj-delta-3",
  "kind": "theorem",
  "name": "proj_delta_3",
  "module_name": "TauLib.BookII.Hartogs.CanonicalBasis",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-canonical-basis/",
  "source_line_start": 407,
  "source_line_end": 408,
  "registry_ids": [
    "II.P09"
  ],
  "related_registry_items": [
    {
      "id": "II.P09",
      "title": "Decomposition Functoriality",
      "url": "/registry/object/II.P09/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CanonicalBasis.lean#L407-L408",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.CanonicalBasis",
        "url": "/verify/taulib/docs/book-ii-hartogs-canonical-basis/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CanonicalBasis.lean#L407-L408",
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

- Module: [TauLib.BookII.Hartogs.CanonicalBasis](/verify/taulib/docs/book-ii-hartogs-canonical-basis/)
- Source path: [`TauLib/BookII/Hartogs/CanonicalBasis.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CanonicalBasis.lean#L407-L408)
- Source range: L407-L408
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.P09` — Decomposition Functoriality

## Immediate Comment / Docstring

```lean
-- Projection delta [II.P09]
```

## Source Excerpt

```lean
theorem proj_delta_3 :
    projection_delta_check 3 = true := by native_decide
```
