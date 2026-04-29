---
{
  "projection_kind": "taulib_declaration",
  "title": "BHEntropyFormula",
  "permalink": "/verify/taulib/docs/book-v-cosmology-no-shrink-extended/bhentropy-formula/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.NoShrinkExtended`.",
  "declaration_id": "TauLib.BookV.Cosmology.NoShrinkExtended::BHEntropyFormula",
  "declaration_slug": "bhentropy-formula",
  "kind": "structure",
  "name": "BHEntropyFormula",
  "module_name": "TauLib.BookV.Cosmology.NoShrinkExtended",
  "module_url": "/verify/taulib/docs/book-v-cosmology-no-shrink-extended/",
  "source_line_start": 215,
  "source_line_end": 224,
  "registry_ids": [
    "V.P96"
  ],
  "related_registry_items": [
    {
      "id": "V.P96",
      "title": "BH Entropy Formula",
      "url": "/registry/object/V.P96/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/NoShrinkExtended.lean#L215-L224",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.NoShrinkExtended",
        "url": "/verify/taulib/docs/book-v-cosmology-no-shrink-extended/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/NoShrinkExtended.lean#L215-L224",
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

- Module: [TauLib.BookV.Cosmology.NoShrinkExtended](/verify/taulib/docs/book-v-cosmology-no-shrink-extended/)
- Source path: [`TauLib/BookV/Cosmology/NoShrinkExtended.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/NoShrinkExtended.lean#L215-L224)
- Source range: L215-L224
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.P96` — BH Entropy Formula

## Immediate Comment / Docstring

```lean
/-- [V.P96] BH entropy: S_BH = k_B · A / (4 · ι_τ²).

    Derived from boundary counting: the torus horizon T² with area A
    has boundary character degrees of freedom proportional to A/ι_τ².
    The factor 4 comes from the bipolar splitting (2 lobes × 2 sectors). -/
```

## Source Excerpt

```lean
structure BHEntropyFormula where
  /-- Number of lobes (always 2). -/
  num_lobes : Nat := 2
  /-- Number of sectors in bipolar split (always 2). -/
  num_bipolar : Nat := 2
  /-- Area quantum is ι_τ². -/
  area_quantum_label : String := "iota_tau^2"
  /-- Prefactor is 1/(4·ι_τ²) = num_lobes × num_bipolar denominator. -/
  prefactor_denom : Nat := 4
  deriving Repr
```
