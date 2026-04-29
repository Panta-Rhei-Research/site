---
{
  "projection_kind": "taulib_declaration",
  "title": "tower_atom_prime_factor",
  "permalink": "/verify/taulib/docs/book-i-coordinates-tower-atoms/tower-atom-prime-factor/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Coordinates.TowerAtoms`.",
  "declaration_id": "TauLib.BookI.Coordinates.TowerAtoms::tower_atom_prime_factor",
  "declaration_slug": "tower-atom-prime-factor",
  "kind": "theorem",
  "name": "tower_atom_prime_factor",
  "module_name": "TauLib.BookI.Coordinates.TowerAtoms",
  "module_url": "/verify/taulib/docs/book-i-coordinates-tower-atoms/",
  "source_line_start": 146,
  "source_line_end": 157,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/TowerAtoms.lean#L146-L157",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/TowerAtoms.lean#L146-L157",
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
- Source path: [`TauLib/BookI/Coordinates/TowerAtoms.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/TowerAtoms.lean#L146-L157)
- Source range: L146-L157
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- All prime factors of T(a,b,c) equal a (when a is prime, b ≥ 1, c ≥ 1). -/
```

## Source Excerpt

```lean
theorem tower_atom_prime_factor (a b c p : TauIdx)
    (ha : idx_prime a) (hb : b ≥ 1) (hc : c ≥ 1)
    (hp : idx_prime p) (hpT : p ∣ tower_atom a b c) : p = a := by
  rw [tower_atom_as_prime_power a b c hc] at hpT
  have htet := tetration_pos a (show a ≥ 1 by have := ha.1; simp only [TauIdx] at *; omega) (c - 1)
  have hexp : b * tetration a (c - 1) ≥ 1 := by
    have h := Nat.mul_le_mul hb htet
    simp only [TauIdx] at *; omega
  have hpa : p ∣ a := prime_dvd_of_dvd_pow hp _ hexp hpT
  rcases ha.2 p hpa with h | h
  · have := hp.1; simp only [TauIdx] at *; omega
  · exact h
```
