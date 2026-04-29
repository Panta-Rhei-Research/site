---
{
  "projection_kind": "taulib_declaration",
  "title": "EquationLayer",
  "permalink": "/verify/taulib/docs/book-iv-physics-internal-equations/equation-layer/",
  "summary_short": "`inductive` declaration in `TauLib.BookIV.Physics.InternalEquations`.",
  "declaration_id": "TauLib.BookIV.Physics.InternalEquations::EquationLayer",
  "declaration_slug": "equation-layer",
  "kind": "inductive",
  "name": "EquationLayer",
  "module_name": "TauLib.BookIV.Physics.InternalEquations",
  "module_url": "/verify/taulib/docs/book-iv-physics-internal-equations/",
  "source_line_start": 55,
  "source_line_end": 69,
  "registry_ids": [
    "IV.D324"
  ],
  "related_registry_items": [
    {
      "id": "IV.D324",
      "title": "Equation Layer",
      "url": "/registry/object/IV.D324/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/InternalEquations.lean#L55-L69",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Physics.InternalEquations",
        "url": "/verify/taulib/docs/book-iv-physics-internal-equations/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/InternalEquations.lean#L55-L69",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
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

- Module: [TauLib.BookIV.Physics.InternalEquations](/verify/taulib/docs/book-iv-physics-internal-equations/)
- Source path: [`TauLib/BookIV/Physics/InternalEquations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/InternalEquations.lean#L55-L69)
- Source range: L55-L69
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `IV.D324` — Equation Layer

## Immediate Comment / Docstring

```lean
/-- [IV.D324] The ontological layer at which an equation lives.
    Layer discipline: every equation belongs to exactly one layer. -/
```

## Source Excerpt

```lean
inductive EquationLayer where
  /-- Layer 0: Pure mathematics. Category theory, algebra, analysis.
      No physics semantics, no units, no measurement concept.
      Examples: axioms K0-K6, Central Theorem, Epstein zeta identity. -/
  | MathKernel
  /-- Layer 1: Internal physics. Sector-enriched H_∂[ω].
      Quantities are tick counts, equations are morphisms.
      ALL dimensionless. No SI, no measurement concept.
      Examples: R₀ as η-step ratio, α as γ-oscillation self-coupling. -/
  | InternalPhysics
  /-- Layer 2: SI bridge. Readout functor R_μ images.
      Domain: Layer 1 objects. Codomain: measurement procedures.
      Examples: m_e = 9.109×10⁻³¹ kg, α⁻¹ ≈ 137.036. -/
  | SIBridge
  deriving Repr, DecidableEq, BEq, Inhabited
```
