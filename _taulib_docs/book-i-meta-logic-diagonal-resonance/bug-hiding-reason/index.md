---
{
  "projection_kind": "taulib_declaration",
  "title": "BugHidingReason",
  "permalink": "/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/bug-hiding-reason/",
  "summary_short": "`inductive` declaration in `TauLib.BookI.MetaLogic.DiagonalResonance`.",
  "declaration_id": "TauLib.BookI.MetaLogic.DiagonalResonance::BugHidingReason",
  "declaration_slug": "bug-hiding-reason",
  "kind": "inductive",
  "name": "BugHidingReason",
  "module_name": "TauLib.BookI.MetaLogic.DiagonalResonance",
  "module_url": "/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/",
  "source_line_start": 144,
  "source_line_end": 150,
  "registry_ids": [
    "I.R24"
  ],
  "related_registry_items": [
    {
      "id": "I.R24",
      "title": "Five Reasons Why The Bug Hides",
      "url": "/registry/object/I.R24/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/DiagonalResonance.lean#L144-L150",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/DiagonalResonance.lean#L144-L150",
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
- Source path: [`TauLib/BookI/MetaLogic/DiagonalResonance.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/DiagonalResonance.lean#L144-L150)
- Source range: L144-L150
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `I.R24` — Five Reasons Why The Bug Hides

## Immediate Comment / Docstring

```lean
/-- [I.R24] Five reasons why diagonal resonance is hard to detect. -/
```

## Source Excerpt

```lean
inductive BugHidingReason where
  | notOneBug           -- Not a bug in one module
  | slippageNotCrash    -- Produces slippage, not a crash
  | everywhereNowhere   -- Everywhere in the plumbing, nowhere in any theorem
  | hidesBehindUtility  -- The wiring-first stack is effective
  | needsClosureDemand  -- Only visible when demanding unique omega
  deriving DecidableEq, Repr
```
