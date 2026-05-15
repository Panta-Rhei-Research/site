---
{
  "projection_kind": "taulib_declaration",
  "title": "BHT2Falsification",
  "permalink": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/bht2-falsification/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Gravity.BHTopoModes`.",
  "declaration_id": "TauLib.BookV.Gravity.BHTopoModes::BHT2Falsification",
  "declaration_slug": "bht2-falsification",
  "kind": "structure",
  "name": "BHT2Falsification",
  "module_name": "TauLib.BookV.Gravity.BHTopoModes",
  "module_url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/",
  "source_line_start": 415,
  "source_line_end": 424,
  "registry_ids": [
    "V.P131"
  ],
  "related_registry_items": [
    {
      "id": "V.P131",
      "title": "Three Falsifiable BH T² Predictions with Fiber Structure Derivation",
      "url": "/registry/object/V.P131/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L415-L424",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Gravity.BHTopoModes",
        "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L415-L424",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "role": "type/data schema",
      "status": "type/data schema"
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

- Module: [TauLib.BookV.Gravity.BHTopoModes](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/)
- Source path: [`TauLib/BookV/Gravity/BHTopoModes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L415-L424)
- Source range: L415-L424
- Kind: `structure`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- `V.P131` — Three Falsifiable BH T² Predictions with Fiber Structure Derivation

## Immediate Comment / Docstring

```lean
/-- [V.P131] Structure capturing the three falsifiable T² BH predictions. -/
```

## Source Excerpt

```lean
structure BHT2Falsification where
  /-- Number of independent falsifiable predictions. -/
  n_predictions : Nat := 3
  /-- Number of observational channels (QNM + shadow + cycle-delay). -/
  n_channels : Nat := 3
  /-- Predictions equal channels. -/
  predictions_eq_channels : n_predictions = n_channels
  /-- Number of free parameters across all predictions. -/
  free_parameters : Nat := 0
  deriving Repr
```
