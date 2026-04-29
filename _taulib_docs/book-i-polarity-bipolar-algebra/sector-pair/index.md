---
{
  "projection_kind": "taulib_declaration",
  "title": "SectorPair",
  "permalink": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/sector-pair/",
  "summary_short": "`structure` declaration in `TauLib.BookI.Polarity.BipolarAlgebra`.",
  "declaration_id": "TauLib.BookI.Polarity.BipolarAlgebra::SectorPair",
  "declaration_slug": "sector-pair",
  "kind": "structure",
  "name": "SectorPair",
  "module_name": "TauLib.BookI.Polarity.BipolarAlgebra",
  "module_url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/",
  "source_line_start": 100,
  "source_line_end": 103,
  "registry_ids": [
    "I.D27"
  ],
  "related_registry_items": [
    {
      "id": "I.D27",
      "title": "Bipolar Spectral Algebra",
      "url": "/registry/object/I.D27/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/BipolarAlgebra.lean#L100-L103",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.BipolarAlgebra",
        "url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/BipolarAlgebra.lean#L100-L103",
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

- Module: [TauLib.BookI.Polarity.BipolarAlgebra](/verify/taulib/docs/book-i-polarity-bipolar-algebra/)
- Source path: [`TauLib/BookI/Polarity/BipolarAlgebra.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/BipolarAlgebra.lean#L100-L103)
- Source range: L100-L103
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `I.D27` — Bipolar Spectral Algebra

## Immediate Comment / Docstring

```lean
/-- [I.D27] Sector pair: the isomorphic representation (u, v) = (re + im, re - im).
    In sector coordinates, multiplication is componentwise. -/
```

## Source Excerpt

```lean
structure SectorPair where
  b_sector : Int  -- = re + im
  c_sector : Int  -- = re - im
  deriving DecidableEq, Repr
```
