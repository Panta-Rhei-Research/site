---
{
  "projection_kind": "taulib_declaration",
  "title": "ProfiniteSpectralPreservation",
  "permalink": "/verify/taulib/docs/book-iv-strong-yang-mills-gap/profinite-spectral-preservation/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.YangMillsGap`.",
  "declaration_id": "TauLib.BookIV.Strong.YangMillsGap::ProfiniteSpectralPreservation",
  "declaration_slug": "profinite-spectral-preservation",
  "kind": "structure",
  "name": "ProfiniteSpectralPreservation",
  "module_name": "TauLib.BookIV.Strong.YangMillsGap",
  "module_url": "/verify/taulib/docs/book-iv-strong-yang-mills-gap/",
  "source_line_start": 280,
  "source_line_end": 287,
  "registry_ids": [
    "IV.T74"
  ],
  "related_registry_items": [
    {
      "id": "IV.T74",
      "title": "Profinite spectral preservation",
      "url": "/registry/object/IV.T74/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/YangMillsGap.lean#L280-L287",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/YangMillsGap.lean#L280-L287",
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
- Source path: [`TauLib/BookIV/Strong/YangMillsGap.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/YangMillsGap.lean#L280-L287)
- Source range: L280-L287
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T74` — Profinite spectral preservation

## Immediate Comment / Docstring

```lean
/-- [IV.T74] Profinite spectral preservation: Q_omega^s has no
    eigenvalues in (0, delta_infinity^s).
    The profinite limit does not introduce new eigenvalues that
    would close the gap. -/
```

## Source Excerpt

```lean
structure ProfiniteSpectralPreservation where
  /-- No eigenvalues in the gap interval. -/
  no_eigenvalues_in_gap : Bool := true
  /-- Profinite limit preserves spectral structure. -/
  preserves_spectrum : Bool := true
  /-- Tower monotonicity ensures gaps only grow. -/
  monotonicity_source : String := "tower monotonicity IV.P108"
  deriving Repr
```
