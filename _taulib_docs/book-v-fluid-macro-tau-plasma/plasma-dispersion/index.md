---
{
  "projection_kind": "taulib_declaration",
  "title": "PlasmaDispersion",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-tau-plasma/plasma-dispersion/",
  "summary_short": "`structure` declaration in `TauLib.BookV.FluidMacro.TauPlasma`.",
  "declaration_id": "TauLib.BookV.FluidMacro.TauPlasma::PlasmaDispersion",
  "declaration_slug": "plasma-dispersion",
  "kind": "structure",
  "name": "PlasmaDispersion",
  "module_name": "TauLib.BookV.FluidMacro.TauPlasma",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-tau-plasma/",
  "source_line_start": 176,
  "source_line_end": 186,
  "registry_ids": [
    "V.P47"
  ],
  "related_registry_items": [
    {
      "id": "V.P47",
      "title": "Plasma cutoff",
      "url": "/registry/object/V.P47/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauPlasma.lean#L176-L186",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauPlasma.lean#L176-L186",
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
- Source path: [`TauLib/BookV/FluidMacro/TauPlasma.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauPlasma.lean#L176-L186)
- Source range: L176-L186
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.P47` — Plasma cutoff

## Immediate Comment / Docstring

```lean
/-- [V.P47] Plasma cutoff: ω² = ω_p² + c²k².
    For ω < ω_p: evanescent; for ω > ω_p: propagating. -/
```

## Source Excerpt

```lean
structure PlasmaDispersion where
  /-- Wave frequency (relative to ω_p, scaled by 100). -/
  omega_scaled : Nat
  /-- Plasma frequency (scaled by 100). -/
  omega_p_scaled : Nat
  /-- Classification. -/
  mode : PlasmaWaveMode
  /-- Classification is correct. -/
  mode_correct : (omega_scaled > omega_p_scaled → mode = .Propagating) ∧
                 (omega_scaled < omega_p_scaled → mode = .Evanescent)
  deriving Repr
```
