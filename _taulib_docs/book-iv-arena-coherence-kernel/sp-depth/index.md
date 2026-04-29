---
{
  "projection_kind": "taulib_declaration",
  "title": "sp_depth",
  "permalink": "/verify/taulib/docs/book-iv-arena-coherence-kernel/sp-depth/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Arena.CoherenceKernel`.",
  "declaration_id": "TauLib.BookIV.Arena.CoherenceKernel::sp_depth",
  "declaration_slug": "sp-depth",
  "kind": "theorem",
  "name": "sp_depth",
  "module_name": "TauLib.BookIV.Arena.CoherenceKernel",
  "module_url": "/verify/taulib/docs/book-iv-arena-coherence-kernel/",
  "source_line_start": 118,
  "source_line_end": 122,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/CoherenceKernel.lean#L118-L122",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Arena.CoherenceKernel",
        "url": "/verify/taulib/docs/book-iv-arena-coherence-kernel/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/CoherenceKernel.lean#L118-L122",
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

- Module: [TauLib.BookIV.Arena.CoherenceKernel](/verify/taulib/docs/book-iv-arena-coherence-kernel/)
- Source path: [`TauLib/BookIV/Arena/CoherenceKernel.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/CoherenceKernel.lean#L118-L122)
- Source range: L118-L122
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Helper: extract depth from sector_physics without exposing coupling Nats. -/
```

## Source Excerpt

```lean
private theorem sp_depth :
    ∀ s : Sector,
    (sector_physics s).depth = match s with
      | .D => 1 | .A => 1 | .B => 2 | .C => 3 | .Omega => 3 := by
  intro s; cases s <;> rfl
```
