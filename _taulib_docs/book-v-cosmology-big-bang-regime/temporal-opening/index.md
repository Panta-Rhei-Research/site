---
{
  "projection_kind": "taulib_declaration",
  "title": "TemporalOpening",
  "permalink": "/verify/taulib/docs/book-v-cosmology-big-bang-regime/temporal-opening/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.BigBangRegime`.",
  "declaration_id": "TauLib.BookV.Cosmology.BigBangRegime::TemporalOpening",
  "declaration_slug": "temporal-opening",
  "kind": "structure",
  "name": "TemporalOpening",
  "module_name": "TauLib.BookV.Cosmology.BigBangRegime",
  "module_url": "/verify/taulib/docs/book-v-cosmology-big-bang-regime/",
  "source_line_start": 66,
  "source_line_end": 77,
  "registry_ids": [
    "V.D152"
  ],
  "related_registry_items": [
    {
      "id": "V.D152",
      "title": "Temporal Opening",
      "url": "/registry/object/V.D152/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BigBangRegime.lean#L66-L77",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.BigBangRegime",
        "url": "/verify/taulib/docs/book-v-cosmology-big-bang-regime/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BigBangRegime.lean#L66-L77",
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

- Module: [TauLib.BookV.Cosmology.BigBangRegime](/verify/taulib/docs/book-v-cosmology-big-bang-regime/)
- Source path: [`TauLib/BookV/Cosmology/BigBangRegime.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BigBangRegime.lean#L66-L77)
- Source range: L66-L77
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D152` — Temporal Opening

## Immediate Comment / Docstring

```lean
/-- [V.D152] Temporal opening: the structural transition from the
    pre-temporal kernel to the first refinement level α₁.

    Properties:
    - Unique: exactly one first level (α₁ is the seed)
    - Irreversible: there is no pre-α₁ state
    - Maximal: boundary-character energy density is highest at α₁ -/
```

## Source Excerpt

```lean
structure TemporalOpening where
  /-- First tick index (always 1). -/
  first_tick : Nat
  /-- First tick is 1. -/
  first_tick_is_one : first_tick = 1
  /-- Whether the opening is unique. -/
  is_unique : Bool := true
  /-- Whether the opening is irreversible. -/
  is_irreversible : Bool := true
  /-- Whether the energy density is maximal. -/
  is_maximal : Bool := true
  deriving Repr
```
