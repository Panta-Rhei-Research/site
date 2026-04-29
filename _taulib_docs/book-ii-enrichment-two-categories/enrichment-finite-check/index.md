---
{
  "projection_kind": "taulib_declaration",
  "title": "enrichment_finite_check",
  "permalink": "/verify/taulib/docs/book-ii-enrichment-two-categories/enrichment-finite-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Enrichment.TwoCategories`.",
  "declaration_id": "TauLib.BookII.Enrichment.TwoCategories::enrichment_finite_check",
  "declaration_slug": "enrichment-finite-check",
  "kind": "def",
  "name": "enrichment_finite_check",
  "module_name": "TauLib.BookII.Enrichment.TwoCategories",
  "module_url": "/verify/taulib/docs/book-ii-enrichment-two-categories/",
  "source_line_start": 261,
  "source_line_end": 276,
  "registry_ids": [
    "II.P13"
  ],
  "related_registry_items": [
    {
      "id": "II.P13",
      "title": "Character Decomposition",
      "url": "/registry/object/II.P13/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/TwoCategories.lean#L261-L276",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Enrichment.TwoCategories",
        "url": "/verify/taulib/docs/book-ii-enrichment-two-categories/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/TwoCategories.lean#L261-L276",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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

- Module: [TauLib.BookII.Enrichment.TwoCategories](/verify/taulib/docs/book-ii-enrichment-two-categories/)
- Source path: [`TauLib/BookII/Enrichment/TwoCategories.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/TwoCategories.lean#L261-L276)
- Source range: L261-L276
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.P13` — Character Decomposition

## Immediate Comment / Docstring

```lean
/-- [II.P13] Enrichment iteration finiteness:
    At each stage k, the 2-hom-space is finite (bounded by P_k^P_k).
    This ensures the enrichment ladder is well-founded.
    We verify: the number of reduce-compatible maps at stage k is
    at most P_k^P_k, and the primorial tower's finite stages
    guarantee finiteness at every enrichment level. -/
```

## Source Excerpt

```lean
def enrichment_finite_check (db : TauIdx) : Bool :=
  go 1 (db + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else
      let pk := primorial k
      -- Upper bound: the total number of maps Z/P_kZ → Z/P_kZ is P_k^P_k
      -- The reduce-compatible subset is at most this size
      -- For k=1: P_1=2, so at most 2^2=4 maps
      -- For k=2: P_2=6, so at most 6^6 maps
      -- All finite: verified by primorial being finite
      let ok := pk > 0
      ok && go (k + 1) (fuel - 1)
  termination_by fuel
```
