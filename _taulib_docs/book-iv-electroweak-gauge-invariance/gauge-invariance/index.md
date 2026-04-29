---
{
  "projection_kind": "taulib_declaration",
  "title": "gauge_invariance",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/gauge-invariance/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.GaugeInvariance`.",
  "declaration_id": "TauLib.BookIV.Electroweak.GaugeInvariance::gauge_invariance",
  "declaration_slug": "gauge-invariance",
  "kind": "theorem",
  "name": "gauge_invariance",
  "module_name": "TauLib.BookIV.Electroweak.GaugeInvariance",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/",
  "source_line_start": 280,
  "source_line_end": 281,
  "registry_ids": [
    "IV.T37"
  ],
  "related_registry_items": [
    {
      "id": "IV.T37",
      "title": "Gauge Invariance Kernel Theorem",
      "url": "/registry/object/IV.T37/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L280-L281",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L280-L281",
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
- Source path: [`TauLib/BookIV/Electroweak/GaugeInvariance.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L280-L281)
- Source range: L280-L281
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T37` — Gauge Invariance Kernel Theorem

## Immediate Comment / Docstring

```lean
/-- [IV.T37] Gauge invariance as structural theorem: physics on τ³
    is independent of the choice of local trivialization.
    All physical observables are σ-equivariant functionals. -/
```

## Source Excerpt

```lean
theorem gauge_invariance (s : SigmaEquivariant) (h : s.equivariant = true) :
    s.is_observable = true := by rw [s.obs_eq]; exact h
```
