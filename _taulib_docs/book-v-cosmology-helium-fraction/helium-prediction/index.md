---
{
  "projection_kind": "taulib_declaration",
  "title": "HeliumPrediction",
  "permalink": "/verify/taulib/docs/book-v-cosmology-helium-fraction/helium-prediction/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.HeliumFraction`.",
  "declaration_id": "TauLib.BookV.Cosmology.HeliumFraction::HeliumPrediction",
  "declaration_slug": "helium-prediction",
  "kind": "structure",
  "name": "HeliumPrediction",
  "module_name": "TauLib.BookV.Cosmology.HeliumFraction",
  "module_url": "/verify/taulib/docs/book-v-cosmology-helium-fraction/",
  "source_line_start": 160,
  "source_line_end": 175,
  "registry_ids": [
    "V.D195"
  ],
  "related_registry_items": [
    {
      "id": "V.D195",
      "title": "Primordial He-4 Mass Fraction",
      "url": "/registry/object/V.D195/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/HeliumFraction.lean#L160-L175",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/HeliumFraction.lean#L160-L175",
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
- Source path: [`TauLib/BookV/Cosmology/HeliumFraction.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/HeliumFraction.lean#L160-L175)
- Source range: L160-L175
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D195` — Primordial He-4 Mass Fraction

## Immediate Comment / Docstring

```lean
/-- [V.D195] Primordial He-4 mass fraction Y_p = 20/81. -/
```

## Source Excerpt

```lean
structure HeliumPrediction where
  /-- Y_p numerator. -/
  yp_num : Nat := 20
  /-- Y_p denominator. -/
  yp_den : Nat := 81
  /-- Route A: (8 × 5) / (27 × 6) = 40/162 = 20/81. -/
  route_a_num : Nat := 8 * 5  -- = 40
  route_a_den : Nat := 27 * 6 -- = 162
  /-- Route B: (4 × 5) / 3⁴. -/
  route_b_num : Nat := 4 * 5  -- = 20
  route_b_den : Nat := 3 ^ 4  -- = 81
  /-- Route A reduces to 20/81. -/
  route_a_reduces : route_a_num / 2 = yp_num ∧ route_a_den / 2 = yp_den
  /-- Route B equals 20/81 directly. -/
  route_b_eq : route_b_num = yp_num ∧ route_b_den = yp_den
  deriving Repr
```
