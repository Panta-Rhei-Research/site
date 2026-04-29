---
{
  "projection_kind": "taulib_declaration",
  "title": "SpectralAlgebraElement",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-central-theorem/spectral-algebra-element/",
  "summary_short": "`structure` declaration in `TauLib.BookII.CentralTheorem.CentralTheorem`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.CentralTheorem::SpectralAlgebraElement",
  "declaration_slug": "spectral-algebra-element",
  "kind": "structure",
  "name": "SpectralAlgebraElement",
  "module_name": "TauLib.BookII.CentralTheorem.CentralTheorem",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-central-theorem/",
  "source_line_start": 61,
  "source_line_end": 65,
  "registry_ids": [
    "II.D60"
  ],
  "related_registry_items": [
    {
      "id": "II.D60",
      "title": "Spectral Algebra",
      "url": "/registry/object/II.D60/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L61-L65",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.CentralTheorem.CentralTheorem",
        "url": "/verify/taulib/docs/book-ii-central-theorem-central-theorem/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L61-L65",
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

- Module: [TauLib.BookII.CentralTheorem.CentralTheorem](/verify/taulib/docs/book-ii-central-theorem-central-theorem/)
- Source path: [`TauLib/BookII/CentralTheorem/CentralTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L61-L65)
- Source range: L61-L65
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `II.D60` — Spectral Algebra

## Immediate Comment / Docstring

```lean
/-- [II.D60] A spectral algebra element at stage k:
    a function Z/P_kZ -> SectorPair that is idempotent-supported.

    Idempotent-supported means: for each x, the sector pair (B, C)
    satisfies e_plus * (B, C) + e_minus * (B, C) = (B, C).
    This is automatically true for all SectorPairs (decompose_recovery),
    so every function to SectorPair is idempotent-supported.

    The stage-k ring structure is componentwise:
    addition and multiplication of SectorPairs are pointwise. -/
```

## Source Excerpt

```lean
structure SpectralAlgebraElement where
  /-- B-channel function: Z/P_kZ -> Int -/
  b_fn : TauIdx -> Int
  /-- C-channel function: Z/P_kZ -> Int -/
  c_fn : TauIdx -> Int
```
