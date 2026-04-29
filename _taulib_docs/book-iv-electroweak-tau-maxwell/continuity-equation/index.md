---
{
  "projection_kind": "taulib_declaration",
  "title": "ContinuityEquation",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/continuity-equation/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.TauMaxwell`.",
  "declaration_id": "TauLib.BookIV.Electroweak.TauMaxwell::ContinuityEquation",
  "declaration_slug": "continuity-equation",
  "kind": "structure",
  "name": "ContinuityEquation",
  "module_name": "TauLib.BookIV.Electroweak.TauMaxwell",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/",
  "source_line_start": 353,
  "source_line_end": 358,
  "registry_ids": [
    "IV.P44"
  ],
  "related_registry_items": [
    {
      "id": "IV.P44",
      "title": "Current Conservation from Gauge Invariance",
      "url": "/registry/object/IV.P44/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauMaxwell.lean#L353-L358",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.TauMaxwell",
        "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauMaxwell.lean#L353-L358",
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

- Module: [TauLib.BookIV.Electroweak.TauMaxwell](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/)
- Source path: [`TauLib/BookIV/Electroweak/TauMaxwell.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauMaxwell.lean#L353-L358)
- Source range: L353-L358
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P44` — Current Conservation from Gauge Invariance

## Immediate Comment / Docstring

```lean
/-- [IV.P44] Source equation implies continuity equation ∂_μ J^μ = 0.
    From d*F = *J and d² = 0: d*J = d²*F = 0 → ∂_μ J^μ = 0.
    Physical content: charge conservation (local form). -/
```

## Source Excerpt

```lean
structure ContinuityEquation where
  /-- d²=0 implies d*J=0. -/
  from_d_squared : Bool := true
  /-- Equivalent to charge conservation. -/
  is_charge_conservation : Bool := true
  deriving Repr
```
