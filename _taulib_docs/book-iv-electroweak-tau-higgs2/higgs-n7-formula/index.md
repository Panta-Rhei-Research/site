---
{
  "projection_kind": "taulib_declaration",
  "title": "higgs_n7_formula",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-n7-formula/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Electroweak.TauHiggs2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.TauHiggs2::higgs_n7_formula",
  "declaration_slug": "higgs-n7-formula",
  "kind": "def",
  "name": "higgs_n7_formula",
  "module_name": "TauLib.BookIV.Electroweak.TauHiggs2",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/",
  "source_line_start": 453,
  "source_line_end": 455,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L453-L455",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L453-L455",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
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
- Source path: [`TauLib/BookIV/Electroweak/TauHiggs2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L453-L455)
- Source range: L453-L455
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- n=7 = 2×|lobes| + |force sectors| = 2×2+3 = 7 (best structural ID).
    Lemniscate L=S¹∨S¹ has 2 lobes × 2 polarities + 3 non-ω sectors {A,B,C}.
    Alternative: n=7 = b₁(τ³)+b₂(τ³)+1 = 3+3+1. CF analysis: n=7 NOT a CF convergent. -/
```

## Source Excerpt

```lean
def higgs_n7_formula : String :=
  "m_H = (4 - ι_τ³/(1-7κ_ω))/κ_ω × m_n ≈ 125.20 GeV (+8.0 ppm, PDG 125.20 GeV, tau-effective). " ++
  "n=7 = 2×lobes+sectors = 2×2+3 (best structural ID)."
```
