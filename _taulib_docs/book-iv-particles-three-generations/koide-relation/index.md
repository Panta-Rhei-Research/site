---
{
  "projection_kind": "taulib_declaration",
  "title": "KoideRelation",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/koide-relation/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::KoideRelation",
  "declaration_slug": "koide-relation",
  "kind": "structure",
  "name": "KoideRelation",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 269,
  "source_line_end": 280,
  "registry_ids": [
    "IV.T84"
  ],
  "related_registry_items": [
    {
      "id": "IV.T84",
      "title": "Koide relation Q=2/3",
      "url": "/registry/object/IV.T84/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L269-L280",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.ThreeGenerations",
        "url": "/verify/taulib/docs/book-iv-particles-three-generations/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L269-L280",
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

- Module: [TauLib.BookIV.Particles.ThreeGenerations](/verify/taulib/docs/book-iv-particles-three-generations/)
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L269-L280)
- Source range: L269-L280
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T84` — Koide relation Q=2/3

## Immediate Comment / Docstring

```lean
/-- [IV.T84] The three charged lepton masses satisfy Q = 2/3 to all orders
    in the lemniscate topology.

    Proof uses ℤ/3ℤ symmetry of L's three sectors (crossing, lobe 1, lobe 2)
    with 120-degree democratic matrix spacing. Q = 2/3 is independent of mass
    scale or Koide phase. Deviation from exact 2/3 is O(α²) ≈ 5×10⁻⁵.

    Experimental: Q_exp = 0.666661 → Q_exp − 2/3 = −6×10⁻⁶. -/
```

## Source Excerpt

```lean
structure KoideRelation where
  /-- Predicted numerator. -/
  predicted_numer : Nat := 2
  /-- Predicted denominator. -/
  predicted_denom : Nat := 3
  /-- Symmetry group order. -/
  symmetry_order : Nat := 3
  /-- Democratic spacing (degrees). -/
  spacing_degrees : Nat := 120
  /-- Deviation order (α^n). -/
  deviation_order : Nat := 2
  deriving Repr
```
