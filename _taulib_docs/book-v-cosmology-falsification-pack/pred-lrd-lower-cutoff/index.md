---
{
  "projection_kind": "taulib_declaration",
  "title": "pred_lrd_lower_cutoff",
  "permalink": "/corpus/taulib/docs/book-v-cosmology-falsification-pack/pred-lrd-lower-cutoff/",
  "summary_short": "`def` declaration in `TauLib.BookV.Cosmology.FalsificationPack`.",
  "declaration_id": "TauLib.BookV.Cosmology.FalsificationPack::pred_lrd_lower_cutoff",
  "declaration_slug": "pred-lrd-lower-cutoff",
  "kind": "def",
  "name": "pred_lrd_lower_cutoff",
  "module_name": "TauLib.BookV.Cosmology.FalsificationPack",
  "module_url": "/corpus/taulib/docs/book-v-cosmology-falsification-pack/",
  "source_line_start": 177,
  "source_line_end": 192,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/FalsificationPack.lean#L177-L192",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/FalsificationPack.lean#L177-L192",
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
- Source path: [`TauLib/BookV/Cosmology/FalsificationPack.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/FalsificationPack.lean#L177-L192)
- Source range: L177-L192
- Kind: `def`
- Public role: `definition`
- Formal status hint: `definition`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Q4 (N15.A): V.T-LRD-1A lower cutoff at 10^4.5 M_sun. -/
```

## Source Excerpt

```lean
def pred_lrd_lower_cutoff : TestablePrediction where
  name := "Q4 (N15.A): LRD seed lower cutoff at 10^4.5 M_sun"
  level := .Quantitative
  description :=
    "V.T-LRD-1A: lower cutoff at 10^4.5 M_sun. ORTHODOX-IMPORTED" ++
    " on value (atomic-cooling halo floor, V.D-LRD-1a;" ++
    " Bromm-Loeb 2003), TAU-DISTINCTIVE on sharpness (V.T109" ++
    " d_top=1 + V.T110 T^2 horizon excludes Pop-III remnant" ++
    " tail). Cross-coupling: V.T108 BBN H-cooling (mu = 0.6" ++
    " from Y_p = 20/81); V.T88 mass gap (S^2 vs T^2 horizon" ++
    " distinction)."
  status :=
    "Pending Inayoshi-corrected M_BH function from JWST cycle 4-5;" ++
    " requires N >= 60 LRDs with M_BH > 10^5.5 M_sun for KS-test" ++
    " 5 sigma."
  currently_testable := false
```
