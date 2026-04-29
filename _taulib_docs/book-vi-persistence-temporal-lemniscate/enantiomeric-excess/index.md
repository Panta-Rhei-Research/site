---
{
  "projection_kind": "taulib_declaration",
  "title": "EnantiomericExcess",
  "permalink": "/verify/taulib/docs/book-vi-persistence-temporal-lemniscate/enantiomeric-excess/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Persistence.TemporalLemniscate`.",
  "declaration_id": "TauLib.BookVI.Persistence.TemporalLemniscate::EnantiomericExcess",
  "declaration_slug": "enantiomeric-excess",
  "kind": "structure",
  "name": "EnantiomericExcess",
  "module_name": "TauLib.BookVI.Persistence.TemporalLemniscate",
  "module_url": "/verify/taulib/docs/book-vi-persistence-temporal-lemniscate/",
  "source_line_start": 161,
  "source_line_end": 170,
  "registry_ids": [
    "VI.D73"
  ],
  "related_registry_items": [
    {
      "id": "VI.D73",
      "title": "Enantiomeric Excess at Refinement Level n",
      "url": "/registry/object/VI.D73/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L161-L170",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Persistence.TemporalLemniscate",
        "url": "/verify/taulib/docs/book-vi-persistence-temporal-lemniscate/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L161-L170",
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

- Module: [TauLib.BookVI.Persistence.TemporalLemniscate](/verify/taulib/docs/book-vi-persistence-temporal-lemniscate/)
- Source path: [`TauLib/BookVI/Persistence/TemporalLemniscate.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L161-L170)
- Source range: L161-L170
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D73` — Enantiomeric Excess at Refinement Level n

## Immediate Comment / Docstring

```lean
/-- [VI.D73] Enantiomeric Excess at refinement level n.
    ee(n) = |[L] - [R]| / ([L] + [R]) measures chirality purity.
    Seeded by ChiralitySeed (VI.D72) at n=0 with ee ≈ 10⁻¹⁷,
    amplified by SelfDesc closure at each refinement level. -/
```

## Source Excerpt

```lean
structure EnantiomericExcess where
  /-- Refinement level (0 = initial seed). -/
  refinement_level : Nat
  /-- ee converges to 1 (100% homochiral). -/
  converges_to_one : Bool := true
  /-- Monotonically increasing with refinement. -/
  monotone : Bool := true
  /-- Seeded by VI.D72 ChiralitySeed. -/
  seed_source : String := "VI.D72"
  deriving Repr
```
