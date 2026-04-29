---
{
  "projection_kind": "taulib_declaration",
  "title": "RhoParameter",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy2/rho-parameter/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.WeakHolonomy2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.WeakHolonomy2::RhoParameter",
  "declaration_slug": "rho-parameter",
  "kind": "structure",
  "name": "RhoParameter",
  "module_name": "TauLib.BookIV.Electroweak.WeakHolonomy2",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy2/",
  "source_line_start": 81,
  "source_line_end": 87,
  "registry_ids": [
    "IV.D123"
  ],
  "related_registry_items": [
    {
      "id": "IV.D123",
      "title": "The Rho Parameter",
      "url": "/registry/object/IV.D123/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L81-L87",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L81-L87",
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
- Source path: [`TauLib/BookIV/Electroweak/WeakHolonomy2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L81-L87)
- Source range: L81-L87
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D123` — The Rho Parameter

## Immediate Comment / Docstring

```lean
/-- [IV.D123] Rho parameter: rho = M_W^2 / (M_Z^2 * cos^2(theta_W)).
    At tree level, rho = 1 exactly (SU(2) custodial symmetry).
    Deviations from 1 measure radiative corrections. -/
```

## Source Excerpt

```lean
structure RhoParameter where
  /-- Rho numerator (scaled to 10000). -/
  numer : Nat
  /-- Rho denominator. -/
  denom : Nat
  denom_pos : denom > 0
  deriving Repr
```
