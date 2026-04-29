---
{
  "projection_kind": "taulib_declaration",
  "title": "five_sector_lifts",
  "permalink": "/verify/taulib/docs/book-iv-physics-planck-character/five-sector-lifts/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Physics.PlanckCharacter`.",
  "declaration_id": "TauLib.BookIV.Physics.PlanckCharacter::five_sector_lifts",
  "declaration_slug": "five-sector-lifts",
  "kind": "theorem",
  "name": "five_sector_lifts",
  "module_name": "TauLib.BookIV.Physics.PlanckCharacter",
  "module_url": "/verify/taulib/docs/book-iv-physics-planck-character/",
  "source_line_start": 247,
  "source_line_end": 247,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/PlanckCharacter.lean#L247-L247",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Physics.PlanckCharacter",
        "url": "/verify/taulib/docs/book-iv-physics-planck-character/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/PlanckCharacter.lean#L247-L247",
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

- Module: [TauLib.BookIV.Physics.PlanckCharacter](/verify/taulib/docs/book-iv-physics-planck-character/)
- Source path: [`TauLib/BookIV/Physics/PlanckCharacter.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/PlanckCharacter.lean#L247-L247)
- Source range: L247-L247
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Exactly 5 sector lifts (one per sector). -/
```

## Source Excerpt

```lean
theorem five_sector_lifts : all_sector_lifts.length = 5 := by rfl
```
