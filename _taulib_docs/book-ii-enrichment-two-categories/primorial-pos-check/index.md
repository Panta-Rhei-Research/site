---
{
  "projection_kind": "taulib_declaration",
  "title": "primorial_pos_check",
  "permalink": "/verify/taulib/docs/book-ii-enrichment-two-categories/primorial-pos-check/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Enrichment.TwoCategories`.",
  "declaration_id": "TauLib.BookII.Enrichment.TwoCategories::primorial_pos_check",
  "declaration_slug": "primorial-pos-check",
  "kind": "theorem",
  "name": "primorial_pos_check",
  "module_name": "TauLib.BookII.Enrichment.TwoCategories",
  "module_url": "/verify/taulib/docs/book-ii-enrichment-two-categories/",
  "source_line_start": 462,
  "source_line_end": 465,
  "registry_ids": [
    "II.P13"
  ],
  "related_registry_items": [
    {
      "id": "II.P13",
      "title": "Character Decomposition",
      "url": "/registry/object/II.P13/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/TwoCategories.lean#L462-L465",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/TwoCategories.lean#L462-L465",
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
- Source path: [`TauLib/BookII/Enrichment/TwoCategories.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/TwoCategories.lean#L462-L465)
- Source range: L462-L465
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.P13` — Character Decomposition

## Immediate Comment / Docstring

```lean
/-- [II.P13] Formal proof: enrichment iteration is well-founded.
    The primorial P_k is positive for all k >= 0.
    Verified computationally for stages 0 through 5. -/
```

## Source Excerpt

```lean
theorem primorial_pos_check :
    (List.range 6).all (fun k => primorial k > 0) = true := by native_decide

end Tau.BookII.Enrichment
```
