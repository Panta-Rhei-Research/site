---
{
  "projection_kind": "taulib_declaration",
  "title": "PositiveGapEachStage",
  "permalink": "/verify/taulib/docs/book-iv-strong-gap-meta-theorem/positive-gap-each-stage/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.GapMetaTheorem`.",
  "declaration_id": "TauLib.BookIV.Strong.GapMetaTheorem::PositiveGapEachStage",
  "declaration_slug": "positive-gap-each-stage",
  "kind": "structure",
  "name": "PositiveGapEachStage",
  "module_name": "TauLib.BookIV.Strong.GapMetaTheorem",
  "module_url": "/verify/taulib/docs/book-iv-strong-gap-meta-theorem/",
  "source_line_start": 240,
  "source_line_end": 245,
  "registry_ids": [
    "IV.L10"
  ],
  "related_registry_items": [
    {
      "id": "IV.L10",
      "title": "Positive gap at each stage",
      "url": "/registry/object/IV.L10/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/GapMetaTheorem.lean#L240-L245",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/GapMetaTheorem.lean#L240-L245",
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
- Source path: [`TauLib/BookIV/Strong/GapMetaTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/GapMetaTheorem.lean#L240-L245)
- Source range: L240-L245
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.L10` — Positive gap at each stage

## Immediate Comment / Docstring

```lean
/-- [IV.L10] For each n >= n_*, the positive gap mu_1^(n) > 0. -/
```

## Source Excerpt

```lean
structure PositiveGapEachStage where
  /-- Gap is positive. -/
  gap_positive : Bool := true
  /-- Follows from KH-3 + finite min of positives is positive. -/
  mechanism : String := "KH-3: Q_n(p,p) > 0 for nontrivial p"
  deriving Repr
```
