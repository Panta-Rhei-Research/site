---
{
  "projection_kind": "taulib_declaration",
  "title": "full_canonical_ladder",
  "permalink": "/corpus/taulib/docs/book-iii-enrichment-canonical-ladder/full-canonical-ladder/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Enrichment.CanonicalLadder`.",
  "declaration_id": "TauLib.BookIII.Enrichment.CanonicalLadder::full_canonical_ladder",
  "declaration_slug": "full-canonical-ladder",
  "kind": "def",
  "name": "full_canonical_ladder",
  "module_name": "TauLib.BookIII.Enrichment.CanonicalLadder",
  "module_url": "/corpus/taulib/docs/book-iii-enrichment-canonical-ladder/",
  "source_line_start": 191,
  "source_line_end": 192,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/CanonicalLadder.lean#L191-L192",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Enrichment.CanonicalLadder",
        "url": "/corpus/taulib/docs/book-iii-enrichment-canonical-ladder/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/CanonicalLadder.lean#L191-L192",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "data/computed value",
      "status": "data/computed value"
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

- Module: [TauLib.BookIII.Enrichment.CanonicalLadder](/corpus/taulib/docs/book-iii-enrichment-canonical-ladder/)
- Source path: [`TauLib/BookIII/Enrichment/CanonicalLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/CanonicalLadder.lean#L191-L192)
- Source range: L191-L192
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- `III.T04` — Canonical Ladder Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T04] Full canonical ladder verification: the master check
    combining all components of the Canonical Ladder Theorem. -/
```

## Source Excerpt

```lean
def full_canonical_ladder (bound db : TauIdx) : Bool :=
  canonical_ladder_check bound db && ladder_checker bound db
```
