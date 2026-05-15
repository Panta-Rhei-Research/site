---
{
  "projection_kind": "taulib_declaration",
  "title": "chain_length",
  "permalink": "/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/chain-length/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Calibration.MassRatioFormula`.",
  "declaration_id": "TauLib.BookIV.Calibration.MassRatioFormula::chain_length",
  "declaration_slug": "chain-length",
  "kind": "theorem",
  "name": "chain_length",
  "module_name": "TauLib.BookIV.Calibration.MassRatioFormula",
  "module_url": "/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/",
  "source_line_start": 363,
  "source_line_end": 363,
  "registry_ids": [
    "IV.T15"
  ],
  "related_registry_items": [
    {
      "id": "IV.T15",
      "title": "Derivation Chain Complete",
      "url": "/registry/object/IV.T15/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/MassRatioFormula.lean#L363-L363",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Calibration.MassRatioFormula",
        "url": "/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/MassRatioFormula.lean#L363-L363",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookIV.Calibration.MassRatioFormula](/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/)
- Source path: [`TauLib/BookIV/Calibration/MassRatioFormula.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/MassRatioFormula.lean#L363-L363)
- Source range: L363-L363
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `IV.T15` — Derivation Chain Complete

## Immediate Comment / Docstring

```lean
/-- [IV.T15] The chain has exactly 10 links. -/
```

## Source Excerpt

```lean
theorem chain_length : r_derivation_chain.length = 10 := by rfl
```
