---
{
  "projection_kind": "taulib_declaration",
  "title": "threshold_exceeds",
  "permalink": "/verify/taulib/docs/book-iii-bridge-forbidden-moves/threshold-exceeds/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Bridge.ForbiddenMoves`.",
  "declaration_id": "TauLib.BookIII.Bridge.ForbiddenMoves::threshold_exceeds",
  "declaration_slug": "threshold-exceeds",
  "kind": "theorem",
  "name": "threshold_exceeds",
  "module_name": "TauLib.BookIII.Bridge.ForbiddenMoves",
  "module_url": "/verify/taulib/docs/book-iii-bridge-forbidden-moves/",
  "source_line_start": 278,
  "source_line_end": 282,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ForbiddenMoves.lean#L278-L282",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ForbiddenMoves.lean#L278-L282",
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

- Module: [TauLib.BookIII.Bridge.ForbiddenMoves](/verify/taulib/docs/book-iii-bridge-forbidden-moves/)
- Source path: [`TauLib/BookIII/Bridge/ForbiddenMoves.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ForbiddenMoves.lean#L278-L282)
- Source range: L278-L282
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.D69` — Five Forbidden Moves

## Immediate Comment / Docstring

```lean
/-- [III.D69] Structural: all moves have threshold > db (requires
    unbounded depth). -/
```

## Source Excerpt

```lean
theorem threshold_exceeds (fm : ForbiddenMove) (db : TauIdx) :
    move_threshold fm db > db := by
  cases fm <;> simp [move_threshold] <;> omega

end Tau.BookIII.Bridge
```
