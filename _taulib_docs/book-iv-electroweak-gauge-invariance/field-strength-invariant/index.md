---
{
  "projection_kind": "taulib_declaration",
  "title": "field_strength_invariant",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/field-strength-invariant/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.GaugeInvariance`.",
  "declaration_id": "TauLib.BookIV.Electroweak.GaugeInvariance::field_strength_invariant",
  "declaration_slug": "field-strength-invariant",
  "kind": "theorem",
  "name": "field_strength_invariant",
  "module_name": "TauLib.BookIV.Electroweak.GaugeInvariance",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/",
  "source_line_start": 289,
  "source_line_end": 289,
  "registry_ids": [
    "IV.T38"
  ],
  "related_registry_items": [
    {
      "id": "IV.T38",
      "title": "Gauge Invariance of F_mu_nu",
      "url": "/registry/object/IV.T38/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L289-L289",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L289-L289",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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
- Source path: [`TauLib/BookIV/Electroweak/GaugeInvariance.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L289-L289)
- Source range: L289-L289
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T38` — Gauge Invariance of F_mu_nu

## Immediate Comment / Docstring

```lean
/-- [IV.T38] F_μν is gauge-invariant: since F = dA and d² = 0,
    the substitution A → A + dΛ gives F → F + d²Λ = F. -/
```

## Source Excerpt

```lean
theorem field_strength_invariant : field_strength.gauge_invariant = true := rfl
```
