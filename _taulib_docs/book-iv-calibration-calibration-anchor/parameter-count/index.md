---
{
  "projection_kind": "taulib_declaration",
  "title": "parameter_count",
  "permalink": "/verify/taulib/docs/book-iv-calibration-calibration-anchor/parameter-count/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Calibration.CalibrationAnchor`.",
  "declaration_id": "TauLib.BookIV.Calibration.CalibrationAnchor::parameter_count",
  "declaration_slug": "parameter-count",
  "kind": "theorem",
  "name": "parameter_count",
  "module_name": "TauLib.BookIV.Calibration.CalibrationAnchor",
  "module_url": "/verify/taulib/docs/book-iv-calibration-calibration-anchor/",
  "source_line_start": 146,
  "source_line_end": 151,
  "registry_ids": [
    "IV.T05"
  ],
  "related_registry_items": [
    {
      "id": "IV.T05",
      "title": "Parameter Count",
      "url": "/registry/object/IV.T05/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchor.lean#L146-L151",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Calibration.CalibrationAnchor",
        "url": "/verify/taulib/docs/book-iv-calibration-calibration-anchor/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchor.lean#L146-L151",
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

- Module: [TauLib.BookIV.Calibration.CalibrationAnchor](/verify/taulib/docs/book-iv-calibration-calibration-anchor/)
- Source path: [`TauLib/BookIV/Calibration/CalibrationAnchor.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchor.lean#L146-L151)
- Source range: L146-L151
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T05` — Parameter Count

## Immediate Comment / Docstring

```lean
/-- [IV.T05] Parameter count: exactly ONE free parameter (the neutron mass).
    All dimensionless quantities are fixed by ι_τ = 2/(π+e).
    All dimensional quantities factor through the single anchor Λ_M = m_n(SI). -/
```

## Source Excerpt

```lean
theorem parameter_count :
    -- Zero free dimensionless parameters (all fixed by ι_τ)
    (0 : Nat) = 0 ∧
    -- One free dimensional parameter (the anchor)
    neutron_anchor.is_sole_anchor = true := by
  exact ⟨rfl, rfl⟩
```
