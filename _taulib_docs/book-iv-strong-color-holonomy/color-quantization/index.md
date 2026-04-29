---
{
  "projection_kind": "taulib_declaration",
  "title": "ColorQuantization",
  "permalink": "/verify/taulib/docs/book-iv-strong-color-holonomy/color-quantization/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.ColorHolonomy`.",
  "declaration_id": "TauLib.BookIV.Strong.ColorHolonomy::ColorQuantization",
  "declaration_slug": "color-quantization",
  "kind": "structure",
  "name": "ColorQuantization",
  "module_name": "TauLib.BookIV.Strong.ColorHolonomy",
  "module_url": "/verify/taulib/docs/book-iv-strong-color-holonomy/",
  "source_line_start": 146,
  "source_line_end": 153,
  "registry_ids": [
    "IV.P89"
  ],
  "related_registry_items": [
    {
      "id": "IV.P89",
      "title": "Color Quantization",
      "url": "/registry/object/IV.P89/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/ColorHolonomy.lean#L146-L153",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/ColorHolonomy.lean#L146-L153",
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
- Source path: [`TauLib/BookIV/Strong/ColorHolonomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/ColorHolonomy.lean#L146-L153)
- Source range: L146-L153
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P89` — Color Quantization

## Immediate Comment / Docstring

```lean
/-- [IV.P89] Color charge is quantized: takes values in the discrete
    group Z/3Z because the compact eta-circle has discrete pi_1 = Z. -/
```

## Source Excerpt

```lean
structure ColorQuantization where
  /-- Group structure: Z/3Z. -/
  group : String := "Z/3Z"
  /-- Discrete (not continuous). -/
  discrete : Bool := true
  /-- Source: pi_1(S^1) = Z, then mod-3 projection. -/
  source : String := "pi_1(S^1) = Z with mod-3 projection at depth 3"
  deriving Repr
```
