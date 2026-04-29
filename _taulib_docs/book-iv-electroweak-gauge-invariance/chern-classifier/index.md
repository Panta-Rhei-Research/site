---
{
  "projection_kind": "taulib_declaration",
  "title": "ChernClassifier",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/chern-classifier/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.GaugeInvariance`.",
  "declaration_id": "TauLib.BookIV.Electroweak.GaugeInvariance::ChernClassifier",
  "declaration_slug": "chern-classifier",
  "kind": "structure",
  "name": "ChernClassifier",
  "module_name": "TauLib.BookIV.Electroweak.GaugeInvariance",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/",
  "source_line_start": 297,
  "source_line_end": 302,
  "registry_ids": [
    "IV.P37"
  ],
  "related_registry_items": [
    {
      "id": "IV.P37",
      "title": "EM Bundle Topology",
      "url": "/registry/object/IV.P37/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L297-L302",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.GaugeInvariance",
        "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L297-L302",
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

- Module: [TauLib.BookIV.Electroweak.GaugeInvariance](/verify/taulib/docs/book-iv-electroweak-gauge-invariance/)
- Source path: [`TauLib/BookIV/Electroweak/GaugeInvariance.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L297-L302)
- Source range: L297-L302
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P37` — EM Bundle Topology

## Immediate Comment / Docstring

```lean
/-- [IV.P37] P_EM is classified by its first Chern class c₁ ∈ ℤ.
    The Chern number is the total magnetic flux through T². -/
```

## Source Excerpt

```lean
structure ChernClassifier where
  /-- First Chern class (integer). -/
  chern_class : Int
  /-- Chern class determines bundle up to isomorphism. -/
  classifies_bundle : Bool := true
  deriving Repr
```
