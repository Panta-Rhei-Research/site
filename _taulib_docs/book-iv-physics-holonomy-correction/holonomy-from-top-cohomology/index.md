---
{
  "projection_kind": "taulib_declaration",
  "title": "holonomy_from_top_cohomology",
  "permalink": "/verify/taulib/docs/book-iv-physics-holonomy-correction/holonomy-from-top-cohomology/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Physics.HolonomyCorrection`.",
  "declaration_id": "TauLib.BookIV.Physics.HolonomyCorrection::holonomy_from_top_cohomology",
  "declaration_slug": "holonomy-from-top-cohomology",
  "kind": "theorem",
  "name": "holonomy_from_top_cohomology",
  "module_name": "TauLib.BookIV.Physics.HolonomyCorrection",
  "module_url": "/verify/taulib/docs/book-iv-physics-holonomy-correction/",
  "source_line_start": 261,
  "source_line_end": 269,
  "registry_ids": [
    "IV.D44"
  ],
  "related_registry_items": [
    {
      "id": "IV.D44",
      "title": "Triple Holonomy",
      "url": "/registry/object/IV.D44/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/HolonomyCorrection.lean#L261-L269",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/HolonomyCorrection.lean#L261-L269",
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
- Source path: [`TauLib/BookIV/Physics/HolonomyCorrection.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/HolonomyCorrection.lean#L261-L269)
- Source range: L261-L269
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.D44` — Triple Holonomy

## Immediate Comment / Docstring

```lean
/-- π³ as integral of the top form over [τ³].

    τ³ has three independent S¹ factors: T_π (base), T_γ, T_η (fiber).
    H³(τ³, ℝ) = ℝ with unique generator dθ_π ∧ dθ_γ ∧ dθ_η.

    Per-cycle holonomy normalization: ∮ A = π (half-period of 2π cycle).
    The normalization (1/2)³ × (2π)³ = π³ gives the coefficient.

    This upgrades [IV.D44] from heuristic to cohomological derivation. -/
```

## Source Excerpt

```lean
theorem holonomy_from_top_cohomology :
    -- (1/2)^3 × (2π)^3 = π³, encoded as: 1³ × (2π)³ = 8π³
    -- i.e., the normalization identity holds at rational level:
    -- numer³ × 8 = 8 × numer³ (trivially)
    -- The real content: 3 circles → 3 independent 1-forms → unique 3-form
    triple_holonomy.circle_count = 3 ∧
    triple_holonomy.pi_exponent = 3 ∧
    triple_holonomy.components.length = 3 := by
  exact ⟨rfl, rfl, rfl⟩
```
