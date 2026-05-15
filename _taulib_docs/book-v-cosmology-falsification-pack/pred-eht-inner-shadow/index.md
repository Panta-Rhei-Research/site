---
{
  "projection_kind": "taulib_declaration",
  "title": "pred_eht_inner_shadow",
  "permalink": "/corpus/taulib/docs/book-v-cosmology-falsification-pack/pred-eht-inner-shadow/",
  "summary_short": "`def` declaration in `TauLib.BookV.Cosmology.FalsificationPack`.",
  "declaration_id": "TauLib.BookV.Cosmology.FalsificationPack::pred_eht_inner_shadow",
  "declaration_slug": "pred-eht-inner-shadow",
  "kind": "def",
  "name": "pred_eht_inner_shadow",
  "module_name": "TauLib.BookV.Cosmology.FalsificationPack",
  "module_url": "/corpus/taulib/docs/book-v-cosmology-falsification-pack/",
  "source_line_start": 342,
  "source_line_end": 350,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/FalsificationPack.lean#L342-L350",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/FalsificationPack.lean#L342-L350",
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
- Source path: [`TauLib/BookV/Cosmology/FalsificationPack.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/FalsificationPack.lean#L342-L350)
- Source range: L342-L350
- Kind: `def`
- Public role: `definition`
- Formal status hint: `definition`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- N17 (Q9): EHT inner shadow at viewing inclinations ι ∈ [30°, 50°]
    (V.T-EHT application).

    V.T-EHT predicts: at ι < ι_crit = arccos(ι_τ) ≈ 70.04° from polar
    axis, a SECOND smaller dark region appears at the center of the
    bright photon ring. No analogue in S² (Schwarzschild/Kerr).

    M87* (i ~17°) and Sgr A* (i ~30°) both within visible regime per
    V.T-EHT. Currently UNADDRESSED in published EHT analyses (Chael+2021
    inner shadow is topologically distinct Kerr+MAD-disk feature).
    Distinguishable from Chael via inclination dependence: V.T-EHT has
    sharp cutoff at ι > 70°; Chael has eccentricity that grows with ι.

    ngEHT Phase 2 (early 2030s) is threshold instrument for definitive
    discrimination. Re-imaging of existing EHT data with inner-shadow
    methodology (Chael+2021 framework) provides first-pass test. -/
```

## Source Excerpt

```lean
def pred_eht_inner_shadow : TestablePrediction where
  name := "Q9 (N17): EHT inner shadow at iota in [30°, 50°] (V.T-EHT)"
  level := .Quantitative
  description :=
    "V.T-EHT: inner shadow visible for iota < arccos(iota_tau) ~ 70°. " ++
    "Falsifier: high-quality EHT image at iota in [30°, 50°] showing NO " ++
    "inner shadow refutes V.T95 + V.T110."
  status := "Testable with EHT 2024+ runs (M87*, Sgr A*) at deeper depth."
  currently_testable := true
```
