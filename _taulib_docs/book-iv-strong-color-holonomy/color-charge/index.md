---
{
  "projection_kind": "taulib_declaration",
  "title": "ColorCharge",
  "permalink": "/verify/taulib/docs/book-iv-strong-color-holonomy/color-charge/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.ColorHolonomy`.",
  "declaration_id": "TauLib.BookIV.Strong.ColorHolonomy::ColorCharge",
  "declaration_slug": "color-charge",
  "kind": "structure",
  "name": "ColorCharge",
  "module_name": "TauLib.BookIV.Strong.ColorHolonomy",
  "module_url": "/verify/taulib/docs/book-iv-strong-color-holonomy/",
  "source_line_start": 79,
  "source_line_end": 84,
  "registry_ids": [
    "IV.D154"
  ],
  "related_registry_items": [
    {
      "id": "IV.D154",
      "title": "Color Charge",
      "url": "/registry/object/IV.D154/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/ColorHolonomy.lean#L79-L84",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Strong.ColorHolonomy",
        "url": "/verify/taulib/docs/book-iv-strong-color-holonomy/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/ColorHolonomy.lean#L79-L84",
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

- Module: [TauLib.BookIV.Strong.ColorHolonomy](/verify/taulib/docs/book-iv-strong-color-holonomy/)
- Source path: [`TauLib/BookIV/Strong/ColorHolonomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/ColorHolonomy.lean#L79-L84)
- Source range: L79-L84
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D154` — Color Charge

## Immediate Comment / Docstring

```lean
/-- [IV.D154] Color charge of a character mode chi_{m,n} on T^2:
    the holonomy class c(chi_{m,n}) := n mod 3, determined by
    the eta-winding number n. -/
```

## Source Excerpt

```lean
structure ColorCharge where
  /-- Eta-winding number mod 3. -/
  color : ColorClass
  /-- Source: eta-circle holonomy at depth 3. -/
  source : String := "eta-winding mod 3"
  deriving Repr
```
