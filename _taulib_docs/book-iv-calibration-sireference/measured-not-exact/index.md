---
{
  "projection_kind": "taulib_declaration",
  "title": "measured_not_exact",
  "permalink": "/verify/taulib/docs/book-iv-calibration-sireference/measured-not-exact/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Calibration.SIReference`.",
  "declaration_id": "TauLib.BookIV.Calibration.SIReference::measured_not_exact",
  "declaration_slug": "measured-not-exact",
  "kind": "theorem",
  "name": "measured_not_exact",
  "module_name": "TauLib.BookIV.Calibration.SIReference",
  "module_url": "/verify/taulib/docs/book-iv-calibration-sireference/",
  "source_line_start": 272,
  "source_line_end": 276,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/SIReference.lean#L272-L276",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/SIReference.lean#L272-L276",
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

- Module: [TauLib.BookIV.Calibration.SIReference](/verify/taulib/docs/book-iv-calibration-sireference/)
- Source path: [`TauLib/BookIV/Calibration/SIReference.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/SIReference.lean#L272-L276)
- Source range: L272-L276
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- No measured constant is flagged as exact. -/
```

## Source Excerpt

```lean
theorem measured_not_exact :
    (si_measured_constants.map SIConstant.is_exact).all (· == false) = true := by
  simp [si_measured_constants, si_neutron_mass, si_electron_mass, si_proton_mass,
        si_alpha_inverse, si_weinberg_sin2, si_strong_coupling,
        si_mass_ratio, si_np_mass_diff, si_gravitational]
```
