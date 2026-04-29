---
{
  "projection_kind": "taulib_declaration",
  "title": "CantorDiagonalApparatus",
  "permalink": "/verify/taulib/docs/book-i-sets-cantor-refutation/cantor-diagonal-apparatus/",
  "summary_short": "`structure` declaration in `TauLib.BookI.Sets.CantorRefutation`.",
  "declaration_id": "TauLib.BookI.Sets.CantorRefutation::CantorDiagonalApparatus",
  "declaration_slug": "cantor-diagonal-apparatus",
  "kind": "structure",
  "name": "CantorDiagonalApparatus",
  "module_name": "TauLib.BookI.Sets.CantorRefutation",
  "module_url": "/verify/taulib/docs/book-i-sets-cantor-refutation/",
  "source_line_start": 142,
  "source_line_end": 151,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/CantorRefutation.lean#L142-L151",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Sets.CantorRefutation",
        "url": "/verify/taulib/docs/book-i-sets-cantor-refutation/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/CantorRefutation.lean#L142-L151",
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

- Module: [TauLib.BookI.Sets.CantorRefutation](/verify/taulib/docs/book-i-sets-cantor-refutation/)
- Source path: [`TauLib/BookI/Sets/CantorRefutation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/CantorRefutation.lean#L142-L151)
- Source range: L142-L151
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The Cantor diagonal argument requires three structural ingredients.
    We show the conjunction of all three is inconsistent in tau. -/
```

## Source Excerpt

```lean
structure CantorDiagonalApparatus where
  /-- A decimal digit extractor -/
  extractor : DecimalDiagonalExtractor
  /-- The diagonal avoids every row -/
  avoids : forall n, extractor.diagonal n ≠ extractor.extract n n
  /-- A comprehension separator -/
  sep : ComprehensionSep
  /-- Sep satisfies the comprehension schema -/
  sep_works : forall (P : TauIdx -> Prop) (a : TauIdx),
    tau_mem a (sep P) <-> P a
```
