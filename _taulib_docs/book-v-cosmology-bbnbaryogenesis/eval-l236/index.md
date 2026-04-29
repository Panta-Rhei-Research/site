---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L236",
  "permalink": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/eval-l236/",
  "summary_short": "`eval` declaration in `TauLib.BookV.Cosmology.BBNBaryogenesis`.",
  "declaration_id": "TauLib.BookV.Cosmology.BBNBaryogenesis::#eval:236",
  "declaration_slug": "eval-l236",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.BookV.Cosmology.BBNBaryogenesis",
  "module_url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/",
  "source_line_start": 236,
  "source_line_end": 236,
  "registry_ids": [
    "V.R323",
    "V.R324",
    "V.R325",
    "V.R326"
  ],
  "related_registry_items": [
    {
      "id": "V.R323",
      "title": "Commutator Magnitude at omega-Crossing",
      "url": "/registry/object/V.R323/"
    },
    {
      "id": "V.R324",
      "title": "eta_B Structural Candidate",
      "url": "/registry/object/V.R324/"
    },
    {
      "id": "V.R325",
      "title": "Primorial-Confinement Bridge",
      "url": "/registry/object/V.R325/"
    },
    {
      "id": "V.R326",
      "title": "Confinement Multiplicity Estimate",
      "url": "/registry/object/V.R326/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L236-L236",
  "formal_status": "computed",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L236-L236",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "eval",
      "status": "computed"
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
- Source path: [`TauLib/BookV/Cosmology/BBNBaryogenesis.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L236-L236)
- Source range: L236-L236
- Kind: `eval`
- Formal status hint: `computed`

## Registry Links

- `V.R323` — Commutator Magnitude at omega-Crossing
- `V.R324` — eta_B Structural Candidate
- `V.R325` — Primorial-Confinement Bridge
- `V.R326` — Confinement Multiplicity Estimate

## Immediate Comment / Docstring

```lean
-- ============================================================
-- REMARKS (comment-only)
-- ============================================================

-- [V.R323] Commutator magnitude |[H_γ, H_η]| ∼ κ(A,B) × κ(B,C)
-- = ι_τ⁸/(1−ι_τ) ≈ 2.80 × 10⁻⁴. Framework-level estimate:
-- the tree-level commutator at the ω-crossing sets the scale for
-- the baryon asymmetry.

-- [V.R324] η_B structural candidate: η_B = α·ι_τ¹⁵·(5/6)
-- = (121/270)·ι_τ¹⁹ ≈ 6.04 × 10⁻¹⁰ (−1.03% from Planck 2018).
-- Conjectural scope: the 5/6 domain-wall factor reappears from Y_p,
-- but the ι_τ¹⁵ exponent needs first-principles derivation.

-- [V.R325] Primorial bridge: p₁₅# / ι_τ³ ≈ 1.55 × 10¹⁹ matches
-- N_QCD = t_QCD/t_C ≈ 1.43 × 10¹⁹ at 8.2%. Framework scope.

-- [V.R326] Multiplicity estimate: N_mult = p₁₅# · κ(C;3)
-- ≈ 3.71 × 10¹⁶ (confinement fraction = ι_τ⁶/(1−ι_τ)). Framework.

-- ============================================================
-- SMOKE TESTS
-- ============================================================
```

## Source Excerpt

```lean
#eval threshold_admissibility.confinement_depth  -- 3
```
