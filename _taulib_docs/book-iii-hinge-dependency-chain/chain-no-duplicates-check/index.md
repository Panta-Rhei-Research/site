---
{
  "projection_kind": "taulib_declaration",
  "title": "chain_no_duplicates_check",
  "permalink": "/verify/taulib/docs/book-iii-hinge-dependency-chain/chain-no-duplicates-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Hinge.DependencyChain`.",
  "declaration_id": "TauLib.BookIII.Hinge.DependencyChain::chain_no_duplicates_check",
  "declaration_slug": "chain-no-duplicates-check",
  "kind": "def",
  "name": "chain_no_duplicates_check",
  "module_name": "TauLib.BookIII.Hinge.DependencyChain",
  "module_url": "/verify/taulib/docs/book-iii-hinge-dependency-chain/",
  "source_line_start": 180,
  "source_line_end": 191,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/DependencyChain.lean#L180-L191",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/DependencyChain.lean#L180-L191",
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
- Source path: [`TauLib/BookIII/Hinge/DependencyChain.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/DependencyChain.lean#L180-L191)
- Source range: L180-L191
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.P29` — Chain Verification Protocol

## Immediate Comment / Docstring

```lean
/-- [III.P29] Acyclicity witness: no link appears twice in the chain. -/
```

## Source Excerpt

```lean
def chain_no_duplicates_check : Bool :=
  go chain_links [] (chain_links.length + 1)
where
  go (links : List ChainLink) (seen : List Nat) (fuel : Nat) : Bool :=
    if fuel = 0 then true
    else match links with
    | [] => true
    | link :: rest =>
      let idx := link.toNat
      let fresh := !(seen.contains idx)
      fresh && go rest (idx :: seen) (fuel - 1)
  termination_by fuel
```
