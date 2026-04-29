---
{
  "projection_kind": "taulib_declaration",
  "title": "DegenerateVacuumManifold",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-tau-higgs/degenerate-vacuum-manifold/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.TauHiggs`.",
  "declaration_id": "TauLib.BookIV.Electroweak.TauHiggs::DegenerateVacuumManifold",
  "declaration_slug": "degenerate-vacuum-manifold",
  "kind": "structure",
  "name": "DegenerateVacuumManifold",
  "module_name": "TauLib.BookIV.Electroweak.TauHiggs",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs/",
  "source_line_start": 258,
  "source_line_end": 267,
  "registry_ids": [
    "IV.P72"
  ],
  "related_registry_items": [
    {
      "id": "IV.P72",
      "title": "Crossing-Point Degeneracy",
      "url": "/registry/object/IV.P72/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs.lean#L258-L267",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs.lean#L258-L267",
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
- Source path: [`TauLib/BookIV/Electroweak/TauHiggs.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs.lean#L258-L267)
- Source range: L258-L267
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P72` — Crossing-Point Degeneracy

## Immediate Comment / Docstring

```lean
/-- [IV.P72] The vacuum manifold is S¹: the set of minima of V_n
    forms a circle in field space. This degeneracy is the geometric
    origin of Goldstone bosons.

    In the τ-framework, S¹ is one lobe of the lemniscate L = S¹ ∨ S¹.
    The vacuum selects a point on one lobe, breaking the continuous
    S¹ symmetry spontaneously. -/
```

## Source Excerpt

```lean
structure DegenerateVacuumManifold where
  /-- Vacuum manifold topology. -/
  topology : String := "S1"
  /-- Dimension of manifold. -/
  dim : Nat := 1
  /-- Number of Goldstone bosons = dim of manifold. -/
  goldstone_count : Nat := 3
  /-- The 3 Goldstones come from SU(2)_L breaking, not just S¹. -/
  from_su2_breaking : Bool := true
  deriving Repr
```
