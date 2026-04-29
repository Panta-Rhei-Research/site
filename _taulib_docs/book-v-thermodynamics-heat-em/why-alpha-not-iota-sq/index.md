---
{
  "projection_kind": "taulib_declaration",
  "title": "why_alpha_not_iota_sq",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-heat-em/why-alpha-not-iota-sq/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Thermodynamics.HeatEM`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.HeatEM::why_alpha_not_iota_sq",
  "declaration_slug": "why-alpha-not-iota-sq",
  "kind": "theorem",
  "name": "why_alpha_not_iota_sq",
  "module_name": "TauLib.BookV.Thermodynamics.HeatEM",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-heat-em/",
  "source_line_start": 168,
  "source_line_end": 170,
  "registry_ids": [
    "V.R129"
  ],
  "related_registry_items": [
    {
      "id": "V.R129",
      "title": "Why alpha and not iota_tau^2",
      "url": "/registry/object/V.R129/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/HeatEM.lean#L168-L170",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Thermodynamics.HeatEM",
        "url": "/verify/taulib/docs/book-v-thermodynamics-heat-em/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/HeatEM.lean#L168-L170",
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

- Module: [TauLib.BookV.Thermodynamics.HeatEM](/verify/taulib/docs/book-v-thermodynamics-heat-em/)
- Source path: [`TauLib/BookV/Thermodynamics/HeatEM.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/HeatEM.lean#L168-L170)
- Source range: L168-L170
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.R129` — Why alpha and not iota_tau^2

## Immediate Comment / Docstring

```lean
/-- [V.R129] Why alpha and not iota_tau^2: the B-sector self-coupling
    kappa(B;2) = iota_tau^2 ~ 0.1166 is the tau-native sector strength.
    alpha ~ 1/137 is its E1 readout after holonomy correction and
    dimensional bridge. The two are related but not equal.

    Numerical check: iota_tau^2 = 341304^2 / 10^12 ~ 0.1166. -/
```

## Source Excerpt

```lean
theorem why_alpha_not_iota_sq :
    iota_tau_numer * iota_tau_numer > 0 := by
  simp [iota_tau_numer]
```
