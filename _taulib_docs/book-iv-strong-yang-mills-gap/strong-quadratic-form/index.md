---
{
  "projection_kind": "taulib_declaration",
  "title": "StrongQuadraticForm",
  "permalink": "/verify/taulib/docs/book-iv-strong-yang-mills-gap/strong-quadratic-form/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.YangMillsGap`.",
  "declaration_id": "TauLib.BookIV.Strong.YangMillsGap::StrongQuadraticForm",
  "declaration_slug": "strong-quadratic-form",
  "kind": "structure",
  "name": "StrongQuadraticForm",
  "module_name": "TauLib.BookIV.Strong.YangMillsGap",
  "module_url": "/verify/taulib/docs/book-iv-strong-yang-mills-gap/",
  "source_line_start": 164,
  "source_line_end": 173,
  "registry_ids": [
    "IV.D174"
  ],
  "related_registry_items": [
    {
      "id": "IV.D174",
      "title": "Strong quadratic form",
      "url": "/registry/object/IV.D174/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/YangMillsGap.lean#L164-L173",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Strong.YangMillsGap",
        "url": "/verify/taulib/docs/book-iv-strong-yang-mills-gap/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/YangMillsGap.lean#L164-L173",
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

- Module: [TauLib.BookIV.Strong.YangMillsGap](/verify/taulib/docs/book-iv-strong-yang-mills-gap/)
- Source path: [`TauLib/BookIV/Strong/YangMillsGap.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/YangMillsGap.lean#L164-L173)
- Source range: L164-L173
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D174` — Strong quadratic form

## Immediate Comment / Docstring

```lean
/-- [IV.D174] Q_n^s(p,q): finite-difference second variation of V_n^s
    around the strong vacuum. The Hessian of the Yang-Mills action
    at the vacuum configuration. -/
```

## Source Excerpt

```lean
structure StrongQuadraticForm where
  /-- Symmetric. -/
  symmetric : Bool := true
  /-- Non-negative definite. -/
  nonneg : Bool := true
  /-- Equality with zero iff gauge-equivalent to vacuum. -/
  zero_iff_gauge_equiv : Bool := true
  /-- Finite rank. -/
  finite_rank : Bool := true
  deriving Repr
```
