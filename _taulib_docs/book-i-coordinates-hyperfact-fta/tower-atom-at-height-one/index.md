---
{
  "projection_kind": "taulib_declaration",
  "title": "tower_atom_at_height_one",
  "permalink": "/verify/taulib/docs/book-i-coordinates-hyperfact-fta/tower-atom-at-height-one/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Coordinates.HyperfactFTA`.",
  "declaration_id": "TauLib.BookI.Coordinates.HyperfactFTA::tower_atom_at_height_one",
  "declaration_slug": "tower-atom-at-height-one",
  "kind": "theorem",
  "name": "tower_atom_at_height_one",
  "module_name": "TauLib.BookI.Coordinates.HyperfactFTA",
  "module_url": "/verify/taulib/docs/book-i-coordinates-hyperfact-fta/",
  "source_line_start": 56,
  "source_line_end": 63,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/HyperfactFTA.lean#L56-L63",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Coordinates.HyperfactFTA",
        "url": "/verify/taulib/docs/book-i-coordinates-hyperfact-fta/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/HyperfactFTA.lean#L56-L63",
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

- Module: [TauLib.BookI.Coordinates.HyperfactFTA](/verify/taulib/docs/book-i-coordinates-hyperfact-fta/)
- Source path: [`TauLib/BookI/Coordinates/HyperfactFTA.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/HyperfactFTA.lean#L56-L63)
- Source range: L56-L63
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- `tower_atom a b 1 = a^b`: the tower atom at height 1 collapses
    to ordinary exponentiation.  Direct from `tetration a 1 = a`. -/
```

## Source Excerpt

```lean
theorem tower_atom_at_height_one (a b : TauIdx) :
    tower_atom a b 1 = a ^ b := by
  show (tetration a 1) ^ b = a ^ b
  have : tetration a 1 = a := by
    show a ^ (tetration a 0) = a
    show a ^ 1 = a
    exact Nat.pow_one a
  rw [this]
```
