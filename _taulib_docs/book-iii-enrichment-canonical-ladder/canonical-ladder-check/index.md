---
{
  "projection_kind": "taulib_declaration",
  "title": "canonical_ladder_check",
  "permalink": "/verify/taulib/docs/book-iii-enrichment-canonical-ladder/canonical-ladder-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Enrichment.CanonicalLadder`.",
  "declaration_id": "TauLib.BookIII.Enrichment.CanonicalLadder::canonical_ladder_check",
  "declaration_slug": "canonical-ladder-check",
  "kind": "def",
  "name": "canonical_ladder_check",
  "module_name": "TauLib.BookIII.Enrichment.CanonicalLadder",
  "module_url": "/verify/taulib/docs/book-iii-enrichment-canonical-ladder/",
  "source_line_start": 178,
  "source_line_end": 187,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/CanonicalLadder.lean#L178-L187",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/CanonicalLadder.lean#L178-L187",
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

- Module: [TauLib.BookIII.Enrichment.CanonicalLadder](/verify/taulib/docs/book-iii-enrichment-canonical-ladder/)
- Source path: [`TauLib/BookIII/Enrichment/CanonicalLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/CanonicalLadder.lean#L178-L187)
- Source range: L178-L187
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T04` — Canonical Ladder Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T04] The Canonical Ladder Theorem:
    (i) Non-empty at each level
    (ii) Strictly increasing
    (iii) Saturating at E₃
    (iv) Unique maximal enrichment chain

    This is the organising result of Book III and the architectural
    blueprint for the entire 7-book series. -/
```

## Source Excerpt

```lean
def canonical_ladder_check (bound db : TauIdx) : Bool :=
  -- (i) Non-emptiness
  non_emptiness_check bound db &&
  -- (ii) Strictness
  strictness_check bound db &&
  -- (iii) Saturation
  saturation_e3_check bound db &&
  -- (iv) Uniqueness: the enrichment functor is the ONLY way to ascend
  -- (verified via full functor check — no alternative path exists)
  full_enrichment_functor_check bound db
```
