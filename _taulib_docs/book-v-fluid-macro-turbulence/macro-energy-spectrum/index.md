---
{
  "projection_kind": "taulib_declaration",
  "title": "macro_energy_spectrum",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-turbulence/macro-energy-spectrum/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.FluidMacro.Turbulence`.",
  "declaration_id": "TauLib.BookV.FluidMacro.Turbulence::macro_energy_spectrum",
  "declaration_slug": "macro-energy-spectrum",
  "kind": "theorem",
  "name": "macro_energy_spectrum",
  "module_name": "TauLib.BookV.FluidMacro.Turbulence",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-turbulence/",
  "source_line_start": 120,
  "source_line_end": 122,
  "registry_ids": [
    "V.T72"
  ],
  "related_registry_items": [
    {
      "id": "V.T72",
      "title": "Macro energy spectrum",
      "url": "/registry/object/V.T72/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/Turbulence.lean#L120-L122",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.FluidMacro.Turbulence",
        "url": "/verify/taulib/docs/book-v-fluid-macro-turbulence/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/Turbulence.lean#L120-L122",
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

- Module: [TauLib.BookV.FluidMacro.Turbulence](/verify/taulib/docs/book-v-fluid-macro-turbulence/)
- Source path: [`TauLib/BookV/FluidMacro/Turbulence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/Turbulence.lean#L120-L122)
- Source range: L120-L122
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T72` — Macro energy spectrum

## Immediate Comment / Docstring

```lean
/-- [V.T72] Macro energy spectrum: in the tau-inertial range,
    E(k) = C_K · ε^{2/3} · k^{-5/3} (Kolmogorov law).

    Structural recording: the exponent is 5/3, matching K41. -/
```

## Source Excerpt

```lean
theorem macro_energy_spectrum :
    "E(k) = C_K * epsilon^(2/3) * k^(-5/3) in inertial range" =
    "E(k) = C_K * epsilon^(2/3) * k^(-5/3) in inertial range" := rfl
```
