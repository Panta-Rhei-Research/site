---
{
  "projection_kind": "taulib_declaration",
  "title": "Decoherence",
  "permalink": "/corpus/taulib/docs/book-iv-quantum-mechanics-measurement/decoherence/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.QuantumMechanics.Measurement`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.Measurement::Decoherence",
  "declaration_slug": "decoherence",
  "kind": "structure",
  "name": "Decoherence",
  "module_name": "TauLib.BookIV.QuantumMechanics.Measurement",
  "module_url": "/corpus/taulib/docs/book-iv-quantum-mechanics-measurement/",
  "source_line_start": 153,
  "source_line_end": 164,
  "registry_ids": [
    "IV.D75"
  ],
  "related_registry_items": [
    {
      "id": "IV.D75",
      "title": "Decoherence",
      "url": "/registry/object/IV.D75/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Measurement.lean#L153-L164",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.QuantumMechanics.Measurement",
        "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-measurement/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Measurement.lean#L153-L164",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "role": "type/data schema",
      "status": "type/data schema"
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

- Module: [TauLib.BookIV.QuantumMechanics.Measurement](/corpus/taulib/docs/book-iv-quantum-mechanics-measurement/)
- Source path: [`TauLib/BookIV/QuantumMechanics/Measurement.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Measurement.lean#L153-L164)
- Source range: L153-L164
- Kind: `structure`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- `IV.D75` — Decoherence

## Immediate Comment / Docstring

```lean
/-- [IV.D75] Decoherence = suppression of off-diagonal density matrix elements.

    In the tau-framework, decoherence is the suppression of off-diagonal
    elements ρ_{mn,m'n'} (m,n ≠ m',n') in the density matrix due to
    coupling with the environment's CR-address lattice.

    Rate: proportional to the number of environmental modes that
    couple to the system's off-diagonal coherences. -/
```

## Source Excerpt

```lean
structure Decoherence where
  /-- Suppression rate numerator (1/time scale, scaled). -/
  suppression_rate_numer : Nat
  /-- Suppression rate denominator. -/
  suppression_rate_denom : Nat
  /-- Denominator positive. -/
  rate_denom_pos : suppression_rate_denom > 0
  /-- Off-diagonal elements vanish in the decoherence limit. -/
  off_diagonal_vanish : Bool := true
  /-- Scope: tau-effective. -/
  scope : String := "tau-effective"
  deriving Repr
```
