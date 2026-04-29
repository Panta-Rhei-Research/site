---
{
  "projection_kind": "taulib_declaration",
  "title": "book3_e1_established",
  "permalink": "/verify/taulib/docs/book-iii-prologue-hartogs-bulk/book3-e1-established/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Prologue.HartogsBulk`.",
  "declaration_id": "TauLib.BookIII.Prologue.HartogsBulk::book3_e1_established",
  "declaration_slug": "book3-e1-established",
  "kind": "def",
  "name": "book3_e1_established",
  "module_name": "TauLib.BookIII.Prologue.HartogsBulk",
  "module_url": "/verify/taulib/docs/book-iii-prologue-hartogs-bulk/",
  "source_line_start": 101,
  "source_line_end": 102,
  "registry_ids": [
    "III.D03"
  ],
  "related_registry_items": [
    {
      "id": "III.D03",
      "title": "E₁ as Gluing Principle",
      "url": "/registry/object/III.D03/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Prologue/HartogsBulk.lean#L101-L102",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Prologue.HartogsBulk",
        "url": "/verify/taulib/docs/book-iii-prologue-hartogs-bulk/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Prologue/HartogsBulk.lean#L101-L102",
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

- Module: [TauLib.BookIII.Prologue.HartogsBulk](/verify/taulib/docs/book-iii-prologue-hartogs-bulk/)
- Source path: [`TauLib/BookIII/Prologue/HartogsBulk.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Prologue/HartogsBulk.lean#L101-L102)
- Source range: L101-L102
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D03` — E₁ as Gluing Principle

## Immediate Comment / Docstring

```lean
/-- [III.D03] The entry point for Book III: E₁ is established.
    Book III begins at E₁ and constructs the full enrichment ladder. -/
```

## Source Excerpt

```lean
def book3_e1_established (bound db k_max : TauIdx) : Bool :=
  book3_starts_at_e1 db bound k_max && e1_gluing_check bound db k_max
```
