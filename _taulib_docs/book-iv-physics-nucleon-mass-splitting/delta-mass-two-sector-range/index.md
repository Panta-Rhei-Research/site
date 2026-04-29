---
{
  "projection_kind": "taulib_declaration",
  "title": "deltaMassTwoSector_range",
  "permalink": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/delta-mass-two-sector-range/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Physics.NucleonMassSplitting`.",
  "declaration_id": "TauLib.BookIV.Physics.NucleonMassSplitting::deltaMassTwoSector_range",
  "declaration_slug": "delta-mass-two-sector-range",
  "kind": "theorem",
  "name": "deltaMassTwoSector_range",
  "module_name": "TauLib.BookIV.Physics.NucleonMassSplitting",
  "module_url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/",
  "source_line_start": 270,
  "source_line_end": 276,
  "registry_ids": [
    "IV.T142"
  ],
  "related_registry_items": [
    {
      "id": "IV.T142",
      "title": "Proton-Neutron Mass Difference — Two-Sector",
      "url": "/registry/object/IV.T142/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L270-L276",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Physics.NucleonMassSplitting",
        "url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L270-L276",
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

- Module: [TauLib.BookIV.Physics.NucleonMassSplitting](/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/)
- Source path: [`TauLib/BookIV/Physics/NucleonMassSplitting.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L270-L276)
- Source range: L270-L276
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T142` — Proton-Neutron Mass Difference — Two-Sector

## Immediate Comment / Docstring

```lean
/-- [IV.T142] Two-sector net formula lies in (1.37, 1.38) × 10⁻³.
    Python lab: δm/m_n ≈ 1.37657e-3 (+33 ppm from PDG).
    The range (1.37e-3, 1.38e-3) contains 1.37657e-3. -/
```

## Source Excerpt

```lean
theorem deltaMassTwoSector_range :
    1370 * (qcd_denom * em_denom) <
      (qcd_numer * em_denom - em_numer * qcd_denom) * 1000000 ∧
    (qcd_numer * em_denom - em_numer * qcd_denom) * 1000000 <
      1380 * (qcd_denom * em_denom) := by
  rw [qcd_numer_val, qcd_denom_val, em_numer_val, em_denom_val]
  constructor <;> native_decide
```
