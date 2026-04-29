---
{
  "projection_kind": "taulib_declaration",
  "title": "ChainLink",
  "permalink": "/verify/taulib/docs/book-iii-hinge-dependency-chain/chain-link/",
  "summary_short": "`inductive` declaration in `TauLib.BookIII.Hinge.DependencyChain`.",
  "declaration_id": "TauLib.BookIII.Hinge.DependencyChain::ChainLink",
  "declaration_slug": "chain-link",
  "kind": "inductive",
  "name": "ChainLink",
  "module_name": "TauLib.BookIII.Hinge.DependencyChain",
  "module_url": "/verify/taulib/docs/book-iii-hinge-dependency-chain/",
  "source_line_start": 48,
  "source_line_end": 63,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/DependencyChain.lean#L48-L63",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/DependencyChain.lean#L48-L63",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
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
- Source path: [`TauLib/BookIII/Hinge/DependencyChain.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/DependencyChain.lean#L48-L63)
- Source range: L48-L63
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- A link in the 14-step dependency chain.
    K0-K6 = the seven axioms (Book I construction).
    E0-E3 = the four enrichment levels (Books I-VII).
    E1p, E2p, E3p = the plus-interfaces (enrichment transitions). -/
```

## Source Excerpt

```lean
inductive ChainLink where
  | K0 : ChainLink   -- void axiom
  | K1 : ChainLink   -- unit axiom
  | K2 : ChainLink   -- polarity axiom
  | K3 : ChainLink   -- boundary axiom
  | K4 : ChainLink   -- denotation axiom
  | K5 : ChainLink   -- composition axiom
  | K6 : ChainLink   -- omega axiom
  | E0 : ChainLink   -- mathematics (Books I-III)
  | E1 : ChainLink   -- physics (Books IV-V)
  | E1p : ChainLink  -- E1+ interface (NS/YM/Hodge acquired)
  | E2 : ChainLink   -- computation (Book VI)
  | E2p : ChainLink  -- E2+ interface (BSD/Langlands acquired)
  | E3 : ChainLink   -- metaphysics (Book VII)
  | E3p : ChainLink  -- E3+ terminal (saturation)
  deriving Repr, DecidableEq, BEq, Inhabited
```
