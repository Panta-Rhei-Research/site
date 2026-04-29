---
{
  "projection_kind": "taulib_declaration",
  "title": "TwoLoopWindowCoeff",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-alpha-derivation/two-loop-window-coeff/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.AlphaDerivation`.",
  "declaration_id": "TauLib.BookIV.Electroweak.AlphaDerivation::TwoLoopWindowCoeff",
  "declaration_slug": "two-loop-window-coeff",
  "kind": "structure",
  "name": "TwoLoopWindowCoeff",
  "module_name": "TauLib.BookIV.Electroweak.AlphaDerivation",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-alpha-derivation/",
  "source_line_start": 416,
  "source_line_end": 427,
  "registry_ids": [
    "IV.D384"
  ],
  "related_registry_items": [
    {
      "id": "IV.D384",
      "title": "Two-Loop Window Coefficient c₂",
      "url": "/registry/object/IV.D384/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L416-L427",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.AlphaDerivation",
        "url": "/verify/taulib/docs/book-iv-electroweak-alpha-derivation/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L416-L427",
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

- Module: [TauLib.BookIV.Electroweak.AlphaDerivation](/verify/taulib/docs/book-iv-electroweak-alpha-derivation/)
- Source path: [`TauLib/BookIV/Electroweak/AlphaDerivation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L416-L427)
- Source range: L416-L427
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D384` — Two-Loop Window Coefficient c₂

## Immediate Comment / Docstring

```lean
/-- [IV.D384] Two-Loop Window Coefficient c₂ = 1/W₄(3) = 1/18.
    Loop order k → window W_{k+2}(·):
    - One-loop: W₃(4) = 5
    - Two-loop: W₄(3) = 18
    - Inflationary: W₅(3) = 19
    The same CF window sequence governs corrections across sectors. -/
```

## Source Excerpt

```lean
structure TwoLoopWindowCoeff where
  /-- One-loop window value. -/
  w3_4 : Nat := 5
  /-- Two-loop window value. -/
  w4_3 : Nat := 18
  /-- Inflationary window value. -/
  w5_3 : Nat := 19
  /-- c₂ denominator = W₄(3). -/
  c2_denom : Nat := 18
  /-- Window sequence is arithmetic at fixed arg 3. -/
  arithmetic_check : w4_3 = w3_4 + 13 := by decide
  deriving Repr
```
