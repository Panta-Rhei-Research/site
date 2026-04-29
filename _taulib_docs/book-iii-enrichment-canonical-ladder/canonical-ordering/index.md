---
{
  "projection_kind": "taulib_declaration",
  "title": "canonical_ordering",
  "permalink": "/verify/taulib/docs/book-iii-enrichment-canonical-ladder/canonical-ordering/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Enrichment.CanonicalLadder`.",
  "declaration_id": "TauLib.BookIII.Enrichment.CanonicalLadder::canonical_ordering",
  "declaration_slug": "canonical-ordering",
  "kind": "theorem",
  "name": "canonical_ordering",
  "module_name": "TauLib.BookIII.Enrichment.CanonicalLadder",
  "module_url": "/verify/taulib/docs/book-iii-enrichment-canonical-ladder/",
  "source_line_start": 277,
  "source_line_end": 283,
  "registry_ids": [
    "III.T04"
  ],
  "related_registry_items": [
    {
      "id": "III.T04",
      "title": "Canonical Ladder Theorem",
      "url": "/registry/object/III.T04/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/CanonicalLadder.lean#L277-L283",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Enrichment.CanonicalLadder",
        "url": "/verify/taulib/docs/book-iii-enrichment-canonical-ladder/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/CanonicalLadder.lean#L277-L283",
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

- Module: [TauLib.BookIII.Enrichment.CanonicalLadder](/verify/taulib/docs/book-iii-enrichment-canonical-ladder/)
- Source path: [`TauLib/BookIII/Enrichment/CanonicalLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/CanonicalLadder.lean#L277-L283)
- Source range: L277-L283
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T04` — Canonical Ladder Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T04] Canonical ordering: E₀ < E₁ < E₂ < E₃ via toNat. -/
```

## Source Excerpt

```lean
theorem canonical_ordering :
    EnrLevel.E0.toNat < EnrLevel.E1.toNat ∧
    EnrLevel.E1.toNat < EnrLevel.E2.toNat ∧
    EnrLevel.E2.toNat < EnrLevel.E3.toNat := by
  exact ⟨by decide, by decide, by decide⟩

end Tau.BookIII.Enrichment
```
