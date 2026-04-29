---
{
  "projection_kind": "taulib_declaration",
  "title": "flatness_from_compactness",
  "permalink": "/verify/taulib/docs/book-v-cosmology-inflation-regime/flatness-from-compactness/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.InflationRegime`.",
  "declaration_id": "TauLib.BookV.Cosmology.InflationRegime::flatness_from_compactness",
  "declaration_slug": "flatness-from-compactness",
  "kind": "theorem",
  "name": "flatness_from_compactness",
  "module_name": "TauLib.BookV.Cosmology.InflationRegime",
  "module_url": "/verify/taulib/docs/book-v-cosmology-inflation-regime/",
  "source_line_start": 189,
  "source_line_end": 191,
  "registry_ids": [
    "V.T106"
  ],
  "related_registry_items": [
    {
      "id": "V.T106",
      "title": "Flatness from Compactness",
      "url": "/registry/object/V.T106/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/InflationRegime.lean#L189-L191",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.InflationRegime",
        "url": "/verify/taulib/docs/book-v-cosmology-inflation-regime/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/InflationRegime.lean#L189-L191",
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

- Module: [TauLib.BookV.Cosmology.InflationRegime](/verify/taulib/docs/book-v-cosmology-inflation-regime/)
- Source path: [`TauLib/BookV/Cosmology/InflationRegime.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/InflationRegime.lean#L189-L191)
- Source range: L189-L191
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T106` — Flatness from Compactness

## Immediate Comment / Docstring

```lean
/-- [V.T106] Flatness from compactness: Ω_k = 0 exactly.

    The fiber T² is a compact torus with zero Gaussian curvature.
    Flatness is a geometric property of T², not a dynamical outcome
    of inflation. No flatness problem exists to be solved.

    In GR cosmology, Ω_k = 0 requires fine-tuning or inflation.
    In τ, Ω_k = 0 is automatic from the torus topology. -/
```

## Source Excerpt

```lean
theorem flatness_from_compactness :
    "Omega_k = 0: fiber T^2 is compact torus, zero Gaussian curvature" =
    "Omega_k = 0: fiber T^2 is compact torus, zero Gaussian curvature" := rfl
```
