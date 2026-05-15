---
{
  "projection_kind": "taulib_declaration",
  "title": "correct_vs_wrong_ratio",
  "permalink": "/corpus/taulib/docs/book-iv-sectors-fine-structure/correct-vs-wrong-ratio/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Sectors.FineStructure`.",
  "declaration_id": "TauLib.BookIV.Sectors.FineStructure::correct_vs_wrong_ratio",
  "declaration_slug": "correct-vs-wrong-ratio",
  "kind": "theorem",
  "name": "correct_vs_wrong_ratio",
  "module_name": "TauLib.BookIV.Sectors.FineStructure",
  "module_url": "/corpus/taulib/docs/book-iv-sectors-fine-structure/",
  "source_line_start": 168,
  "source_line_end": 174,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/FineStructure.lean#L168-L174",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Sectors.FineStructure",
        "url": "/corpus/taulib/docs/book-iv-sectors-fine-structure/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/FineStructure.lean#L168-L174",
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

- Module: [TauLib.BookIV.Sectors.FineStructure](/corpus/taulib/docs/book-iv-sectors-fine-structure/)
- Source path: [`TauLib/BookIV/Sectors/FineStructure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/FineStructure.lean#L168-L174)
- Source range: L168-L174
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The correct and wrong formulas differ by the ratio 128/15.
    correct/wrong = (8/15)/(1/16) = 128/15.
    Cross-multiplied: correct_numer · wrong_denom · 15 = wrong_numer · correct_denom · 128. -/
```

## Source Excerpt

```lean
theorem correct_vs_wrong_ratio :
    alpha_spectral_numer * wrong_alpha_denom * 15 =
    wrong_alpha_numer * alpha_spectral_denom * 128 := by
  simp [alpha_spectral_numer, alpha_spectral_denom,
        wrong_alpha_numer, wrong_alpha_denom,
        iota_fourth_numer, iota_fourth_denom]
  ring
```
