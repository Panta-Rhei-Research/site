---
{
  "projection_kind": "taulib_declaration",
  "title": "WilsonLoopDef",
  "permalink": "/verify/taulib/docs/book-iv-strong-color-holonomy/wilson-loop-def/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.ColorHolonomy`.",
  "declaration_id": "TauLib.BookIV.Strong.ColorHolonomy::WilsonLoopDef",
  "declaration_slug": "wilson-loop-def",
  "kind": "structure",
  "name": "WilsonLoopDef",
  "module_name": "TauLib.BookIV.Strong.ColorHolonomy",
  "module_url": "/verify/taulib/docs/book-iv-strong-color-holonomy/",
  "source_line_start": 310,
  "source_line_end": 318,
  "registry_ids": [
    "IV.D157"
  ],
  "related_registry_items": [
    {
      "id": "IV.D157",
      "title": "Wilson Loop",
      "url": "/registry/object/IV.D157/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/ColorHolonomy.lean#L310-L318",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/ColorHolonomy.lean#L310-L318",
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
- Source path: [`TauLib/BookIV/Strong/ColorHolonomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/ColorHolonomy.lean#L310-L318)
- Source range: L310-L318
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D157` — Wilson Loop

## Immediate Comment / Docstring

```lean
/-- [IV.D157] Wilson loop W(gamma) = (1/3) Tr U(gamma):
    gauge-invariant trace of holonomy around a closed path.
    Area-law decay signals confinement; perimeter-law signals deconfinement. -/
```

## Source Excerpt

```lean
structure WilsonLoopDef where
  /-- Normalization factor: 1/N_c. -/
  normalization_numer : Nat := 1
  normalization_denom : Nat := 3
  /-- Order parameter for confinement. -/
  is_order_parameter : Bool := true
  /-- Area law implies confinement. -/
  area_law_implies_confinement : Bool := true
  deriving Repr
```
