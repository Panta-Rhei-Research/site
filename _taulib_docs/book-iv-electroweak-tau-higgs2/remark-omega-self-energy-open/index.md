---
{
  "projection_kind": "taulib_declaration",
  "title": "remark_omega_self_energy_open",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/remark-omega-self-energy-open/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Electroweak.TauHiggs2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.TauHiggs2::remark_omega_self_energy_open",
  "declaration_slug": "remark-omega-self-energy-open",
  "kind": "def",
  "name": "remark_omega_self_energy_open",
  "module_name": "TauLib.BookIV.Electroweak.TauHiggs2",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/",
  "source_line_start": 409,
  "source_line_end": 410,
  "registry_ids": [
    "IV.R399"
  ],
  "related_registry_items": [
    {
      "id": "IV.R399",
      "title": "Open: omega Self-Energy Correction and Coefficient-6 Identification",
      "url": "/registry/object/IV.R399/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L409-L410",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L409-L410",
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
- Source path: [`TauLib/BookIV/Electroweak/TauHiggs2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L409-L410)
- Source range: L409-L410
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.R399` — Open: omega Self-Energy Correction and Coefficient-6 Identification

## Immediate Comment / Docstring

```lean
/-- [IV.R399] Open remark: structural identification of coefficient 6 in the
    bonus formula (4 − ι_τ³/(1−6κ_ω))/κ_ω = 133.315 at +68 ppm. -/
```

## Source Excerpt

```lean
def remark_omega_self_energy_open : String :=
  "Open: coefficient 6 in n=6 formula (+68 ppm) — possible: 6=W_3(4)+1, 6=2*b1(tau^3), or higher CF-window value"
```
