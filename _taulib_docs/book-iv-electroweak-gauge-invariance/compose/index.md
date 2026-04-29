---
{
  "projection_kind": "taulib_declaration",
  "title": "TransitionFunction.compose",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/compose/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Electroweak.GaugeInvariance`.",
  "declaration_id": "TauLib.BookIV.Electroweak.GaugeInvariance::TransitionFunction.compose",
  "declaration_slug": "compose",
  "kind": "def",
  "name": "TransitionFunction.compose",
  "module_name": "TauLib.BookIV.Electroweak.GaugeInvariance",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/",
  "source_line_start": 121,
  "source_line_end": 125,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L121-L125",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.GaugeInvariance",
        "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L121-L125",
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

- Module: [TauLib.BookIV.Electroweak.GaugeInvariance](/verify/taulib/docs/book-iv-electroweak-gauge-invariance/)
- Source path: [`TauLib/BookIV/Electroweak/GaugeInvariance.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L121-L125)
- Source range: L121-L125
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Cocycle composition: transition function winding numbers add. -/
```

## Source Excerpt

```lean
def TransitionFunction.compose (g₁ g₂ : TransitionFunction)
    (_h : g₁.patch_v = g₂.patch_u) : TransitionFunction where
  patch_u := g₁.patch_u
  patch_v := g₂.patch_v
  winding := g₁.winding + g₂.winding
```
