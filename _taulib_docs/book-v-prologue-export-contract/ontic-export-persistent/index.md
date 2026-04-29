---
{
  "projection_kind": "taulib_declaration",
  "title": "ontic_export_persistent",
  "permalink": "/verify/taulib/docs/book-v-prologue-export-contract/ontic-export-persistent/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Prologue.ExportContract`.",
  "declaration_id": "TauLib.BookV.Prologue.ExportContract::ontic_export_persistent",
  "declaration_slug": "ontic-export-persistent",
  "kind": "theorem",
  "name": "ontic_export_persistent",
  "module_name": "TauLib.BookV.Prologue.ExportContract",
  "module_url": "/verify/taulib/docs/book-v-prologue-export-contract/",
  "source_line_start": 130,
  "source_line_end": 132,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Prologue/ExportContract.lean#L130-L132",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Prologue.ExportContract",
        "url": "/verify/taulib/docs/book-v-prologue-export-contract/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Prologue/ExportContract.lean#L130-L132",
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

- Module: [TauLib.BookV.Prologue.ExportContract](/verify/taulib/docs/book-v-prologue-export-contract/)
- Source path: [`TauLib/BookV/Prologue/ExportContract.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Prologue/ExportContract.lean#L130-L132)
- Source range: L130-L132
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Ontic particles are persistent (from Book IV). -/
```

## Source Excerpt

```lean
theorem ontic_export_persistent (p : OnticParticleExport) :
    p.particle.mass.is_persistent = true :=
  p.particle.persistent_proof
```
