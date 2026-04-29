---
{
  "projection_kind": "taulib_declaration",
  "title": "GaugeData",
  "permalink": "/verify/taulib/docs/book-iii-physics-strong-sector/gauge-data/",
  "summary_short": "`structure` declaration in `TauLib.BookIII.Physics.StrongSector`.",
  "declaration_id": "TauLib.BookIII.Physics.StrongSector::GaugeData",
  "declaration_slug": "gauge-data",
  "kind": "structure",
  "name": "GaugeData",
  "module_name": "TauLib.BookIII.Physics.StrongSector",
  "module_url": "/verify/taulib/docs/book-iii-physics-strong-sector/",
  "source_line_start": 94,
  "source_line_end": 102,
  "registry_ids": [
    "III.D44"
  ],
  "related_registry_items": [
    {
      "id": "III.D44",
      "title": "τ-Admissible Gauge Data",
      "url": "/registry/object/III.D44/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/StrongSector.lean#L94-L102",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Physics.StrongSector",
        "url": "/verify/taulib/docs/book-iii-physics-strong-sector/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/StrongSector.lean#L94-L102",
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

- Module: [TauLib.BookIII.Physics.StrongSector](/verify/taulib/docs/book-iii-physics-strong-sector/)
- Source path: [`TauLib/BookIII/Physics/StrongSector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/StrongSector.lean#L94-L102)
- Source range: L94-L102
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `III.D44` — τ-Admissible Gauge Data

## Immediate Comment / Docstring

```lean
/-- [III.D44] Gauge data at E₁ level: the enriched sector information
    beyond the bare BNF. -/
```

## Source Excerpt

```lean
structure GaugeData where
  depth : TauIdx
  b_product : TauIdx     -- product of B-type primes
  c_product : TauIdx     -- product of C-type primes
  x_product : TauIdx     -- product of X-type primes
  b_count : TauIdx       -- number of B-type primes
  c_count : TauIdx       -- number of C-type primes
  x_count : TauIdx       -- number of X-type primes
  deriving Repr, DecidableEq, BEq
```
