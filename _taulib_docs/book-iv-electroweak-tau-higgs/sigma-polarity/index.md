---
{
  "projection_kind": "taulib_declaration",
  "title": "SigmaPolarity",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-tau-higgs/sigma-polarity/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.TauHiggs`.",
  "declaration_id": "TauLib.BookIV.Electroweak.TauHiggs::SigmaPolarity",
  "declaration_slug": "sigma-polarity",
  "kind": "structure",
  "name": "SigmaPolarity",
  "module_name": "TauLib.BookIV.Electroweak.TauHiggs",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs/",
  "source_line_start": 176,
  "source_line_end": 183,
  "registry_ids": [
    "IV.D139"
  ],
  "related_registry_items": [
    {
      "id": "IV.D139",
      "title": "σ-Polarity Condition",
      "url": "/registry/object/IV.D139/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs.lean#L176-L183",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.TauHiggs",
        "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs.lean#L176-L183",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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

- Module: [TauLib.BookIV.Electroweak.TauHiggs](/verify/taulib/docs/book-iv-electroweak-tau-higgs/)
- Source path: [`TauLib/BookIV/Electroweak/TauHiggs.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs.lean#L176-L183)
- Source range: L176-L183
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D139` — σ-Polarity Condition

## Immediate Comment / Docstring

```lean
/-- [IV.D139] The surviving Higgs excitation has σ-polarity σ = +1,
    meaning it is unpolarized (neither χ₊ nor χ₋ dominant).
    This reflects its origin at the CROSSING point of the
    lemniscate, where both lobes meet. -/
```

## Source Excerpt

```lean
structure SigmaPolarity where
  /-- Polarity value: +1 = unpolarized. -/
  sigma : Int := 1
  /-- At crossing point. -/
  at_crossing : Bool := true
  /-- Neither lobe dominates. -/
  unpolarized : Bool := true
  deriving Repr
```
