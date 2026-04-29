---
{
  "projection_kind": "taulib_declaration",
  "title": "minkowski_from_chart",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-lorentz-no-minkowski/minkowski-from-chart/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.LorentzNoMinkowski`.",
  "declaration_id": "TauLib.BookV.GravityField.LorentzNoMinkowski::minkowski_from_chart",
  "declaration_slug": "minkowski-from-chart",
  "kind": "theorem",
  "name": "minkowski_from_chart",
  "module_name": "TauLib.BookV.GravityField.LorentzNoMinkowski",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-lorentz-no-minkowski/",
  "source_line_start": 200,
  "source_line_end": 202,
  "registry_ids": [
    "V.T25"
  ],
  "related_registry_items": [
    {
      "id": "V.T25",
      "title": "Minkowski as chart shadow --- cf. III.D76",
      "url": "/registry/object/V.T25/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/LorentzNoMinkowski.lean#L200-L202",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.LorentzNoMinkowski",
        "url": "/verify/taulib/docs/book-v-gravity-field-lorentz-no-minkowski/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/LorentzNoMinkowski.lean#L200-L202",
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

- Module: [TauLib.BookV.GravityField.LorentzNoMinkowski](/verify/taulib/docs/book-v-gravity-field-lorentz-no-minkowski/)
- Source path: [`TauLib/BookV/GravityField/LorentzNoMinkowski.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/LorentzNoMinkowski.lean#L200-L202)
- Source range: L200-L202
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T25` — Minkowski as chart shadow --- cf. III.D76

## Immediate Comment / Docstring

```lean
/-- [V.T25] Minkowski spacetime η_μν = diag(-1,+1,+1,+1) emerges
    as the flat-space limit of a local τ³ chart.

    The Minkowski metric is:
    - A local approximation (valid in one chart neighborhood)
    - The zeroth-order term in the chart readout expansion
    - NOT a global arena (globally replaced by τ³ boundary data)

    This theorem records that the chart signature determines Minkowski. -/
```

## Source Excerpt

```lean
theorem minkowski_from_chart (c : LocalTau3Chart) :
    c.signature = lorentzian_signature ∧ c.dimension = 4 :=
  ⟨c.sig_lorentzian, c.dim_is_four⟩
```
