---
{
  "projection_kind": "taulib_declaration",
  "title": "ChargedCurrent",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-ewmixing/charged-current/",
  "summary_short": "`inductive` declaration in `TauLib.BookIV.Electroweak.EWMixing`.",
  "declaration_id": "TauLib.BookIV.Electroweak.EWMixing::ChargedCurrent",
  "declaration_slug": "charged-current",
  "kind": "inductive",
  "name": "ChargedCurrent",
  "module_name": "TauLib.BookIV.Electroweak.EWMixing",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-ewmixing/",
  "source_line_start": 129,
  "source_line_end": 134,
  "registry_ids": [
    "IV.D129"
  ],
  "related_registry_items": [
    {
      "id": "IV.D129",
      "title": "Charged W Bosons",
      "url": "/registry/object/IV.D129/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWMixing.lean#L129-L134",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.EWMixing",
        "url": "/verify/taulib/docs/book-iv-electroweak-ewmixing/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWMixing.lean#L129-L134",
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

- Module: [TauLib.BookIV.Electroweak.EWMixing](/verify/taulib/docs/book-iv-electroweak-ewmixing/)
- Source path: [`TauLib/BookIV/Electroweak/EWMixing.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWMixing.lean#L129-L134)
- Source range: L129-L134
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `IV.D129` — Charged W Bosons

## Immediate Comment / Docstring

```lean
/-- [IV.D129] W± charged currents: the off-diagonal SU(2)_L
    generators that mediate charge-changing weak interactions.
    These do NOT mix with B: only the neutral W³ mixes. -/
```

## Source Excerpt

```lean
inductive ChargedCurrent where
  /-- W+ raises weak isospin by 1. -/
  | Wplus
  /-- W- lowers weak isospin by 1. -/
  | Wminus
  deriving Repr, DecidableEq, BEq
```
