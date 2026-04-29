---
{
  "projection_kind": "taulib_declaration",
  "title": "newtonian_recovery",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-linear-einstein/newtonian-recovery/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.LinearEinstein`.",
  "declaration_id": "TauLib.BookV.GravityField.LinearEinstein::newtonian_recovery",
  "declaration_slug": "newtonian-recovery",
  "kind": "theorem",
  "name": "newtonian_recovery",
  "module_name": "TauLib.BookV.GravityField.LinearEinstein",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-linear-einstein/",
  "source_line_start": 215,
  "source_line_end": 218,
  "registry_ids": [
    "V.T28"
  ],
  "related_registry_items": [
    {
      "id": "V.T28",
      "title": "Newtonian limit recovery",
      "url": "/registry/object/V.T28/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/LinearEinstein.lean#L215-L218",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.LinearEinstein",
        "url": "/verify/taulib/docs/book-v-gravity-field-linear-einstein/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/LinearEinstein.lean#L215-L218",
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

- Module: [TauLib.BookV.GravityField.LinearEinstein](/verify/taulib/docs/book-v-gravity-field-linear-einstein/)
- Source path: [`TauLib/BookV/GravityField/LinearEinstein.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/LinearEinstein.lean#L215-L218)
- Source range: L215-L218
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T28` — Newtonian limit recovery

## Immediate Comment / Docstring

```lean
/-- [V.T28] The static, weak-field limit of the linearized τ-Einstein
    equation recovers Newtonian gravity: F = -GMm/r².

    This follows from the chart readout of the first-order
    linearized equation with static matter distribution.
    The coupling κ_τ maps to 8πG/c⁴ under readout. -/
```

## Source Excerpt

```lean
theorem newtonian_recovery :
    first_order_einstein.order = 1 ∧
    first_order_einstein.kappa.kappa_numer = iotaD - iota := by
  exact ⟨rfl, first_order_einstein.kappa.is_one_minus_iota.1⟩
```
