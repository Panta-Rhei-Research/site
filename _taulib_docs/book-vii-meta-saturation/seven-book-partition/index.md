---
{
  "projection_kind": "taulib_declaration",
  "title": "SevenBookPartition",
  "permalink": "/verify/taulib/docs/book-vii-meta-saturation/seven-book-partition/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Meta.Saturation`.",
  "declaration_id": "TauLib.BookVII.Meta.Saturation::SevenBookPartition",
  "declaration_slug": "seven-book-partition",
  "kind": "structure",
  "name": "SevenBookPartition",
  "module_name": "TauLib.BookVII.Meta.Saturation",
  "module_url": "/verify/taulib/docs/book-vii-meta-saturation/",
  "source_line_start": 144,
  "source_line_end": 156,
  "registry_ids": [
    "VII.P02"
  ],
  "related_registry_items": [
    {
      "id": "VII.P02",
      "title": "Seven-Book Partition",
      "url": "/registry/object/VII.P02/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L144-L156",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Meta.Saturation",
        "url": "/verify/taulib/docs/book-vii-meta-saturation/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L144-L156",
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

- Module: [TauLib.BookVII.Meta.Saturation](/verify/taulib/docs/book-vii-meta-saturation/)
- Source path: [`TauLib/BookVII/Meta/Saturation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L144-L156)
- Source range: L144-L156
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.P02` — Seven-Book Partition

## Immediate Comment / Docstring

```lean
/-- [VII.P02] Seven-Book Partition: four layers require minimum 7 books.
    E₀: 3 books (I foundation + II holomorphy + III spectrum)
    E₁: 2 books (IV microcosm + V macrocosm)
    E₂: 1 book (VI life)
    E₃: 1 book (VII metaphysics)
    Total: 3 + 2 + 1 + 1 = 7 -/
```

## Source Excerpt

```lean
structure SevenBookPartition where
  e0_books : Nat
  e0_eq : e0_books = 3
  e1_books : Nat
  e1_eq : e1_books = 2
  e2_books : Nat
  e2_eq : e2_books = 1
  e3_books : Nat
  e3_eq : e3_books = 1
  total : Nat
  total_eq : total = 7
  sum_eq : e0_books + e1_books + e2_books + e3_books = total
  deriving Repr
```
