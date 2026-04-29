---
{
  "projection_kind": "taulib_declaration",
  "title": "e3_non_emptiness",
  "permalink": "/verify/taulib/docs/book-vii-meta-registers/e3-non-emptiness/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Meta.Registers`.",
  "declaration_id": "TauLib.BookVII.Meta.Registers::e3_non_emptiness",
  "declaration_slug": "e3-non-emptiness",
  "kind": "theorem",
  "name": "e3_non_emptiness",
  "module_name": "TauLib.BookVII.Meta.Registers",
  "module_url": "/verify/taulib/docs/book-vii-meta-registers/",
  "source_line_start": 265,
  "source_line_end": 267,
  "registry_ids": [
    "VII.T02"
  ],
  "related_registry_items": [
    {
      "id": "VII.T02",
      "title": "E₃ Non-Emptiness",
      "url": "/registry/object/VII.T02/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L265-L267",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Meta.Registers",
        "url": "/verify/taulib/docs/book-vii-meta-registers/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L265-L267",
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

- Module: [TauLib.BookVII.Meta.Registers](/verify/taulib/docs/book-vii-meta-registers/)
- Source path: [`TauLib/BookVII/Meta/Registers.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L265-L267)
- Source range: L265-L267
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VII.T02` — E₃ Non-Emptiness

## Immediate Comment / Docstring

```lean
/-- [VII.T02] E₃ Non-Emptiness: E₃ enrichment layer is non-empty.
    BH basin law-code is constructive witness satisfying SelfDesc². -/
```

## Source Excerpt

```lean
theorem e3_non_emptiness :
    bh_basin.selfdesc_squared = true :=
  rfl
```
