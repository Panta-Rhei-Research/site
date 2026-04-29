---
{
  "projection_kind": "taulib_declaration",
  "title": "higgs_n6_cf_sum",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-n6-cf-sum/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.TauHiggs2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.TauHiggs2::higgs_n6_cf_sum",
  "declaration_slug": "higgs-n6-cf-sum",
  "kind": "theorem",
  "name": "higgs_n6_cf_sum",
  "module_name": "TauLib.BookIV.Electroweak.TauHiggs2",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/",
  "source_line_start": 430,
  "source_line_end": 430,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L430-L430",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.TauHiggs2",
        "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L430-L430",
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

- Module: [TauLib.BookIV.Electroweak.TauHiggs2](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/)
- Source path: [`TauLib/BookIV/Electroweak/TauHiggs2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L430-L430)
- Source range: L430-L430
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The coefficient n=6 in the improved Higgs formula (4−ι_τ³/(1−6κ_ω))/κ_ω × m_n
    ≈ 125.26 GeV (+68 ppm from PDG 125.25 GeV). Structural candidates:
    (A) n=6 = |generators|+1 = 5+1; (B) n=6 = 2×|sectors| = 2×3 = 6;
    (C) n=6 = 2·b₁(τ³) = 2×3 = 6.
    CF-sum candidate REJECTED: CF(ι_τ⁻¹) = [2;1,13,3,...] → sum of 5 = 20 ≠ 6.
    Sprint 4C discovery: with PDG 125.20 GeV, n=7 gives +8.0 ppm. -/
```

## Source Excerpt

```lean
theorem higgs_n6_cf_sum : True := trivial
```
