---
{
  "projection_kind": "taulib_declaration",
  "title": "TauSphaleronQuestion",
  "permalink": "/verify/taulib/docs/book-iv-coda-complete-ledger/tau-sphaleron-question/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Coda.CompleteLedger`.",
  "declaration_id": "TauLib.BookIV.Coda.CompleteLedger::TauSphaleronQuestion",
  "declaration_slug": "tau-sphaleron-question",
  "kind": "structure",
  "name": "TauSphaleronQuestion",
  "module_name": "TauLib.BookIV.Coda.CompleteLedger",
  "module_url": "/verify/taulib/docs/book-iv-coda-complete-ledger/",
  "source_line_start": 171,
  "source_line_end": 182,
  "registry_ids": [
    "IV.D242"
  ],
  "related_registry_items": [
    {
      "id": "IV.D242",
      "title": "tau-sphaleron question",
      "url": "/registry/object/IV.D242/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/CompleteLedger.lean#L171-L182",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Coda.CompleteLedger",
        "url": "/verify/taulib/docs/book-iv-coda-complete-ledger/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/CompleteLedger.lean#L171-L182",
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

- Module: [TauLib.BookIV.Coda.CompleteLedger](/verify/taulib/docs/book-iv-coda-complete-ledger/)
- Source path: [`TauLib/BookIV/Coda/CompleteLedger.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/CompleteLedger.lean#L171-L182)
- Source range: L171-L182
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D242` — tau-sphaleron question

## Immediate Comment / Docstring

```lean
/-- [IV.D242] (Conjectural) The tau-sphaleron question: can a
    non-perturbative process in Category tau change the topological
    winding number theta by a nonzero integer while respecting all
    tower compatibility conditions?

    In orthodox electroweak theory, sphalerons mediate baryon-number
    violation through tunneling over a potential barrier.

    In Category tau, this requires base-fiber coupling (the transition
    must pass through the omega-sector), which cannot be resolved on
    the fiber T^2 alone. Deferred to Book V. -/
```

## Source Excerpt

```lean
structure TauSphaleronQuestion where
  /-- Question: can theta change non-perturbatively? -/
  question : String := "Can theta change by nonzero integer non-perturbatively?"
  /-- Requires base-fiber coupling. -/
  requires_base_fiber : Bool := true
  /-- Cannot be resolved on T^2 alone. -/
  fiber_insufficient : Bool := true
  /-- Deferred to Book V. -/
  deferred : String := "Book V"
  /-- Scope: conjectural. -/
  scope : String := "conjectural"
  deriving Repr
```
