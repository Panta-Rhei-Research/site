---
{
  "projection_kind": "taulib_declaration",
  "title": "GoldstoneAbsorption",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/goldstone-absorption/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.TauHiggs2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.TauHiggs2::GoldstoneAbsorption",
  "declaration_slug": "goldstone-absorption",
  "kind": "structure",
  "name": "GoldstoneAbsorption",
  "module_name": "TauLib.BookIV.Electroweak.TauHiggs2",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/",
  "source_line_start": 258,
  "source_line_end": 271,
  "registry_ids": [
    "IV.P76"
  ],
  "related_registry_items": [
    {
      "id": "IV.P76",
      "title": "Goldstone Modes at Crossing Point",
      "url": "/registry/object/IV.P76/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L258-L271",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.TauHiggs2",
        "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L258-L271",
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

- Module: [TauLib.BookIV.Electroweak.TauHiggs2](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/)
- Source path: [`TauLib/BookIV/Electroweak/TauHiggs2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L258-L271)
- Source range: L258-L271
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P76` — Goldstone Modes at Crossing Point

## Immediate Comment / Docstring

```lean
/-- [IV.P76] Three Goldstone bosons (from the 3 zero eigenvalues of
    the Hessian) are absorbed by W+, W-, and Z to become their
    longitudinal polarization modes.

    Before eating: W+, W-, Z are massless with 2 polarizations each.
    After eating: W+, W-, Z are massive with 3 polarizations each.

    Counting: 3 × 2 + 3 = 3 × 3 (6 + 3 = 9 DOF, conserved). -/
```

## Source Excerpt

```lean
structure GoldstoneAbsorption where
  /-- Number of Goldstones eaten. -/
  goldstones_eaten : Nat := 3
  /-- Bosons gaining mass. -/
  massive_bosons : List String := ["W+", "W-", "Z"]
  /-- Polarization count before. -/
  pol_before : Nat := 6  -- 3 × 2 transverse
  /-- DOF from Goldstones. -/
  goldstone_dof : Nat := 3
  /-- Polarization count after. -/
  pol_after : Nat := 9  -- 3 × 3 (2 transverse + 1 longitudinal each)
  /-- DOF conservation. -/
  dof_conserved : pol_before + goldstone_dof = pol_after := by omega
  deriving Repr
```
