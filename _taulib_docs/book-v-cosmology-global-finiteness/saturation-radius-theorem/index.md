---
{
  "projection_kind": "taulib_declaration",
  "title": "saturation_radius_theorem",
  "permalink": "/verify/taulib/docs/book-v-cosmology-global-finiteness/saturation-radius-theorem/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.GlobalFiniteness`.",
  "declaration_id": "TauLib.BookV.Cosmology.GlobalFiniteness::saturation_radius_theorem",
  "declaration_slug": "saturation-radius-theorem",
  "kind": "theorem",
  "name": "saturation_radius_theorem",
  "module_name": "TauLib.BookV.Cosmology.GlobalFiniteness",
  "module_url": "/verify/taulib/docs/book-v-cosmology-global-finiteness/",
  "source_line_start": 186,
  "source_line_end": 187,
  "registry_ids": [
    "V.T117"
  ],
  "related_registry_items": [
    {
      "id": "V.T117",
      "title": "Saturation Radius Theorem",
      "url": "/registry/object/V.T117/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/GlobalFiniteness.lean#L186-L187",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.GlobalFiniteness",
        "url": "/verify/taulib/docs/book-v-cosmology-global-finiteness/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/GlobalFiniteness.lean#L186-L187",
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

- Module: [TauLib.BookV.Cosmology.GlobalFiniteness](/verify/taulib/docs/book-v-cosmology-global-finiteness/)
- Source path: [`TauLib/BookV/Cosmology/GlobalFiniteness.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/GlobalFiniteness.lean#L186-L187)
- Source range: L186-L187
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T117` — Saturation Radius Theorem

## Immediate Comment / Docstring

```lean
/-- [V.T117] Saturation radius theorem: R_sat is finite.

    Bounded by R_sat ≤ C · t_∞ · c where:
    - t_∞ = Σ p_k⁻¹ (total profinite time, convergent)
    - c = speed of light
    - C = geometric constant from T² fiber volume

    The saturation radius is a structural property of τ³
    (not a chart-level concept like the observable universe). -/
```

## Source Excerpt

```lean
theorem saturation_radius_theorem (r : SaturationRadius) :
    r.radius_numer > 0 := r.finite
```
