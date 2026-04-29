---
{
  "projection_kind": "taulib_declaration",
  "title": "ComplexityMonotone",
  "permalink": "/verify/taulib/docs/book-vi-persistence-persistence-sector/complexity-monotone/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Persistence.PersistenceSector`.",
  "declaration_id": "TauLib.BookVI.Persistence.PersistenceSector::ComplexityMonotone",
  "declaration_slug": "complexity-monotone",
  "kind": "structure",
  "name": "ComplexityMonotone",
  "module_name": "TauLib.BookVI.Persistence.PersistenceSector",
  "module_url": "/verify/taulib/docs/book-vi-persistence-persistence-sector/",
  "source_line_start": 237,
  "source_line_end": 246,
  "registry_ids": [
    "VI.L15"
  ],
  "related_registry_items": [
    {
      "id": "VI.L15",
      "title": "Complexity Monotone",
      "url": "/registry/object/VI.L15/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/PersistenceSector.lean#L237-L246",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Persistence.PersistenceSector",
        "url": "/verify/taulib/docs/book-vi-persistence-persistence-sector/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/PersistenceSector.lean#L237-L246",
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

- Module: [TauLib.BookVI.Persistence.PersistenceSector](/verify/taulib/docs/book-vi-persistence-persistence-sector/)
- Source path: [`TauLib/BookVI/Persistence/PersistenceSector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/PersistenceSector.lean#L237-L246)
- Source range: L237-L246
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.L15` — Complexity Monotone

## Immediate Comment / Docstring

```lean
/-- [VI.L15] Complexity Monotone Lemma: C(n) ≤ C(n+1).
    Defects decrease geometrically (V.T62), so freed capacity
    C(n) = N − |D_n| increases monotonically.
    Proof: |D_{n+1}| ≤ (1−ι_τ)|D_n| < |D_n| ⟹ C(n+1) > C(n). -/
```

## Source Excerpt

```lean
structure ComplexityMonotone where
  /-- Defect decay rate per step: (1−ι_τ). -/
  decay_rate_factor : String := "1 - iota_tau"
  /-- C(n) ≤ C(n+1) for all n. -/
  monotone_increasing : Bool := true
  /-- Derived from V.T62 geometric decay. -/
  derived_from_geometric_decay : Bool := true
  /-- Scope: τ-effective. -/
  scope : String := "tau_effective"
  deriving Repr
```
