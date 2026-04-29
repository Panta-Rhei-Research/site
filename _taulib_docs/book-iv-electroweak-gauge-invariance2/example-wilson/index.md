---
{
  "projection_kind": "taulib_declaration",
  "title": "example_wilson",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/example-wilson/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Electroweak.GaugeInvariance2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.GaugeInvariance2::example_wilson",
  "declaration_slug": "example-wilson",
  "kind": "def",
  "name": "example_wilson",
  "module_name": "TauLib.BookIV.Electroweak.GaugeInvariance2",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/",
  "source_line_start": 340,
  "source_line_end": 340,
  "registry_ids": [
    "IV.R25",
    "IV.R359",
    "IV.R360",
    "IV.R362"
  ],
  "related_registry_items": [
    {
      "id": "IV.R25",
      "title": "Gauge Invariance Is Geometric Not Dynamic",
      "url": "/registry/object/IV.R25/"
    },
    {
      "id": "IV.R359",
      "title": "Physical content lives in the curvature",
      "url": "/registry/object/IV.R359/"
    },
    {
      "id": "IV.R360",
      "title": "Experimental confirmation",
      "url": "/registry/object/IV.R360/"
    },
    {
      "id": "IV.R362",
      "title": "The AB effect as an observable",
      "url": "/registry/object/IV.R362/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L340-L340",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.GaugeInvariance2",
        "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L340-L340",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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

- Module: [TauLib.BookIV.Electroweak.GaugeInvariance2](/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/)
- Source path: [`TauLib/BookIV/Electroweak/GaugeInvariance2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L340-L340)
- Source range: L340-L340
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.R25` — Gauge Invariance Is Geometric Not Dynamic
- `IV.R359` — Physical content lives in the curvature
- `IV.R360` — Experimental confirmation
- `IV.R362` — The AB effect as an observable

## Immediate Comment / Docstring

```lean
-- [IV.R25] The connection A_μ is the fundamental dynamical variable,
-- not the field strength F_μν. F is derived from A by differentiation.

-- [IV.R359] Gauge invariance is not a symmetry imposed by hand but
-- a structural consequence of the principal bundle formulation.

-- [IV.R360] The AB effect proves that A_μ contains more physical
-- information than F_μν: the holonomy is not determined by curvature
-- alone on non-simply-connected spaces.

-- [IV.R362] The seven-step derivation chain shows that Maxwell theory
-- is an INEVITABLE consequence of K0-K6, not a separate physical law.

-- ============================================================
-- SMOKE TESTS
-- ============================================================
```

## Source Excerpt

```lean
def example_wilson : WilsonLoop := wilson_u1 3
```
