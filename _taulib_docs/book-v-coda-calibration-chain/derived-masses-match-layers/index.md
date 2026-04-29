---
{
  "projection_kind": "taulib_declaration",
  "title": "derived_masses_match_layers",
  "permalink": "/verify/taulib/docs/book-v-coda-calibration-chain/derived-masses-match-layers/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Coda.CalibrationChain`.",
  "declaration_id": "TauLib.BookV.Coda.CalibrationChain::derived_masses_match_layers",
  "declaration_slug": "derived-masses-match-layers",
  "kind": "theorem",
  "name": "derived_masses_match_layers",
  "module_name": "TauLib.BookV.Coda.CalibrationChain",
  "module_url": "/verify/taulib/docs/book-v-coda-calibration-chain/",
  "source_line_start": 82,
  "source_line_end": 84,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/CalibrationChain.lean#L82-L84",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/CalibrationChain.lean#L82-L84",
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
- Source path: [`TauLib/BookV/Coda/CalibrationChain.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/CalibrationChain.lean#L82-L84)
- Source range: L82-L84
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Derived mass count equals layer count: one mass per layer. -/
```

## Source Excerpt

```lean
theorem derived_masses_match_layers :
    mass_derivation.n_derived = mass_derivation.n_layers := by
  rw [mass_derivation.derived_eq, mass_derivation.layers_eq]
```
