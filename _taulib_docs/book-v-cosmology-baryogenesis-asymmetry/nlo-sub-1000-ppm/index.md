---
{
  "projection_kind": "taulib_declaration",
  "title": "nlo_sub_1000_ppm",
  "permalink": "/verify/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/nlo-sub-1000-ppm/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.BaryogenesisAsymmetry`.",
  "declaration_id": "TauLib.BookV.Cosmology.BaryogenesisAsymmetry::nlo_sub_1000_ppm",
  "declaration_slug": "nlo-sub-1000-ppm",
  "kind": "theorem",
  "name": "nlo_sub_1000_ppm",
  "module_name": "TauLib.BookV.Cosmology.BaryogenesisAsymmetry",
  "module_url": "/verify/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/",
  "source_line_start": 337,
  "source_line_end": 347,
  "registry_ids": [
    "V.R469"
  ],
  "related_registry_items": [
    {
      "id": "V.R469",
      "title": "Baryogenesis Assessment (Wave 47)",
      "url": "/registry/object/V.R469/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L337-L347",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.BaryogenesisAsymmetry",
        "url": "/verify/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L337-L347",
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

- Module: [TauLib.BookV.Cosmology.BaryogenesisAsymmetry](/verify/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/)
- Source path: [`TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L337-L347)
- Source range: L337-L347
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.R469` — Baryogenesis Assessment (Wave 47)

## Immediate Comment / Docstring

```lean
/-- [V.R469] Assessment: NLO brings η_B below 1000 ppm threshold. -/
```

## Source Excerpt

```lean
theorem nlo_sub_1000_ppm :
    baryogenesis_nlo.nlo_deviation_ppm < 1000 := by native_decide

-- ============================================================
-- SMOKE TESTS
-- ============================================================

#check tau_generator_count               -- proof: list length = 5
#check exponent_15_structure             -- proof: 3 * 5 = 15
#check yp_baryogenesis_shared_factor    -- should type-check
#check eta_B_algebraic_identity         -- should type-check
```
