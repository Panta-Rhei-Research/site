---
{
  "projection_kind": "taulib_declaration",
  "title": "dependency_chain_check",
  "permalink": "/verify/taulib/docs/book-iii-hinge-dependency-chain/dependency-chain-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Hinge.DependencyChain`.",
  "declaration_id": "TauLib.BookIII.Hinge.DependencyChain::dependency_chain_check",
  "declaration_slug": "dependency-chain-check",
  "kind": "def",
  "name": "dependency_chain_check",
  "module_name": "TauLib.BookIII.Hinge.DependencyChain",
  "module_url": "/verify/taulib/docs/book-iii-hinge-dependency-chain/",
  "source_line_start": 153,
  "source_line_end": 156,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/DependencyChain.lean#L153-L156",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/DependencyChain.lean#L153-L156",
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
- Source path: [`TauLib/BookIII/Hinge/DependencyChain.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/DependencyChain.lean#L153-L156)
- Source range: L153-L156
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D66` — Complete Dependency Chain

## Immediate Comment / Docstring

```lean
/-- [III.D66] Complete dependency chain check: strict order, layer validity,
    and tower coherence all hold simultaneously. -/
```

## Source Excerpt

```lean
def dependency_chain_check (bound db : TauIdx) : Bool :=
  chain_strict_order_check &&
  chain_layer_check bound db &&
  chain_tower_check bound db
```
