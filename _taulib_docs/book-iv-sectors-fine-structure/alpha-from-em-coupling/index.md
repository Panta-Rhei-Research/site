---
{
  "projection_kind": "taulib_declaration",
  "title": "alpha_from_em_coupling",
  "permalink": "/verify/taulib/docs/book-iv-sectors-fine-structure/alpha-from-em-coupling/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Sectors.FineStructure`.",
  "declaration_id": "TauLib.BookIV.Sectors.FineStructure::alpha_from_em_coupling",
  "declaration_slug": "alpha-from-em-coupling",
  "kind": "theorem",
  "name": "alpha_from_em_coupling",
  "module_name": "TauLib.BookIV.Sectors.FineStructure",
  "module_url": "/verify/taulib/docs/book-iv-sectors-fine-structure/",
  "source_line_start": 186,
  "source_line_end": 195,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/FineStructure.lean#L186-L195",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Sectors.FineStructure",
        "url": "/verify/taulib/docs/book-iv-sectors-fine-structure/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/FineStructure.lean#L186-L195",
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

- Module: [TauLib.BookIV.Sectors.FineStructure](/verify/taulib/docs/book-iv-sectors-fine-structure/)
- Source path: [`TauLib/BookIV/Sectors/FineStructure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/FineStructure.lean#L186-L195)
- Source range: L186-L195
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- α_spectral = (8/15) · κ(B;2)²: the fine structure constant
    is the EM self-coupling SQUARED, scaled by the primorial
    factor 8/15 = 2³/(3·5).

    Since κ(B;2) = ι_τ², we have:
    α = (8/15) · (ι_τ²)² = (8/15) · ι_τ⁴. -/
```

## Source Excerpt

```lean
theorem alpha_from_em_coupling :
    alpha_spectral_numer = 8 * (kappa_BB.numer * kappa_BB.numer) ∧
    alpha_spectral_denom = 15 * (kappa_BB.denom * kappa_BB.denom) := by
  constructor
  · simp [alpha_spectral_numer, kappa_BB,
          iota_fourth_numer, iota_sq_numer,
          iota, iota_tau_numer]
  · simp [alpha_spectral_denom, kappa_BB,
          iota_fourth_denom, iota_sq_denom,
          iotaD, iota_tau_denom]
```
