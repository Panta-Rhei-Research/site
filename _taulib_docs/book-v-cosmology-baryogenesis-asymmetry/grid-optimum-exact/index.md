---
{
  "projection_kind": "taulib_declaration",
  "title": "grid_optimum_exact",
  "permalink": "/verify/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/grid-optimum-exact/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.BaryogenesisAsymmetry`.",
  "declaration_id": "TauLib.BookV.Cosmology.BaryogenesisAsymmetry::grid_optimum_exact",
  "declaration_slug": "grid-optimum-exact",
  "kind": "theorem",
  "name": "grid_optimum_exact",
  "module_name": "TauLib.BookV.Cosmology.BaryogenesisAsymmetry",
  "module_url": "/verify/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/",
  "source_line_start": 282,
  "source_line_end": 283,
  "registry_ids": [
    "V.T189"
  ],
  "related_registry_items": [
    {
      "id": "V.T189",
      "title": "Grid Optimum Structural Derivation: (203/175, 609/700)",
      "url": "/registry/object/V.T189/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L282-L283",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L282-L283",
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
- Source path: [`TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L282-L283)
- Source range: L282-L283
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T189` — Grid Optimum Structural Derivation: (203/175, 609/700)

## Immediate Comment / Docstring

```lean
/-- [V.T189] Grid Optimum Structural Derivation.
    (Δpq,Δpr) = (203/175, 609/700) = (8/7+3/175, 6/7+9/700) at +18.5 ppm. -/
```

## Source Excerpt

```lean
theorem grid_optimum_exact :
    (8 : Rat) / 7 + 3 / 175 = 203 / 175 := by norm_num
```
