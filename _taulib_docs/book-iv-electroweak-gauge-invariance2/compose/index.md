---
{
  "projection_kind": "taulib_declaration",
  "title": "WilsonLoop.compose",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/compose/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Electroweak.GaugeInvariance2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.GaugeInvariance2::WilsonLoop.compose",
  "declaration_slug": "compose",
  "kind": "def",
  "name": "WilsonLoop.compose",
  "module_name": "TauLib.BookIV.Electroweak.GaugeInvariance2",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/",
  "source_line_start": 83,
  "source_line_end": 87,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L83-L87",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.GaugeInvariance2",
        "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L83-L87",
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

- Module: [TauLib.BookIV.Electroweak.GaugeInvariance2](/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/)
- Source path: [`TauLib/BookIV/Electroweak/GaugeInvariance2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L83-L87)
- Source range: L83-L87
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Wilson loop composition (abelian case). -/
```

## Source Excerpt

```lean
def WilsonLoop.compose (w₁ w₂ : WilsonLoop) : WilsonLoop where
  phase_numer := w₁.phase_numer * w₂.phase_denom + w₂.phase_numer * w₁.phase_denom
  phase_denom := w₁.phase_denom * w₂.phase_denom
  denom_pos := Nat.mul_pos w₁.denom_pos w₂.denom_pos
  abelian := w₁.abelian && w₂.abelian
```
