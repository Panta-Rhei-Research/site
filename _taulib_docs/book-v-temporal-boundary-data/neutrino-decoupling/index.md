---
{
  "projection_kind": "taulib_declaration",
  "title": "NeutrinoDecoupling",
  "permalink": "/verify/taulib/docs/book-v-temporal-boundary-data/neutrino-decoupling/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Temporal.BoundaryData`.",
  "declaration_id": "TauLib.BookV.Temporal.BoundaryData::NeutrinoDecoupling",
  "declaration_slug": "neutrino-decoupling",
  "kind": "structure",
  "name": "NeutrinoDecoupling",
  "module_name": "TauLib.BookV.Temporal.BoundaryData",
  "module_url": "/verify/taulib/docs/book-v-temporal-boundary-data/",
  "source_line_start": 121,
  "source_line_end": 128,
  "registry_ids": [
    "V.D38"
  ],
  "related_registry_items": [
    {
      "id": "V.D38",
      "title": "Neutrino decoupling orbit depth",
      "url": "/registry/object/V.D38/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/BoundaryData.lean#L121-L128",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/BoundaryData.lean#L121-L128",
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
- Source path: [`TauLib/BookV/Temporal/BoundaryData.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/BoundaryData.lean#L121-L128)
- Source range: L121-L128
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D38` — Neutrino decoupling orbit depth

## Immediate Comment / Docstring

```lean
/-- [V.D38] Neutrino decoupling orbit depth n_nu: the orbit depth
    at which the pi-sector (weak force) interaction rate Gamma_pi(n_nu)
    drops below the base progression rate on tau^1.

    Since n_nu < n_rec, the CnuB encodes H_partial[omega] at an earlier,
    higher-energy orbit depth. -/
```

## Source Excerpt

```lean
structure NeutrinoDecoupling where
  /-- Orbit depth of neutrino decoupling. -/
  depth : Nat
  /-- Depth must be positive. -/
  depth_pos : depth > 0
  /-- Number of neutrino species (from A-sector structure). -/
  species_count : Nat := 3
  deriving Repr
```
