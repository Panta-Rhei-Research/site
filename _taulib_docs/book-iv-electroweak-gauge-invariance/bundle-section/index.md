---
{
  "projection_kind": "taulib_declaration",
  "title": "BundleSection",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/bundle-section/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.GaugeInvariance`.",
  "declaration_id": "TauLib.BookIV.Electroweak.GaugeInvariance::BundleSection",
  "declaration_slug": "bundle-section",
  "kind": "structure",
  "name": "BundleSection",
  "module_name": "TauLib.BookIV.Electroweak.GaugeInvariance",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/",
  "source_line_start": 133,
  "source_line_end": 138,
  "registry_ids": [
    "IV.D88"
  ],
  "related_registry_items": [
    {
      "id": "IV.D88",
      "title": "Section of the EM Bundle",
      "url": "/registry/object/IV.D88/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L133-L138",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L133-L138",
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
- Source path: [`TauLib/BookIV/Electroweak/GaugeInvariance.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L133-L138)
- Source range: L133-L138
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D88` — Section of the EM Bundle

## Immediate Comment / Docstring

```lean
/-- [IV.D88] A section of P_EM: a smooth map s: T² → P_EM with
    π ∘ s = id. Existence of a global section iff bundle is trivial. -/
```

## Source Excerpt

```lean
structure BundleSection where
  /-- Whether the section is global (defined on all of T²). -/
  is_global : Bool
  /-- Chern class is zero (required for global section to exist). -/
  chern_is_zero : Bool
  deriving Repr
```
