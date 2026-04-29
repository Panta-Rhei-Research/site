---
{
  "projection_kind": "taulib_declaration",
  "title": "example_bh_epoch",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cosmological-endstate/example-bh-epoch/",
  "summary_short": "`def` declaration in `TauLib.BookV.Cosmology.CosmologicalEndstate`.",
  "declaration_id": "TauLib.BookV.Cosmology.CosmologicalEndstate::example_bh_epoch",
  "declaration_slug": "example-bh-epoch",
  "kind": "def",
  "name": "example_bh_epoch",
  "module_name": "TauLib.BookV.Cosmology.CosmologicalEndstate",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cosmological-endstate/",
  "source_line_start": 109,
  "source_line_end": 113,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CosmologicalEndstate.lean#L109-L113",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.CosmologicalEndstate",
        "url": "/verify/taulib/docs/book-v-cosmology-cosmological-endstate/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CosmologicalEndstate.lean#L109-L113",
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

- Module: [TauLib.BookV.Cosmology.CosmologicalEndstate](/verify/taulib/docs/book-v-cosmology-cosmological-endstate/)
- Source path: [`TauLib/BookV/Cosmology/CosmologicalEndstate.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CosmologicalEndstate.lean#L109-L113)
- Source range: L109-L113
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Example: BH-dominated at depth 1000, 90% BH entropy. -/
```

## Source Excerpt

```lean
def example_bh_epoch : BHDominatedEpoch where
  onset_depth := 1000
  onset_pos := by omega
  bh_fraction_pct := 90
  bh_dominant := by omega
```
