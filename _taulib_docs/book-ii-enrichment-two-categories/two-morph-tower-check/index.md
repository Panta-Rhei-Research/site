---
{
  "projection_kind": "taulib_declaration",
  "title": "two_morph_tower_check",
  "permalink": "/verify/taulib/docs/book-ii-enrichment-two-categories/two-morph-tower-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Enrichment.TwoCategories`.",
  "declaration_id": "TauLib.BookII.Enrichment.TwoCategories::two_morph_tower_check",
  "declaration_slug": "two-morph-tower-check",
  "kind": "def",
  "name": "two_morph_tower_check",
  "module_name": "TauLib.BookII.Enrichment.TwoCategories",
  "module_url": "/verify/taulib/docs/book-ii-enrichment-two-categories/",
  "source_line_start": 185,
  "source_line_end": 201,
  "registry_ids": [
    "II.D56"
  ],
  "related_registry_items": [
    {
      "id": "II.D56",
      "title": "2-Morphism",
      "url": "/registry/object/II.D56/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/TwoCategories.lean#L185-L201",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Enrichment.TwoCategories",
        "url": "/verify/taulib/docs/book-ii-enrichment-two-categories/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/TwoCategories.lean#L185-L201",
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

- Module: [TauLib.BookII.Enrichment.TwoCategories](/verify/taulib/docs/book-ii-enrichment-two-categories/)
- Source path: [`TauLib/BookII/Enrichment/TwoCategories.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/TwoCategories.lean#L185-L201)
- Source range: L185-L201
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D56` — 2-Morphism

## Immediate Comment / Docstring

```lean
/-- [II.D56] 2-morphism tower coherence check:
    A 2-cell eta is tower-coherent if reduce(eta(x, l), k) = eta(reduce(x, k), k)
    for k <= l. We verify this for the sample 2-cells. -/
```

## Source Excerpt

```lean
def two_morph_tower_check (bound db : TauIdx) : Bool :=
  go 2 1 1 ((bound + 1) * (db + 1) * (db + 1))
where
  go (x k l fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k > db then go (x + 1) 1 1 (fuel - 1)
    else if l > db then go x (k + 1) (k + 1) (fuel - 1)
    else if k > l then go x k (l + 1) (fuel - 1)
    else
      -- Check two_sq: reduce(sq(x, l), k) = sq(x, k)
      -- We check: reduce(sq(x, l), k) = sq(x, k)
      let sq_ok := reduce (two_sq x l) k == two_sq x k
      -- Check id_two_cell: reduce(reduce(x, l), k) = reduce(x, k) — this is reduction_compat
      let id_ok := reduce (id_two_cell x l) k == id_two_cell x k
      sq_ok && id_ok && go x k (l + 1) (fuel - 1)
  termination_by fuel
```
