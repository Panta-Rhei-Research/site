---
{
  "projection_kind": "taulib_declaration",
  "title": "higgs_factor_four",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-factor-four/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.TauHiggs2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.TauHiggs2::higgs_factor_four",
  "declaration_slug": "higgs-factor-four",
  "kind": "theorem",
  "name": "higgs_factor_four",
  "module_name": "TauLib.BookIV.Electroweak.TauHiggs2",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/",
  "source_line_start": 374,
  "source_line_end": 375,
  "registry_ids": [
    "IV.T150"
  ],
  "related_registry_items": [
    {
      "id": "IV.T150",
      "title": "Factor-4 from Non-omega Generator Count",
      "url": "/registry/object/IV.T150/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L374-L375",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.TauHiggs2",
        "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L374-L375",
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

- Module: [TauLib.BookIV.Electroweak.TauHiggs2](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/)
- Source path: [`TauLib/BookIV/Electroweak/TauHiggs2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L374-L375)
- Source range: L374-L375
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T150` — Factor-4 from Non-omega Generator Count

## Immediate Comment / Docstring

```lean
/-- Factor 4 = |non-ω generators| = 4. [IV.T150]
    This is the factor appearing in m_H/m_n = (4 − X)/κ_ω. -/
```

## Source Excerpt

```lean
theorem higgs_factor_four :
    [NonOmegaGenerator.alpha, .pi, .gamma, .eta].length = 4 := by rfl
```
