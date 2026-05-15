---
{
  "projection_kind": "taulib_declaration",
  "title": "ScopeLabel",
  "permalink": "/corpus/taulib/docs/book-iii-bridge-bridge-axiom/scope-label/",
  "summary_short": "`inductive` declaration in `TauLib.BookIII.Bridge.BridgeAxiom`.",
  "declaration_id": "TauLib.BookIII.Bridge.BridgeAxiom::ScopeLabel",
  "declaration_slug": "scope-label",
  "kind": "inductive",
  "name": "ScopeLabel",
  "module_name": "TauLib.BookIII.Bridge.BridgeAxiom",
  "module_url": "/corpus/taulib/docs/book-iii-bridge-bridge-axiom/",
  "source_line_start": 58,
  "source_line_end": 63,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/BridgeAxiom.lean#L58-L63",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Bridge.BridgeAxiom",
        "url": "/corpus/taulib/docs/book-iii-bridge-bridge-axiom/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/BridgeAxiom.lean#L58-L63",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
      "role": "type/data schema",
      "status": "type/data schema"
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

- Module: [TauLib.BookIII.Bridge.BridgeAxiom](/corpus/taulib/docs/book-iii-bridge-bridge-axiom/)
- Source path: [`TauLib/BookIII/Bridge/BridgeAxiom.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/BridgeAxiom.lean#L58-L63)
- Source range: L58-L63
- Kind: `inductive`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The four scope labels used throughout Book III.
    Establishes the honesty discipline for claims. -/
```

## Source Excerpt

```lean
inductive ScopeLabel where
  | established : ScopeLabel     -- proved in classical mathematics
  | tau_effective : ScopeLabel   -- proved within tau at native level
  | conjectural : ScopeLabel     -- depends on unproved bridge identification
  | metaphorical : ScopeLabel    -- suggestive analogy, not a theorem
  deriving Repr, DecidableEq, BEq
```
