---
{
  "projection_kind": "taulib_declaration",
  "title": "nlo_sub_1000_ppm",
  "permalink": "/corpus/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/nlo-sub-1000-ppm/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.BaryogenesisAsymmetry`.",
  "declaration_id": "TauLib.BookV.Cosmology.BaryogenesisAsymmetry::nlo_sub_1000_ppm",
  "declaration_slug": "nlo-sub-1000-ppm",
  "kind": "theorem",
  "name": "nlo_sub_1000_ppm",
  "module_name": "TauLib.BookV.Cosmology.BaryogenesisAsymmetry",
  "module_url": "/corpus/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/",
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
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.BaryogenesisAsymmetry",
        "url": "/corpus/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
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
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookV.Cosmology.BaryogenesisAsymmetry](/corpus/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/)
- Source path: [`TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L337-L347)
- Source range: L337-L347
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

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
