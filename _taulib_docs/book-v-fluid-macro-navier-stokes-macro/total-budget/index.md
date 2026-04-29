---
{
  "projection_kind": "taulib_declaration",
  "title": "MacroDefectTransport.totalBudget",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/total-budget/",
  "summary_short": "`def` declaration in `TauLib.BookV.FluidMacro.NavierStokesMacro`.",
  "declaration_id": "TauLib.BookV.FluidMacro.NavierStokesMacro::MacroDefectTransport.totalBudget",
  "declaration_slug": "total-budget",
  "kind": "def",
  "name": "MacroDefectTransport.totalBudget",
  "module_name": "TauLib.BookV.FluidMacro.NavierStokesMacro",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/",
  "source_line_start": 86,
  "source_line_end": 87,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/NavierStokesMacro.lean#L86-L87",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.FluidMacro.NavierStokesMacro",
        "url": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/NavierStokesMacro.lean#L86-L87",
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

- Module: [TauLib.BookV.FluidMacro.NavierStokesMacro](/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/)
- Source path: [`TauLib/BookV/FluidMacro/NavierStokesMacro.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/NavierStokesMacro.lean#L86-L87)
- Source range: L86-L87
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Total macro defect budget at level n. -/
```

## Source Excerpt

```lean
def MacroDefectTransport.totalBudget (d : MacroDefectTransport) : Nat :=
  d.mobility_n + d.vorticity_n + d.compression_n + d.topological_n
```
