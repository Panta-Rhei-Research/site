---
{
  "projection_kind": "taulib_declaration",
  "title": "MacroRefinementEntropy.toFloat",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/to-float-l135/",
  "summary_short": "`def` declaration in `TauLib.BookV.Thermodynamics.EntropySplitting`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.EntropySplitting::MacroRefinementEntropy.toFloat",
  "declaration_slug": "to-float-l135",
  "kind": "def",
  "name": "MacroRefinementEntropy.toFloat",
  "module_name": "TauLib.BookV.Thermodynamics.EntropySplitting",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/",
  "source_line_start": 135,
  "source_line_end": 136,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L135-L136",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Thermodynamics.EntropySplitting",
        "url": "/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L135-L136",
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

- Module: [TauLib.BookV.Thermodynamics.EntropySplitting](/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/)
- Source path: [`TauLib/BookV/Thermodynamics/EntropySplitting.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L135-L136)
- Source range: L135-L136
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Refinement entropy as Float. -/
```

## Source Excerpt

```lean
def MacroRefinementEntropy.toFloat (e : MacroRefinementEntropy) : Float :=
  Float.ofNat e.s_ref_numer / Float.ofNat e.s_ref_denom
```
