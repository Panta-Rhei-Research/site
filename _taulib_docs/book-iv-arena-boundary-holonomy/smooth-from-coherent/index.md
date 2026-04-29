---
{
  "projection_kind": "taulib_declaration",
  "title": "smooth_from_coherent",
  "permalink": "/verify/taulib/docs/book-iv-arena-boundary-holonomy/smooth-from-coherent/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Arena.BoundaryHolonomy`.",
  "declaration_id": "TauLib.BookIV.Arena.BoundaryHolonomy::smooth_from_coherent",
  "declaration_slug": "smooth-from-coherent",
  "kind": "theorem",
  "name": "smooth_from_coherent",
  "module_name": "TauLib.BookIV.Arena.BoundaryHolonomy",
  "module_url": "/verify/taulib/docs/book-iv-arena-boundary-holonomy/",
  "source_line_start": 203,
  "source_line_end": 205,
  "registry_ids": [
    "IV.P153"
  ],
  "related_registry_items": [
    {
      "id": "IV.P153",
      "title": "Smooth manifold from coherent readouts",
      "url": "/registry/object/IV.P153/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L203-L205",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Arena.BoundaryHolonomy",
        "url": "/verify/taulib/docs/book-iv-arena-boundary-holonomy/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L203-L205",
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

- Module: [TauLib.BookIV.Arena.BoundaryHolonomy](/verify/taulib/docs/book-iv-arena-boundary-holonomy/)
- Source path: [`TauLib/BookIV/Arena/BoundaryHolonomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L203-L205)
- Source range: L203-L205
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.P153` — Smooth manifold from coherent readouts

## Immediate Comment / Docstring

```lean
/-- [IV.P153] Coherent chart readouts produce smooth manifold structure.
    When sector lifts are mutually consistent, the readout space is
    a smooth 4-manifold (locally ℝ⁴). -/
```

## Source Excerpt

```lean
theorem smooth_from_coherent :
    all_sector_lifts.length = 5 ∧ chart_readout.target_dim = 4 := by
  simp [all_sector_lifts, chart_readout]
```
