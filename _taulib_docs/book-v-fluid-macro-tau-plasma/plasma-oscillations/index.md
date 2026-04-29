---
{
  "projection_kind": "taulib_declaration",
  "title": "plasma_oscillations",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-tau-plasma/plasma-oscillations/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.FluidMacro.TauPlasma`.",
  "declaration_id": "TauLib.BookV.FluidMacro.TauPlasma::plasma_oscillations",
  "declaration_slug": "plasma-oscillations",
  "kind": "theorem",
  "name": "plasma_oscillations",
  "module_name": "TauLib.BookV.FluidMacro.TauPlasma",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-tau-plasma/",
  "source_line_start": 156,
  "source_line_end": 158,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauPlasma.lean#L156-L158",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauPlasma.lean#L156-L158",
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

- Module: [TauLib.BookV.FluidMacro.TauPlasma](/verify/taulib/docs/book-v-fluid-macro-tau-plasma/)
- Source path: [`TauLib/BookV/FluidMacro/TauPlasma.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauPlasma.lean#L156-L158)
- Source range: L156-L158
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Plasma oscillations are longitudinal. -/
```

## Source Excerpt

```lean
theorem plasma_oscillations (po : PlasmaOscillation)
    (h : po.is_longitudinal = true) :
    po.is_longitudinal = true := h
```
