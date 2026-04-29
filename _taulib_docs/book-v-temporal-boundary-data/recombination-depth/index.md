---
{
  "projection_kind": "taulib_declaration",
  "title": "RecombinationDepth",
  "permalink": "/verify/taulib/docs/book-v-temporal-boundary-data/recombination-depth/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Temporal.BoundaryData`.",
  "declaration_id": "TauLib.BookV.Temporal.BoundaryData::RecombinationDepth",
  "declaration_slug": "recombination-depth",
  "kind": "structure",
  "name": "RecombinationDepth",
  "module_name": "TauLib.BookV.Temporal.BoundaryData",
  "module_url": "/verify/taulib/docs/book-v-temporal-boundary-data/",
  "source_line_start": 72,
  "source_line_end": 79,
  "registry_ids": [
    "V.D36"
  ],
  "related_registry_items": [
    {
      "id": "V.D36",
      "title": "Recombination orbit depth",
      "url": "/registry/object/V.D36/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/BoundaryData.lean#L72-L79",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Temporal.BoundaryData",
        "url": "/verify/taulib/docs/book-v-temporal-boundary-data/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/BoundaryData.lean#L72-L79",
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

- Module: [TauLib.BookV.Temporal.BoundaryData](/verify/taulib/docs/book-v-temporal-boundary-data/)
- Source path: [`TauLib/BookV/Temporal/BoundaryData.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/BoundaryData.lean#L72-L79)
- Source range: L72-L79
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D36` — Recombination orbit depth

## Immediate Comment / Docstring

```lean
/-- [V.D36] Recombination orbit depth n_rec: the orbit depth on tau^1
    at which photon-baryon decoupling occurs.

    At n_rec the omega-sector binding energy exceeds the gamma-sector
    photon energy for hydrogen-like boundary characters.

    z_rec ~ 1100 in the orthodox readout. -/
```

## Source Excerpt

```lean
structure RecombinationDepth where
  /-- Orbit depth of recombination. -/
  depth : Nat
  /-- Depth must be positive (physical event). -/
  depth_pos : depth > 0
  /-- Approximate redshift (z ~ 1100). -/
  redshift : Nat := 1100
  deriving Repr
```
