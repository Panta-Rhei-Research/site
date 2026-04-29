---
{
  "projection_kind": "taulib_declaration",
  "title": "j_swap_proj_plus",
  "permalink": "/verify/taulib/docs/book-ii-regularity-three-lemma-chain/j-swap-proj-plus/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Regularity.ThreeLemmaChain`.",
  "declaration_id": "TauLib.BookII.Regularity.ThreeLemmaChain::j_swap_proj_plus",
  "declaration_slug": "j-swap-proj-plus",
  "kind": "theorem",
  "name": "j_swap_proj_plus",
  "module_name": "TauLib.BookII.Regularity.ThreeLemmaChain",
  "module_url": "/verify/taulib/docs/book-ii-regularity-three-lemma-chain/",
  "source_line_start": 207,
  "source_line_end": 209,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L207-L209",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Regularity.ThreeLemmaChain",
        "url": "/verify/taulib/docs/book-ii-regularity-three-lemma-chain/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L207-L209",
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

- Module: [TauLib.BookII.Regularity.ThreeLemmaChain](/verify/taulib/docs/book-ii-regularity-three-lemma-chain/)
- Source path: [`TauLib/BookII/Regularity/ThreeLemmaChain.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L207-L209)
- Source range: L207-L209
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- j-swap swaps the idempotent projections (formal). -/
```

## Source Excerpt

```lean
theorem j_swap_proj_plus (bp : SectorPair) :
    j_swap (proj_plus bp) = proj_minus (j_swap bp) := by
  simp [j_swap, proj_plus, proj_minus, SectorPair.mul, e_plus_sector, e_minus_sector]
```
