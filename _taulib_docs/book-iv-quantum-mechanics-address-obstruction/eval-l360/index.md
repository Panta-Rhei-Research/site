---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L360",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/eval-l360/",
  "summary_short": "`eval` declaration in `TauLib.BookIV.QuantumMechanics.AddressObstruction`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.AddressObstruction::#eval:360",
  "declaration_slug": "eval-l360",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.BookIV.QuantumMechanics.AddressObstruction",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/",
  "source_line_start": 360,
  "source_line_end": 360,
  "registry_ids": [
    "IV.R316",
    "IV.R318",
    "IV.R320"
  ],
  "related_registry_items": [
    {
      "id": "IV.R316",
      "title": "The mechanism in plain language",
      "url": "/registry/object/IV.R316/"
    },
    {
      "id": "IV.R318",
      "title": "Boundary witness budget",
      "url": "/registry/object/IV.R318/"
    },
    {
      "id": "IV.R320",
      "title": "Physical interpretation",
      "url": "/registry/object/IV.R320/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L360-L360",
  "formal_status": "computed",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.QuantumMechanics.AddressObstruction",
        "url": "/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L360-L360",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "eval",
      "status": "computed"
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

- Module: [TauLib.BookIV.QuantumMechanics.AddressObstruction](/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/)
- Source path: [`TauLib/BookIV/QuantumMechanics/AddressObstruction.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L360-L360)
- Source range: L360-L360
- Kind: `eval`
- Formal status hint: `computed`

## Registry Links

- `IV.R316` — The mechanism in plain language
- `IV.R318` — Boundary witness budget
- `IV.R320` — Physical interpretation

## Immediate Comment / Docstring

```lean
-- [IV.R316] The uncertainty principle is an ADDRESS OBSTRUCTION:
-- it is not that measurement disturbs the system, but that no state
-- can have a sharp address in both conjugate variables simultaneously.
-- (Structural remark)

-- [IV.R318] "Measurement" in tau means "readout functor application":
-- no collapse postulate is needed. The state WAS always spread;
-- the readout projects to a specific address.
-- (Structural remark)

-- [IV.R320] The Planck character hbar_tau is the crossing-point mediator:
-- it lives at the omega-sector where both lobes of L intersect.
-- This is WHY it mediates between conjugate uncertainties.
-- (Structural remark — verified by crossing_mediator)

-- ============================================================
-- SMOKE TESTS
-- ============================================================
```

## Source Excerpt

```lean
#eval crossing_mediator.numer              -- 1
```
