---
{
  "projection_kind": "taulib_declaration",
  "title": "ladderOp",
  "permalink": "/verify/taulib/docs/book-i-orbit-ladder/ladder-op/",
  "summary_short": "`def` declaration in `TauLib.BookI.Orbit.Ladder`.",
  "declaration_id": "TauLib.BookI.Orbit.Ladder::ladderOp",
  "declaration_slug": "ladder-op",
  "kind": "def",
  "name": "ladderOp",
  "module_name": "TauLib.BookI.Orbit.Ladder",
  "module_url": "/verify/taulib/docs/book-i-orbit-ladder/",
  "source_line_start": 57,
  "source_line_end": 62,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Ladder.lean#L57-L62",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Orbit.Ladder",
        "url": "/verify/taulib/docs/book-i-orbit-ladder/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Ladder.lean#L57-L62",
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

- Module: [TauLib.BookI.Orbit.Ladder](/verify/taulib/docs/book-i-orbit-ladder/)
- Source path: [`TauLib/BookI/Orbit/Ladder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Ladder.lean#L57-L62)
- Source range: L57-L62
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The hyperoperation at each ladder level (on Nat = depth values). -/
```

## Source Excerpt

```lean
def ladderOp : LadderLevel → Nat → Nat → Nat
  | .rho_level, _, m => m + 1        -- ρ: successor (ignores first arg)
  | .add_level, n, m => n + m        -- addition
  | .mul_level, n, m => n * m        -- multiplication
  | .exp_level, n, m => n ^ m        -- exponentiation
  | .tet_level, n, m => tetration n m -- tetration
```
