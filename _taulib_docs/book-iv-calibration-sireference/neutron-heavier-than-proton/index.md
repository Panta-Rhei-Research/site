---
{
  "projection_kind": "taulib_declaration",
  "title": "neutron_heavier_than_proton",
  "permalink": "/verify/taulib/docs/book-iv-calibration-sireference/neutron-heavier-than-proton/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Calibration.SIReference`.",
  "declaration_id": "TauLib.BookIV.Calibration.SIReference::neutron_heavier_than_proton",
  "declaration_slug": "neutron-heavier-than-proton",
  "kind": "theorem",
  "name": "neutron_heavier_than_proton",
  "module_name": "TauLib.BookIV.Calibration.SIReference",
  "module_url": "/verify/taulib/docs/book-iv-calibration-sireference/",
  "source_line_start": 283,
  "source_line_end": 286,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/SIReference.lean#L283-L286",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/SIReference.lean#L283-L286",
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
- Source path: [`TauLib/BookIV/Calibration/SIReference.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/SIReference.lean#L283-L286)
- Source range: L283-L286
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The neutron mass is the heaviest measured particle mass.
    m_n > m_p (neutron heavier than proton). -/
```

## Source Excerpt

```lean
theorem neutron_heavier_than_proton :
    si_neutron_mass.numer * si_proton_mass.denom >
    si_proton_mass.numer * si_neutron_mass.denom := by
  simp [si_neutron_mass, si_proton_mass]
```
