---
{
  "projection_kind": "taulib_declaration",
  "title": "higgs_mass_range",
  "permalink": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-mass-range/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.TauHiggs2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.TauHiggs2::higgs_mass_range",
  "declaration_slug": "higgs-mass-range",
  "kind": "theorem",
  "name": "higgs_mass_range",
  "module_name": "TauLib.BookIV.Electroweak.TauHiggs2",
  "module_url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/",
  "source_line_start": 241,
  "source_line_end": 244,
  "registry_ids": [
    "IV.P75"
  ],
  "related_registry_items": [
    {
      "id": "IV.P75",
      "title": "Higgs Mass Readout",
      "url": "/registry/object/IV.P75/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L241-L244",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.TauHiggs2",
        "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L241-L244",
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

- Module: [TauLib.BookIV.Electroweak.TauHiggs2](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/)
- Source path: [`TauLib/BookIV/Electroweak/TauHiggs2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L241-L244)
- Source range: L241-L244
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `IV.P75` — Higgs Mass Readout

## Immediate Comment / Docstring

```lean
/-- [IV.P75] The τ-predicted Higgs mass is in the range 124-126 GeV,
    consistent with the experimental measurement of 125.1 ± 0.14 GeV. -/
```

## Source Excerpt

```lean
theorem higgs_mass_range :
    tau_higgs_mass.mass_MeV > 124000 ∧
    tau_higgs_mass.mass_MeV < 126000 := by
  simp [tau_higgs_mass]
```
