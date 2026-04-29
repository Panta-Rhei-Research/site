---
{
  "projection_kind": "taulib_declaration",
  "title": "abcd_distinct_12_64",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-categoricity/abcd-distinct-12-64/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.CentralTheorem.Categoricity`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.Categoricity::abcd_distinct_12_64",
  "declaration_slug": "abcd-distinct-12-64",
  "kind": "theorem",
  "name": "abcd_distinct_12_64",
  "module_name": "TauLib.BookII.CentralTheorem.Categoricity",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-categoricity/",
  "source_line_start": 370,
  "source_line_end": 371,
  "registry_ids": [
    "II.D61"
  ],
  "related_registry_items": [
    {
      "id": "II.D61",
      "title": "Moduli Space",
      "url": "/registry/object/II.D61/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/Categoricity.lean#L370-L371",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.CentralTheorem.Categoricity",
        "url": "/verify/taulib/docs/book-ii-central-theorem-categoricity/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/Categoricity.lean#L370-L371",
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

- Module: [TauLib.BookII.CentralTheorem.Categoricity](/verify/taulib/docs/book-ii-central-theorem-categoricity/)
- Source path: [`TauLib/BookII/CentralTheorem/Categoricity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/Categoricity.lean#L370-L371)
- Source range: L370-L371
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.D61` — Moduli Space

## Immediate Comment / Docstring

```lean
/-- [II.D61] The ABCD chart is injective at specific values (verified computationally).
    from_tau_idx is injective because to_tau_idx is a left inverse.
    The general computational check is abcd_roundtrip_check. -/
```

## Source Excerpt

```lean
theorem abcd_distinct_12_64 :
    from_tau_idx 12 ≠ from_tau_idx 64 := by native_decide
```
