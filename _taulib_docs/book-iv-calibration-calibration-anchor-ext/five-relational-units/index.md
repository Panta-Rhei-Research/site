---
{
  "projection_kind": "taulib_declaration",
  "title": "five_relational_units",
  "permalink": "/verify/taulib/docs/book-iv-calibration-calibration-anchor-ext/five-relational-units/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Calibration.CalibrationAnchorExt`.",
  "declaration_id": "TauLib.BookIV.Calibration.CalibrationAnchorExt::five_relational_units",
  "declaration_slug": "five-relational-units",
  "kind": "def",
  "name": "five_relational_units",
  "module_name": "TauLib.BookIV.Calibration.CalibrationAnchorExt",
  "module_url": "/verify/taulib/docs/book-iv-calibration-calibration-anchor-ext/",
  "source_line_start": 87,
  "source_line_end": 93,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L87-L93",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Calibration.CalibrationAnchorExt",
        "url": "/verify/taulib/docs/book-iv-calibration-calibration-anchor-ext/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L87-L93",
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

- Module: [TauLib.BookIV.Calibration.CalibrationAnchorExt](/verify/taulib/docs/book-iv-calibration-calibration-anchor-ext/)
- Source path: [`TauLib/BookIV/Calibration/CalibrationAnchorExt.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L87-L93)
- Source range: L87-L93
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The five relational units with representative scaled values.

    M = neutron mass, L = length scale, H = frequency scale,
    Q = elementary charge, R = mass ratio m_n/m_e. -/
```

## Source Excerpt

```lean
def five_relational_units : List RelationalUnit := [
  ⟨"M", "Neutron mass (mass scale, kg)", 167492749804, 100000000000000000000000000000000000000, by decide⟩,
  ⟨"L", "Length scale (π/2)·r_n (m)", 86173, 100000000000000, by decide⟩,
  ⟨"H", "Frequency scale R·f_e (Hz)", 22560, 10, by decide⟩,
  ⟨"Q", "Elementary charge e (C)", 1602176634, 10000000000000000000000000000, by decide⟩,
  ⟨"R", "Mass ratio m_n/m_e (dimensionless)", 183868366173, 100000000, by decide⟩
]
```
