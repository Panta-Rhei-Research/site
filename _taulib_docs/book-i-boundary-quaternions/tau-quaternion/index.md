---
{
  "projection_kind": "taulib_declaration",
  "title": "TauQuaternion",
  "permalink": "/verify/taulib/docs/book-i-boundary-quaternions/tau-quaternion/",
  "summary_short": "`structure` declaration in `TauLib.BookI.Boundary.Quaternions`.",
  "declaration_id": "TauLib.BookI.Boundary.Quaternions::TauQuaternion",
  "declaration_slug": "tau-quaternion",
  "kind": "structure",
  "name": "TauQuaternion",
  "module_name": "TauLib.BookI.Boundary.Quaternions",
  "module_url": "/verify/taulib/docs/book-i-boundary-quaternions/",
  "source_line_start": 45,
  "source_line_end": 49,
  "registry_ids": [
    "I.D87"
  ],
  "related_registry_items": [
    {
      "id": "I.D87",
      "title": "Elliptic Quaternions",
      "url": "/registry/object/I.D87/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Quaternions.lean#L45-L49",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.Quaternions",
        "url": "/verify/taulib/docs/book-i-boundary-quaternions/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Quaternions.lean#L45-L49",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "status": "defined"
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

- Module: [TauLib.BookI.Boundary.Quaternions](/verify/taulib/docs/book-i-boundary-quaternions/)
- Source path: [`TauLib/BookI/Boundary/Quaternions.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Quaternions.lean#L45-L49)
- Source range: L45-L49
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `I.D87` — Elliptic Quaternions

## Immediate Comment / Docstring

```lean
/-- [I.D87] TauQuaternion: elliptic quaternions over constructive reals.
    Components: w (scalar/real), x (i), y (j), z (k). -/
```

## Source Excerpt

```lean
structure TauQuaternion where
  w : TauReal
  x : TauReal
  y : TauReal
  z : TauReal
```
