---
{
  "projection_kind": "taulib_declaration",
  "title": "chain_strict_order_check",
  "permalink": "/verify/taulib/docs/book-iii-hinge-dependency-chain/chain-strict-order-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Hinge.DependencyChain`.",
  "declaration_id": "TauLib.BookIII.Hinge.DependencyChain::chain_strict_order_check",
  "declaration_slug": "chain-strict-order-check",
  "kind": "def",
  "name": "chain_strict_order_check",
  "module_name": "TauLib.BookIII.Hinge.DependencyChain",
  "module_url": "/verify/taulib/docs/book-iii-hinge-dependency-chain/",
  "source_line_start": 117,
  "source_line_end": 125,
  "registry_ids": [
    "III.D66"
  ],
  "related_registry_items": [
    {
      "id": "III.D66",
      "title": "Complete Dependency Chain",
      "url": "/registry/object/III.D66/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/DependencyChain.lean#L117-L125",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/DependencyChain.lean#L117-L125",
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
- Source path: [`TauLib/BookIII/Hinge/DependencyChain.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/DependencyChain.lean#L117-L125)
- Source range: L117-L125
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D66` — Complete Dependency Chain

## Immediate Comment / Docstring

```lean
/-- [III.D66] Verify that the chain is strictly ordered: each link's
    index is strictly less than the next link's index. -/
```

## Source Excerpt

```lean
def chain_strict_order_check : Bool :=
  go chain_links
where
  go : List ChainLink -> Bool
    | [] => true
    | [_] => true
    | a :: b :: rest =>
      -- Strict ordering + successor consistency
      a.toNat < b.toNat && a.succ.toNat <= b.toNat && go (b :: rest)
```
