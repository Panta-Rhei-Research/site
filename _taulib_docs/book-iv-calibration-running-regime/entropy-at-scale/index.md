---
{
  "projection_kind": "taulib_declaration",
  "title": "EntropyAtScale",
  "permalink": "/verify/taulib/docs/book-iv-calibration-running-regime/entropy-at-scale/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Calibration.RunningRegime`.",
  "declaration_id": "TauLib.BookIV.Calibration.RunningRegime::EntropyAtScale",
  "declaration_slug": "entropy-at-scale",
  "kind": "structure",
  "name": "EntropyAtScale",
  "module_name": "TauLib.BookIV.Calibration.RunningRegime",
  "module_url": "/verify/taulib/docs/book-iv-calibration-running-regime/",
  "source_line_start": 112,
  "source_line_end": 122,
  "registry_ids": [
    "IV.D302"
  ],
  "related_registry_items": [
    {
      "id": "IV.D302",
      "title": "Entropy splitting",
      "url": "/registry/object/IV.D302/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/RunningRegime.lean#L112-L122",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/RunningRegime.lean#L112-L122",
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

- Module: [TauLib.BookIV.Calibration.RunningRegime](/verify/taulib/docs/book-iv-calibration-running-regime/)
- Source path: [`TauLib/BookIV/Calibration/RunningRegime.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/RunningRegime.lean#L112-L122)
- Source range: L112-L122
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D302` — Entropy splitting

## Immediate Comment / Docstring

```lean
/-- [IV.D302] Entropy splitting at scale μ: S_X(μ) = S_vis(μ) + S_hid(μ).
    S_vis is the entropy visible to instruments at scale μ.
    S_hid is the entropy hidden below that resolution. -/
```

## Source Excerpt

```lean
structure EntropyAtScale where
  /-- Sector. -/
  sector : Tau.BookIII.Sectors.Sector
  /-- Visible entropy numerator. -/
  s_vis_numer : Nat
  /-- Hidden entropy numerator. -/
  s_hid_numer : Nat
  /-- Total is conserved (vis + hid = total). -/
  total_numer : Nat
  total_split : total_numer = s_vis_numer + s_hid_numer
  deriving Repr
```
