---
{
  "projection_kind": "taulib_declaration",
  "title": "id_two_cell_tower_coherent",
  "permalink": "/verify/taulib/docs/book-ii-enrichment-two-categories/id-two-cell-tower-coherent/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Enrichment.TwoCategories`.",
  "declaration_id": "TauLib.BookII.Enrichment.TwoCategories::id_two_cell_tower_coherent",
  "declaration_slug": "id-two-cell-tower-coherent",
  "kind": "theorem",
  "name": "id_two_cell_tower_coherent",
  "module_name": "TauLib.BookII.Enrichment.TwoCategories",
  "module_url": "/verify/taulib/docs/book-ii-enrichment-two-categories/",
  "source_line_start": 444,
  "source_line_end": 447,
  "registry_ids": [
    "II.D55"
  ],
  "related_registry_items": [
    {
      "id": "II.D55",
      "title": "2-Category Structure",
      "url": "/registry/object/II.D55/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/TwoCategories.lean#L444-L447",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/TwoCategories.lean#L444-L447",
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

- Module: [TauLib.BookII.Enrichment.TwoCategories](/verify/taulib/docs/book-ii-enrichment-two-categories/)
- Source path: [`TauLib/BookII/Enrichment/TwoCategories.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/TwoCategories.lean#L444-L447)
- Source range: L444-L447
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.D55` — 2-Category Structure

## Immediate Comment / Docstring

```lean
/-- [II.D55] Formal proof: the identity 2-cell is tower-coherent.
    reduce(id_two_cell(x, l), k) = id_two_cell(x, k) for k <= l.
    This is reduction_compat. -/
```

## Source Excerpt

```lean
theorem id_two_cell_tower_coherent (x : TauIdx) {k l : TauIdx} (h : k ≤ l) :
    reduce (id_two_cell x l) k = id_two_cell x k := by
  simp only [id_two_cell]
  exact reduction_compat x h
```
