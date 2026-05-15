---
{
  "projection_kind": "taulib_declaration",
  "title": "readout_landscape_unique",
  "permalink": "/corpus/taulib/docs/book-iv-calibration-running-regime/readout-landscape-unique/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Calibration.RunningRegime`.",
  "declaration_id": "TauLib.BookIV.Calibration.RunningRegime::readout_landscape_unique",
  "declaration_slug": "readout-landscape-unique",
  "kind": "theorem",
  "name": "readout_landscape_unique",
  "module_name": "TauLib.BookIV.Calibration.RunningRegime",
  "module_url": "/corpus/taulib/docs/book-iv-calibration-running-regime/",
  "source_line_start": 173,
  "source_line_end": 174,
  "registry_ids": [
    "IV.T113"
  ],
  "related_registry_items": [
    {
      "id": "IV.T113",
      "title": "Readout Landscape Theorem",
      "url": "/registry/object/IV.T113/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/RunningRegime.lean#L173-L174",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Calibration.RunningRegime",
        "url": "/corpus/taulib/docs/book-iv-calibration-running-regime/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/RunningRegime.lean#L173-L174",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookIV.Calibration.RunningRegime](/corpus/taulib/docs/book-iv-calibration-running-regime/)
- Source path: [`TauLib/BookIV/Calibration/RunningRegime.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/RunningRegime.lean#L173-L174)
- Source range: L173-L174
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `IV.T113` — Readout Landscape Theorem

## Immediate Comment / Docstring

```lean
/-- [IV.T113] The readout landscape is uniquely determined by the
    boundary holonomy algebra and the enrichment layer E₁.
    No additional input is needed beyond ι_τ. -/
```

## Source Excerpt

```lean
theorem readout_landscape_unique :
    (ReadoutLandscape.mk 5 rfl true rfl).determined = true := rfl
```
