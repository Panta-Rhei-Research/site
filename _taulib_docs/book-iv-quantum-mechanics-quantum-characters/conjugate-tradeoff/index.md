---
{
  "projection_kind": "taulib_declaration",
  "title": "conjugate_tradeoff",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/conjugate-tradeoff/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.QuantumMechanics.QuantumCharacters`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.QuantumCharacters::conjugate_tradeoff",
  "declaration_slug": "conjugate-tradeoff",
  "kind": "theorem",
  "name": "conjugate_tradeoff",
  "module_name": "TauLib.BookIV.QuantumMechanics.QuantumCharacters",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/",
  "source_line_start": 223,
  "source_line_end": 228,
  "registry_ids": [
    "IV.P15"
  ],
  "related_registry_items": [
    {
      "id": "IV.P15",
      "title": "Conjugate Precision Trade-off",
      "url": "/registry/object/IV.P15/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean#L223-L228",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.QuantumMechanics.QuantumCharacters",
        "url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean#L223-L228",
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

- Module: [TauLib.BookIV.QuantumMechanics.QuantumCharacters](/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/)
- Source path: [`TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean#L223-L228)
- Source range: L223-L228
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.P15` — Conjugate Precision Trade-off

## Immediate Comment / Docstring

```lean
/-- [IV.P15] Conjugate precision trade-off: sharpening in one direction
    (gamma-tube) necessarily spreads in the conjugate direction (eta-tube).
    This is the structural origin of the uncertainty principle.
    Formalized: if gamma-precision * eta-precision <= total_budget,
    increasing one decreases the other. -/
```

## Source Excerpt

```lean
theorem conjugate_tradeoff
    (p_gamma p_eta budget : Nat)
    (h_budget : p_gamma * p_eta ≤ budget)
    (_ : p_gamma > 0) (h_eta_pos : p_eta > 0) :
    p_gamma ≤ budget / p_eta :=
  Nat.le_div_iff_mul_le h_eta_pos |>.mpr h_budget
```
