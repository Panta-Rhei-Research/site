---
{
  "projection_kind": "taulib_declaration",
  "title": "anticolor",
  "permalink": "/verify/taulib/docs/book-iv-strong-color-holonomy/anticolor/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Strong.ColorHolonomy`.",
  "declaration_id": "TauLib.BookIV.Strong.ColorHolonomy::anticolor",
  "declaration_slug": "anticolor",
  "kind": "def",
  "name": "anticolor",
  "module_name": "TauLib.BookIV.Strong.ColorHolonomy",
  "module_url": "/verify/taulib/docs/book-iv-strong-color-holonomy/",
  "source_line_start": 105,
  "source_line_end": 109,
  "registry_ids": [
    "IV.D155"
  ],
  "related_registry_items": [
    {
      "id": "IV.D155",
      "title": "Anti-Color",
      "url": "/registry/object/IV.D155/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/ColorHolonomy.lean#L105-L109",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/ColorHolonomy.lean#L105-L109",
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

- Module: [TauLib.BookIV.Strong.ColorHolonomy](/verify/taulib/docs/book-iv-strong-color-holonomy/)
- Source path: [`TauLib/BookIV/Strong/ColorHolonomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/ColorHolonomy.lean#L105-L109)
- Source range: L105-L109
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.D155` — Anti-Color

## Immediate Comment / Docstring

```lean
/-- [IV.D155] Anticolor: the conjugate class c_bar := (3-c) mod 3.
    Anti-red = red, anti-green = blue, anti-blue = green. -/
```

## Source Excerpt

```lean
def anticolor (c : ColorClass) : ColorClass :=
  match c with
  | .red   => .red    -- (3-0) mod 3 = 0
  | .green => .blue   -- (3-1) mod 3 = 2
  | .blue  => .green  -- (3-2) mod 3 = 1
```
