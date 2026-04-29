---
{
  "projection_kind": "taulib_declaration",
  "title": "HePacking",
  "permalink": "/verify/taulib/docs/book-v-cosmology-helium-fraction/he-packing/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.HeliumFraction`.",
  "declaration_id": "TauLib.BookV.Cosmology.HeliumFraction::HePacking",
  "declaration_slug": "he-packing",
  "kind": "structure",
  "name": "HePacking",
  "module_name": "TauLib.BookV.Cosmology.HeliumFraction",
  "module_url": "/verify/taulib/docs/book-v-cosmology-helium-fraction/",
  "source_line_start": 66,
  "source_line_end": 81,
  "registry_ids": [
    "V.D192"
  ],
  "related_registry_items": [
    {
      "id": "V.D192",
      "title": "He-4 Packing Maximum",
      "url": "/registry/object/V.D192/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/HeliumFraction.lean#L66-L81",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.HeliumFraction",
        "url": "/verify/taulib/docs/book-v-cosmology-helium-fraction/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/HeliumFraction.lean#L66-L81",
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

- Module: [TauLib.BookV.Cosmology.HeliumFraction](/verify/taulib/docs/book-v-cosmology-helium-fraction/)
- Source path: [`TauLib/BookV/Cosmology/HeliumFraction.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/HeliumFraction.lean#L66-L81)
- Source range: L66-L81
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D192` — He-4 Packing Maximum

## Immediate Comment / Docstring

```lean
/-- [V.D192] He-4 packing maximum: 2×2×2 blocks in 3×3×3 macrocells.
    Packing fraction = 8/27. -/
```

## Source Excerpt

```lean
structure HePacking where
  /-- Block size per axis. -/
  block_side : Nat := 2
  /-- Macrocell size per axis. -/
  macro_side : Nat := 3
  /-- Numerator of packing fraction. -/
  pack_num : Nat := 8
  /-- Denominator of packing fraction. -/
  pack_den : Nat := 27
  /-- Block volume = block_side³. -/
  block_vol : block_side ^ 3 = pack_num
  /-- Macrocell volume = macro_side³. -/
  macro_vol : macro_side ^ 3 = pack_den
  /-- Stride = block_side + 1 = macro_side. -/
  stride_eq : block_side + 1 = macro_side
  deriving Repr
```
