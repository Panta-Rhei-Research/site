---
{
  "projection_kind": "taulib_declaration",
  "title": "OrthodoxFoundation",
  "permalink": "/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/orthodox-foundation/",
  "summary_short": "`inductive` declaration in `TauLib.BookI.MetaLogic.DiagonalResonance`.",
  "declaration_id": "TauLib.BookI.MetaLogic.DiagonalResonance::OrthodoxFoundation",
  "declaration_slug": "orthodox-foundation",
  "kind": "inductive",
  "name": "OrthodoxFoundation",
  "module_name": "TauLib.BookI.MetaLogic.DiagonalResonance",
  "module_url": "/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/",
  "source_line_start": 164,
  "source_line_end": 168,
  "registry_ids": [
    "I.R25"
  ],
  "related_registry_items": [
    {
      "id": "I.R25",
      "title": "Orthodox Foundations Under the Lens",
      "url": "/registry/object/I.R25/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/DiagonalResonance.lean#L164-L168",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/DiagonalResonance.lean#L164-L168",
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

- Module: [TauLib.BookI.MetaLogic.DiagonalResonance](/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/)
- Source path: [`TauLib/BookI/MetaLogic/DiagonalResonance.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/DiagonalResonance.lean#L164-L168)
- Source range: L164-L168
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `I.R25` — Orthodox Foundations Under the Lens

## Immediate Comment / Docstring

```lean
/-- [I.R25] Three orthodox foundations examined for diagonal resonance. -/
```

## Source Excerpt

```lean
inductive OrthodoxFoundation where
  | ZFC    -- Zermelo-Fraenkel with Choice
  | CIC    -- Calculus of Inductive Constructions (Lean/Coq)
  | HoTT   -- Homotopy Type Theory
  deriving DecidableEq, Repr
```
