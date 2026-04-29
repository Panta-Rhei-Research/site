---
{
  "projection_kind": "taulib_declaration",
  "title": "sigma_exponent_asymmetry",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/sigma-exponent-asymmetry-l654/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.NeutrinoMode`.",
  "declaration_id": "TauLib.BookIV.Electroweak.NeutrinoMode::sigma_exponent_asymmetry",
  "declaration_slug": "sigma-exponent-asymmetry-l654",
  "kind": "theorem",
  "name": "sigma_exponent_asymmetry",
  "module_name": "TauLib.BookIV.Electroweak.NeutrinoMode",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/",
  "source_line_start": 654,
  "source_line_end": 659,
  "registry_ids": [
    "V.P128"
  ],
  "related_registry_items": [
    {
      "id": "V.P128",
      "title": "Asymmetry in sigma-Exponents: Delta_pq - Delta_pr approx 2/13 (CF-structural candidate)",
      "url": "/registry/object/V.P128/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L654-L659",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.NeutrinoMode",
        "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L654-L659",
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

- Module: [TauLib.BookIV.Electroweak.NeutrinoMode](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/)
- Source path: [`TauLib/BookIV/Electroweak/NeutrinoMode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L654-L659)
- Source range: L654-L659
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P128` — Asymmetry in sigma-Exponents: Delta_pq - Delta_pr approx 2/13 (CF-structural candidate)

## Immediate Comment / Docstring

```lean
/-- [V.P128] Conjunction: a₂=13, numerator=2, CF-structural, approximate. -/
```

## Source Excerpt

```lean
theorem sigma_exponent_asymmetry :
    sigma_exponent_asymmetry_data.cf_coefficient = 13 ∧
    sigma_exponent_asymmetry_data.asymmetry_numerator = 2 ∧
    sigma_exponent_asymmetry_data.is_cf_structural = true ∧
    sigma_exponent_asymmetry_data.cf_approximate = true :=
  ⟨rfl, rfl, rfl, rfl⟩
```
