---
{
  "projection_kind": "taulib_declaration",
  "title": "SakharovConditions",
  "permalink": "/verify/taulib/docs/book-v-cosmology-threshold-ladder/sakharov-conditions/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.ThresholdLadder`.",
  "declaration_id": "TauLib.BookV.Cosmology.ThresholdLadder::SakharovConditions",
  "declaration_slug": "sakharov-conditions",
  "kind": "structure",
  "name": "SakharovConditions",
  "module_name": "TauLib.BookV.Cosmology.ThresholdLadder",
  "module_url": "/verify/taulib/docs/book-v-cosmology-threshold-ladder/",
  "source_line_start": 185,
  "source_line_end": 194,
  "registry_ids": [
    "V.R220"
  ],
  "related_registry_items": [
    {
      "id": "V.R220",
      "title": "Sakharov Conditions",
      "url": "/registry/object/V.R220/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/ThresholdLadder.lean#L185-L194",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.ThresholdLadder",
        "url": "/verify/taulib/docs/book-v-cosmology-threshold-ladder/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/ThresholdLadder.lean#L185-L194",
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

- Module: [TauLib.BookV.Cosmology.ThresholdLadder](/verify/taulib/docs/book-v-cosmology-threshold-ladder/)
- Source path: [`TauLib/BookV/Cosmology/ThresholdLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/ThresholdLadder.lean#L185-L194)
- Source range: L185-L194
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.R220` — Sakharov Conditions

## Immediate Comment / Docstring

```lean
/-- [V.R220] Two of three Sakharov conditions for baryogenesis are
    structural in τ: CP violation from the bipolar lemniscate, and
    departure from thermal equilibrium from the refinement cascade.

    The third condition (baryon number violation) requires the
    ω-sector crossing. All three are met at the L_B threshold. -/
```

## Source Excerpt

```lean
structure SakharovConditions where
  /-- CP violation from lemniscate bipolarity. -/
  cp_violation : Bool := true
  /-- Departure from equilibrium from refinement cascade. -/
  departure_from_eq : Bool := true
  /-- Baryon number violation from ω-sector. -/
  baryon_violation : Bool := true
  /-- All three met. -/
  all_met : Bool := true
  deriving Repr
```
