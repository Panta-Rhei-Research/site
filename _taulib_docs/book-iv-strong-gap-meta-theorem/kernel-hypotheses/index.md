---
{
  "projection_kind": "taulib_declaration",
  "title": "KernelHypotheses",
  "permalink": "/verify/taulib/docs/book-iv-strong-gap-meta-theorem/kernel-hypotheses/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.GapMetaTheorem`.",
  "declaration_id": "TauLib.BookIV.Strong.GapMetaTheorem::KernelHypotheses",
  "declaration_slug": "kernel-hypotheses",
  "kind": "structure",
  "name": "KernelHypotheses",
  "module_name": "TauLib.BookIV.Strong.GapMetaTheorem",
  "module_url": "/verify/taulib/docs/book-iv-strong-gap-meta-theorem/",
  "source_line_start": 187,
  "source_line_end": 196,
  "registry_ids": [
    "IV.D168"
  ],
  "related_registry_items": [
    {
      "id": "IV.D168",
      "title": "Three kernel hypotheses",
      "url": "/registry/object/IV.D168/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/GapMetaTheorem.lean#L187-L196",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/GapMetaTheorem.lean#L187-L196",
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
- Source path: [`TauLib/BookIV/Strong/GapMetaTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/GapMetaTheorem.lean#L187-L196)
- Source range: L187-L196
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D168` — Three kernel hypotheses

## Immediate Comment / Docstring

```lean
/-- [IV.D168] The three kernel hypotheses for a tau-holonomy sector:
    (KH-1) Eventual stationarity of combinatorial type beyond n_*
    (KH-2) Refinement monotonicity of the defect functional
    (KH-3) Discrete Hessian has strictly positive gap for n >= n_* -/
```

## Source Excerpt

```lean
structure KernelHypotheses where
  /-- (KH-1) Stationarity beyond stabilization horizon n_*. -/
  kh1_stationarity : Bool := true
  /-- (KH-2) Defect functional is refinement-monotone. -/
  kh2_monotonicity : Bool := true
  /-- (KH-3) Positive spectral gap beyond n_*. -/
  kh3_positive_gap : Bool := true
  /-- Stabilization horizon. -/
  stabilization_horizon : Nat
  deriving Repr
```
