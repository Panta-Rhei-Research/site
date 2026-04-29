---
{
  "projection_kind": "taulib_declaration",
  "title": "si_neutron_mass",
  "permalink": "/verify/taulib/docs/book-iv-calibration-sireference/si-neutron-mass/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Calibration.SIReference`.",
  "declaration_id": "TauLib.BookIV.Calibration.SIReference::si_neutron_mass",
  "declaration_slug": "si-neutron-mass",
  "kind": "def",
  "name": "si_neutron_mass",
  "module_name": "TauLib.BookIV.Calibration.SIReference",
  "module_url": "/verify/taulib/docs/book-iv-calibration-sireference/",
  "source_line_start": 134,
  "source_line_end": 139,
  "registry_ids": [
    "IV.D27"
  ],
  "related_registry_items": [
    {
      "id": "IV.D27",
      "title": "SI Measured Constants",
      "url": "/registry/object/IV.D27/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/SIReference.lean#L134-L139",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Calibration.SIReference",
        "url": "/verify/taulib/docs/book-iv-calibration-sireference/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/SIReference.lean#L134-L139",
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

- Module: [TauLib.BookIV.Calibration.SIReference](/verify/taulib/docs/book-iv-calibration-sireference/)
- Source path: [`TauLib/BookIV/Calibration/SIReference.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/SIReference.lean#L134-L139)
- Source range: L134-L139
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.D27` — SI Measured Constants

## Immediate Comment / Docstring

```lean
/-- [IV.D27] Neutron mass: m_n = 1.674 927 498 04(95) × 10⁻²⁷ kg.
    THE calibration anchor — the single experimental input.
    Relative uncertainty: 5.7 × 10⁻¹⁰.
    Stored as 167492749804 / 10³⁸. -/
```

## Source Excerpt

```lean
def si_neutron_mass : SIConstant where
  name := "Neutron mass m_n"
  numer := 167492749804
  denom := 100000000000000000000000000000000000000  -- 10³⁸
  denom_pos := by omega
  is_exact := false
```
