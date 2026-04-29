---
{
  "projection_kind": "taulib_declaration",
  "title": "TenRegimeInstantiations",
  "permalink": "/verify/taulib/docs/book-iv-many-body-nflboundary/ten-regime-instantiations/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.ManyBody.NFLBoundary`.",
  "declaration_id": "TauLib.BookIV.ManyBody.NFLBoundary::TenRegimeInstantiations",
  "declaration_slug": "ten-regime-instantiations",
  "kind": "structure",
  "name": "TenRegimeInstantiations",
  "module_name": "TauLib.BookIV.ManyBody.NFLBoundary",
  "module_url": "/verify/taulib/docs/book-iv-many-body-nflboundary/",
  "source_line_start": 149,
  "source_line_end": 159,
  "registry_ids": [
    "IV.P229"
  ],
  "related_registry_items": [
    {
      "id": "IV.P229",
      "title": "Ten Regime Instantiations",
      "url": "/registry/object/IV.P229/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/NFLBoundary.lean#L149-L159",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/NFLBoundary.lean#L149-L159",
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
- Source path: [`TauLib/BookIV/ManyBody/NFLBoundary.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/NFLBoundary.lean#L149-L159)
- Source range: L149-L159
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P229` — Ten Regime Instantiations

## Immediate Comment / Docstring

```lean
/-- [IV.P229] The decidable meta-theorem instantiates for all ten regimes.
    Each regime is a corollary via a horizon-contractivity lemma. -/
```

## Source Excerpt

```lean
structure TenRegimeInstantiations where
  /-- Number of regimes. -/
  num_regimes : Nat := 10
  /-- All decidable at finite refinement. -/
  all_decidable : Bool := true
  /-- Regime labels. -/
  regimes : List String :=
    ["Crystal", "Glass", "Quasicrystal",
     "Euler", "Navier-Stokes", "MHD", "Plasma",
     "Superfluid", "Superconductor", "Ferromagnet"]
  deriving Repr
```
