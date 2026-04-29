---
{
  "projection_kind": "taulib_declaration",
  "title": "neutron_minimality",
  "permalink": "/verify/taulib/docs/book-iv-calibration-calibration-anchor-ext/neutron-minimality-l291/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Calibration.CalibrationAnchorExt`.",
  "declaration_id": "TauLib.BookIV.Calibration.CalibrationAnchorExt::neutron_minimality",
  "declaration_slug": "neutron-minimality-l291",
  "kind": "theorem",
  "name": "neutron_minimality",
  "module_name": "TauLib.BookIV.Calibration.CalibrationAnchorExt",
  "module_url": "/verify/taulib/docs/book-iv-calibration-calibration-anchor-ext/",
  "source_line_start": 291,
  "source_line_end": 295,
  "registry_ids": [
    "IV.P166"
  ],
  "related_registry_items": [
    {
      "id": "IV.P166",
      "title": "Neutron Minimality",
      "url": "/registry/object/IV.P166/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L291-L295",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L291-L295",
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

- Module: [TauLib.BookIV.Calibration.CalibrationAnchorExt](/verify/taulib/docs/book-iv-calibration-calibration-anchor-ext/)
- Source path: [`TauLib/BookIV/Calibration/CalibrationAnchorExt.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L291-L295)
- Source range: L291-L295
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.P166` — Neutron Minimality

## Immediate Comment / Docstring

```lean
/-- [IV.P166] The neutron is both unpolarized and minimal. -/
```

## Source Excerpt

```lean
theorem neutron_minimality :
    is_unpolarized neutron_minimal.bundle = true ∧
    neutron_minimal.is_minimal = true ∧
    neutron_minimal.is_stable = true := by
  exact ⟨rfl, rfl, rfl⟩
```
