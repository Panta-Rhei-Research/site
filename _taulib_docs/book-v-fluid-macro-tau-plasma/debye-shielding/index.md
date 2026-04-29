---
{
  "projection_kind": "taulib_declaration",
  "title": "DebyeShielding",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-tau-plasma/debye-shielding/",
  "summary_short": "`structure` declaration in `TauLib.BookV.FluidMacro.TauPlasma`.",
  "declaration_id": "TauLib.BookV.FluidMacro.TauPlasma::DebyeShielding",
  "declaration_slug": "debye-shielding",
  "kind": "structure",
  "name": "DebyeShielding",
  "module_name": "TauLib.BookV.FluidMacro.TauPlasma",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-tau-plasma/",
  "source_line_start": 220,
  "source_line_end": 227,
  "registry_ids": [
    "V.P48"
  ],
  "related_registry_items": [
    {
      "id": "V.P48",
      "title": "Debye shielding",
      "url": "/registry/object/V.P48/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauPlasma.lean#L220-L227",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.FluidMacro.TauPlasma",
        "url": "/verify/taulib/docs/book-v-fluid-macro-tau-plasma/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauPlasma.lean#L220-L227",
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

- Module: [TauLib.BookV.FluidMacro.TauPlasma](/verify/taulib/docs/book-v-fluid-macro-tau-plasma/)
- Source path: [`TauLib/BookV/FluidMacro/TauPlasma.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauPlasma.lean#L220-L227)
- Source range: L220-L227
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.P48` — Debye shielding

## Immediate Comment / Docstring

```lean
/-- [V.P48] Debye shielding: a test charge Q in a τ-plasma is screened:
    φ(r) = Q/(4π ε₀ r) · exp(-r/λ_D)

    The Coulomb potential is exponentially suppressed beyond λ_D. -/
```

## Source Excerpt

```lean
structure DebyeShielding where
  /-- Debye length. -/
  debye_length : DebyeLength
  /-- Test charge value. -/
  test_charge : ChargeQuantum
  /-- Shielding is exponential. -/
  is_exponential : Bool := true
  deriving Repr
```
