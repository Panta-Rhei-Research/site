---
{
  "projection_kind": "taulib_declaration",
  "title": "chain_linearity_check",
  "permalink": "/verify/taulib/docs/book-iii-hinge-dependency-chain/chain-linearity-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Hinge.DependencyChain`.",
  "declaration_id": "TauLib.BookIII.Hinge.DependencyChain::chain_linearity_check",
  "declaration_slug": "chain-linearity-check",
  "kind": "def",
  "name": "chain_linearity_check",
  "module_name": "TauLib.BookIII.Hinge.DependencyChain",
  "module_url": "/verify/taulib/docs/book-iii-hinge-dependency-chain/",
  "source_line_start": 165,
  "source_line_end": 177,
  "registry_ids": [
    "III.P29"
  ],
  "related_registry_items": [
    {
      "id": "III.P29",
      "title": "Chain Verification Protocol",
      "url": "/registry/object/III.P29/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/DependencyChain.lean#L165-L177",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Hinge.DependencyChain",
        "url": "/verify/taulib/docs/book-iii-hinge-dependency-chain/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/DependencyChain.lean#L165-L177",
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

- Module: [TauLib.BookIII.Hinge.DependencyChain](/verify/taulib/docs/book-iii-hinge-dependency-chain/)
- Source path: [`TauLib/BookIII/Hinge/DependencyChain.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/DependencyChain.lean#L165-L177)
- Source range: L165-L177
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.P29` — Chain Verification Protocol

## Immediate Comment / Docstring

```lean
/-- [III.P29] Chain linearity: the chain has no cycles.
    Verification: for every pair (i, j) with i < j in the chain,
    link_i.toNat < link_j.toNat (no backward edges). -/
```

## Source Excerpt

```lean
def chain_linearity_check : Bool :=
  go chain_links 0 (chain_links.length + 1)
where
  go (links : List ChainLink) (prev_idx fuel : Nat) : Bool :=
    if fuel = 0 then true
    else match links with
    | [] => true
    | link :: rest =>
      let curr := link.toNat
      let ok := if prev_idx == 0 && curr == 0 then true
                else curr > prev_idx || (curr == 0 && prev_idx == 0)
      ok && go rest curr (fuel - 1)
  termination_by fuel
```
