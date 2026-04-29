---
{
  "projection_kind": "taulib_declaration",
  "title": "tower_atom_pos",
  "permalink": "/verify/taulib/docs/book-i-coordinates-tower-atoms/tower-atom-pos/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Coordinates.TowerAtoms`.",
  "declaration_id": "TauLib.BookI.Coordinates.TowerAtoms::tower_atom_pos",
  "declaration_slug": "tower-atom-pos",
  "kind": "theorem",
  "name": "tower_atom_pos",
  "module_name": "TauLib.BookI.Coordinates.TowerAtoms",
  "module_url": "/verify/taulib/docs/book-i-coordinates-tower-atoms/",
  "source_line_start": 104,
  "source_line_end": 108,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/TowerAtoms.lean#L104-L108",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Coordinates.TowerAtoms",
        "url": "/verify/taulib/docs/book-i-coordinates-tower-atoms/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/TowerAtoms.lean#L104-L108",
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

- Module: [TauLib.BookI.Coordinates.TowerAtoms](/verify/taulib/docs/book-i-coordinates-tower-atoms/)
- Source path: [`TauLib/BookI/Coordinates/TowerAtoms.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/TowerAtoms.lean#L104-L108)
- Source range: L104-L108
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Tower atoms are positive for a ≥ 1. -/
```

## Source Excerpt

```lean
theorem tower_atom_pos (a b c : TauIdx) (ha : a ≥ 1) : tower_atom a b c > 0 := by
  unfold tower_atom
  have := tetration_pos a ha c
  exact Nat.pos_of_ne_zero (Nat.ne_zero_of_lt (Nat.lt_of_lt_of_le
    (show 0 < 1 by omega) (Nat.one_le_pow b (tetration a c) (by omega))))
```
