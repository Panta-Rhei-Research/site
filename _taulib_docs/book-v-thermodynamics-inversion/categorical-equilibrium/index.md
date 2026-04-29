---
{
  "projection_kind": "taulib_declaration",
  "title": "CategoricalEquilibrium",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-inversion/categorical-equilibrium/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Thermodynamics.Inversion`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.Inversion::CategoricalEquilibrium",
  "declaration_slug": "categorical-equilibrium",
  "kind": "structure",
  "name": "CategoricalEquilibrium",
  "module_name": "TauLib.BookV.Thermodynamics.Inversion",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-inversion/",
  "source_line_start": 119,
  "source_line_end": 126,
  "registry_ids": [
    "V.D83"
  ],
  "related_registry_items": [
    {
      "id": "V.D83",
      "title": "Thermodynamic equilibrium---categorical",
      "url": "/registry/object/V.D83/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/Inversion.lean#L119-L126",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Thermodynamics.Inversion",
        "url": "/verify/taulib/docs/book-v-thermodynamics-inversion/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/Inversion.lean#L119-L126",
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

- Module: [TauLib.BookV.Thermodynamics.Inversion](/verify/taulib/docs/book-v-thermodynamics-inversion/)
- Source path: [`TauLib/BookV/Thermodynamics/Inversion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/Inversion.lean#L119-L126)
- Source range: L119-L126
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D83` — Thermodynamic equilibrium---categorical

## Immediate Comment / Docstring

```lean
/-- [V.D83] Categorical thermodynamic equilibrium: a configuration
    with vanishing defect entropy (S_def = 0), meaning all holomorphic
    continuations are structurally trivial.

    This differs from classical thermal equilibrium (maximal disorder):
    categorical equilibrium is MINIMAL disorder, not maximal. -/
```

## Source Excerpt

```lean
structure CategoricalEquilibrium where
  /-- Defect entropy at equilibrium (zero). -/
  s_def : Nat := 0
  /-- Equilibrium means zero defect entropy. -/
  is_equilibrium : s_def = 0 := by rfl
  /-- Post-equilibrium evolution is defect-free circulation. -/
  is_circulation : Bool := true
  deriving Repr
```
