---
{
  "projection_kind": "taulib_declaration",
  "title": "ChemotaxisFunctor",
  "permalink": "/verify/taulib/docs/book-vi-agency-agency-sector/chemotaxis-functor/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Agency.AgencySector`.",
  "declaration_id": "TauLib.BookVI.Agency.AgencySector::ChemotaxisFunctor",
  "declaration_slug": "chemotaxis-functor",
  "kind": "structure",
  "name": "ChemotaxisFunctor",
  "module_name": "TauLib.BookVI.Agency.AgencySector",
  "module_url": "/verify/taulib/docs/book-vi-agency-agency-sector/",
  "source_line_start": 129,
  "source_line_end": 138,
  "registry_ids": [
    "VI.D31"
  ],
  "related_registry_items": [
    {
      "id": "VI.D31",
      "title": "Metabolic Circulation",
      "url": "/registry/object/VI.D31/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Agency/AgencySector.lean#L129-L138",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Agency.AgencySector",
        "url": "/verify/taulib/docs/book-vi-agency-agency-sector/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Agency/AgencySector.lean#L129-L138",
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

- Module: [TauLib.BookVI.Agency.AgencySector](/verify/taulib/docs/book-vi-agency-agency-sector/)
- Source path: [`TauLib/BookVI/Agency/AgencySector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Agency/AgencySector.lean#L129-L138)
- Source range: L129-L138
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D31` — Metabolic Circulation

## Immediate Comment / Docstring

```lean
/-- [VI.D31] Chemotaxis Functor: directed spatial agency.
    Maps chemical gradient to motility direction.
    The simplest Agency instantiation: bacterium swimming up gradient. -/
```

## Source Excerpt

```lean
structure ChemotaxisFunctor where
  /-- Input: chemical gradient signal. -/
  input_type : String := "chemical_gradient"
  /-- Output: motility direction. -/
  output_type : String := "motility_direction"
  /-- Preserves distinction (carrier boundary intact during motion). -/
  preserves_distinction : Bool := true
  /-- Scope: τ-effective. -/
  scope : String := "tau-effective"
  deriving Repr
```
