---
{
  "projection_kind": "taulib_declaration",
  "title": "IdentitySlippage",
  "permalink": "/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/identity-slippage/",
  "summary_short": "`structure` declaration in `TauLib.BookI.MetaLogic.DiagonalResonance`.",
  "declaration_id": "TauLib.BookI.MetaLogic.DiagonalResonance::IdentitySlippage",
  "declaration_slug": "identity-slippage",
  "kind": "structure",
  "name": "IdentitySlippage",
  "module_name": "TauLib.BookI.MetaLogic.DiagonalResonance",
  "module_url": "/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/",
  "source_line_start": 75,
  "source_line_end": 77,
  "registry_ids": [
    "I.D90"
  ],
  "related_registry_items": [
    {
      "id": "I.D90",
      "title": "Identity Slippage",
      "url": "/registry/object/I.D90/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/DiagonalResonance.lean#L75-L77",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.MetaLogic.DiagonalResonance",
        "url": "/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/DiagonalResonance.lean#L75-L77",
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

- Module: [TauLib.BookI.MetaLogic.DiagonalResonance](/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/)
- Source path: [`TauLib/BookI/MetaLogic/DiagonalResonance.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/DiagonalResonance.lean#L75-L77)
- Source range: L75-L77
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `I.D90` — Identity Slippage

## Immediate Comment / Docstring

```lean
/-- [I.D90] Identity slippage: a foundation exhibits identity slippage if
    diagonal resonance prevents distinct ontic objects from being preserved
    as distinct under global projection. -/
```

## Source Excerpt

```lean
structure IdentitySlippage where
  resonance : DiagonalResonance
  is_full : resonance.isFullResonance = true
```
