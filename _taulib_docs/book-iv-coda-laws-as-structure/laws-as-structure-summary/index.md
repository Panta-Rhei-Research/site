---
{
  "projection_kind": "taulib_declaration",
  "title": "LawsAsStructureSummary",
  "permalink": "/verify/taulib/docs/book-iv-coda-laws-as-structure/laws-as-structure-summary/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Coda.LawsAsStructure`.",
  "declaration_id": "TauLib.BookIV.Coda.LawsAsStructure::LawsAsStructureSummary",
  "declaration_slug": "laws-as-structure-summary",
  "kind": "structure",
  "name": "LawsAsStructureSummary",
  "module_name": "TauLib.BookIV.Coda.LawsAsStructure",
  "module_url": "/verify/taulib/docs/book-iv-coda-laws-as-structure/",
  "source_line_start": 238,
  "source_line_end": 249,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/LawsAsStructure.lean#L238-L249",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/LawsAsStructure.lean#L238-L249",
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
- Source path: [`TauLib/BookIV/Coda/LawsAsStructure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/LawsAsStructure.lean#L238-L249)
- Source range: L238-L249
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Summary: what "laws as structure" means. Physical laws in tau are:
    1. Not empirical regularities on a blank substrate
    2. Not axioms of a physical theory
    3. Structural consequences of the categorical architecture K0-K6
    4. Each law = a tower-natural transformation
    5. Conservation = naturality condition -/
```

## Source Excerpt

```lean
structure LawsAsStructureSummary where
  /-- Not empirical. -/
  not_empirical : Bool := true
  /-- Not imposed axioms. -/
  not_imposed : Bool := true
  /-- Structural consequences. -/
  structural : Bool := true
  /-- Law = tower-natural transformation. -/
  law_is_nat_trans : Bool := true
  /-- Conservation = naturality. -/
  conservation_is_naturality : Bool := true
  deriving Repr
```
