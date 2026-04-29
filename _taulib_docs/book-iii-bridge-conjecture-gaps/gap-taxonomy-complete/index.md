---
{
  "projection_kind": "taulib_declaration",
  "title": "gap_taxonomy_complete",
  "permalink": "/verify/taulib/docs/book-iii-bridge-conjecture-gaps/gap-taxonomy-complete/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Bridge.ConjectureGaps`.",
  "declaration_id": "TauLib.BookIII.Bridge.ConjectureGaps::gap_taxonomy_complete",
  "declaration_slug": "gap-taxonomy-complete",
  "kind": "def",
  "name": "gap_taxonomy_complete",
  "module_name": "TauLib.BookIII.Bridge.ConjectureGaps",
  "module_url": "/verify/taulib/docs/book-iii-bridge-conjecture-gaps/",
  "source_line_start": 201,
  "source_line_end": 205,
  "registry_ids": [
    "III.T80"
  ],
  "related_registry_items": [
    {
      "id": "III.T80",
      "title": "Bridge Necessary Insufficient",
      "url": "/registry/object/III.T80/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ConjectureGaps.lean#L201-L205",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ConjectureGaps.lean#L201-L205",
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

- Module: [TauLib.BookIII.Bridge.ConjectureGaps](/verify/taulib/docs/book-iii-bridge-conjecture-gaps/)
- Source path: [`TauLib/BookIII/Bridge/ConjectureGaps.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ConjectureGaps.lean#L201-L205)
- Source range: L201-L205
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T80` — Bridge Necessary Insufficient

## Immediate Comment / Docstring

```lean
/-- [III.T80] The three gap types form a complete taxonomy. -/
```

## Source Excerpt

```lean
def gap_taxonomy_complete : Bool :=
  let gaps := all_conjectures.map conjecture_gap_type
  let types := gaps.map GapType.toNat
  types.eraseDups.length == 3 &&
  types.contains 0 && types.contains 1 && types.contains 2
```
