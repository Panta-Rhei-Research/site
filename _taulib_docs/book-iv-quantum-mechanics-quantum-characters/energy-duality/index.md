---
{
  "projection_kind": "taulib_declaration",
  "title": "EnergyDuality",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/energy-duality/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.QuantumMechanics.QuantumCharacters`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.QuantumCharacters::EnergyDuality",
  "declaration_slug": "energy-duality",
  "kind": "structure",
  "name": "EnergyDuality",
  "module_name": "TauLib.BookIV.QuantumMechanics.QuantumCharacters",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/",
  "source_line_start": 180,
  "source_line_end": 194,
  "registry_ids": [
    "IV.P14"
  ],
  "related_registry_items": [
    {
      "id": "IV.P14",
      "title": "Energy Duality",
      "url": "/registry/object/IV.P14/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean#L180-L194",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean#L180-L194",
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

- Module: [TauLib.BookIV.QuantumMechanics.QuantumCharacters](/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/)
- Source path: [`TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean#L180-L194)
- Source range: L180-L194
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P14` — Energy Duality

## Immediate Comment / Docstring

```lean
/-- [IV.P14] Energy duality: E = mc^2 (fiber stiffness) and E = hbar*omega
    (base frequency) read the same eigenvalue of the defect coherence
    functional from two complementary perspectives.
    Formalized: the two energy indices agree structurally. -/
```

## Source Excerpt

```lean
structure EnergyDuality where
  /-- Mass-derived energy numerator. -/
  e_mass_numer : Nat
  /-- Mass-derived energy denominator. -/
  e_mass_denom : Nat
  /-- Frequency-derived energy numerator. -/
  e_freq_numer : Nat
  /-- Frequency-derived energy denominator. -/
  e_freq_denom : Nat
  /-- Both denominators positive. -/
  mass_denom_pos : e_mass_denom > 0
  freq_denom_pos : e_freq_denom > 0
  /-- Duality: same eigenvalue (cross-multiplication). -/
  duality : e_mass_numer * e_freq_denom = e_freq_numer * e_mass_denom
  deriving Repr
```
