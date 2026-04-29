---
{
  "projection_kind": "taulib_declaration",
  "title": "ParticleKind",
  "permalink": "/verify/taulib/docs/book-iv-physics-quantity-framework/particle-kind/",
  "summary_short": "`inductive` declaration in `TauLib.BookIV.Physics.QuantityFramework`.",
  "declaration_id": "TauLib.BookIV.Physics.QuantityFramework::ParticleKind",
  "declaration_slug": "particle-kind",
  "kind": "inductive",
  "name": "ParticleKind",
  "module_name": "TauLib.BookIV.Physics.QuantityFramework",
  "module_url": "/verify/taulib/docs/book-iv-physics-quantity-framework/",
  "source_line_start": 111,
  "source_line_end": 121,
  "registry_ids": [
    "IV.D12"
  ],
  "related_registry_items": [
    {
      "id": "IV.D12",
      "title": "Particle Kind",
      "url": "/registry/object/IV.D12/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/QuantityFramework.lean#L111-L121",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/QuantityFramework.lean#L111-L121",
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
- Source path: [`TauLib/BookIV/Physics/QuantityFramework.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/QuantityFramework.lean#L111-L121)
- Source range: L111-L121
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `IV.D12` — Particle Kind

## Immediate Comment / Docstring

```lean
/-- [IV.D12] Particle classification in the τ-framework.
    The τ-kernel distinguishes three kinds of carriers. -/
```

## Source Excerpt

```lean
inductive ParticleKind where
  /-- Persistent localized defect bundle with stable T² fiber.
      Example: neutron (first ontic particle = minimal mass-bearing config). -/
  | Ontic
  /-- Null transport along τ¹ with degenerate S¹ fiber (not T²).
      Example: photon (null transport with degenerate circular fiber). -/
  | Radiation
  /-- Intermediate exchange carrier (not persistent).
      Example: virtual photon in Feynman diagrams. -/
  | Virtual
  deriving Repr, DecidableEq, BEq, Inhabited
```
