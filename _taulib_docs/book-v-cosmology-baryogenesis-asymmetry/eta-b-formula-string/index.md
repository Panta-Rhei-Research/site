---
{
  "projection_kind": "taulib_declaration",
  "title": "eta_B_formula_string",
  "permalink": "/verify/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/eta-b-formula-string/",
  "summary_short": "`def` declaration in `TauLib.BookV.Cosmology.BaryogenesisAsymmetry`.",
  "declaration_id": "TauLib.BookV.Cosmology.BaryogenesisAsymmetry::eta_B_formula_string",
  "declaration_slug": "eta-b-formula-string",
  "kind": "def",
  "name": "eta_B_formula_string",
  "module_name": "TauLib.BookV.Cosmology.BaryogenesisAsymmetry",
  "module_url": "/verify/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/",
  "source_line_start": 131,
  "source_line_end": 136,
  "registry_ids": [
    "V.T172"
  ],
  "related_registry_items": [
    {
      "id": "V.T172",
      "title": "Primary Baryogenesis Formula: η_B = α·ι_τ¹⁵·(5/6)",
      "url": "/registry/object/V.T172/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L131-L136",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L131-L136",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
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
- Source path: [`TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L131-L136)
- Source range: L131-L136
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.T172` — Primary Baryogenesis Formula: η_B = α·ι_τ¹⁵·(5/6)

## Immediate Comment / Docstring

```lean
/-- Documentation of the primary baryogenesis formula [V.T172].

    η_B = α·ι_τ¹⁵·(5/6) = (121/270)·ι_τ¹⁹ ≈ 6.041 × 10⁻¹⁰
    Planck 2018: (6.104 ± 0.058) × 10⁻¹⁰
    Deviation: −1.03% (−1.09σ) — within observational uncertainty.

    Scope: τ-effective (upgraded from conjectural V.R324). -/
```

## Source Excerpt

```lean
def eta_B_formula_string : String :=
  "η_B = α·ι_τ¹⁵·(5/6) = (121/270)·ι_τ¹⁹ ≈ 6.041×10⁻¹⁰ " ++
  "(Planck 2018: 6.104×10⁻¹⁰, deviation −1.03%, −1.09σ). " ++
  "Structural basis: exponent 15 = dim(τ³)×|gen| = 3×5 (V.T170), " ++
  "(5/6) = threshold-counting coefficient shared with Y_p (V.T171), " ++
  "α = (121/225)·ι_τ⁴ gives algebraic form (121/270)·ι_τ¹⁹."
```
