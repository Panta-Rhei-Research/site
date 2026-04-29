---
{
  "projection_kind": "taulib_declaration",
  "title": "hol_assoc_check",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-category-structure/hol-assoc-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.CategoryStructure`.",
  "declaration_id": "TauLib.BookII.Hartogs.CategoryStructure::hol_assoc_check",
  "declaration_slug": "hol-assoc-check",
  "kind": "def",
  "name": "hol_assoc_check",
  "module_name": "TauLib.BookII.Hartogs.CategoryStructure",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-category-structure/",
  "source_line_start": 117,
  "source_line_end": 130,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CategoryStructure.lean#L117-L130",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CategoryStructure.lean#L117-L130",
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
- Source path: [`TauLib/BookII/Hartogs/CategoryStructure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CategoryStructure.lean#L117-L130)
- Source range: L117-L130
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T29` — Associativity of Holomorphic Composition

## Immediate Comment / Docstring

```lean
/-- [II.T29] Associativity check for holomorphic composition.
    For sample endomorphisms f, g, h, verify:
    hol_comp f (hol_comp g h) n k = hol_comp (hol_comp f g) h n k

    This holds definitionally because:
    LHS = f(g(h(n, k), k), k)
    RHS = f(g(h(n, k), k), k)
    which are identical by function application. -/
```

## Source Excerpt

```lean
def hol_assoc_check (bound db : TauIdx) : Bool :=
  go 2 1 ((bound + 1) * (db + 1))
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k > db then go (x + 1) 1 (fuel - 1)
    else
      -- f = hol_id, g = hol_sq, h = hol_dbl
      let lhs := hol_comp hol_id (hol_comp hol_sq hol_dbl) x k
      let rhs := hol_comp (hol_comp hol_id hol_sq) hol_dbl x k
      let ok := lhs == rhs
      ok && go x (k + 1) (fuel - 1)
  termination_by fuel
```
