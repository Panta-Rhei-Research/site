---
{
  "projection_kind": "taulib_declaration",
  "title": "boundary_supports_null",
  "permalink": "/verify/taulib/docs/book-v-temporal-macro-readout/boundary-supports-null/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Temporal.MacroReadout`.",
  "declaration_id": "TauLib.BookV.Temporal.MacroReadout::boundary_supports_null",
  "declaration_slug": "boundary-supports-null",
  "kind": "theorem",
  "name": "boundary_supports_null",
  "module_name": "TauLib.BookV.Temporal.MacroReadout",
  "module_url": "/verify/taulib/docs/book-v-temporal-macro-readout/",
  "source_line_start": 69,
  "source_line_end": 73,
  "registry_ids": [
    "V.T14"
  ],
  "related_registry_items": [
    {
      "id": "V.T14",
      "title": "Photon Existence Theorem",
      "url": "/registry/object/V.T14/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/MacroReadout.lean#L69-L73",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/MacroReadout.lean#L69-L73",
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

- Module: [TauLib.BookV.Temporal.MacroReadout](/verify/taulib/docs/book-v-temporal-macro-readout/)
- Source path: [`TauLib/BookV/Temporal/MacroReadout.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/MacroReadout.lean#L69-L73)
- Source range: L69-L73
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T14` — Photon Existence Theorem

## Immediate Comment / Docstring

```lean
/-- [V.T14] The boundary holonomy algebra supports null intertwiners.
    EM generator gamma at depth 2 allows null transport on τ¹. -/
```

## Source Excerpt

```lean
theorem boundary_supports_null :
    em_sector.generator = .gamma ∧
    em_sector.depth = 2 ∧
    photon_null.sector = .B := by
  exact ⟨rfl, rfl, rfl⟩
```
