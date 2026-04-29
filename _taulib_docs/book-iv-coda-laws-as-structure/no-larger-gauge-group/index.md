---
{
  "projection_kind": "taulib_declaration",
  "title": "NoLargerGaugeGroup",
  "permalink": "/verify/taulib/docs/book-iv-coda-laws-as-structure/no-larger-gauge-group/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Coda.LawsAsStructure`.",
  "declaration_id": "TauLib.BookIV.Coda.LawsAsStructure::NoLargerGaugeGroup",
  "declaration_slug": "no-larger-gauge-group",
  "kind": "structure",
  "name": "NoLargerGaugeGroup",
  "module_name": "TauLib.BookIV.Coda.LawsAsStructure",
  "module_url": "/verify/taulib/docs/book-iv-coda-laws-as-structure/",
  "source_line_start": 141,
  "source_line_end": 150,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/LawsAsStructure.lean#L141-L150",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/LawsAsStructure.lean#L141-L150",
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
- Source path: [`TauLib/BookIV/Coda/LawsAsStructure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/LawsAsStructure.lean#L141-L150)
- Source range: L141-L150
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Why no larger gauge group: fixed by 5 generators from K0-K6. -/
```

## Source Excerpt

```lean
structure NoLargerGaugeGroup where
  /-- Number of generators fixed by axioms. -/
  num_generators : Nat := 5
  /-- No embedding into SU(5). -/
  no_su5 : Bool := true
  /-- No embedding into SO(10). -/
  no_so10 : Bool := true
  /-- No proton decay. -/
  no_proton_decay : Bool := true
  deriving Repr
```
