---
{
  "projection_kind": "taulib_declaration",
  "title": "tower_finite_decidable",
  "permalink": "/verify/taulib/docs/book-iii-bridge-conjecture-gaps/tower-finite-decidable/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Bridge.ConjectureGaps`.",
  "declaration_id": "TauLib.BookIII.Bridge.ConjectureGaps::tower_finite_decidable",
  "declaration_slug": "tower-finite-decidable",
  "kind": "theorem",
  "name": "tower_finite_decidable",
  "module_name": "TauLib.BookIII.Bridge.ConjectureGaps",
  "module_url": "/verify/taulib/docs/book-iii-bridge-conjecture-gaps/",
  "source_line_start": 213,
  "source_line_end": 214,
  "registry_ids": [
    "III.T79"
  ],
  "related_registry_items": [
    {
      "id": "III.T79",
      "title": "Tower Finite Decidable",
      "url": "/registry/object/III.T79/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ConjectureGaps.lean#L213-L214",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Bridge.ConjectureGaps",
        "url": "/verify/taulib/docs/book-iii-bridge-conjecture-gaps/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ConjectureGaps.lean#L213-L214",
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

- Module: [TauLib.BookIII.Bridge.ConjectureGaps](/verify/taulib/docs/book-iii-bridge-conjecture-gaps/)
- Source path: [`TauLib/BookIII/Bridge/ConjectureGaps.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ConjectureGaps.lean#L213-L214)
- Source range: L213-L214
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T79` — Tower Finite Decidable

## Immediate Comment / Docstring

```lean
/-- [III.T79] Tower decidability: all three conjectures have defined
    gap types, forbidden moves, and scope labels. -/
```

## Source Excerpt

```lean
theorem tower_finite_decidable :
    tower_decidable_check = true := by native_decide
```
