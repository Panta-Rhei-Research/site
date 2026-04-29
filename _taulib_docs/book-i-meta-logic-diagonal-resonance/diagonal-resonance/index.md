---
{
  "projection_kind": "taulib_declaration",
  "title": "DiagonalResonance",
  "permalink": "/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/diagonal-resonance/",
  "summary_short": "`structure` declaration in `TauLib.BookI.MetaLogic.DiagonalResonance`.",
  "declaration_id": "TauLib.BookI.MetaLogic.DiagonalResonance::DiagonalResonance",
  "declaration_slug": "diagonal-resonance",
  "kind": "structure",
  "name": "DiagonalResonance",
  "module_name": "TauLib.BookI.MetaLogic.DiagonalResonance",
  "module_url": "/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/",
  "source_line_start": 39,
  "source_line_end": 43,
  "registry_ids": [
    "I.D89"
  ],
  "related_registry_items": [
    {
      "id": "I.D89",
      "title": "Diagonal Resonance",
      "url": "/registry/object/I.D89/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/DiagonalResonance.lean#L39-L43",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/DiagonalResonance.lean#L39-L43",
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
- Source path: [`TauLib/BookI/MetaLogic/DiagonalResonance.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/DiagonalResonance.lean#L39-L43)
- Source range: L39-L43
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `I.D89` — Diagonal Resonance

## Immediate Comment / Docstring

```lean
/-- [I.D89] A foundation's diagonal resonance profile: which components are present. -/
```

## Source Excerpt

```lean
structure DiagonalResonance where
  contraction_present : Bool     -- (L) free meta-level contraction
  equality_congruence : Bool     -- (E) equality-as-congruence with full substitution
  self_products : Bool           -- (P) ontic self-products with diagonal materialization
  deriving DecidableEq, Repr
```
