---
{
  "projection_kind": "taulib_declaration",
  "title": "e1_gluing_8_3_3",
  "permalink": "/verify/taulib/docs/book-iii-prologue-hartogs-bulk/e1-gluing-8-3-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Prologue.HartogsBulk`.",
  "declaration_id": "TauLib.BookIII.Prologue.HartogsBulk::e1_gluing_8_3_3",
  "declaration_slug": "e1-gluing-8-3-3",
  "kind": "theorem",
  "name": "e1_gluing_8_3_3",
  "module_name": "TauLib.BookIII.Prologue.HartogsBulk",
  "module_url": "/verify/taulib/docs/book-iii-prologue-hartogs-bulk/",
  "source_line_start": 135,
  "source_line_end": 136,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Prologue/HartogsBulk.lean#L135-L136",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Prologue/HartogsBulk.lean#L135-L136",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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
- Source path: [`TauLib/BookIII/Prologue/HartogsBulk.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Prologue/HartogsBulk.lean#L135-L136)
- Source range: L135-L136
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.D03` — E₁ as Gluing Principle

## Immediate Comment / Docstring

```lean
-- E₁ gluing [III.D03]
```

## Source Excerpt

```lean
theorem e1_gluing_8_3_3 :
    e1_gluing_check 8 3 3 = true := by native_decide
```
