---
{
  "projection_kind": "taulib_declaration",
  "title": "FFromCommutator",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/ffrom-commutator/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.GaugeInvariance`.",
  "declaration_id": "TauLib.BookIV.Electroweak.GaugeInvariance::FFromCommutator",
  "declaration_slug": "ffrom-commutator",
  "kind": "structure",
  "name": "FFromCommutator",
  "module_name": "TauLib.BookIV.Electroweak.GaugeInvariance",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/",
  "source_line_start": 332,
  "source_line_end": 337,
  "registry_ids": [
    "IV.P39"
  ],
  "related_registry_items": [
    {
      "id": "IV.P39",
      "title": "Explicit Form of F_mu_nu",
      "url": "/registry/object/IV.P39/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L332-L337",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L332-L337",
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
- Source path: [`TauLib/BookIV/Electroweak/GaugeInvariance.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L332-L337)
- Source range: L332-L337
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P39` — Explicit Form of F_mu_nu

## Immediate Comment / Docstring

```lean
/-- [IV.P39] F_μν arises from the commutator of covariant derivatives:
    [D_μ, D_ν] = ieF_μν. This is the geometric definition of curvature. -/
```

## Source Excerpt

```lean
structure FFromCommutator where
  /-- F is the commutator of D. -/
  is_commutator : Bool := true
  /-- The factor is ie. -/
  factor_is_ie : Bool := true
  deriving Repr
```
