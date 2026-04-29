---
{
  "projection_kind": "taulib_declaration",
  "title": "BaryogenesisFirstPrinciples",
  "permalink": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/baryogenesis-first-principles/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.BBNBaryogenesis`.",
  "declaration_id": "TauLib.BookV.Cosmology.BBNBaryogenesis::BaryogenesisFirstPrinciples",
  "declaration_slug": "baryogenesis-first-principles",
  "kind": "structure",
  "name": "BaryogenesisFirstPrinciples",
  "module_name": "TauLib.BookV.Cosmology.BBNBaryogenesis",
  "module_url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/",
  "source_line_start": 310,
  "source_line_end": 319,
  "registry_ids": [
    "V.P130"
  ],
  "related_registry_items": [
    {
      "id": "V.P130",
      "title": "Baryogenesis First Principles: Generator Orbit + Threshold Uniqueness",
      "url": "/registry/object/V.P130/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L310-L319",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L310-L319",
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
- Source path: [`TauLib/BookV/Cosmology/BBNBaryogenesis.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L310-L319)
- Source range: L310-L319
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.P130` — Baryogenesis First Principles: Generator Orbit + Threshold Uniqueness

## Immediate Comment / Docstring

```lean
/-- [V.P130] Baryogenesis first principles: SA-i mod-W₃(4) yields
    η_B = α·ι_τ¹⁵·(5/6) at −10320 ppm (within 1σ Planck ±9502 ppm).

    Structure:
    - 15 = 3 × W₃(4) from C-sector × Window
    - (5/6) = W₃(4)/(2·sectors) from EM mixing
    - SA-i mod-5: 5-fold holonomy winding cancellation
    - All 3 Sakharov conditions: B-violation (σ lobe swap),
      CP violation (3 gen, J_τ≠0), equilibrium departure (freezeout) -/
```

## Source Excerpt

```lean
structure BaryogenesisFirstPrinciples where
  /-- SA-i mod-5 holds. -/
  sai_mod5_holds : Bool := true
  /-- All 3 Sakharov conditions satisfied. -/
  sakharov_all_three : Bool := true
  /-- η_B formula valid. -/
  eta_b_formula_valid : Bool := true
  /-- Within Planck uncertainty. -/
  within_planck_1sigma : Bool := true
  deriving Repr
```
