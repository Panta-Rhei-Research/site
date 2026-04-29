---
{
  "projection_kind": "taulib_declaration",
  "title": "FiniteStageSpectral",
  "permalink": "/verify/taulib/docs/book-iv-strong-gap-meta-theorem/finite-stage-spectral/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.GapMetaTheorem`.",
  "declaration_id": "TauLib.BookIV.Strong.GapMetaTheorem::FiniteStageSpectral",
  "declaration_slug": "finite-stage-spectral",
  "kind": "structure",
  "name": "FiniteStageSpectral",
  "module_name": "TauLib.BookIV.Strong.GapMetaTheorem",
  "module_url": "/verify/taulib/docs/book-iv-strong-gap-meta-theorem/",
  "source_line_start": 228,
  "source_line_end": 235,
  "registry_ids": [
    "IV.L9"
  ],
  "related_registry_items": [
    {
      "id": "IV.L9",
      "title": "Finite-stage spectral problem",
      "url": "/registry/object/IV.L9/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/GapMetaTheorem.lean#L228-L235",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/GapMetaTheorem.lean#L228-L235",
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
- Source path: [`TauLib/BookIV/Strong/GapMetaTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/GapMetaTheorem.lean#L228-L235)
- Source range: L228-L235
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.L9` — Finite-stage spectral problem

## Immediate Comment / Docstring

```lean
/-- [IV.L9] At each stage n >= n_0, Q_n is a symmetric non-negative
    bilinear form with finite spectrum 0 = mu_0 <= mu_1 <= ... -/
```

## Source Excerpt

```lean
structure FiniteStageSpectral where
  /-- Symmetric. -/
  symmetric : Bool := true
  /-- Non-negative. -/
  nonneg : Bool := true
  /-- Finite spectrum. -/
  finite_spectrum : Bool := true
  deriving Repr
```
