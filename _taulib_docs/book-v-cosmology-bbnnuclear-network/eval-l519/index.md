---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L519",
  "permalink": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/eval-l519/",
  "summary_short": "`eval` declaration in `TauLib.BookV.Cosmology.BBNNuclearNetwork`.",
  "declaration_id": "TauLib.BookV.Cosmology.BBNNuclearNetwork::#eval:519",
  "declaration_slug": "eval-l519",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.BookV.Cosmology.BBNNuclearNetwork",
  "module_url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/",
  "source_line_start": 519,
  "source_line_end": 519,
  "registry_ids": [
    "V.R427",
    "V.R428",
    "V.R429",
    "V.R430",
    "V.R431",
    "V.R432",
    "V.R433",
    "V.R434",
    "V.R435",
    "V.R436",
    "V.R437",
    "V.R438"
  ],
  "related_registry_items": [
    {
      "id": "V.R427",
      "title": "D/H Anti-correlation",
      "url": "/registry/object/V.R427/"
    },
    {
      "id": "V.R428",
      "title": "N3 Status Upgrade",
      "url": "/registry/object/V.R428/"
    },
    {
      "id": "V.R429",
      "title": "⁷Be Production as B-Sector",
      "url": "/registry/object/V.R429/"
    },
    {
      "id": "V.R430",
      "title": "EM Phase-Space Restriction",
      "url": "/registry/object/V.R430/"
    },
    {
      "id": "V.R431",
      "title": "Voxel Packing Connection",
      "url": "/registry/object/V.R431/"
    },
    {
      "id": "V.R432",
      "title": "Packing Threshold at A = 7",
      "url": "/registry/object/V.R432/"
    },
    {
      "id": "V.R433",
      "title": "Stellar Depletion and Spite Plateau",
      "url": "/registry/object/V.R433/"
    },
    {
      "id": "V.R434",
      "title": "All Four from Single η_B",
      "url": "/registry/object/V.R434/"
    },
    {
      "id": "V.R435",
      "title": "N3 Falsification Update",
      "url": "/registry/object/V.R435/"
    },
    {
      "id": "V.R436",
      "title": "N4 Falsification Update",
      "url": "/registry/object/V.R436/"
    },
    {
      "id": "V.R437",
      "title": "Wave 25 BBN Prediction Table",
      "url": "/registry/object/V.R437/"
    },
    {
      "id": "V.R438",
      "title": "Cross-Sprint Consistency",
      "url": "/registry/object/V.R438/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L519-L519",
  "formal_status": "computed",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.BBNNuclearNetwork",
        "url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L519-L519",
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

- Module: [TauLib.BookV.Cosmology.BBNNuclearNetwork](/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/)
- Source path: [`TauLib/BookV/Cosmology/BBNNuclearNetwork.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L519-L519)
- Source range: L519-L519
- Kind: `eval`
- Formal status hint: `computed`

## Registry Links

- `V.R427` — D/H Anti-correlation
- `V.R428` — N3 Status Upgrade
- `V.R429` — ⁷Be Production as B-Sector
- `V.R430` — EM Phase-Space Restriction
- `V.R431` — Voxel Packing Connection
- `V.R432` — Packing Threshold at A = 7
- `V.R433` — Stellar Depletion and Spite Plateau
- `V.R434` — All Four from Single η_B
- `V.R435` — N3 Falsification Update
- `V.R436` — N4 Falsification Update
- `V.R437` — Wave 25 BBN Prediction Table
- `V.R438` — Cross-Sprint Consistency

## Immediate Comment / Docstring

```lean
-- ============================================================
-- REMARKS (comment-only)
-- ============================================================

-- [V.R427] D/H anti-correlation: lower η_B → less D-burning → higher
-- D/H. The sensitivity d(ln(D/H))/d(ln η_B) ≈ −1.6 is a standard BBN
-- result. The +2.3σ overshoot is physically expected from the −1.03%
-- shift in η_B(τ) relative to Planck.

-- [V.R428] N3 status upgrade: with Theorem D/H from τ, falsification
-- item N3 upgrades from Contact (~5%) to τ-effective (+2.3σ).

-- [V.R429] ⁷Be production (Reaction 9) is B-sector (EM radiative
-- capture). The B-sector coupling κ(B;2) = ι_τ² operates in the 2D
-- fiber T², providing the mechanism for selective suppression.

-- [V.R430] The suppression is specific to EM radiative captures
-- (B-sector). Strong-sector (C-sector) reactions are unaffected because
-- they operate through the full τ³ geometry.

-- [V.R431] 1/3 = 1/dim(τ³) connects to: stride 3 in He-4 packing
-- (V.D192), 15 = 3×5 baryogenesis exponent (V.T170), and 3 generations
-- from H₁(τ³;ℤ) ≅ ℤ³.

-- [V.R432] Nuclei with A ≤ 4 fit the 2×2×2 voxel block within
-- the 3×3×3 macrocell. A = 7 cannot tile → EM capture must span
-- the full τ³, triggering the dimensional restriction S = 1/3.

-- [V.R433] Standard stellar models predict ~15% surface lithium
-- depletion. Applied: 1.87×10⁻¹⁰ × 0.85 = 1.59×10⁻¹⁰, matching
-- the Spite plateau (1.6 ± 0.3) × 10⁻¹⁰ essentially exactly.

-- [V.R434] All four light-element abundances from a single η_B
-- = (121/270)·ι_τ¹⁹. Zero free parameters. Nuclear physics is
-- standard; only the cosmological input differs from SBBN.

-- [V.R435] N3 falsification update: D/H precision upgraded from
-- ~5% to +2.3σ, scope from Contact to τ-effective.

-- [V.R436] N4 falsification update: Li-7 prediction upgraded from
-- "factor of 2" to "+0.9σ", with 1/3 fiber suppression mechanism.

-- [V.R437] Wave 25 BBN prediction table: 4 species, single η_B,
-- zero free parameters. Worst deviation +2.3σ (D/H). Lithium problem
-- resolved at +0.9σ.

-- [V.R438] Cross-sprint consistency: the factor 1/3 = dim(τ¹)/dim(τ³)
-- that resolves the lithium problem is the same structural constant
-- appearing in He-4 packing, baryogenesis, and generation counting.

-- ============================================================
-- SMOKE TESTS
-- ============================================================
```

## Source Excerpt

```lean
#eval deuterium_bottleneck.temp_001MeV      -- 7
```
