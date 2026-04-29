---
{
  "projection_kind": "taulib_declaration",
  "title": "VnMinimumCircle",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-tau-higgs/vn-minimum-circle/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.TauHiggs`.",
  "declaration_id": "TauLib.BookIV.Electroweak.TauHiggs::VnMinimumCircle",
  "declaration_slug": "vn-minimum-circle",
  "kind": "structure",
  "name": "VnMinimumCircle",
  "module_name": "TauLib.BookIV.Electroweak.TauHiggs",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs/",
  "source_line_start": 278,
  "source_line_end": 285,
  "registry_ids": [
    "IV.P73"
  ],
  "related_registry_items": [
    {
      "id": "IV.P73",
      "title": "Finite-Stage Vacuum Existence and Uniqueness",
      "url": "/registry/object/IV.P73/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs.lean#L278-L285",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.TauHiggs",
        "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs.lean#L278-L285",
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

- Module: [TauLib.BookIV.Electroweak.TauHiggs](/verify/taulib/docs/book-iv-electroweak-tau-higgs/)
- Source path: [`TauLib/BookIV/Electroweak/TauHiggs.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs.lean#L278-L285)
- Source range: L278-L285
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P73` — Finite-Stage Vacuum Existence and Uniqueness

## Immediate Comment / Docstring

```lean
/-- [IV.P73] The minimum of V_n lies on a circle S¹ of radius v_EW
    in the (Re φ, Im φ) plane. All points on this circle are
    physically equivalent (related by a U(1) gauge transformation). -/
```

## Source Excerpt

```lean
structure VnMinimumCircle where
  /-- Radius of the minimum circle in MeV. -/
  radius_MeV : Nat := 246200
  /-- The circle is a gauge orbit. -/
  is_gauge_orbit : Bool := true
  /-- All points physically equivalent. -/
  all_equivalent : Bool := true
  deriving Repr
```
