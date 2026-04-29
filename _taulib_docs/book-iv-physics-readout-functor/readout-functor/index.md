---
{
  "projection_kind": "taulib_declaration",
  "title": "ReadoutFunctor",
  "permalink": "/verify/taulib/docs/book-iv-physics-readout-functor/readout-functor/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Physics.ReadoutFunctor`.",
  "declaration_id": "TauLib.BookIV.Physics.ReadoutFunctor::ReadoutFunctor",
  "declaration_slug": "readout-functor",
  "kind": "structure",
  "name": "ReadoutFunctor",
  "module_name": "TauLib.BookIV.Physics.ReadoutFunctor",
  "module_url": "/verify/taulib/docs/book-iv-physics-readout-functor/",
  "source_line_start": 101,
  "source_line_end": 114,
  "registry_ids": [
    "IV.D326"
  ],
  "related_registry_items": [
    {
      "id": "IV.D326",
      "title": "Readout Functor",
      "url": "/registry/object/IV.D326/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/ReadoutFunctor.lean#L101-L114",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Physics.ReadoutFunctor",
        "url": "/verify/taulib/docs/book-iv-physics-readout-functor/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/ReadoutFunctor.lean#L101-L114",
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

- Module: [TauLib.BookIV.Physics.ReadoutFunctor](/verify/taulib/docs/book-iv-physics-readout-functor/)
- Source path: [`TauLib/BookIV/Physics/ReadoutFunctor.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/ReadoutFunctor.lean#L101-L114)
- Source range: L101-L114
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D326` — Readout Functor

## Immediate Comment / Docstring

```lean
/-- [IV.D326] The readout functor R_μ.

    Domain: Internal categorical objects in H_∂[ω] (Layer 1).
    Codomain: Operational measurement procedures (Layer 2).

    Properties:
    - Preserves internal identities (a homomorphism, not a lossy projection)
    - Has a single empirical anchor (m_n)
    - Uses exactly 4 exact SI defining constants (c, h, e, k_B)
    - Every other SI value is DERIVED, not independently measured -/
```

## Source Excerpt

```lean
structure ReadoutFunctor where
  /-- Number of independent empirical inputs (must be 1 = m_n). -/
  num_anchors : Nat
  /-- The anchor count is exactly 1. -/
  single_anchor : num_anchors = 1
  /-- Number of exact SI defining constants used. -/
  num_exact_si : Nat
  /-- Exactly 4 exact SI constants (c, h, e, k_B). -/
  four_exact : num_exact_si = 4
  /-- R_μ preserves internal identities (is a functor, not just a function). -/
  preserves_identities : Bool
  /-- Identity preservation is true. -/
  preserves_true : preserves_identities = true
  deriving Repr
```
