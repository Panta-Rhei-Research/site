---
{
  "projection_kind": "taulib_declaration",
  "title": "pred_lrd_upper_cutoff",
  "permalink": "/corpus/taulib/docs/book-v-cosmology-falsification-pack/pred-lrd-upper-cutoff/",
  "summary_short": "`def` declaration in `TauLib.BookV.Cosmology.FalsificationPack`.",
  "declaration_id": "TauLib.BookV.Cosmology.FalsificationPack::pred_lrd_upper_cutoff",
  "declaration_slug": "pred-lrd-upper-cutoff",
  "kind": "def",
  "name": "pred_lrd_upper_cutoff",
  "module_name": "TauLib.BookV.Cosmology.FalsificationPack",
  "module_url": "/corpus/taulib/docs/book-v-cosmology-falsification-pack/",
  "source_line_start": 195,
  "source_line_end": 214,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/FalsificationPack.lean#L195-L214",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/FalsificationPack.lean#L195-L214",
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
- Source path: [`TauLib/BookV/Cosmology/FalsificationPack.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/FalsificationPack.lean#L195-L214)
- Source range: L195-L214
- Kind: `def`
- Public role: `definition`
- Formal status hint: `definition`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Q5 (N15.B): V.T-LRD-1B upper cutoff at 10^(6.5 plus or minus 0.15) M_sun. -/
```

## Source Excerpt

```lean
def pred_lrd_upper_cutoff : TestablePrediction where
  name := "Q5 (N15.B): LRD seed upper cutoff at 10^(6.5+-0.15) M_sun"
  level := .Quantitative
  description :=
    "V.T-LRD-1B: upper cutoff at 10^(6.5+-0.15) M_sun." ++
    " TAU-DISTINCTIVE; load-bearing N15 signature 1 falsifier." ++
    " Anchored on V.T110 + new structural lemma" ++
    " J_max^{T^2} = iota_tau * sqrt(kappa_D) * G * M^2 / c" ++
    " (V.D-LRD-1d, currently in HeavySeedBirth.lean, not yet" ++
    " promoted to a separate registry entry). Wave R7 cross-" ++
    "validation: Specialists E (Wald-Carter-Penrose lens) and" ++
    " G (categorical/homological lens) independently converged" ++
    " on iota_tau-power exponent = 1. Cross-coupling:" ++
    " inflation N11 (A_s -> sigma_8 -> M_h^{ACH,max}" ++
    " normalisation, logarithmically weak)."
  status :=
    "Currently testable: KS test discriminating flat-with-cutoff" ++
    " vs orthodox DCBH power-law extension; 5 sigma at N >= 60" ++
    " Inayoshi-corrected LRDs (JWST cycle 4-5 sample)."
  currently_testable := true
```
