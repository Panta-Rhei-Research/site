---
{
  "projection_kind": "taulib_declaration",
  "title": "pred_lrd_flat_shape",
  "permalink": "/corpus/taulib/docs/book-v-cosmology-falsification-pack/pred-lrd-flat-shape/",
  "summary_short": "`def` declaration in `TauLib.BookV.Cosmology.FalsificationPack`.",
  "declaration_id": "TauLib.BookV.Cosmology.FalsificationPack::pred_lrd_flat_shape",
  "declaration_slug": "pred-lrd-flat-shape",
  "kind": "def",
  "name": "pred_lrd_flat_shape",
  "module_name": "TauLib.BookV.Cosmology.FalsificationPack",
  "module_url": "/corpus/taulib/docs/book-v-cosmology-falsification-pack/",
  "source_line_start": 217,
  "source_line_end": 234,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/FalsificationPack.lean#L217-L234",
  "formal_status": "defined",
  "declaration_role": "definition",
  "formal_status_label": "definition",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.FalsificationPack",
        "url": "/corpus/taulib/docs/book-v-cosmology-falsification-pack/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/FalsificationPack.lean#L217-L234",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "definition",
      "status": "definition"
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

- Module: [TauLib.BookV.Cosmology.FalsificationPack](/corpus/taulib/docs/book-v-cosmology-falsification-pack/)
- Source path: [`TauLib/BookV/Cosmology/FalsificationPack.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/FalsificationPack.lean#L217-L234)
- Source range: L217-L234
- Kind: `def`
- Public role: `definition`
- Formal status hint: `definition`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Q6 (N15.C): V.T-LRD-1C flat interior |dlogN/dlogM| ≤ 0.3. -/
```

## Source Excerpt

```lean
def pred_lrd_flat_shape : TestablePrediction where
  name := "Q6 (N15.C): LRD seed flat interior shape |beta| <= 0.3"
  level := .Quantitative
  description :=
    "V.T-LRD-1C: |dlogN/dlogM_BH| <= 0.3 in interior" ++
    " 10^4.5-10^6.5 M_sun. TAU-DISTINCTIVE: unit Jacobian" ++
    " |dlogM_BH/dlogλ| = 1 from T^2-coherence f_BH(λ) prop 1/λ" ++
    " in regime λ > λ_⋆ ~ iota_tau * λ_bar. Discriminator vs" ++
    " orthodox DCBH (β ≈ -0.9 from Sheth-Tormen halo-MF" ++
    " inheritance) at > 5 sigma for N >= 60 LRDs. Wave R7" ++
    " Specialist G provides homological grounding via coherence" ++
    " projection Pi_coh on H_1(T^2;Z) tensor R. Cross-coupling:" ++
    " V.T110 (the unit-Jacobian lemma is a structural extension" ++
    " of V.T110, not yet a separate registry entry)."
  status :=
    "Currently testable: same JWST cycle 4-5 sample as Q5;" ++
    " statistical comparison of flat-shape vs power-law DCBH."
  currently_testable := true
```
