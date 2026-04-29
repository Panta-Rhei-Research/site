---
{
  "projection_kind": "taulib_declaration",
  "title": "PrimaryInvariant",
  "permalink": "/verify/taulib/docs/book-iv-physics-quantity-framework/primary-invariant/",
  "summary_short": "`inductive` declaration in `TauLib.BookIV.Physics.QuantityFramework`.",
  "declaration_id": "TauLib.BookIV.Physics.QuantityFramework::PrimaryInvariant",
  "declaration_slug": "primary-invariant",
  "kind": "inductive",
  "name": "PrimaryInvariant",
  "module_name": "TauLib.BookIV.Physics.QuantityFramework",
  "module_url": "/verify/taulib/docs/book-iv-physics-quantity-framework/",
  "source_line_start": 50,
  "source_line_end": 66,
  "registry_ids": [
    "IV.D09"
  ],
  "related_registry_items": [
    {
      "id": "IV.D09",
      "title": "Primary Invariant",
      "url": "/registry/object/IV.D09/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/QuantityFramework.lean#L50-L66",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Physics.QuantityFramework",
        "url": "/verify/taulib/docs/book-iv-physics-quantity-framework/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/QuantityFramework.lean#L50-L66",
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

- Module: [TauLib.BookIV.Physics.QuantityFramework](/verify/taulib/docs/book-iv-physics-quantity-framework/)
- Source path: [`TauLib/BookIV/Physics/QuantityFramework.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/QuantityFramework.lean#L50-L66)
- Source range: L50-L66
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `IV.D09` — Primary Invariant

## Immediate Comment / Docstring

```lean
/-- [IV.D09] The 5 primary physical invariants of the τ-framework.
    These exhaust the independent physical degrees of freedom;
    all other physical quantities are derived from these five. -/
```

## Source Excerpt

```lean
inductive PrimaryInvariant where
  /-- Coherence defect novelty measure: S = S_def + S_ref.
      S_def → 0 at coherence horizon; S_ref unbounded. -/
  | Entropy
  /-- Defect novelty event sequence parameter (ρ-iteration depth).
      Time emerges from defect dynamics ordering, NOT from spacetime. -/
  | Time
  /-- Coherence cost of maintaining localized defect bundle structure.
      Energy ∝ defect-tuple magnitude & stability degree. -/
  | Energy
  /-- Inertial invariant of persistent T² defect bundle.
      Mass = boundary-fixed-point of defect bundle's coherence functional. -/
  | Mass
  /-- Frame holonomy sector coupling (GR sector).
      Curvature = holonomy defect on frame transport. -/
  | Gravity
  deriving Repr, DecidableEq, BEq, Inhabited
```
