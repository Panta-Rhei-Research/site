---
{
  "projection_kind": "taulib_declaration",
  "title": "EWSynthesisPrediction",
  "permalink": "/corpus/taulib/docs/book-iv-electroweak-ewsynthesis/ewsynthesis-prediction/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.EWSynthesis`.",
  "declaration_id": "TauLib.BookIV.Electroweak.EWSynthesis::EWSynthesisPrediction",
  "declaration_slug": "ewsynthesis-prediction",
  "kind": "structure",
  "name": "EWSynthesisPrediction",
  "module_name": "TauLib.BookIV.Electroweak.EWSynthesis",
  "module_url": "/corpus/taulib/docs/book-iv-electroweak-ewsynthesis/",
  "source_line_start": 121,
  "source_line_end": 134,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWSynthesis.lean#L121-L134",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.EWSynthesis",
        "url": "/corpus/taulib/docs/book-iv-electroweak-ewsynthesis/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWSynthesis.lean#L121-L134",
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

- Module: [TauLib.BookIV.Electroweak.EWSynthesis](/corpus/taulib/docs/book-iv-electroweak-ewsynthesis/)
- Source path: [`TauLib/BookIV/Electroweak/EWSynthesis.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWSynthesis.lean#L121-L134)
- Source range: L121-L134
- Kind: `structure`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- An EW prediction entry: name, τ-value, experimental value, deviation. -/
```

## Source Excerpt

```lean
structure EWSynthesisPrediction where
  /-- Quantity name. -/
  name : String
  /-- τ-predicted value numerator. -/
  tau_numer : Nat
  /-- τ-predicted value denominator. -/
  tau_denom : Nat
  /-- Experimental value numerator. -/
  exp_numer : Nat
  /-- Experimental value denominator. -/
  exp_denom : Nat
  /-- Approximate deviation in parts per million. -/
  deviation_ppm : Nat
  deriving Repr
```
