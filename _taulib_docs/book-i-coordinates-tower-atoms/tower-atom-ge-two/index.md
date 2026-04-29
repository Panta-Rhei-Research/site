---
{
  "projection_kind": "taulib_declaration",
  "title": "tower_atom_ge_two",
  "permalink": "/verify/taulib/docs/book-i-coordinates-tower-atoms/tower-atom-ge-two/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Coordinates.TowerAtoms`.",
  "declaration_id": "TauLib.BookI.Coordinates.TowerAtoms::tower_atom_ge_two",
  "declaration_slug": "tower-atom-ge-two",
  "kind": "theorem",
  "name": "tower_atom_ge_two",
  "module_name": "TauLib.BookI.Coordinates.TowerAtoms",
  "module_url": "/verify/taulib/docs/book-i-coordinates-tower-atoms/",
  "source_line_start": 94,
  "source_line_end": 101,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/TowerAtoms.lean#L94-L101",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/TowerAtoms.lean#L94-L101",
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
- Source path: [`TauLib/BookI/Coordinates/TowerAtoms.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/TowerAtoms.lean#L94-L101)
- Source range: L94-L101
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Tower atoms are at least 2 for prime base, b ≥ 1, c ≥ 1. -/
```

## Source Excerpt

```lean
theorem tower_atom_ge_two (a b c : TauIdx) (ha : a ≥ 2) (hb : b ≥ 1) (hc : c ≥ 1) :
    tower_atom a b c ≥ 2 := by
  unfold tower_atom
  have htet : tetration a c ≥ 2 := Nat.le_trans ha (tetration_ge_base a ha c hc)
  have hpow : (tetration a c) ^ b ≥ (tetration a c) ^ 1 :=
    Nat.pow_le_pow_right (by omega : tetration a c > 0) hb
  rw [Nat.pow_one] at hpow
  exact Nat.le_trans htet hpow
```
