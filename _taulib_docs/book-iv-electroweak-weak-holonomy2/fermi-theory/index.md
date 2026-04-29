---
{
  "projection_kind": "taulib_declaration",
  "title": "FermiTheory",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy2/fermi-theory/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.WeakHolonomy2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.WeakHolonomy2::FermiTheory",
  "declaration_slug": "fermi-theory",
  "kind": "structure",
  "name": "FermiTheory",
  "module_name": "TauLib.BookIV.Electroweak.WeakHolonomy2",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy2/",
  "source_line_start": 139,
  "source_line_end": 146,
  "registry_ids": [
    "IV.T57"
  ],
  "related_registry_items": [
    {
      "id": "IV.T57",
      "title": "Low-Energy Limit of W Exchange (Fermi Limit)",
      "url": "/registry/object/IV.T57/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L139-L146",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.WeakHolonomy2",
        "url": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy2/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L139-L146",
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

- Module: [TauLib.BookIV.Electroweak.WeakHolonomy2](/verify/taulib/docs/book-iv-electroweak-weak-holonomy2/)
- Source path: [`TauLib/BookIV/Electroweak/WeakHolonomy2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L139-L146)
- Source range: L139-L146
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T57` — Low-Energy Limit of W Exchange (Fermi Limit)

## Immediate Comment / Docstring

```lean
/-- [IV.T57] At energies far below M_W, the W propagator contracts
    to a point, producing the Fermi four-fermion contact interaction:
    L_Fermi = -(G_F/sqrt(2)) * (J_mu)^dagger * J^mu.
    Structural: Fermi theory is the E < M_W limit of W exchange. -/
```

## Source Excerpt

```lean
structure FermiTheory where
  /-- The energy scale is below M_W. -/
  energy_below_mw : Bool
  below_true : energy_below_mw = true
  /-- Contact interaction dimension (4-fermion = dim 6 operator). -/
  operator_dim : Nat
  dim_eq : operator_dim = 6
  deriving Repr
```
