---
{
  "projection_kind": "taulib_declaration",
  "title": "DiscreteSymmetryStatus",
  "permalink": "/verify/taulib/docs/book-iv-coda-laws-as-structure/discrete-symmetry-status/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Coda.LawsAsStructure`.",
  "declaration_id": "TauLib.BookIV.Coda.LawsAsStructure::DiscreteSymmetryStatus",
  "declaration_slug": "discrete-symmetry-status",
  "kind": "structure",
  "name": "DiscreteSymmetryStatus",
  "module_name": "TauLib.BookIV.Coda.LawsAsStructure",
  "module_url": "/verify/taulib/docs/book-iv-coda-laws-as-structure/",
  "source_line_start": 168,
  "source_line_end": 177,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/LawsAsStructure.lean#L168-L177",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Coda.LawsAsStructure",
        "url": "/verify/taulib/docs/book-iv-coda-laws-as-structure/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/LawsAsStructure.lean#L168-L177",
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

- Module: [TauLib.BookIV.Coda.LawsAsStructure](/verify/taulib/docs/book-iv-coda-laws-as-structure/)
- Source path: [`TauLib/BookIV/Coda/LawsAsStructure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/LawsAsStructure.lean#L168-L177)
- Source range: L168-L177
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Discrete symmetry status in Category tau. -/
```

## Source Excerpt

```lean
structure DiscreteSymmetryStatus where
  /-- C (charge conjugation): can be violated. -/
  c_violable : Bool := true
  /-- P (parity): violated in A-sector. -/
  p_violated : Bool := true
  /-- CP: can be violated (EW phase). -/
  cp_violable : Bool := true
  /-- CPT: preserved (structural). -/
  cpt_preserved : Bool := true
  deriving Repr
```
