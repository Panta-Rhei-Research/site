---
{
  "projection_kind": "taulib_declaration",
  "title": "Commitment",
  "permalink": "/verify/taulib/docs/book-vii-meta-commitment/commitment/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Meta.Commitment`.",
  "declaration_id": "TauLib.BookVII.Meta.Commitment::Commitment",
  "declaration_slug": "commitment",
  "kind": "structure",
  "name": "Commitment",
  "module_name": "TauLib.BookVII.Meta.Commitment",
  "module_url": "/verify/taulib/docs/book-vii-meta-commitment/",
  "source_line_start": 110,
  "source_line_end": 116,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Commitment.lean#L110-L116",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Meta.Commitment",
        "url": "/verify/taulib/docs/book-vii-meta-commitment/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Commitment.lean#L110-L116",
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

- Module: [TauLib.BookVII.Meta.Commitment](/verify/taulib/docs/book-vii-meta-commitment/)
- Source path: [`TauLib/BookVII/Meta/Commitment.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Commitment.lean#L110-L116)
- Source range: L110-L116
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- A structural commitment in the Panta Rhei framework:
    a place where the monograph explicitly declines to force
    a stance via proof, for reasons given in the warrant.

    Commitments are inspectable data (`def` values), not
    performative `sorry`-closed propositions. A `Commitment`
    adds no axioms, asserts no proposition, and cannot be used
    as a premise in any theorem; it is a structured record.

    Fields:
    - `statement`: the commitment claim, verbatim from the monograph.
    - `warrant`: the methodological justification for declining
      to force a stance, explicitly traceable to Book VII's
      No-Forced-Stance discipline (`VII.T47`).
    - `registry_id`: the canonical registry identifier
      (e.g., `"VII.T46"`) for cross-reference with the
      monograph's LaTeX source. -/
```

## Source Excerpt

```lean
structure Commitment where
  statement : String
  warrant : String
  registry_id : String
  deriving Repr, Inhabited

end Tau.BookVII.Meta.Commitment
```
