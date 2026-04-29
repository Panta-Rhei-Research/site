---
{
  "projection_kind": "taulib_declaration",
  "title": "iota_power_factorization",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-exponent-derivation/iota-power-factorization/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.ExponentDerivation`.",
  "declaration_id": "TauLib.BookV.GravityField.ExponentDerivation::iota_power_factorization",
  "declaration_slug": "iota-power-factorization",
  "kind": "theorem",
  "name": "iota_power_factorization",
  "module_name": "TauLib.BookV.GravityField.ExponentDerivation",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-exponent-derivation/",
  "source_line_start": 239,
  "source_line_end": 269,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/ExponentDerivation.lean#L239-L269",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.ExponentDerivation",
        "url": "/verify/taulib/docs/book-v-gravity-field-exponent-derivation/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/ExponentDerivation.lean#L239-L269",
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

- Module: [TauLib.BookV.GravityField.ExponentDerivation](/verify/taulib/docs/book-v-gravity-field-exponent-derivation/)
- Source path: [`TauLib/BookV/GravityField/ExponentDerivation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/ExponentDerivation.lean#L239-L269)
- Source range: L239-L269
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- 72 = 2³ × 3² (prime factorization). -/
```

## Source Excerpt

```lean
theorem iota_power_factorization : 72 = 2^3 * 3^2 := by omega

-- ============================================================
-- SYNTHESIS: OQ.03 RESOLUTION
-- ============================================================

/-!
## OQ.03 Resolution

**Before:** PARTIALLY RESOLVED — three independent arguments select 18
  but no single proof derives it from topology alone.

**After:** τ-EFFECTIVE — the exponent 18 is the product of three
  independently determined τ³ structural invariants:

  18 = b₁(T²) × dim(τ³) × |{π,γ,η}| = 2 × 3 × 3

  Each factor is:
  - **b₁(T²) = 2**: verified against `canonical_coupling.tree_factor`
    (double appearance in κ_n = 2√3 and exponent)
  - **dim(τ³) = 3**: verified against `triple_holonomy.circle_count`
    (double appearance in π³ holonomy and exponent)
  - **|solenoidal| = 3**: verified against `solenoidalGenerators.length`
    (kernel definition in Diagonal.lean)

  The three cross-verifications against existing Lean structures prove
  the decomposition is not ad hoc: each factor was already formalized
  for a different purpose before this sprint.

  **Status:** OQ.03 → τ-EFFECTIVE (upgraded from PARTIALLY RESOLVED)
-/
```
