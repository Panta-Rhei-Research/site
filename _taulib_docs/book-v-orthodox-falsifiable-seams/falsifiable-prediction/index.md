---
{
  "projection_kind": "taulib_declaration",
  "title": "FalsifiablePrediction",
  "permalink": "/corpus/taulib/docs/book-v-orthodox-falsifiable-seams/falsifiable-prediction/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Orthodox.FalsifiableSeams`.",
  "declaration_id": "TauLib.BookV.Orthodox.FalsifiableSeams::FalsifiablePrediction",
  "declaration_slug": "falsifiable-prediction",
  "kind": "structure",
  "name": "FalsifiablePrediction",
  "module_name": "TauLib.BookV.Orthodox.FalsifiableSeams",
  "module_url": "/corpus/taulib/docs/book-v-orthodox-falsifiable-seams/",
  "source_line_start": 89,
  "source_line_end": 100,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/FalsifiableSeams.lean#L89-L100",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Orthodox.FalsifiableSeams",
        "url": "/corpus/taulib/docs/book-v-orthodox-falsifiable-seams/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/FalsifiableSeams.lean#L89-L100",
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

- Module: [TauLib.BookV.Orthodox.FalsifiableSeams](/corpus/taulib/docs/book-v-orthodox-falsifiable-seams/)
- Source path: [`TauLib/BookV/Orthodox/FalsifiableSeams.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/FalsifiableSeams.lean#L89-L100)
- Source range: L89-L100
- Kind: `structure`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- A falsifiable prediction of the tau-framework. -/
```

## Source Excerpt

```lean
structure FalsifiablePrediction where
  /-- Name of the prediction. -/
  name : String
  /-- What tau predicts. -/
  prediction : String
  /-- What would falsify it. -/
  falsifier : String
  /-- Prediction strength. -/
  strength : PredictionStrength
  /-- Registry entry ID. -/
  registry_id : String
  deriving Repr
```
