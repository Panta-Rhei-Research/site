---
{
  "projection_kind": "taulib_declaration",
  "title": "higgs_n6_formula",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-n6-formula/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Electroweak.TauHiggs2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.TauHiggs2::higgs_n6_formula",
  "declaration_slug": "higgs-n6-formula",
  "kind": "def",
  "name": "higgs_n6_formula",
  "module_name": "TauLib.BookIV.Electroweak.TauHiggs2",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/",
  "source_line_start": 433,
  "source_line_end": 434,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L433-L434",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L433-L434",
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
- Source path: [`TauLib/BookIV/Electroweak/TauHiggs2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L433-L434)
- Source range: L433-L434
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
-- CF(ι_τ⁻¹) = [2;1,13,3,1,1,1,42,...] — third term is 13, NOT 1
```

## Source Excerpt

```lean
def higgs_n6_formula : String :=
  "m_H = (4 - ι_τ³/(1 - 6κ_ω))/κ_ω × m_n ≈ 125.26 GeV (+68 ppm, PDG 125.25; n=7 gives +8 ppm with PDG 125.20)"
```
