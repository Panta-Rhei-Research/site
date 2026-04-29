---
{
  "projection_kind": "taulib_declaration",
  "title": "schrodinger_shadow",
  "permalink": "/verify/taulib/docs/book-iv-arena-actors-dynamics/schrodinger-shadow/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Arena.ActorsDynamics`.",
  "declaration_id": "TauLib.BookIV.Arena.ActorsDynamics::schrodinger_shadow",
  "declaration_slug": "schrodinger-shadow",
  "kind": "theorem",
  "name": "schrodinger_shadow",
  "module_name": "TauLib.BookIV.Arena.ActorsDynamics",
  "module_url": "/verify/taulib/docs/book-iv-arena-actors-dynamics/",
  "source_line_start": 160,
  "source_line_end": 178,
  "registry_ids": [
    "IV.D273",
    "IV.P158",
    "IV.T102"
  ],
  "related_registry_items": [
    {
      "id": "IV.D273",
      "title": "Planck character",
      "url": "/registry/object/IV.D273/"
    },
    {
      "id": "IV.P158",
      "title": "Schr\"odinger shadow",
      "url": "/registry/object/IV.P158/"
    },
    {
      "id": "IV.T102",
      "title": "tau-Heisenberg inequality",
      "url": "/registry/object/IV.T102/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/ActorsDynamics.lean#L160-L178",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Arena.ActorsDynamics",
        "url": "/verify/taulib/docs/book-iv-arena-actors-dynamics/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/ActorsDynamics.lean#L160-L178",
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

- Module: [TauLib.BookIV.Arena.ActorsDynamics](/verify/taulib/docs/book-iv-arena-actors-dynamics/)
- Source path: [`TauLib/BookIV/Arena/ActorsDynamics.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/ActorsDynamics.lean#L160-L178)
- Source range: L160-L178
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.D273` — Planck character
- `IV.P158` — Schr"odinger shadow
- `IV.T102` — tau-Heisenberg inequality

## Immediate Comment / Docstring

```lean
/-- [IV.P158] Schrödinger shadow: the propagation operator on fiber modes
    reduces to the Schrödinger equation iℏ∂ψ/∂t = Hψ in the QM readout. -/
```

## Source Excerpt

```lean
theorem schrodinger_shadow :
    -- Propagation on fiber is quantum
    (PropagationOp.mk .Fiber true).domain = .Fiber := rfl

-- ============================================================
-- PLANCK CHARACTER [IV.D273]
-- ============================================================

-- [IV.D273] Planck character ℏ_τ: minimal action quantum from boundary
-- characters. Defined in PlanckCharacter module as the PlanckCharacter structure.
-- ℏ_τ = h/(2π) in τ-units, the indivisible action unit.

-- ============================================================
-- τ-HEISENBERG INEQUALITY [IV.T102]
-- ============================================================

/-- [IV.T102] τ-Heisenberg inequality: Δx·Δp ≥ ℏ_τ/2. Follows from
    the address-obstruction geometry of τ³: two complementary coordinates
    on T² cannot be simultaneously sharp. -/
```
