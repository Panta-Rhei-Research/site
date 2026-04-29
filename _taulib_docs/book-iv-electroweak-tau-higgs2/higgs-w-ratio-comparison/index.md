---
{
  "projection_kind": "taulib_declaration",
  "title": "higgs_w_ratio_comparison",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-w-ratio-comparison/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Electroweak.TauHiggs2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.TauHiggs2::higgs_w_ratio_comparison",
  "declaration_slug": "higgs-w-ratio-comparison",
  "kind": "def",
  "name": "higgs_w_ratio_comparison",
  "module_name": "TauLib.BookIV.Electroweak.TauHiggs2",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/",
  "source_line_start": 404,
  "source_line_end": 405,
  "registry_ids": [
    "IV.P188"
  ],
  "related_registry_items": [
    {
      "id": "IV.P188",
      "title": "m_H/m_W Ratio [auto-upgrades with IV.P199]",
      "url": "/registry/object/IV.P188/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L404-L405",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L404-L405",
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
- Source path: [`TauLib/BookIV/Electroweak/TauHiggs2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L404-L405)
- Source range: L404-L405
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.P188` — m_H/m_W Ratio [auto-upgrades with IV.P199]

## Immediate Comment / Docstring

```lean
/-- [IV.P188] m_H/m_W ratio from ω-sector (Higgs) and A-sector (W boson) NLO formulas.
    PDG: m_H/m_W = 125.25/80.3692 = 1.55840.
    τ-prediction (NLO): m_H/m_W = 1.55899, deviation +379 ppm.
    Uses IV.T151 (Higgs, +493 ppm) and IV.T148 (M_W, −0.42 ppm). -/
```

## Source Excerpt

```lean
def higgs_w_ratio_comparison : String :=
  "m_H/m_W: PDG=1.55840, tau(NLO)=1.55899, deviation=+379 ppm [conjectural]"
```
