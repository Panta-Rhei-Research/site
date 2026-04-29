---
{
  "projection_kind": "taulib_declaration",
  "title": "OntologicalPriority",
  "permalink": "/verify/taulib/docs/book-iv-calibration-calibration-anchor/ontological-priority/",
  "summary_short": "`inductive` declaration in `TauLib.BookIV.Calibration.CalibrationAnchor`.",
  "declaration_id": "TauLib.BookIV.Calibration.CalibrationAnchor::OntologicalPriority",
  "declaration_slug": "ontological-priority",
  "kind": "inductive",
  "name": "OntologicalPriority",
  "module_name": "TauLib.BookIV.Calibration.CalibrationAnchor",
  "module_url": "/verify/taulib/docs/book-iv-calibration-calibration-anchor/",
  "source_line_start": 205,
  "source_line_end": 210,
  "registry_ids": [
    "IV.R07"
  ],
  "related_registry_items": [
    {
      "id": "IV.R07",
      "title": "Ontological Priority",
      "url": "/registry/object/IV.R07/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchor.lean#L205-L210",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchor.lean#L205-L210",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
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

- Module: [TauLib.BookIV.Calibration.CalibrationAnchor](/verify/taulib/docs/book-iv-calibration-calibration-anchor/)
- Source path: [`TauLib/BookIV/Calibration/CalibrationAnchor.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchor.lean#L205-L210)
- Source range: L205-L210
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `IV.R07` — Ontological Priority

## Immediate Comment / Docstring

```lean
/-- [IV.R07] Ontological priority chain: the order in which particles
    emerge from the τ-framework's defect bundle analysis.

    n → p → e⁻ → m_P

    - Neutron: minimal stable unpolarized T² defect bundle
    - Proton: neutron + weak polarization δ_A
    - Electron: electroweak arc resonance
    - Planck mass: dimensional combination (not a particle) -/
```

## Source Excerpt

```lean
inductive OntologicalPriority
  | Neutron       -- 1st: minimal stable T² defect
  | Proton        -- 2nd: neutron + weak polarization
  | Electron      -- 3rd: EW arc resonance
  | PlanckMass    -- 4th: dimensional combination
  deriving Repr, DecidableEq
```
