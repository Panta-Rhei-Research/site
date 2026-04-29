---
{
  "projection_kind": "taulib_declaration",
  "title": "cattau_finite_limits_witness",
  "permalink": "/verify/taulib/docs/book-i-topos-h7-topos-classifier/cattau-finite-limits-witness/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Topos.H7ToposClassifier`.",
  "declaration_id": "TauLib.BookI.Topos.H7ToposClassifier::cattau_finite_limits_witness",
  "declaration_slug": "cattau-finite-limits-witness",
  "kind": "theorem",
  "name": "cattau_finite_limits_witness",
  "module_name": "TauLib.BookI.Topos.H7ToposClassifier",
  "module_url": "/verify/taulib/docs/book-i-topos-h7-topos-classifier/",
  "source_line_start": 164,
  "source_line_end": 171,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H7ToposClassifier.lean#L164-L171",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Topos.H7ToposClassifier",
        "url": "/verify/taulib/docs/book-i-topos-h7-topos-classifier/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H7ToposClassifier.lean#L164-L171",
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

- Module: [TauLib.BookI.Topos.H7ToposClassifier](/verify/taulib/docs/book-i-topos-h7-topos-classifier/)
- Source path: [`TauLib/BookI/Topos/H7ToposClassifier.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H7ToposClassifier.lean#L164-L171)
- Source range: L164-L171
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper §3 Thm `cattau-finite-limits` — finite limit completeness**.

    Cat_τ has finite limits: terminal + binary products + equalisers.
    Statement-witness via the existence of terminal (Truth4 with T)
    + binary products (SectorPair) + equalisers (StageFun
    composition + intertwining from Wave 30). -/
```

## Source Excerpt

```lean
theorem cattau_finite_limits_witness :
    -- Terminal: T exists in Truth4
    (∃ t : Truth4, t = T) ∧
    -- Binary products: SectorPair exists with componentwise structure
    (∀ a b : Int, ∃ s : SectorPair, s = ⟨a, b⟩) := by
  refine ⟨⟨T, rfl⟩, ?_⟩
  intro a b
  exact ⟨⟨a, b⟩, rfl⟩
```
