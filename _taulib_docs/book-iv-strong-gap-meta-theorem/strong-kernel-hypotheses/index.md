---
{
  "projection_kind": "taulib_declaration",
  "title": "strong_kernel_hypotheses",
  "permalink": "/verify/taulib/docs/book-iv-strong-gap-meta-theorem/strong-kernel-hypotheses/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Strong.GapMetaTheorem`.",
  "declaration_id": "TauLib.BookIV.Strong.GapMetaTheorem::strong_kernel_hypotheses",
  "declaration_slug": "strong-kernel-hypotheses",
  "kind": "def",
  "name": "strong_kernel_hypotheses",
  "module_name": "TauLib.BookIV.Strong.GapMetaTheorem",
  "module_url": "/verify/taulib/docs/book-iv-strong-gap-meta-theorem/",
  "source_line_start": 291,
  "source_line_end": 292,
  "registry_ids": [
    "IV.P102"
  ],
  "related_registry_items": [
    {
      "id": "IV.P102",
      "title": "Strong sector kernel hypotheses",
      "url": "/registry/object/IV.P102/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/GapMetaTheorem.lean#L291-L292",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/GapMetaTheorem.lean#L291-L292",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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
- Source path: [`TauLib/BookIV/Strong/GapMetaTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/GapMetaTheorem.lean#L291-L292)
- Source range: L291-L292
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.P102` — Strong sector kernel hypotheses

## Immediate Comment / Docstring

```lean
/-- [IV.P102] Strong sector kernel hypotheses:
    KH-1 at n_* = 3, KH-2 from L_s[n] subset L_s[n+1],
    KH-3 deferred to ch41 (requires curvature analysis). -/
```

## Source Excerpt

```lean
def strong_kernel_hypotheses : KernelHypotheses where
  stabilization_horizon := 3
```
