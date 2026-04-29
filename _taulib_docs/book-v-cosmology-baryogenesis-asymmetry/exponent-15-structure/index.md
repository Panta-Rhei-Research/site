---
{
  "projection_kind": "taulib_declaration",
  "title": "exponent_15_structure",
  "permalink": "/verify/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/exponent-15-structure/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.BaryogenesisAsymmetry`.",
  "declaration_id": "TauLib.BookV.Cosmology.BaryogenesisAsymmetry::exponent_15_structure",
  "declaration_slug": "exponent-15-structure",
  "kind": "theorem",
  "name": "exponent_15_structure",
  "module_name": "TauLib.BookV.Cosmology.BaryogenesisAsymmetry",
  "module_url": "/verify/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/",
  "source_line_start": 59,
  "source_line_end": 59,
  "registry_ids": [
    "V.T170"
  ],
  "related_registry_items": [
    {
      "id": "V.T170",
      "title": "Baryogenesis Exponent 15 = dim(τ³) × |generators|",
      "url": "/registry/object/V.T170/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L59-L59",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L59-L59",
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
- Source path: [`TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L59-L59)
- Source range: L59-L59
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T170` — Baryogenesis Exponent 15 = dim(τ³) × |generators|

## Immediate Comment / Docstring

```lean
/-- Exponent 15 = dim(τ³) × |generators| = 3 × 5. [V.T170]

    dim(τ³) = 3: the fibered product τ³ = τ¹ ×_f T² has three independent
    directions (two fiber from T², one base from τ¹).

    |generators| = 5: the generator set {α, π, γ, η, ω} has cardinality 5. -/
```

## Source Excerpt

```lean
theorem exponent_15_structure : 3 * 5 = 15 := by rfl
```
