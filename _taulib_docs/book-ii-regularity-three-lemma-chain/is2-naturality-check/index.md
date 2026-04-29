---
{
  "projection_kind": "taulib_declaration",
  "title": "is2_naturality_check",
  "permalink": "/verify/taulib/docs/book-ii-regularity-three-lemma-chain/is2-naturality-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Regularity.ThreeLemmaChain`.",
  "declaration_id": "TauLib.BookII.Regularity.ThreeLemmaChain::is2_naturality_check",
  "declaration_slug": "is2-naturality-check",
  "kind": "def",
  "name": "is2_naturality_check",
  "module_name": "TauLib.BookII.Regularity.ThreeLemmaChain",
  "module_url": "/verify/taulib/docs/book-ii-regularity-three-lemma-chain/",
  "source_line_start": 266,
  "source_line_end": 287,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L266-L287",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L266-L287",
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

- Module: [TauLib.BookII.Regularity.ThreeLemmaChain](/verify/taulib/docs/book-ii-regularity-three-lemma-chain/)
- Source path: [`TauLib/BookII/Regularity/ThreeLemmaChain.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L266-L287)
- Source range: L266-L287
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [II.T33, IS2] Stagewise naturality: tower coherence of B and C
    components individually. Reducing the B-channel at a finer stage
    to a coarser stage gives the B-channel at the coarser stage. -/
```

## Source Excerpt

```lean
def is2_naturality_check (bound db : TauIdx) : Bool :=
  go 2 1 ((bound + 1) * (db + 1))
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k >= db then go (x + 1) 1 (fuel - 1)
    else
      -- Compare B and C at stage k vs stage k+1 reduced to k
      let rx_k := reduce x k
      let rx_k1 := reduce x (k + 1)
      let rx_k1_reduced := reduce rx_k1 k
      -- B-channel coherence
      let b_k := (from_tau_idx rx_k).b
      let b_k1r := (from_tau_idx rx_k1_reduced).b
      -- C-channel coherence
      let c_k := (from_tau_idx rx_k).c
      let c_k1r := (from_tau_idx rx_k1_reduced).c
      -- Since rx_k1_reduced = rx_k (by tower coherence), charts agree
      let ok := b_k == b_k1r && c_k == c_k1r
      ok && go x (k + 1) (fuel - 1)
  termination_by fuel
```
