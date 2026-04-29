---
{
  "projection_kind": "taulib_declaration",
  "title": "ColorNeutrality",
  "permalink": "/verify/taulib/docs/book-iv-strong-color-holonomy/color-neutrality/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.ColorHolonomy`.",
  "declaration_id": "TauLib.BookIV.Strong.ColorHolonomy::ColorNeutrality",
  "declaration_slug": "color-neutrality",
  "kind": "structure",
  "name": "ColorNeutrality",
  "module_name": "TauLib.BookIV.Strong.ColorHolonomy",
  "module_url": "/verify/taulib/docs/book-iv-strong-color-holonomy/",
  "source_line_start": 125,
  "source_line_end": 130,
  "registry_ids": [
    "IV.D156"
  ],
  "related_registry_items": [
    {
      "id": "IV.D156",
      "title": "Color Neutrality",
      "url": "/registry/object/IV.D156/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/ColorHolonomy.lean#L125-L130",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/ColorHolonomy.lean#L125-L130",
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
- Source path: [`TauLib/BookIV/Strong/ColorHolonomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/ColorHolonomy.lean#L125-L130)
- Source range: L125-L130
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D156` — Color Neutrality

## Immediate Comment / Docstring

```lean
/-- [IV.D156] Color-neutral (color singlet): total eta-holonomy is
    trivial, i.e., sum of eta-winding numbers is 0 mod 3. -/
```

## Source Excerpt

```lean
structure ColorNeutrality where
  /-- Total winding sum mod 3. -/
  total_mod3 : Nat := 0
  /-- Singlet condition. -/
  is_singlet : Bool := true
  deriving Repr
```
