---
{
  "projection_kind": "taulib_declaration",
  "title": "IsingHamiltonian",
  "permalink": "/verify/taulib/docs/book-iv-many-body-magnetism/ising-hamiltonian/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.ManyBody.Magnetism`.",
  "declaration_id": "TauLib.BookIV.ManyBody.Magnetism::IsingHamiltonian",
  "declaration_slug": "ising-hamiltonian",
  "kind": "structure",
  "name": "IsingHamiltonian",
  "module_name": "TauLib.BookIV.ManyBody.Magnetism",
  "module_url": "/verify/taulib/docs/book-iv-many-body-magnetism/",
  "source_line_start": 73,
  "source_line_end": 82,
  "registry_ids": [
    "IV.D388"
  ],
  "related_registry_items": [
    {
      "id": "IV.D388",
      "title": "τ-Ising Hamiltonian on T²",
      "url": "/registry/object/IV.D388/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/Magnetism.lean#L73-L82",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.ManyBody.Magnetism",
        "url": "/verify/taulib/docs/book-iv-many-body-magnetism/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/Magnetism.lean#L73-L82",
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

- Module: [TauLib.BookIV.ManyBody.Magnetism](/verify/taulib/docs/book-iv-many-body-magnetism/)
- Source path: [`TauLib/BookIV/ManyBody/Magnetism.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/Magnetism.lean#L73-L82)
- Source range: L73-L82
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D388` — τ-Ising Hamiltonian on T²

## Immediate Comment / Docstring

```lean
/-- [IV.D388] The τ-Ising Hamiltonian on a finite lattice Λ ⊂ T²:
    H = -J Σ_{⟨i,j⟩} σ_i σ_j - h Σ_i σ_i
    with periodic boundary conditions enforced by T² topology.
    J > 0 favors alignment (ferromagnetic), σ_i ∈ {-1, +1}. -/
```

## Source Excerpt

```lean
structure IsingHamiltonian where
  /-- Exchange coupling J > 0. -/
  exchange_positive : Bool := true
  /-- Spins take values ±1. -/
  spin_values : List Int := [-1, 1]
  /-- Periodic BCs from T² topology. -/
  periodic_from_torus : Bool := true
  /-- No edges on T² — every site has same coordination number. -/
  uniform_coordination : Bool := true
  deriving Repr
```
