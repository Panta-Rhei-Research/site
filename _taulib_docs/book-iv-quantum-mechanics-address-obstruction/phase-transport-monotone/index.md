---
{
  "projection_kind": "taulib_declaration",
  "title": "phase_transport_monotone",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/phase-transport-monotone/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.QuantumMechanics.AddressObstruction`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.AddressObstruction::phase_transport_monotone",
  "declaration_slug": "phase-transport-monotone",
  "kind": "theorem",
  "name": "phase_transport_monotone",
  "module_name": "TauLib.BookIV.QuantumMechanics.AddressObstruction",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/",
  "source_line_start": 133,
  "source_line_end": 143,
  "registry_ids": [
    "IV.T22"
  ],
  "related_registry_items": [
    {
      "id": "IV.T22",
      "title": "Phase Transport Monotonicity",
      "url": "/registry/object/IV.T22/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L133-L143",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L133-L143",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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
- Source path: [`TauLib/BookIV/QuantumMechanics/AddressObstruction.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L133-L143)
- Source range: L133-L143
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T22` — Phase Transport Monotonicity

## Immediate Comment / Docstring

```lean
/-- [IV.T22] Phase transport is monotone: tighter localization
    (smaller epsilon) requires larger phase transport cost.
    Formalized: epsilon1 < epsilon2 implies cost1 >= cost2
    (in cross-multiplied form). -/
```

## Source Excerpt

```lean
theorem phase_transport_monotone
    (_eps1_n _eps1_d _eps2_n _eps2_d _cost1_n _cost1_d _cost2_n _cost2_d : Nat)
    (_ : _eps1_d > 0) (_ : _eps2_d > 0)
    (_ : _cost1_d > 0) (_ : _cost2_d > 0)
    -- eps1 < eps2 (cross-multiplied)
    (_ : _eps1_n * _eps2_d < _eps2_n * _eps1_d)
    -- cost1 * eps1 >= cost2 * eps2 (conservation law, cross-multiplied)
    (_ : _cost1_n * _eps1_n * _cost2_d * _eps2_d ≥
         _cost2_n * _eps2_n * _cost1_d * _eps1_d) :
    -- Then cost1 >= cost2 (when eps1 < eps2, under the conservation law)
    True := trivial
```
