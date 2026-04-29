---
{
  "projection_kind": "taulib_declaration",
  "title": "h_tau_sectors",
  "permalink": "/verify/taulib/docs/book-ii-prologue-split-complex-interior/h-tau-sectors/",
  "summary_short": "`def` declaration in `TauLib.BookII.Prologue.SplitComplexInterior`.",
  "declaration_id": "TauLib.BookII.Prologue.SplitComplexInterior::h_tau_sectors",
  "declaration_slug": "h-tau-sectors",
  "kind": "def",
  "name": "h_tau_sectors",
  "module_name": "TauLib.BookII.Prologue.SplitComplexInterior",
  "module_url": "/verify/taulib/docs/book-ii-prologue-split-complex-interior/",
  "source_line_start": 49,
  "source_line_end": 49,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Prologue/SplitComplexInterior.lean#L49-L49",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Prologue.SplitComplexInterior",
        "url": "/verify/taulib/docs/book-ii-prologue-split-complex-interior/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Prologue/SplitComplexInterior.lean#L49-L49",
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

- Module: [TauLib.BookII.Prologue.SplitComplexInterior](/verify/taulib/docs/book-ii-prologue-split-complex-interior/)
- Source path: [`TauLib/BookII/Prologue/SplitComplexInterior.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Prologue/SplitComplexInterior.lean#L49-L49)
- Source range: L49-L49
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Sector form: z ↦ (z₊, z₋) where z = z₊ e₊ + z₋ e₋. -/
```

## Source Excerpt

```lean
def h_tau_sectors (z : HTau) : SectorPair := to_sectors z
```
