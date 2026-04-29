---
{
  "projection_kind": "taulib_declaration",
  "title": "SU3GaugeAlgebra",
  "permalink": "/verify/taulib/docs/book-iv-strong-color-holonomy/su3-gauge-algebra/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.ColorHolonomy`.",
  "declaration_id": "TauLib.BookIV.Strong.ColorHolonomy::SU3GaugeAlgebra",
  "declaration_slug": "su3-gauge-algebra",
  "kind": "structure",
  "name": "SU3GaugeAlgebra",
  "module_name": "TauLib.BookIV.Strong.ColorHolonomy",
  "module_url": "/verify/taulib/docs/book-iv-strong-color-holonomy/",
  "source_line_start": 217,
  "source_line_end": 228,
  "registry_ids": [
    "IV.T69"
  ],
  "related_registry_items": [
    {
      "id": "IV.T69",
      "title": "SU(3) Gauge Algebra",
      "url": "/registry/object/IV.T69/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/ColorHolonomy.lean#L217-L228",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/ColorHolonomy.lean#L217-L228",
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
- Source path: [`TauLib/BookIV/Strong/ColorHolonomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/ColorHolonomy.lean#L217-L228)
- Source range: L217-L228
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T69` — SU(3) Gauge Algebra

## Immediate Comment / Docstring

```lean
/-- [IV.T69] The gauge algebra of the strong sector is isomorphic to su(3).
    Forced by three structural constraints:
    1. Chi_minus-dominant polarity (non-abelian)
    2. Primorial depth 3 (three color classes, rank 2)
    3. Color-neutral vacuum (traceless: U(3) -> SU(3))

    Dimension: 3^2 - 1 = 8 generators (the 8 gluon types). -/
```

## Source Excerpt

```lean
structure SU3GaugeAlgebra where
  /-- Lie algebra dimension: N_c^2 - 1. -/
  dimension : Nat := 8
  /-- Number of colors N_c. -/
  num_colors : Nat := 3
  /-- Rank of the algebra. -/
  rank : Nat := 2
  /-- The three forcing constraints. -/
  constraint_1 : String := "chi_minus-dominant => non-abelian"
  constraint_2 : String := "depth-3 => three colors, rank 2"
  constraint_3 : String := "color-neutral vacuum => traceless (SU not U)"
  deriving Repr
```
