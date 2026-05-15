---
{
  "projection_kind": "taulib_declaration",
  "title": "export_invariants_match",
  "permalink": "/corpus/taulib/docs/book-v-prologue-export-contract/export-invariants-match/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Prologue.ExportContract`.",
  "declaration_id": "TauLib.BookV.Prologue.ExportContract::export_invariants_match",
  "declaration_slug": "export-invariants-match",
  "kind": "theorem",
  "name": "export_invariants_match",
  "module_name": "TauLib.BookV.Prologue.ExportContract",
  "module_url": "/corpus/taulib/docs/book-v-prologue-export-contract/",
  "source_line_start": 209,
  "source_line_end": 210,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Prologue/ExportContract.lean#L209-L210",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Prologue.ExportContract",
        "url": "/corpus/taulib/docs/book-v-prologue-export-contract/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Prologue/ExportContract.lean#L209-L210",
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

- Module: [TauLib.BookV.Prologue.ExportContract](/corpus/taulib/docs/book-v-prologue-export-contract/)
- Source path: [`TauLib/BookV/Prologue/ExportContract.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Prologue/ExportContract.lean#L209-L210)
- Source range: L209-L210
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Export invariants match primary invariants. -/
```

## Source Excerpt

```lean
theorem export_invariants_match :
    primary_invariants.length = canonical_export.invariant_count := by rfl
```
