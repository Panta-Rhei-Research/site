---
{
  "projection_kind": "taulib_declaration",
  "title": "ChargeDensity",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/charge-density/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.TauMaxwell`.",
  "declaration_id": "TauLib.BookIV.Electroweak.TauMaxwell::ChargeDensity",
  "declaration_slug": "charge-density",
  "kind": "structure",
  "name": "ChargeDensity",
  "module_name": "TauLib.BookIV.Electroweak.TauMaxwell",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/",
  "source_line_start": 372,
  "source_line_end": 377,
  "registry_ids": [
    "IV.P45"
  ],
  "related_registry_items": [
    {
      "id": "IV.P45",
      "title": "Charge Density as Winding-Number Density",
      "url": "/registry/object/IV.P45/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauMaxwell.lean#L372-L377",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.TauMaxwell",
        "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauMaxwell.lean#L372-L377",
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

- Module: [TauLib.BookIV.Electroweak.TauMaxwell](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/)
- Source path: [`TauLib/BookIV/Electroweak/TauMaxwell.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauMaxwell.lean#L372-L377)
- Source range: L372-L377
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P45` — Charge Density as Winding-Number Density

## Immediate Comment / Docstring

```lean
/-- [IV.P45] Charge density ρ = J^0: count of winding numbers
    per unit spatial volume. A positive ρ corresponds to net
    positive winding (protons); negative to electrons. -/
```

## Source Excerpt

```lean
structure ChargeDensity where
  /-- Is the time-component of J. -/
  is_j_zero : Bool := true
  /-- Counts winding numbers per volume. -/
  is_winding_count : Bool := true
  deriving Repr
```
