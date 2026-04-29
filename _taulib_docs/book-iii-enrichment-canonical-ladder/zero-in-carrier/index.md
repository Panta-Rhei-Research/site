---
{
  "projection_kind": "taulib_declaration",
  "title": "zero_in_carrier",
  "permalink": "/verify/taulib/docs/book-iii-enrichment-canonical-ladder/zero-in-carrier/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Enrichment.CanonicalLadder`.",
  "declaration_id": "TauLib.BookIII.Enrichment.CanonicalLadder::zero_in_carrier",
  "declaration_slug": "zero-in-carrier",
  "kind": "theorem",
  "name": "zero_in_carrier",
  "module_name": "TauLib.BookIII.Enrichment.CanonicalLadder",
  "module_url": "/verify/taulib/docs/book-iii-enrichment-canonical-ladder/",
  "source_line_start": 256,
  "source_line_end": 258,
  "registry_ids": [
    "III.T01"
  ],
  "related_registry_items": [
    {
      "id": "III.T01",
      "title": "Non-Emptiness Theorem",
      "url": "/registry/object/III.T01/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/CanonicalLadder.lean#L256-L258",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/CanonicalLadder.lean#L256-L258",
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
- Source path: [`TauLib/BookIII/Enrichment/CanonicalLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/CanonicalLadder.lean#L256-L258)
- Source range: L256-L258
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T01` — Non-Emptiness Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T01] Structural non-emptiness: reduce(0, k) = 0 provides
    a witness at every stage. Zero is always in the carrier. -/
```

## Source Excerpt

```lean
theorem zero_in_carrier (k : TauIdx) :
    reduce 0 k = 0 := by
  simp [reduce, Nat.zero_mod]
```
