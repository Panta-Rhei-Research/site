---
{
  "projection_kind": "taulib_declaration",
  "title": "observed_cmb",
  "permalink": "/verify/taulib/docs/book-v-cosmology-threshold-ladder/observed-cmb/",
  "summary_short": "`def` declaration in `TauLib.BookV.Cosmology.ThresholdLadder`.",
  "declaration_id": "TauLib.BookV.Cosmology.ThresholdLadder::observed_cmb",
  "declaration_slug": "observed-cmb",
  "kind": "def",
  "name": "observed_cmb",
  "module_name": "TauLib.BookV.Cosmology.ThresholdLadder",
  "module_url": "/verify/taulib/docs/book-v-cosmology-threshold-ladder/",
  "source_line_start": 267,
  "source_line_end": 270,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/ThresholdLadder.lean#L267-L270",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.ThresholdLadder",
        "url": "/verify/taulib/docs/book-v-cosmology-threshold-ladder/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/ThresholdLadder.lean#L267-L270",
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

- Module: [TauLib.BookV.Cosmology.ThresholdLadder](/verify/taulib/docs/book-v-cosmology-threshold-ladder/)
- Source path: [`TauLib/BookV/Cosmology/ThresholdLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/ThresholdLadder.lean#L267-L270)
- Source range: L267-L270
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The observed CMB. -/
```

## Source Excerpt

```lean
def observed_cmb : CmbOrigin where
  temp_mK := 2725
  redshift_times_10 := 11000
  temp_range := ⟨by omega, by omega⟩
```
