---
{
  "projection_kind": "taulib_declaration",
  "title": "chart_recovers_efe",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-tau-einstein-eq/chart-recovers-efe/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.TauEinsteinEq`.",
  "declaration_id": "TauLib.BookV.GravityField.TauEinsteinEq::chart_recovers_efe",
  "declaration_slug": "chart-recovers-efe",
  "kind": "theorem",
  "name": "chart_recovers_efe",
  "module_name": "TauLib.BookV.GravityField.TauEinsteinEq",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-tau-einstein-eq/",
  "source_line_start": 206,
  "source_line_end": 208,
  "registry_ids": [
    "V.T26"
  ],
  "related_registry_items": [
    {
      "id": "V.T26",
      "title": "Chart shadow recovery",
      "url": "/registry/object/V.T26/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauEinsteinEq.lean#L206-L208",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.TauEinsteinEq",
        "url": "/verify/taulib/docs/book-v-gravity-field-tau-einstein-eq/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauEinsteinEq.lean#L206-L208",
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

- Module: [TauLib.BookV.GravityField.TauEinsteinEq](/verify/taulib/docs/book-v-gravity-field-tau-einstein-eq/)
- Source path: [`TauLib/BookV/GravityField/TauEinsteinEq.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauEinsteinEq.lean#L206-L208)
- Source range: L206-L208
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T26` — Chart shadow recovery

## Immediate Comment / Docstring

```lean
/-- [V.T26] The chart readout homomorphism Φ_p : H_∂[ω] → Jet_p[ω]
    maps the τ-Einstein identity to the orthodox Einstein field equations:

    R^H = κ_τ · T^mat  →  G_μν = (8πG/c⁴) T_μν

    The chart must be local and 4-dimensional. -/
```

## Source Excerpt

```lean
theorem chart_recovers_efe (c : LocalTau3Chart) :
    c.dimension = 4 ∧ c.signature = lorentzian_signature :=
  ⟨c.dim_is_four, c.sig_lorentzian⟩
```
