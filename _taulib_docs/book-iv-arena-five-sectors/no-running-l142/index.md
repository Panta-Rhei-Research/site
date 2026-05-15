---
{
  "projection_kind": "taulib_declaration",
  "title": "no_running",
  "permalink": "/corpus/taulib/docs/book-iv-arena-five-sectors/no-running-l142/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Arena.FiveSectors`.",
  "declaration_id": "TauLib.BookIV.Arena.FiveSectors::no_running",
  "declaration_slug": "no-running-l142",
  "kind": "def",
  "name": "no_running",
  "module_name": "TauLib.BookIV.Arena.FiveSectors",
  "module_url": "/corpus/taulib/docs/book-iv-arena-five-sectors/",
  "source_line_start": 142,
  "source_line_end": 146,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/FiveSectors.lean#L142-L146",
  "formal_status": "defined",
  "declaration_role": "definition",
  "formal_status_label": "definition",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Arena.FiveSectors",
        "url": "/corpus/taulib/docs/book-iv-arena-five-sectors/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/FiveSectors.lean#L142-L146",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "definition",
      "status": "definition"
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

- Module: [TauLib.BookIV.Arena.FiveSectors](/corpus/taulib/docs/book-iv-arena-five-sectors/)
- Source path: [`TauLib/BookIV/Arena/FiveSectors.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/FiveSectors.lean#L142-L146)
- Source range: L142-L146
- Kind: `def`
- Public role: `definition`
- Formal status hint: `definition`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The no-running principle instance. -/
```

## Source Excerpt

```lean
def no_running : NoRunning where
  beta_zero := true
  beta_true := rfl
  fixed_count := 15
  fixed_eq := rfl
```
