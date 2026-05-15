---
{
  "projection_kind": "taulib_declaration",
  "title": "full_calibration_check",
  "permalink": "/corpus/taulib/docs/book-ii-hartogs-calibrated-split-complex/full-calibration-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.CalibratedSplitComplex`.",
  "declaration_id": "TauLib.BookII.Hartogs.CalibratedSplitComplex::full_calibration_check",
  "declaration_slug": "full-calibration-check",
  "kind": "def",
  "name": "full_calibration_check",
  "module_name": "TauLib.BookII.Hartogs.CalibratedSplitComplex",
  "module_url": "/corpus/taulib/docs/book-ii-hartogs-calibrated-split-complex/",
  "source_line_start": 256,
  "source_line_end": 259,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CalibratedSplitComplex.lean#L256-L259",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.CalibratedSplitComplex",
        "url": "/corpus/taulib/docs/book-ii-hartogs-calibrated-split-complex/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CalibratedSplitComplex.lean#L256-L259",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "data/computed value",
      "status": "data/computed value"
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

- Module: [TauLib.BookII.Hartogs.CalibratedSplitComplex](/corpus/taulib/docs/book-ii-hartogs-calibrated-split-complex/)
- Source path: [`TauLib/BookII/Hartogs/CalibratedSplitComplex.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CalibratedSplitComplex.lean#L256-L259)
- Source range: L256-L259
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Extended consistency including channel calibration. -/
```

## Source Excerpt

```lean
def full_calibration_check : Bool :=
  calibration_consistency_check &&
  b_channel_pi_calibration 5 &&
  c_channel_e_calibration 5
```
