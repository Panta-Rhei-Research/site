---
{
  "projection_kind": "taulib_declaration",
  "title": "LinearityCensus",
  "permalink": "/verify/taulib/docs/book-i-meta-logic-linearity-audit/linearity-census/",
  "summary_short": "`structure` declaration in `TauLib.BookI.MetaLogic.LinearityAudit`.",
  "declaration_id": "TauLib.BookI.MetaLogic.LinearityAudit::LinearityCensus",
  "declaration_slug": "linearity-census",
  "kind": "structure",
  "name": "LinearityCensus",
  "module_name": "TauLib.BookI.MetaLogic.LinearityAudit",
  "module_url": "/verify/taulib/docs/book-i-meta-logic-linearity-audit/",
  "source_line_start": 265,
  "source_line_end": 275,
  "registry_ids": [
    "I.T38"
  ],
  "related_registry_items": [
    {
      "id": "I.T38",
      "title": "Linearity Census",
      "url": "/registry/object/I.T38/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/LinearityAudit.lean#L265-L275",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.MetaLogic.LinearityAudit",
        "url": "/verify/taulib/docs/book-i-meta-logic-linearity-audit/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/LinearityAudit.lean#L265-L275",
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

- Module: [TauLib.BookI.MetaLogic.LinearityAudit](/verify/taulib/docs/book-i-meta-logic-linearity-audit/)
- Source path: [`TauLib/BookI/MetaLogic/LinearityAudit.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/LinearityAudit.lean#L265-L275)
- Source range: L265-L275
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `I.T38` — Linearity Census

## Immediate Comment / Docstring

```lean
/-- [I.T38] The Linearity Census Theorem.

    Of 82 pre-MetaLogic TauLib modules:
    - 80 are fully constructive (no classical axioms at all)
    - 1 uses Classical.em (Coordinates/Primes.lean), but both sites
      are on decidable predicates and hence eliminable
    - 1 uses the funext tactic (Holomorphy/SpectralCoefficients.lean),
      which depends on the funext kernel axiom (always present in CIC)

    The bottom line: TauLib is constructively valid modulo 2 eliminable
    Classical.em sites and 1 kernel axiom use. -/
```

## Source Excerpt

```lean
structure LinearityCensus where
  /-- Total module count -/
  total : census.length = 82
  /-- Constructive module count -/
  constructive : (census.filter (fun m => m.class_ == .constructive)).length = 80
  /-- Classical module count -/
  classical : (census.filter (fun m => m.class_ == .classical)).length = 1
  /-- Kernel axiom module count -/
  kernel : (census.filter (fun m => m.class_ == .kernelAxiom)).length = 1
  /-- The Classical.em sites are eliminable -/
  em_sites_eliminable : EmEliminability
```
