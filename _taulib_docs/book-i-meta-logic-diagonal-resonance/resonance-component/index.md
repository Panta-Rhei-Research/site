---
{
  "projection_kind": "taulib_declaration",
  "title": "ResonanceComponent",
  "permalink": "/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/resonance-component/",
  "summary_short": "`inductive` declaration in `TauLib.BookI.MetaLogic.DiagonalResonance`.",
  "declaration_id": "TauLib.BookI.MetaLogic.DiagonalResonance::ResonanceComponent",
  "declaration_slug": "resonance-component",
  "kind": "inductive",
  "name": "ResonanceComponent",
  "module_name": "TauLib.BookI.MetaLogic.DiagonalResonance",
  "module_url": "/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/",
  "source_line_start": 32,
  "source_line_end": 36,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/DiagonalResonance.lean#L32-L36",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/DiagonalResonance.lean#L32-L36",
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
- Source path: [`TauLib/BookI/MetaLogic/DiagonalResonance.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/DiagonalResonance.lean#L32-L36)
- Source range: L32-L36
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `I.D89` — Diagonal Resonance

## Immediate Comment / Docstring

```lean
/-- [I.D89] The three components of diagonal resonance. -/
```

## Source Excerpt

```lean
inductive ResonanceComponent where
  | L  -- Meta-level contraction / free token reuse
  | E  -- Equality-as-congruence (substitution = identification)
  | P  -- Ontic self-products / diagonal materialization
  deriving DecidableEq, Repr
```
