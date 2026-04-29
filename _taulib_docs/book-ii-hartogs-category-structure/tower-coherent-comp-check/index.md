---
{
  "projection_kind": "taulib_declaration",
  "title": "tower_coherent_comp_check",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-category-structure/tower-coherent-comp-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.CategoryStructure`.",
  "declaration_id": "TauLib.BookII.Hartogs.CategoryStructure::tower_coherent_comp_check",
  "declaration_slug": "tower-coherent-comp-check",
  "kind": "def",
  "name": "tower_coherent_comp_check",
  "module_name": "TauLib.BookII.Hartogs.CategoryStructure",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-category-structure/",
  "source_line_start": 278,
  "source_line_end": 291,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CategoryStructure.lean#L278-L291",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CategoryStructure.lean#L278-L291",
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
- Source path: [`TauLib/BookII/Hartogs/CategoryStructure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CategoryStructure.lean#L278-L291)
- Source range: L278-L291
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Tower coherence of composed reduce-based endomorphisms.
    If f(n, k) = reduce(g(n), k) for some g, then f is tower-coherent.
    Composing two such f's gives another tower-coherent endomorphism. -/
```

## Source Excerpt

```lean
def tower_coherent_comp_check (bound db : TauIdx) : Bool :=
  go 2 1 1 ((bound + 1) * (db + 1) * (db + 1))
where
  go (x k l fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k > db then go (x + 1) 1 1 (fuel - 1)
    else if l > db then go x (k + 1) 1 (fuel - 1)
    else
      -- For (sq . dbl): check reduce(comp(x, l), k) = comp(x, k) for k <= l
      let ok := !(k ≤ l) ||
        (reduce (hol_comp hol_sq hol_dbl x l) k == hol_comp hol_sq hol_dbl x k)
      ok && go x k (l + 1) (fuel - 1)
  termination_by fuel
```
