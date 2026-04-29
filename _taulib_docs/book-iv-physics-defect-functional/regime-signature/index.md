---
{
  "projection_kind": "taulib_declaration",
  "title": "RegimeSignature",
  "permalink": "/verify/taulib/docs/book-iv-physics-defect-functional/regime-signature/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Physics.DefectFunctional`.",
  "declaration_id": "TauLib.BookIV.Physics.DefectFunctional::RegimeSignature",
  "declaration_slug": "regime-signature",
  "kind": "structure",
  "name": "RegimeSignature",
  "module_name": "TauLib.BookIV.Physics.DefectFunctional",
  "module_url": "/verify/taulib/docs/book-iv-physics-defect-functional/",
  "source_line_start": 139,
  "source_line_end": 154,
  "registry_ids": [
    "IV.D19"
  ],
  "related_registry_items": [
    {
      "id": "IV.D19",
      "title": "Regime Signature",
      "url": "/registry/object/IV.D19/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/DefectFunctional.lean#L139-L154",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Physics.DefectFunctional",
        "url": "/verify/taulib/docs/book-iv-physics-defect-functional/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/DefectFunctional.lean#L139-L154",
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

- Module: [TauLib.BookIV.Physics.DefectFunctional](/verify/taulib/docs/book-iv-physics-defect-functional/)
- Source path: [`TauLib/BookIV/Physics/DefectFunctional.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/DefectFunctional.lean#L139-L154)
- Source range: L139-L154
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D19` — Regime Signature

## Immediate Comment / Docstring

```lean
/-- [IV.D19] Regime signature: the structural properties that
    distinguish each fluid regime.

    Each regime is characterized by a combination of boolean flags
    and optional bounds on defect components. -/
```

## Source Excerpt

```lean
structure RegimeSignature where
  /-- Which regime this signature describes. -/
  regime : FluidRegime
  /-- Upper bound on mobility (Some k = mobility ≤ k, None = no bound). -/
  mobility_bound : Option Nat
  /-- Whether Kelvin circulation invariant holds (∮ u·dl conserved). -/
  kelvin_invariant : Bool
  /-- Whether energy dissipation is present. -/
  dissipation : Bool
  /-- Whether coupled to EM holonomy sector. -/
  em_coupled : Bool
  /-- Whether circulation is quantized (hard lattice constraint). -/
  quantized_circulation : Bool
  /-- Whether compression defect must vanish (incompressibility). -/
  incompressible : Bool
  deriving Repr
```
