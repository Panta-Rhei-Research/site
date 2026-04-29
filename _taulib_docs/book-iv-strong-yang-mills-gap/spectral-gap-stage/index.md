---
{
  "projection_kind": "taulib_declaration",
  "title": "SpectralGapStage",
  "permalink": "/verify/taulib/docs/book-iv-strong-yang-mills-gap/spectral-gap-stage/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.YangMillsGap`.",
  "declaration_id": "TauLib.BookIV.Strong.YangMillsGap::SpectralGapStage",
  "declaration_slug": "spectral-gap-stage",
  "kind": "structure",
  "name": "SpectralGapStage",
  "module_name": "TauLib.BookIV.Strong.YangMillsGap",
  "module_url": "/verify/taulib/docs/book-iv-strong-yang-mills-gap/",
  "source_line_start": 186,
  "source_line_end": 193,
  "registry_ids": [
    "IV.D175"
  ],
  "related_registry_items": [
    {
      "id": "IV.D175",
      "title": "Spectral gap at stage~n",
      "url": "/registry/object/IV.D175/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/YangMillsGap.lean#L186-L193",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/YangMillsGap.lean#L186-L193",
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
- Source path: [`TauLib/BookIV/Strong/YangMillsGap.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/YangMillsGap.lean#L186-L193)
- Source range: L186-L193
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D175` — Spectral gap at stage~n

## Immediate Comment / Docstring

```lean
/-- [IV.D175] delta_n^s := lambda_1^(n) = min{lambda > 0 in Spec(Q_n^s)},
    the smallest nonzero eigenvalue. The gap mode g_n is the
    corresponding eigenmode (lightest excitation). -/
```

## Source Excerpt

```lean
structure SpectralGapStage where
  /-- Stage n. -/
  stage : Nat
  /-- The gap is the smallest nonzero eigenvalue. -/
  is_min_nonzero : Bool := true
  /-- Associated gap mode g_n exists. -/
  gap_mode_exists : Bool := true
  deriving Repr
```
