---
{
  "projection_kind": "taulib_declaration",
  "title": "BaryogenesisSAIMechanism",
  "permalink": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/baryogenesis-saimechanism/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.BBNBaryogenesis`.",
  "declaration_id": "TauLib.BookV.Cosmology.BBNBaryogenesis::BaryogenesisSAIMechanism",
  "declaration_slug": "baryogenesis-saimechanism",
  "kind": "structure",
  "name": "BaryogenesisSAIMechanism",
  "module_name": "TauLib.BookV.Cosmology.BBNBaryogenesis",
  "module_url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/",
  "source_line_start": 257,
  "source_line_end": 272,
  "registry_ids": [
    "V.D238"
  ],
  "related_registry_items": [
    {
      "id": "V.D238",
      "title": "SA-i mod-W₃(4) Baryogenesis Mechanism: ι_τ¹⁵ = (ι_τ³)^W₃(4)",
      "url": "/registry/object/V.D238/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L257-L272",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.BBNBaryogenesis",
        "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L257-L272",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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

- Module: [TauLib.BookV.Cosmology.BBNBaryogenesis](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/)
- Source path: [`TauLib/BookV/Cosmology/BBNBaryogenesis.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L257-L272)
- Source range: L257-L272
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D238` — SA-i mod-W₃(4) Baryogenesis Mechanism: ι_τ¹⁵ = (ι_τ³)^W₃(4)

## Immediate Comment / Docstring

```lean
/-- [V.D238] SA-i mod-W₃(4) baryogenesis mechanism.
    η_B = α·ι_τ^15·(5/6): ι_τ^15=(ι_τ³)^W₃(4) from SA-i mod-5.
    (5/6)=W₃(4)/(2·sectors)=5/6.

    - Geometric sum: S₅ = Σ_{k=0}^{4} ι_τ^{3k} = (1−ι_τ¹⁵)/(1−ι_τ³)
    - Each generator contributes ι_τ^{dim(τ³)} = ι_τ³
    - Parallel: SA-i mod-3 → θ_QCD=0 (IV.T160); SA-i mod-5 → baryogenesis -/
```

## Source Excerpt

```lean
structure BaryogenesisSAIMechanism where
  /-- SA-i modulus = W₃(4) = 5. -/
  sai_modulus : Nat
  /-- Modulus equals 5. -/
  modulus_eq : sai_modulus = 5
  /-- Exponent = dim(τ³) × modulus = 15. -/
  exponent : Nat
  /-- Exponent equals 15. -/
  exponent_eq : exponent = 15
  /-- Exponent = 3 × 5. -/
  exponent_decomp : exponent = 3 * sai_modulus
  /-- Coefficient numerator = W₃(4) = 5. -/
  coeff_num : Nat := 5
  /-- Coefficient denominator = 2 × sectors = 6. -/
  coeff_den : Nat := 6
  deriving Repr
```
