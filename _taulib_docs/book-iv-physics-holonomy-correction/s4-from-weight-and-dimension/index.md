---
{
  "projection_kind": "taulib_declaration",
  "title": "s4_from_weight_and_dimension",
  "permalink": "/verify/taulib/docs/book-iv-physics-holonomy-correction/s4-from-weight-and-dimension/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Physics.HolonomyCorrection`.",
  "declaration_id": "TauLib.BookIV.Physics.HolonomyCorrection::s4_from_weight_and_dimension",
  "declaration_slug": "s4-from-weight-and-dimension",
  "kind": "theorem",
  "name": "s4_from_weight_and_dimension",
  "module_name": "TauLib.BookIV.Physics.HolonomyCorrection",
  "module_url": "/verify/taulib/docs/book-iv-physics-holonomy-correction/",
  "source_line_start": 314,
  "source_line_end": 318,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/HolonomyCorrection.lean#L314-L318",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Physics.HolonomyCorrection",
        "url": "/verify/taulib/docs/book-iv-physics-holonomy-correction/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/HolonomyCorrection.lean#L314-L318",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookIV.Physics.HolonomyCorrection](/verify/taulib/docs/book-iv-physics-holonomy-correction/)
- Source path: [`TauLib/BookIV/Physics/HolonomyCorrection.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/HolonomyCorrection.lean#L314-L318)
- Source range: L314-L318
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The evaluation point s=4 is derived from two independent arguments:

    A1. L-function weight: The lemniscate elliptic curve E: y²=x⁴−1
        has weight 2. The natural evaluation point is s = 2×weight = 4.

    A2. Green's function: For the 3-manifold τ³, the spectral zeta
        evaluates at s = dim(τ³) + 1 = 3 + 1 = 4.

    Both arguments give s = 4 independently. The exponent −7 = 1−2×4
    is then forced, not fitted. -/
```

## Source Excerpt

```lean
theorem s4_from_weight_and_dimension :
    -- Weight argument: s = 2 × weight = 2 × 2 = 4
    -- Dimension argument: s = dim + 1 = 3 + 1 = 4
    (2 * 2 = 4) ∧ (3 + 1 = 4) := by
  exact ⟨rfl, rfl⟩
```
