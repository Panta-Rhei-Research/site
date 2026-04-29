---
{
  "projection_kind": "taulib_declaration",
  "title": "ladder_has_four_levels",
  "permalink": "/verify/taulib/docs/book-iii-enrichment-canonical-ladder/ladder-has-four-levels/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Enrichment.CanonicalLadder`.",
  "declaration_id": "TauLib.BookIII.Enrichment.CanonicalLadder::ladder_has_four_levels",
  "declaration_slug": "ladder-has-four-levels",
  "kind": "theorem",
  "name": "ladder_has_four_levels",
  "module_name": "TauLib.BookIII.Enrichment.CanonicalLadder",
  "module_url": "/verify/taulib/docs/book-iii-enrichment-canonical-ladder/",
  "source_line_start": 273,
  "source_line_end": 274,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/CanonicalLadder.lean#L273-L274",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/CanonicalLadder.lean#L273-L274",
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
- Source path: [`TauLib/BookIII/Enrichment/CanonicalLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/CanonicalLadder.lean#L273-L274)
- Source range: L273-L274
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T04` — Canonical Ladder Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T04] Structural uniqueness: three applications of succ from
    any starting level reach E₃. The ladder has exactly 4 levels. -/
```

## Source Excerpt

```lean
theorem ladder_has_four_levels :
    [EnrLevel.E0, EnrLevel.E1, EnrLevel.E2, EnrLevel.E3].length = 4 := rfl
```
