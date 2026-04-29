---
{
  "projection_kind": "taulib_declaration",
  "title": "NonOmegaGenerator",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/non-omega-generator/",
  "summary_short": "`inductive` declaration in `TauLib.BookIV.Electroweak.TauHiggs2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.TauHiggs2::NonOmegaGenerator",
  "declaration_slug": "non-omega-generator",
  "kind": "inductive",
  "name": "NonOmegaGenerator",
  "module_name": "TauLib.BookIV.Electroweak.TauHiggs2",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/",
  "source_line_start": 368,
  "source_line_end": 370,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L368-L370",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L368-L370",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
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

- Module: [TauLib.BookIV.Electroweak.TauHiggs2](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/)
- Source path: [`TauLib/BookIV/Electroweak/TauHiggs2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L368-L370)
- Source range: L368-L370
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `IV.T150` — Factor-4 from Non-omega Generator Count

## Immediate Comment / Docstring

```lean
/-- The four non-ω generators of Category τ.
    The ω-crossing = γ∩η is the intersection; the remaining four
    generators count as the "non-ω" generators. [IV.T150] -/
```

## Source Excerpt

```lean
inductive NonOmegaGenerator
  | alpha | pi | gamma | eta
  deriving Repr, DecidableEq
```
