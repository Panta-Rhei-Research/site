---
{
  "projection_kind": "taulib_declaration",
  "title": "SplittingRatioControl",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/splitting-ratio-control/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Thermodynamics.EntropySplitting`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.EntropySplitting::SplittingRatioControl",
  "declaration_slug": "splitting-ratio-control",
  "kind": "structure",
  "name": "SplittingRatioControl",
  "module_name": "TauLib.BookV.Thermodynamics.EntropySplitting",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/",
  "source_line_start": 245,
  "source_line_end": 250,
  "registry_ids": [
    "V.P28"
  ],
  "related_registry_items": [
    {
      "id": "V.P28",
      "title": "iota_tau controls the splitting ratio",
      "url": "/registry/object/V.P28/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L245-L250",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Thermodynamics.EntropySplitting",
        "url": "/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L245-L250",
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

- Module: [TauLib.BookV.Thermodynamics.EntropySplitting](/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/)
- Source path: [`TauLib/BookV/Thermodynamics/EntropySplitting.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L245-L250)
- Source range: L245-L250
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.P28` — iota_tau controls the splitting ratio

## Immediate Comment / Docstring

```lean
/-- [V.P28] iota_tau controls the splitting ratio:
    S_def(n)/S(n) <= (1-iota_tau)^n * S_def(0) / (n ln p).

    The crossover depth n* at which S_def drops below S_ref
    is determined by iota_tau alone. -/
```

## Source Excerpt

```lean
structure SplittingRatioControl where
  /-- Crossover depth estimate (orbit steps). -/
  crossover_depth : Nat
  /-- The controlling constant is iota_tau. -/
  controlled_by_iota : Bool := true
  deriving Repr
```
