---
{
  "projection_kind": "taulib_declaration",
  "title": "hol_assoc_exhaustive_check",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-category-structure/hol-assoc-exhaustive-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.CategoryStructure`.",
  "declaration_id": "TauLib.BookII.Hartogs.CategoryStructure::hol_assoc_exhaustive_check",
  "declaration_slug": "hol-assoc-exhaustive-check",
  "kind": "def",
  "name": "hol_assoc_exhaustive_check",
  "module_name": "TauLib.BookII.Hartogs.CategoryStructure",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-category-structure/",
  "source_line_start": 150,
  "source_line_end": 199,
  "registry_ids": [
    "II.T29"
  ],
  "related_registry_items": [
    {
      "id": "II.T29",
      "title": "Associativity of Holomorphic Composition",
      "url": "/registry/object/II.T29/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CategoryStructure.lean#L150-L199",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.CategoryStructure",
        "url": "/verify/taulib/docs/book-ii-hartogs-category-structure/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CategoryStructure.lean#L150-L199",
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

- Module: [TauLib.BookII.Hartogs.CategoryStructure](/verify/taulib/docs/book-ii-hartogs-category-structure/)
- Source path: [`TauLib/BookII/Hartogs/CategoryStructure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CategoryStructure.lean#L150-L199)
- Source range: L150-L199
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T29` — Associativity of Holomorphic Composition

## Immediate Comment / Docstring

```lean
/-- [II.T29] Associativity for ALL triples from {id, sq, dbl, zero}.
    Tests all 4^3 = 64 triples on [2, bound] x [1, db]. -/
```

## Source Excerpt

```lean
def hol_assoc_exhaustive_check (bound db : TauIdx) : Bool :=
  let fns := [hol_id, hol_sq, hol_dbl, hol_zero]
  go_f fns fns fns 2 1 bound db (4 * 4 * 4 * (bound + 1) * (db + 1))
where
  go_f (fs gs hs : List (TauIdx -> TauIdx -> TauIdx))
       (x k : Nat) (bound db : Nat)
       (fuel : Nat) : Bool :=
    if fuel = 0 then true
    else
      match fs with
      | [] => true
      | f :: fs' =>
        go_g f gs hs x k bound db (fuel - 1) &&
        go_f fs' gs hs x k bound db (fuel - 1)
  termination_by fuel
  go_g (f : TauIdx -> TauIdx -> TauIdx)
       (gs hs : List (TauIdx -> TauIdx -> TauIdx))
       (x k : Nat) (bound db : Nat)
       (fuel : Nat) : Bool :=
    if fuel = 0 then true
    else
      match gs with
      | [] => true
      | g :: gs' =>
        go_h f g hs x k bound db (fuel - 1) &&
        go_g f gs' hs x k bound db (fuel - 1)
  termination_by fuel
  go_h (f g : TauIdx -> TauIdx -> TauIdx)
       (hs : List (TauIdx -> TauIdx -> TauIdx))
       (x k : Nat) (bound db : Nat)
       (fuel : Nat) : Bool :=
    if fuel = 0 then true
    else
      match hs with
      | [] => true
      | h :: hs' =>
        verify f g h x k bound db (fuel - 1) &&
        go_h f g hs' x k bound db (fuel - 1)
  termination_by fuel
  verify (f g h : TauIdx -> TauIdx -> TauIdx)
         (x k : Nat) (bound db : Nat)
         (fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k > db then verify f g h (x + 1) 1 bound db (fuel - 1)
    else
      let lhs := hol_comp f (hol_comp g h) x k
      let rhs := hol_comp (hol_comp f g) h x k
      (lhs == rhs) && verify f g h x (k + 1) bound db (fuel - 1)
  termination_by fuel
```
