---
{
  "projection_kind": "taulib_declaration",
  "title": "HiggsN7",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-n7/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.TauHiggs2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.TauHiggs2::HiggsN7",
  "declaration_slug": "higgs-n7",
  "kind": "structure",
  "name": "HiggsN7",
  "module_name": "TauLib.BookIV.Electroweak.TauHiggs2",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/",
  "source_line_start": 461,
  "source_line_end": 470,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L461-L470",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L461-L470",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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
- Source path: [`TauLib/BookIV/Electroweak/TauHiggs2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L461-L470)
- Source range: L461-L470
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- (4 - ι_τ³/(1-7κ_ω))/κ_ω × m_n = 125.2010 GeV at +8.0 ppm from PDG 125.20 GeV.
    n-scan: n=5: +892 ppm, n=6: +466 ppm, n=7: +8.0 ppm ***, n=8: -486 ppm.
    n=7 = 2×lobes + sectors = 2×2+3 (structural decomposition). -/
```

## Source Excerpt

```lean
structure HiggsN7 where
  /-- n=7 structural coefficient. -/
  n_value : Nat
  /-- n equals 7. -/
  n_eq : n_value = 7
  /-- Structural: 2×lobes + sectors. -/
  structural_decomp : n_value = 2 * 2 + 3
  /-- Within τ-effective threshold. -/
  tau_effective : Bool := true
  deriving Repr
```
