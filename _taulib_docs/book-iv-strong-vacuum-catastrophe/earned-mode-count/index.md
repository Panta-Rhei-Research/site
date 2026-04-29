---
{
  "projection_kind": "taulib_declaration",
  "title": "EarnedModeCount",
  "permalink": "/verify/taulib/docs/book-iv-strong-vacuum-catastrophe/earned-mode-count/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.VacuumCatastrophe`.",
  "declaration_id": "TauLib.BookIV.Strong.VacuumCatastrophe::EarnedModeCount",
  "declaration_slug": "earned-mode-count",
  "kind": "structure",
  "name": "EarnedModeCount",
  "module_name": "TauLib.BookIV.Strong.VacuumCatastrophe",
  "module_url": "/verify/taulib/docs/book-iv-strong-vacuum-catastrophe/",
  "source_line_start": 141,
  "source_line_end": 148,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L141-L148",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Strong.VacuumCatastrophe",
        "url": "/verify/taulib/docs/book-iv-strong-vacuum-catastrophe/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L141-L148",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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

- Module: [TauLib.BookIV.Strong.VacuumCatastrophe](/verify/taulib/docs/book-iv-strong-vacuum-catastrophe/)
- Source path: [`TauLib/BookIV/Strong/VacuumCatastrophe.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L141-L148)
- Source range: L141-L148
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- A mode count with its classification. -/
```

## Source Excerpt

```lean
structure EarnedModeCount where
  /-- Type of mode count. -/
  count_type : ModeCountType
  /-- If earned: finite at each stage. -/
  finite_each_stage : Bool
  /-- If unearned: leads to divergence. -/
  leads_to_divergence : Bool
  deriving Repr
```
