---
{
  "projection_kind": "taulib_declaration",
  "title": "RefinementDrift.depth_diff",
  "permalink": "/verify/taulib/docs/book-v-temporal-macro-readout/depth-diff/",
  "summary_short": "`def` declaration in `TauLib.BookV.Temporal.MacroReadout`.",
  "declaration_id": "TauLib.BookV.Temporal.MacroReadout::RefinementDrift.depth_diff",
  "declaration_slug": "depth-diff",
  "kind": "def",
  "name": "RefinementDrift.depth_diff",
  "module_name": "TauLib.BookV.Temporal.MacroReadout",
  "module_url": "/verify/taulib/docs/book-v-temporal-macro-readout/",
  "source_line_start": 145,
  "source_line_end": 146,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/MacroReadout.lean#L145-L146",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Temporal.MacroReadout",
        "url": "/verify/taulib/docs/book-v-temporal-macro-readout/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/MacroReadout.lean#L145-L146",
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

- Module: [TauLib.BookV.Temporal.MacroReadout](/verify/taulib/docs/book-v-temporal-macro-readout/)
- Source path: [`TauLib/BookV/Temporal/MacroReadout.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/MacroReadout.lean#L145-L146)
- Source range: L145-L146
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Depth difference (positive for redshift). -/
```

## Source Excerpt

```lean
def RefinementDrift.depth_diff (d : RefinementDrift) : Nat :=
  d.n_receiver - d.n_source
```
