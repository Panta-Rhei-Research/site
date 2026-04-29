---
{
  "projection_kind": "taulib_declaration",
  "title": "DecimalDiagonalExtractor",
  "permalink": "/verify/taulib/docs/book-i-sets-cantor-refutation/decimal-diagonal-extractor/",
  "summary_short": "`structure` declaration in `TauLib.BookI.Sets.CantorRefutation`.",
  "declaration_id": "TauLib.BookI.Sets.CantorRefutation::DecimalDiagonalExtractor",
  "declaration_slug": "decimal-diagonal-extractor",
  "kind": "structure",
  "name": "DecimalDiagonalExtractor",
  "module_name": "TauLib.BookI.Sets.CantorRefutation",
  "module_url": "/verify/taulib/docs/book-i-sets-cantor-refutation/",
  "source_line_start": 53,
  "source_line_end": 59,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/CantorRefutation.lean#L53-L59",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/CantorRefutation.lean#L53-L59",
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
- Source path: [`TauLib/BookI/Sets/CantorRefutation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/CantorRefutation.lean#L53-L59)
- Source range: L53-L59
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- A "decimal digit extractor" would be a total function that, given an
    enumeration index n and a digit position k, returns the k-th digit
    of the n-th real number. The Cantor argument demands that the
    diagonal d(n) = extract(n, n) can be "modified" to avoid every row.

    The fundamental obstruction: any extractor whose diagonal avoids
    itself is self-contradictory (diagonal(n) = extract(n,n) by definition,
    yet the avoidance condition demands diagonal(n) != extract(n,n)). -/
```

## Source Excerpt

```lean
structure DecimalDiagonalExtractor where
  /-- The digit extraction function: extract(n, k) = k-th digit of n-th real -/
  extract : TauIdx -> TauIdx -> TauIdx
  /-- The diagonal: d(n) = extract(n, n) -/
  diagonal : TauIdx -> TauIdx
  /-- The diagonal is defined by self-application -/
  diagonal_def : forall n, diagonal n = extract n n
```
