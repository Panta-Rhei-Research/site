---
{
  "projection_kind": "taulib_declaration",
  "title": "LocalTrivialization",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/local-trivialization/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.GaugeInvariance`.",
  "declaration_id": "TauLib.BookIV.Electroweak.GaugeInvariance::LocalTrivialization",
  "declaration_slug": "local-trivialization",
  "kind": "structure",
  "name": "LocalTrivialization",
  "module_name": "TauLib.BookIV.Electroweak.GaugeInvariance",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/",
  "source_line_start": 95,
  "source_line_end": 100,
  "registry_ids": [
    "IV.D86"
  ],
  "related_registry_items": [
    {
      "id": "IV.D86",
      "title": "Local Trivialization",
      "url": "/registry/object/IV.D86/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L95-L100",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L95-L100",
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
- Source path: [`TauLib/BookIV/Electroweak/GaugeInvariance.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L95-L100)
- Source range: L95-L100
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D86` — Local Trivialization

## Immediate Comment / Docstring

```lean
/-- [IV.D86] A local trivialization of P_EM over a patch U_i ⊂ T².
    On each patch, P_EM|_{U_i} ≅ U_i × U(1). -/
```

## Source Excerpt

```lean
structure LocalTrivialization where
  /-- Patch index. -/
  patch_index : Nat
  /-- The trivialization is smooth. -/
  smooth : Bool := true
  deriving Repr
```
