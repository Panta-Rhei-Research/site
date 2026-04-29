---
{
  "projection_kind": "taulib_declaration",
  "title": "DecidableMeta",
  "permalink": "/verify/taulib/docs/book-iv-many-body-nflboundary/decidable-meta/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.ManyBody.NFLBoundary`.",
  "declaration_id": "TauLib.BookIV.ManyBody.NFLBoundary::DecidableMeta",
  "declaration_slug": "decidable-meta",
  "kind": "structure",
  "name": "DecidableMeta",
  "module_name": "TauLib.BookIV.ManyBody.NFLBoundary",
  "module_url": "/verify/taulib/docs/book-iv-many-body-nflboundary/",
  "source_line_start": 122,
  "source_line_end": 133,
  "registry_ids": [
    "IV.T211"
  ],
  "related_registry_items": [
    {
      "id": "IV.T211",
      "title": "Decidable Phase Classification Meta-Theorem",
      "url": "/registry/object/IV.T211/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/NFLBoundary.lean#L122-L133",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.ManyBody.NFLBoundary",
        "url": "/verify/taulib/docs/book-iv-many-body-nflboundary/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/NFLBoundary.lean#L122-L133",
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

- Module: [TauLib.BookIV.ManyBody.NFLBoundary](/verify/taulib/docs/book-iv-many-body-nflboundary/)
- Source path: [`TauLib/BookIV/ManyBody/NFLBoundary.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/NFLBoundary.lean#L122-L133)
- Source range: L122-L133
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T211` — Decidable Phase Classification Meta-Theorem

## Immediate Comment / Docstring

```lean
/-- [IV.T211] **Decidable Phase Classification.**
    At fixed refinement stage n with bounded budget K, every regime
    predicate is decidable by finite recursion on NF-coded states.

    Why: (1) NF code space is finite at stage n; (2) each d_j is
    computable from NF code; (3) each regime condition is decidable
    on finite codes; (4) conjunction of decidable predicates is decidable. -/
```

## Source Excerpt

```lean
structure DecidableMeta where
  /-- NF code space is finite. -/
  finite_code_space : Bool := true
  /-- Each defect component computable. -/
  components_computable : Bool := true
  /-- Each regime condition decidable. -/
  conditions_decidable : Bool := true
  /-- Conjunction of decidable is decidable. -/
  conjunction_decidable : Bool := true
  /-- No real-number arithmetic required. -/
  no_reals : Bool := true
  deriving Repr
```
