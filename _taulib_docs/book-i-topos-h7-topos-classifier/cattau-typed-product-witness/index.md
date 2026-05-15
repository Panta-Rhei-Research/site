---
{
  "projection_kind": "taulib_declaration",
  "title": "cattau_typed_product_witness",
  "permalink": "/corpus/taulib/docs/book-i-topos-h7-topos-classifier/cattau-typed-product-witness/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Topos.H7ToposClassifier`.",
  "declaration_id": "TauLib.BookI.Topos.H7ToposClassifier::cattau_typed_product_witness",
  "declaration_slug": "cattau-typed-product-witness",
  "kind": "theorem",
  "name": "cattau_typed_product_witness",
  "module_name": "TauLib.BookI.Topos.H7ToposClassifier",
  "module_url": "/corpus/taulib/docs/book-i-topos-h7-topos-classifier/",
  "source_line_start": 152,
  "source_line_end": 156,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H7ToposClassifier.lean#L152-L156",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Topos.H7ToposClassifier",
        "url": "/corpus/taulib/docs/book-i-topos-h7-topos-classifier/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H7ToposClassifier.lean#L152-L156",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookI.Topos.H7ToposClassifier](/corpus/taulib/docs/book-i-topos-h7-topos-classifier/)
- Source path: [`TauLib/BookI/Topos/H7ToposClassifier.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H7ToposClassifier.lean#L152-L156)
- Source range: L152-L156
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper §3 Thm `typed-product-exists` — witness via SectorPair**.

    The typed binary product X ×_τ Y in Cat_τ corresponds to the
    SectorPair structure: a pair `⟨b, c⟩ : Int × Int` with
    componentwise operations.  The "typed" qualifier reflects
    that this product respects the bipolar B/C bipartition
    (a typed-pair, not a free pair). -/
```

## Source Excerpt

```lean
theorem cattau_typed_product_witness (a b : Int) :
    -- The typed product structure: SectorPair pairs with B/C
    -- componentwise multiplication preserving bipartition
    SectorPair.mul ⟨a, 0⟩ ⟨0, b⟩ = ⟨0, 0⟩ := by
  simp [SectorPair.mul]
```
