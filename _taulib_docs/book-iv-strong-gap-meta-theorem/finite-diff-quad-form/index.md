---
{
  "projection_kind": "taulib_declaration",
  "title": "FiniteDiffQuadForm",
  "permalink": "/verify/taulib/docs/book-iv-strong-gap-meta-theorem/finite-diff-quad-form/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.GapMetaTheorem`.",
  "declaration_id": "TauLib.BookIV.Strong.GapMetaTheorem::FiniteDiffQuadForm",
  "declaration_slug": "finite-diff-quad-form",
  "kind": "structure",
  "name": "FiniteDiffQuadForm",
  "module_name": "TauLib.BookIV.Strong.GapMetaTheorem",
  "module_url": "/verify/taulib/docs/book-iv-strong-gap-meta-theorem/",
  "source_line_start": 128,
  "source_line_end": 135,
  "registry_ids": [
    "IV.D165"
  ],
  "related_registry_items": [
    {
      "id": "IV.D165",
      "title": "Finite-difference quadratic form",
      "url": "/registry/object/IV.D165/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/GapMetaTheorem.lean#L128-L135",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/GapMetaTheorem.lean#L128-L135",
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
- Source path: [`TauLib/BookIV/Strong/GapMetaTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/GapMetaTheorem.lean#L128-L135)
- Source range: L128-L135
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D165` — Finite-difference quadratic form

## Immediate Comment / Docstring

```lean
/-- [IV.D165] Q_n(p,q) := V_n(Omega^* + p + q) - V_n(Omega^* + p)
                           - V_n(Omega^* + q) + V_n(Omega^*)
    The second-order excitation cost around the vacuum. -/
```

## Source Excerpt

```lean
structure FiniteDiffQuadForm where
  /-- Symmetric bilinear form. -/
  symmetric : Bool := true
  /-- Non-negative definite. -/
  nonneg : Bool := true
  /-- Finite rank at each stage. -/
  finite_rank : Bool := true
  deriving Repr
```
