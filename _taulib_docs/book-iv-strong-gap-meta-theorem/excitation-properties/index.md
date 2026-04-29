---
{
  "projection_kind": "taulib_declaration",
  "title": "ExcitationProperties",
  "permalink": "/verify/taulib/docs/book-iv-strong-gap-meta-theorem/excitation-properties/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.GapMetaTheorem`.",
  "declaration_id": "TauLib.BookIV.Strong.GapMetaTheorem::ExcitationProperties",
  "declaration_slug": "excitation-properties",
  "kind": "structure",
  "name": "ExcitationProperties",
  "module_name": "TauLib.BookIV.Strong.GapMetaTheorem",
  "module_url": "/verify/taulib/docs/book-iv-strong-gap-meta-theorem/",
  "source_line_start": 168,
  "source_line_end": 175,
  "registry_ids": [
    "IV.P98"
  ],
  "related_registry_items": [
    {
      "id": "IV.P98",
      "title": "Properties of h_n",
      "url": "/registry/object/IV.P98/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/GapMetaTheorem.lean#L168-L175",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Strong.GapMetaTheorem",
        "url": "/verify/taulib/docs/book-iv-strong-gap-meta-theorem/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/GapMetaTheorem.lean#L168-L175",
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

- Module: [TauLib.BookIV.Strong.GapMetaTheorem](/verify/taulib/docs/book-iv-strong-gap-meta-theorem/)
- Source path: [`TauLib/BookIV/Strong/GapMetaTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/GapMetaTheorem.lean#L168-L175)
- Source range: L168-L175
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P98` — Properties of h_n

## Immediate Comment / Docstring

```lean
/-- [IV.P98] Properties of h_n: exists, unique, positive excitation cost. -/
```

## Source Excerpt

```lean
structure ExcitationProperties where
  /-- Exists for sufficiently large n. -/
  exists_ : Bool := true
  /-- Unique by lexicographic order. -/
  unique : Bool := true
  /-- Strictly positive cost Q_n(h_n, h_n) > 0. -/
  positive_cost : Bool := true
  deriving Repr
```
