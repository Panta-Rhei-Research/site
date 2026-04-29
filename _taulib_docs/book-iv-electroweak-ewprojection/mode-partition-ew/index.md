---
{
  "projection_kind": "taulib_declaration",
  "title": "mode_partition_EW",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-ewprojection/mode-partition-ew/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.EWProjection`.",
  "declaration_id": "TauLib.BookIV.Electroweak.EWProjection::mode_partition_EW",
  "declaration_slug": "mode-partition-ew",
  "kind": "theorem",
  "name": "mode_partition_EW",
  "module_name": "TauLib.BookIV.Electroweak.EWProjection",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-ewprojection/",
  "source_line_start": 116,
  "source_line_end": 116,
  "registry_ids": [
    "IV.T136"
  ],
  "related_registry_items": [
    {
      "id": "IV.T136",
      "title": "EW Partition Theorem",
      "url": "/registry/object/IV.T136/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWProjection.lean#L116-L116",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.EWProjection",
        "url": "/verify/taulib/docs/book-iv-electroweak-ewprojection/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWProjection.lean#L116-L116",
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

- Module: [TauLib.BookIV.Electroweak.EWProjection](/verify/taulib/docs/book-iv-electroweak-ewprojection/)
- Source path: [`TauLib/BookIV/Electroweak/EWProjection.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWProjection.lean#L116-L116)
- Source range: L116-L116
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T136` — EW Partition Theorem

## Immediate Comment / Docstring

```lean
/-- [IV.T136] The 15 boundary modes partition into 5 + 3 + 7.
    This is a structural partition: EW-active ⊔ strong ⊔ complement = all. -/
```

## Source Excerpt

```lean
theorem mode_partition_EW : 5 + 3 + 7 = 15 := by omega
```
