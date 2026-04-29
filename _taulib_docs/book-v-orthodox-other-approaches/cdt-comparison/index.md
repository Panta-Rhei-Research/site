---
{
  "projection_kind": "taulib_declaration",
  "title": "cdt_comparison",
  "permalink": "/verify/taulib/docs/book-v-orthodox-other-approaches/cdt-comparison/",
  "summary_short": "`def` declaration in `TauLib.BookV.Orthodox.OtherApproaches`.",
  "declaration_id": "TauLib.BookV.Orthodox.OtherApproaches::cdt_comparison",
  "declaration_slug": "cdt-comparison",
  "kind": "def",
  "name": "cdt_comparison",
  "module_name": "TauLib.BookV.Orthodox.OtherApproaches",
  "module_url": "/verify/taulib/docs/book-v-orthodox-other-approaches/",
  "source_line_start": 119,
  "source_line_end": 124,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/OtherApproaches.lean#L119-L124",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Orthodox.OtherApproaches",
        "url": "/verify/taulib/docs/book-v-orthodox-other-approaches/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/OtherApproaches.lean#L119-L124",
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

- Module: [TauLib.BookV.Orthodox.OtherApproaches](/verify/taulib/docs/book-v-orthodox-other-approaches/)
- Source path: [`TauLib/BookV/Orthodox/OtherApproaches.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/OtherApproaches.lean#L119-L124)
- Source range: L119-L124
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- CDT comparison. -/
```

## Source Excerpt

```lean
def cdt_comparison : ApproachComparison where
  approach := .CDT
  shared_feature := "emergent geometry from combinatorial building blocks"
  key_difference := "tau: analytic (boundary algebra); CDT: Monte Carlo (path integral)"
  free_params := 3  -- bare couplings
  has_landscape := false
```
