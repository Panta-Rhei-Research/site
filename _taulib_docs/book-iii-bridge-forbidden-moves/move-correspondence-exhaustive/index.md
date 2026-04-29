---
{
  "projection_kind": "taulib_declaration",
  "title": "move_correspondence_exhaustive",
  "permalink": "/verify/taulib/docs/book-iii-bridge-forbidden-moves/move-correspondence-exhaustive/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Bridge.ForbiddenMoves`.",
  "declaration_id": "TauLib.BookIII.Bridge.ForbiddenMoves::move_correspondence_exhaustive",
  "declaration_slug": "move-correspondence-exhaustive",
  "kind": "def",
  "name": "move_correspondence_exhaustive",
  "module_name": "TauLib.BookIII.Bridge.ForbiddenMoves",
  "module_url": "/verify/taulib/docs/book-iii-bridge-forbidden-moves/",
  "source_line_start": 186,
  "source_line_end": 197,
  "registry_ids": [
    "III.T43"
  ],
  "related_registry_items": [
    {
      "id": "III.T43",
      "title": "Move-Bridge Correspondence",
      "url": "/registry/object/III.T43/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ForbiddenMoves.lean#L186-L197",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Bridge.ForbiddenMoves",
        "url": "/verify/taulib/docs/book-iii-bridge-forbidden-moves/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ForbiddenMoves.lean#L186-L197",
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

- Module: [TauLib.BookIII.Bridge.ForbiddenMoves](/verify/taulib/docs/book-iii-bridge-forbidden-moves/)
- Source path: [`TauLib/BookIII/Bridge/ForbiddenMoves.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ForbiddenMoves.lean#L186-L197)
- Source range: L186-L197
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T43` — Move-Bridge Correspondence

## Immediate Comment / Docstring

```lean
/-- [III.T43] Correspondence exhaustiveness: all 5 moves are distinct
    and each has a violated axiom. -/
```

## Source Excerpt

```lean
def move_correspondence_exhaustive : Bool :=
  -- All moves have distinct indices
  let indices := all_forbidden_moves.map ForbiddenMove.toNat
  let distinct := indices.length == 5 &&
    indices.eraseDups.length == 5
  -- All moves have a violated axiom
  let all_violated := all_forbidden_moves.all (fun fm =>
    (violated_axiom fm).toNat <= 13)
  -- Bridge damage is bounded
  let all_bounded := all_forbidden_moves.all (fun fm =>
    bridge_damage fm <= 3)
  distinct && all_violated && all_bounded
```
