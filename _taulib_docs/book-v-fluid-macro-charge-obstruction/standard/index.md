---
{
  "projection_kind": "taulib_declaration",
  "title": "MacroEMField.standard",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/standard/",
  "summary_short": "`def` declaration in `TauLib.BookV.FluidMacro.ChargeObstruction`.",
  "declaration_id": "TauLib.BookV.FluidMacro.ChargeObstruction::MacroEMField.standard",
  "declaration_slug": "standard",
  "kind": "def",
  "name": "MacroEMField.standard",
  "module_name": "TauLib.BookV.FluidMacro.ChargeObstruction",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/",
  "source_line_start": 180,
  "source_line_end": 181,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L180-L181",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.FluidMacro.ChargeObstruction",
        "url": "/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L180-L181",
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

- Module: [TauLib.BookV.FluidMacro.ChargeObstruction](/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/)
- Source path: [`TauLib/BookV/FluidMacro/ChargeObstruction.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L180-L181)
- Source range: L180-L181
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- EM field tensor has 6 independent components (F_{μν} antisymmetric 4×4). -/
```

## Source Excerpt

```lean
def MacroEMField.standard : MacroEMField where
  nonzero_components := 6
```
