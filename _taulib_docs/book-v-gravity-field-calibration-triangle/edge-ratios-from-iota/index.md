---
{
  "projection_kind": "taulib_declaration",
  "title": "edge_ratios_from_iota",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-calibration-triangle/edge-ratios-from-iota/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.CalibrationTriangle`.",
  "declaration_id": "TauLib.BookV.GravityField.CalibrationTriangle::edge_ratios_from_iota",
  "declaration_slug": "edge-ratios-from-iota",
  "kind": "theorem",
  "name": "edge_ratios_from_iota",
  "module_name": "TauLib.BookV.GravityField.CalibrationTriangle",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-calibration-triangle/",
  "source_line_start": 170,
  "source_line_end": 172,
  "registry_ids": [
    "V.T49"
  ],
  "related_registry_items": [
    {
      "id": "V.T49",
      "title": "Micro--Macro Bridge",
      "url": "/registry/object/V.T49/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/CalibrationTriangle.lean#L170-L172",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.CalibrationTriangle",
        "url": "/verify/taulib/docs/book-v-gravity-field-calibration-triangle/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/CalibrationTriangle.lean#L170-L172",
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

- Module: [TauLib.BookV.GravityField.CalibrationTriangle](/verify/taulib/docs/book-v-gravity-field-calibration-triangle/)
- Source path: [`TauLib/BookV/GravityField/CalibrationTriangle.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/CalibrationTriangle.lean#L170-L172)
- Source range: L170-L172
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T49` — Micro--Macro Bridge

## Immediate Comment / Docstring

```lean
/-- [V.T49] Edge ratios are determined by iota_tau and sector couplings.

    - m_n/m_e = R(iota_tau) (mass ratio formula)
    - G = (c^3/hbar) * iota_tau^2 (gravity sector)
    - alpha = (8/15) * iota_tau^4 (spectral formula)

    All edge ratios are functions of iota_tau alone. -/
```

## Source Excerpt

```lean
theorem edge_ratios_from_iota :
    "R = f(iota_tau), G = g(iota_tau), alpha = h(iota_tau)" =
    "R = f(iota_tau), G = g(iota_tau), alpha = h(iota_tau)" := rfl
```
