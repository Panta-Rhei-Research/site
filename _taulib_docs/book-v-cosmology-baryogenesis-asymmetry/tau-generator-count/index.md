---
{
  "projection_kind": "taulib_declaration",
  "title": "tau_generator_count",
  "permalink": "/verify/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/tau-generator-count/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.BaryogenesisAsymmetry`.",
  "declaration_id": "TauLib.BookV.Cosmology.BaryogenesisAsymmetry::tau_generator_count",
  "declaration_slug": "tau-generator-count",
  "kind": "theorem",
  "name": "tau_generator_count",
  "module_name": "TauLib.BookV.Cosmology.BaryogenesisAsymmetry",
  "module_url": "/verify/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/",
  "source_line_start": 72,
  "source_line_end": 73,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L72-L73",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L72-L73",
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
- Source path: [`TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L72-L73)
- Source range: L72-L73
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T170` — Baryogenesis Exponent 15 = dim(τ³) × |generators|

## Immediate Comment / Docstring

```lean
/-- There are exactly 5 τ-generators. [V.T170] -/
```

## Source Excerpt

```lean
theorem tau_generator_count :
    [TauGenerator.alpha, .pi, .gamma, .eta, .omega].length = 5 := by rfl
```
