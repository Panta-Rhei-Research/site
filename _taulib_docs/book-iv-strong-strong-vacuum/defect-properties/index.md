---
{
  "projection_kind": "taulib_declaration",
  "title": "DefectProperties",
  "permalink": "/verify/taulib/docs/book-iv-strong-strong-vacuum/defect-properties/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.StrongVacuum`.",
  "declaration_id": "TauLib.BookIV.Strong.StrongVacuum::DefectProperties",
  "declaration_slug": "defect-properties",
  "kind": "structure",
  "name": "DefectProperties",
  "module_name": "TauLib.BookIV.Strong.StrongVacuum",
  "module_url": "/verify/taulib/docs/book-iv-strong-strong-vacuum/",
  "source_line_start": 191,
  "source_line_end": 196,
  "registry_ids": [
    "IV.P83"
  ],
  "related_registry_items": [
    {
      "id": "IV.P83",
      "title": "Properties of \\Delta_n^s",
      "url": "/registry/object/IV.P83/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongVacuum.lean#L191-L196",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Strong.StrongVacuum",
        "url": "/verify/taulib/docs/book-iv-strong-strong-vacuum/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongVacuum.lean#L191-L196",
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

- Module: [TauLib.BookIV.Strong.StrongVacuum](/verify/taulib/docs/book-iv-strong-strong-vacuum/)
- Source path: [`TauLib/BookIV/Strong/StrongVacuum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongVacuum.lean#L191-L196)
- Source range: L191-L196
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P83` — Properties of \Delta_n^s

## Immediate Comment / Docstring

```lean
/-- [IV.P83] Properties of Delta_n^s: non-negative, vanishes on id,
    finite-valued, refinement-monotone. -/
```

## Source Excerpt

```lean
structure DefectProperties where
  nonneg : Bool := true
  vanishes_on_id : Bool := true
  finite_valued : Bool := true
  refinement_monotone : Bool := true
  deriving Repr
```
