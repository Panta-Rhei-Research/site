---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L47",
  "permalink": "/verify/taulib/docs/tour-foundations/eval-l47/",
  "summary_short": "`eval` declaration in `TauLib.Tour.Foundations`.",
  "declaration_id": "TauLib.Tour.Foundations::#eval:47",
  "declaration_slug": "eval-l47",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.Tour.Foundations",
  "module_url": "/verify/taulib/docs/tour-foundations/",
  "source_line_start": 47,
  "source_line_end": 108,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/Foundations.lean#L47-L108",
  "formal_status": "computed",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.Tour.Foundations",
        "url": "/verify/taulib/docs/tour-foundations/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/Foundations.lean#L47-L108",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "eval",
      "status": "computed"
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

- Module: [TauLib.Tour.Foundations](/verify/taulib/docs/tour-foundations/)
- Source path: [`TauLib/Tour/Foundations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/Foundations.lean#L47-L108)
- Source range: L47-L108
- Kind: `eval`
- Formal status hint: `computed`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
No immediate Lean doc/comment block was detected for this declaration.
```

## Source Excerpt

```lean
#eval Generator.omega.toNat  -- 4

-- There are exactly five. No more, no fewer.
-- (The `Generator` inductive has exactly 5 constructors.)

-- ================================================================
-- PART 2: THE SIX AXIOMS (K1–K6)
-- ================================================================

-- K0 (Universe Postulate) is implicit in Lean's type system:
-- declaring `Generator : Type` and `TauObj : Type` postulates
-- the universe of discourse.

-- K1: Strict Order — the five generators are strictly ordered.
#check @K1_strict_order

-- K2: Omega Fixed Point — ρ(ω) = ω at every depth. ω is the
-- unique element that the iterator cannot move.
#check @K2_omega_fixed

-- K3: Orbit-Seeded Generation — applying ρ to any non-ω generator g
-- produces an object seeded by g. This generates the orbit rays.
#check @K3_orbit_seeded

-- K4: No-Jump (Cover) — ρ advances depth by exactly 1. No skipping.
#check @K4_no_jump

-- K5: Beacon Non-Successor — ω is never reached by iterating ρ.
-- It stands outside all orbit rays as the fixed-point beacon.
#check @K5_beacon_non_succ

-- K6: Object Closure — every TauObj is either a generator or ρ-generated.
-- Nothing exists outside the axioms.
#check @K6_object_closure

-- ================================================================
-- PART 3: THE ρ OPERATOR AND ORBIT RAYS
-- ================================================================

-- ρ is the sole primitive operator. It maps TauObj → TauObj.
-- On non-ω objects, it advances depth by 1 (K4).
-- On ω, it returns ω (K2).

#check @rho  -- TauObj → TauObj

-- Starting from generator α and iterating ρ, we get the orbit ray O_α:
--   α, ρ(α), ρ²(α), ρ³(α), ...
-- This infinite sequence becomes τ-Idx — the internal natural numbers.

-- The four orbit rays (from α, π, γ, η) are pairwise disjoint:
#check @orbit_disjoint

-- ω sits alone as a fixed point, outside all rays.

-- ================================================================
-- PART 4: τ-IDX — INTERNAL NATURAL NUMBERS
-- ================================================================

-- TauIdx is Nat — but earned from the orbit ray O_α, not postulated.
-- The natural numbers are a *consequence* of the axioms, not an input.

#check TauIdx  -- = Nat (but with internal meaning)
```
