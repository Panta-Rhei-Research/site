---
{
  "projection_kind": "taulib_declaration",
  "title": "ColorNumberTheorem",
  "permalink": "/verify/taulib/docs/book-iv-strong-color-holonomy/color-number-theorem/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.ColorHolonomy`.",
  "declaration_id": "TauLib.BookIV.Strong.ColorHolonomy::ColorNumberTheorem",
  "declaration_slug": "color-number-theorem",
  "kind": "structure",
  "name": "ColorNumberTheorem",
  "module_name": "TauLib.BookIV.Strong.ColorHolonomy",
  "module_url": "/verify/taulib/docs/book-iv-strong-color-holonomy/",
  "source_line_start": 274,
  "source_line_end": 289,
  "registry_ids": [
    "IV.T70"
  ],
  "related_registry_items": [
    {
      "id": "IV.T70",
      "title": "Color Number Theorem",
      "url": "/registry/object/IV.T70/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/ColorHolonomy.lean#L274-L289",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/ColorHolonomy.lean#L274-L289",
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
- Source path: [`TauLib/BookIV/Strong/ColorHolonomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/ColorHolonomy.lean#L274-L289)
- Source range: L274-L289
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T70` — Color Number Theorem

## Immediate Comment / Docstring

```lean
/-- [IV.T70] N_c = 3 is uniquely determined by:
    - Primorial depth d = 3
    - CRT decomposition Z/30Z = Z/2Z x Z/3Z x Z/5Z
    - Removal of polarity factor Z/2Z
    - Chi_minus-dominant resolution selects the Z/3Z factor

    The primorial 30 = 2 * 3 * 5, and depth 3 activates all three
    prime factors. The Z/2Z factor is absorbed by polarity,
    and Z/5Z is the EM depth-2 factor. The remaining Z/3Z gives N_c = 3. -/
```

## Source Excerpt

```lean
structure ColorNumberTheorem where
  /-- Number of colors. -/
  num_colors : Nat := 3
  /-- Primorial at depth 3. -/
  primorial_3 : Nat := 30
  /-- CRT factors. -/
  crt_factor_2 : Nat := 2
  crt_factor_3 : Nat := 3
  crt_factor_5 : Nat := 5
  /-- Z/2Z absorbed by polarity. -/
  polarity_absorbs : String := "Z/2Z"
  /-- Z/5Z is the EM depth-2 factor. -/
  em_factor : String := "Z/5Z"
  /-- Z/3Z is the strong color factor. -/
  strong_factor : String := "Z/3Z"
  deriving Repr
```
