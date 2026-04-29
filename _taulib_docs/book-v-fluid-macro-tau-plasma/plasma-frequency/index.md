---
{
  "projection_kind": "taulib_declaration",
  "title": "PlasmaFrequency",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-tau-plasma/plasma-frequency/",
  "summary_short": "`structure` declaration in `TauLib.BookV.FluidMacro.TauPlasma`.",
  "declaration_id": "TauLib.BookV.FluidMacro.TauPlasma::PlasmaFrequency",
  "declaration_slug": "plasma-frequency",
  "kind": "structure",
  "name": "PlasmaFrequency",
  "module_name": "TauLib.BookV.FluidMacro.TauPlasma",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-tau-plasma/",
  "source_line_start": 130,
  "source_line_end": 139,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauPlasma.lean#L130-L139",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauPlasma.lean#L130-L139",
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
- Source path: [`TauLib/BookV/FluidMacro/TauPlasma.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauPlasma.lean#L130-L139)
- Source range: L130-L139
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Plasma frequency: ω_p = √(n₀ e² / (m_e ε₀)).
    Encoded as scaled rational. -/
```

## Source Excerpt

```lean
structure PlasmaFrequency where
  /-- Frequency numerator (scaled). -/
  numer : Nat
  /-- Frequency denominator. -/
  denom : Nat
  /-- Denominator positive. -/
  denom_pos : denom > 0
  /-- Frequency is positive. -/
  freq_pos : numer > 0
  deriving Repr
```
