---
{
  "projection_kind": "taulib_declaration",
  "title": "TauEnstrophy.fromTransport",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-turbulence/from-transport/",
  "summary_short": "`def` declaration in `TauLib.BookV.FluidMacro.Turbulence`.",
  "declaration_id": "TauLib.BookV.FluidMacro.Turbulence::TauEnstrophy.fromTransport",
  "declaration_slug": "from-transport",
  "kind": "def",
  "name": "TauEnstrophy.fromTransport",
  "module_name": "TauLib.BookV.FluidMacro.Turbulence",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-turbulence/",
  "source_line_start": 165,
  "source_line_end": 167,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/Turbulence.lean#L165-L167",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/Turbulence.lean#L165-L167",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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

- Module: [TauLib.BookV.FluidMacro.Turbulence](/verify/taulib/docs/book-v-fluid-macro-turbulence/)
- Source path: [`TauLib/BookV/FluidMacro/Turbulence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/Turbulence.lean#L165-L167)
- Source range: L165-L167
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Enstrophy from a defect transport state. -/
```

## Source Excerpt

```lean
def TauEnstrophy.fromTransport (d : MacroDefectTransport) : TauEnstrophy where
  vorticity_sq_half := d.vorticity_n * d.vorticity_n / 2
  level := d.level
```
