---
{
  "projection_kind": "taulib_declaration",
  "title": "WeinbergAngle",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy2/weinberg-angle/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.WeakHolonomy2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.WeakHolonomy2::WeinbergAngle",
  "declaration_slug": "weinberg-angle",
  "kind": "structure",
  "name": "WeinbergAngle",
  "module_name": "TauLib.BookIV.Electroweak.WeakHolonomy2",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy2/",
  "source_line_start": 42,
  "source_line_end": 50,
  "registry_ids": [
    "IV.D121"
  ],
  "related_registry_items": [
    {
      "id": "IV.D121",
      "title": "Weinberg Angle from Tau-Couplings",
      "url": "/registry/object/IV.D121/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L42-L50",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L42-L50",
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
- Source path: [`TauLib/BookIV/Electroweak/WeakHolonomy2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L42-L50)
- Source range: L42-L50
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D121` — Weinberg Angle from Tau-Couplings

## Immediate Comment / Docstring

```lean
/-- [IV.D121] Weinberg angle theta_W: the mixing angle between the
    neutral A-sector and B-sector gauge bosons. Determines how the
    W3 and B (hypercharge) bosons mix to produce Z and photon.
    sin^2(theta_W) = 0.2312 (PDG 2022). -/
```

## Source Excerpt

```lean
structure WeinbergAngle where
  /-- sin^2(theta_W) numerator (scaled to 10000). -/
  sin2_numer : Nat
  /-- sin^2(theta_W) denominator. -/
  sin2_denom : Nat
  denom_pos : sin2_denom > 0
  /-- sin^2 is between 0 and 1. -/
  bounded : sin2_numer ≤ sin2_denom
  deriving Repr
```
