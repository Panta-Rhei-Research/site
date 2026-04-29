---
{
  "projection_kind": "taulib_declaration",
  "title": "mass_derivation_layer2",
  "permalink": "/verify/taulib/docs/book-v-coda-calibration-chain/mass-derivation-layer2-l74/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Coda.CalibrationChain`.",
  "declaration_id": "TauLib.BookV.Coda.CalibrationChain::mass_derivation_layer2",
  "declaration_slug": "mass-derivation-layer2-l74",
  "kind": "theorem",
  "name": "mass_derivation_layer2",
  "module_name": "TauLib.BookV.Coda.CalibrationChain",
  "module_url": "/verify/taulib/docs/book-v-coda-calibration-chain/",
  "source_line_start": 74,
  "source_line_end": 79,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/CalibrationChain.lean#L74-L79",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Coda.CalibrationChain",
        "url": "/verify/taulib/docs/book-v-coda-calibration-chain/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/CalibrationChain.lean#L74-L79",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookV.Coda.CalibrationChain](/verify/taulib/docs/book-v-coda-calibration-chain/)
- Source path: [`TauLib/BookV/Coda/CalibrationChain.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/CalibrationChain.lean#L74-L79)
- Source range: L74-L79
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Layer 2 derives 3 masses from 3 layers with single anchor. -/
```

## Source Excerpt

```lean
theorem mass_derivation_layer2 :
    mass_derivation.n_derived = 3 ∧
    mass_derivation.n_layers = 3 ∧
    mass_derivation.single_anchor = true ∧
    mass_derivation.zero_additional_params = true :=
  ⟨rfl, rfl, rfl, rfl⟩
```
