---
{
  "projection_kind": "taulib_declaration",
  "title": "entropy_invariance",
  "permalink": "/verify/taulib/docs/book-iv-calibration-running-regime/entropy-invariance/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Calibration.RunningRegime`.",
  "declaration_id": "TauLib.BookIV.Calibration.RunningRegime::entropy_invariance",
  "declaration_slug": "entropy-invariance",
  "kind": "theorem",
  "name": "entropy_invariance",
  "module_name": "TauLib.BookIV.Calibration.RunningRegime",
  "module_url": "/verify/taulib/docs/book-iv-calibration-running-regime/",
  "source_line_start": 126,
  "source_line_end": 129,
  "registry_ids": [
    "IV.P170"
  ],
  "related_registry_items": [
    {
      "id": "IV.P170",
      "title": "Total Entropy Invariance",
      "url": "/registry/object/IV.P170/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/RunningRegime.lean#L126-L129",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Calibration.RunningRegime",
        "url": "/verify/taulib/docs/book-iv-calibration-running-regime/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/RunningRegime.lean#L126-L129",
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

- Module: [TauLib.BookIV.Calibration.RunningRegime](/verify/taulib/docs/book-iv-calibration-running-regime/)
- Source path: [`TauLib/BookIV/Calibration/RunningRegime.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/RunningRegime.lean#L126-L129)
- Source range: L126-L129
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.P170` — Total Entropy Invariance

## Immediate Comment / Docstring

```lean
/-- [IV.P170] Total entropy invariance: S_total is μ-independent.
    dS_vis/dμ = −dS_hid/dμ for each sector. -/
```

## Source Excerpt

```lean
theorem entropy_invariance :
    -- Entropy conservation: total = vis + hid always
    ∀ (e : EntropyAtScale), e.total_numer = e.s_vis_numer + e.s_hid_numer :=
  fun e => e.total_split
```
