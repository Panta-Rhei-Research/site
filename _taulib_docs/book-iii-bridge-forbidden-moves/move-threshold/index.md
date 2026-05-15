---
{
  "projection_kind": "taulib_declaration",
  "title": "move_threshold",
  "permalink": "/corpus/taulib/docs/book-iii-bridge-forbidden-moves/move-threshold/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Bridge.ForbiddenMoves`.",
  "declaration_id": "TauLib.BookIII.Bridge.ForbiddenMoves::move_threshold",
  "declaration_slug": "move-threshold",
  "kind": "def",
  "name": "move_threshold",
  "module_name": "TauLib.BookIII.Bridge.ForbiddenMoves",
  "module_url": "/corpus/taulib/docs/book-iii-bridge-forbidden-moves/",
  "source_line_start": 79,
  "source_line_end": 85,
  "registry_ids": [
    "III.D69"
  ],
  "related_registry_items": [
    {
      "id": "III.D69",
      "title": "Five Forbidden Moves",
      "url": "/registry/object/III.D69/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ForbiddenMoves.lean#L79-L85",
  "formal_status": "defined",
  "declaration_role": "definition",
  "formal_status_label": "definition",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Bridge.ForbiddenMoves",
        "url": "/corpus/taulib/docs/book-iii-bridge-forbidden-moves/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ForbiddenMoves.lean#L79-L85",
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

- Module: [TauLib.BookIII.Bridge.ForbiddenMoves](/corpus/taulib/docs/book-iii-bridge-forbidden-moves/)
- Source path: [`TauLib/BookIII/Bridge/ForbiddenMoves.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ForbiddenMoves.lean#L79-L85)
- Source range: L79-L85
- Kind: `def`
- Public role: `definition`
- Formal status hint: `definition`

## Registry Links

- `III.D69` — Five Forbidden Moves

## Immediate Comment / Docstring

```lean
/-- [III.D69] The minimum primorial depth at which the forbidden move
    manifests. Below this depth, the move is harmless (finite state space
    makes everything bounded). -/
```

## Source Excerpt

```lean
def move_threshold (fm : ForbiddenMove) (db : TauIdx) : TauIdx :=
  match fm with
  | .unbounded_fanout           => db + 1   -- exceeds any finite depth
  | .global_equality            => db + 1   -- requires entire tower
  | .succinct_circuits          => db + 1   -- circuit must see all levels
  | .exponential_quantification => db + 1   -- 2^Prim(k) exceeds any level
  | .nonlocal_disguise          => db + 1   -- NF uniqueness is tower-global
```
