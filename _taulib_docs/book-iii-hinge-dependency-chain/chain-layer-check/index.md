---
{
  "projection_kind": "taulib_declaration",
  "title": "chain_layer_check",
  "permalink": "/verify/taulib/docs/book-iii-hinge-dependency-chain/chain-layer-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Hinge.DependencyChain`.",
  "declaration_id": "TauLib.BookIII.Hinge.DependencyChain::chain_layer_check",
  "declaration_slug": "chain-layer-check",
  "kind": "def",
  "name": "chain_layer_check",
  "module_name": "TauLib.BookIII.Hinge.DependencyChain",
  "module_url": "/verify/taulib/docs/book-iii-hinge-dependency-chain/",
  "source_line_start": 130,
  "source_line_end": 141,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/DependencyChain.lean#L130-L141",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/DependencyChain.lean#L130-L141",
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
- Source path: [`TauLib/BookIII/Hinge/DependencyChain.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/DependencyChain.lean#L130-L141)
- Source range: L130-L141
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D66` — Complete Dependency Chain

## Immediate Comment / Docstring

```lean
/-- [III.D66] Verify that each enrichment level's layer template is valid
    at the corresponding chain link. For K-links, verify that the axiom
    level infrastructure (primorial, reduce, etc.) is operational. -/
```

## Source Excerpt

```lean
def chain_layer_check (bound db : TauIdx) : Bool :=
  go chain_links bound db (chain_links.length + 1)
where
  go (links : List ChainLink) (bound db fuel : Nat) : Bool :=
    if fuel = 0 then true
    else match links with
    | [] => true
    | link :: rest =>
      let lev := link.toEnrLevel
      let layer_ok := layer_valid_at lev bound db
      layer_ok && go rest bound db (fuel - 1)
  termination_by fuel
```
