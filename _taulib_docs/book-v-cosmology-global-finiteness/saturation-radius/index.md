---
{
  "projection_kind": "taulib_declaration",
  "title": "SaturationRadius",
  "permalink": "/verify/taulib/docs/book-v-cosmology-global-finiteness/saturation-radius/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.GlobalFiniteness`.",
  "declaration_id": "TauLib.BookV.Cosmology.GlobalFiniteness::SaturationRadius",
  "declaration_slug": "saturation-radius",
  "kind": "structure",
  "name": "SaturationRadius",
  "module_name": "TauLib.BookV.Cosmology.GlobalFiniteness",
  "module_url": "/verify/taulib/docs/book-v-cosmology-global-finiteness/",
  "source_line_start": 162,
  "source_line_end": 171,
  "registry_ids": [
    "V.D179"
  ],
  "related_registry_items": [
    {
      "id": "V.D179",
      "title": "Saturation radius",
      "url": "/registry/object/V.D179/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/GlobalFiniteness.lean#L162-L171",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.GlobalFiniteness",
        "url": "/verify/taulib/docs/book-v-cosmology-global-finiteness/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/GlobalFiniteness.lean#L162-L171",
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

- Module: [TauLib.BookV.Cosmology.GlobalFiniteness](/verify/taulib/docs/book-v-cosmology-global-finiteness/)
- Source path: [`TauLib/BookV/Cosmology/GlobalFiniteness.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/GlobalFiniteness.lean#L162-L171)
- Source range: L162-L171
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D179` — Saturation radius

## Immediate Comment / Docstring

```lean
/-- [V.D179] Saturation radius R_sat: the smallest length scale such
    that every eternal motif appearing anywhere in τ³ already appears
    within a ball of radius R_sat.

    R_sat is finite because:
    1. The motif count is finite (V.T116)
    2. τ¹ is compact with finite circumference
    3. Motifs distribute uniformly in the long run -/
```

## Source Excerpt

```lean
structure SaturationRadius where
  /-- Radius numerator (in natural units). -/
  radius_numer : Nat
  /-- Radius denominator. -/
  radius_denom : Nat
  /-- Denominator positive. -/
  denom_pos : radius_denom > 0
  /-- Radius is finite (bounded above). -/
  finite : radius_numer > 0
  deriving Repr
```
