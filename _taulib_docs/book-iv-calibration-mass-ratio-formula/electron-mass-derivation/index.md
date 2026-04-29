---
{
  "projection_kind": "taulib_declaration",
  "title": "ElectronMassDerivation",
  "permalink": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/electron-mass-derivation/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Calibration.MassRatioFormula`.",
  "declaration_id": "TauLib.BookIV.Calibration.MassRatioFormula::ElectronMassDerivation",
  "declaration_slug": "electron-mass-derivation",
  "kind": "structure",
  "name": "ElectronMassDerivation",
  "module_name": "TauLib.BookIV.Calibration.MassRatioFormula",
  "module_url": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/",
  "source_line_start": 315,
  "source_line_end": 324,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/MassRatioFormula.lean#L315-L324",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Calibration.MassRatioFormula",
        "url": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/MassRatioFormula.lean#L315-L324",
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

- Module: [TauLib.BookIV.Calibration.MassRatioFormula](/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/)
- Source path: [`TauLib/BookIV/Calibration/MassRatioFormula.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/MassRatioFormula.lean#L315-L324)
- Source range: L315-L324
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The electron mass from the calibration anchor:
    m_e = m_n / R

    Using CODATA m_n and the Level 1+ R, this gives:
    m_e = 1.674927498 × 10⁻²⁷ / 1838.684 ≈ 9.1094 × 10⁻³¹ kg

    Matching CODATA m_e = 9.1093837015 × 10⁻³¹ kg to sub-ppm. -/
```

## Source Excerpt

```lean
structure ElectronMassDerivation where
  /-- Anchor: neutron mass. -/
  anchor : SIConstant := si_neutron_mass
  /-- Mass ratio: R. -/
  ratio : SIConstant := si_mass_ratio
  /-- Derived: electron mass. -/
  target : SIConstant := si_electron_mass
  /-- The derivation: m_e = m_n / R. -/
  relation : String := "m_e = m_n / R"
  deriving Repr
```
