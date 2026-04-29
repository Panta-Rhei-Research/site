---
{
  "projection_kind": "taulib_declaration",
  "title": "yp_in_observational_range",
  "permalink": "/verify/taulib/docs/book-v-cosmology-helium-fraction/yp-in-observational-range/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.HeliumFraction`.",
  "declaration_id": "TauLib.BookV.Cosmology.HeliumFraction::yp_in_observational_range",
  "declaration_slug": "yp-in-observational-range",
  "kind": "theorem",
  "name": "yp_in_observational_range",
  "module_name": "TauLib.BookV.Cosmology.HeliumFraction",
  "module_url": "/verify/taulib/docs/book-v-cosmology-helium-fraction/",
  "source_line_start": 243,
  "source_line_end": 245,
  "registry_ids": [
    "V.P112"
  ],
  "related_registry_items": [
    {
      "id": "V.P112",
      "title": "Y_p Observational Consistency",
      "url": "/registry/object/V.P112/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/HeliumFraction.lean#L243-L245",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.HeliumFraction",
        "url": "/verify/taulib/docs/book-v-cosmology-helium-fraction/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/HeliumFraction.lean#L243-L245",
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

- Module: [TauLib.BookV.Cosmology.HeliumFraction](/verify/taulib/docs/book-v-cosmology-helium-fraction/)
- Source path: [`TauLib/BookV/Cosmology/HeliumFraction.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/HeliumFraction.lean#L243-L245)
- Source range: L243-L245
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P112` — Y_p Observational Consistency

## Immediate Comment / Docstring

```lean
/-- [V.P112] Y_p = 20/81 = 0.24691... is within the observational
    range Y_p ∈ (0.244, 0.250) at 2σ. -/
```

## Source Excerpt

```lean
theorem yp_in_observational_range :
    yp_times_1000 ≥ 244 ∧ yp_times_1000 ≤ 250 := by
  constructor <;> native_decide
```
