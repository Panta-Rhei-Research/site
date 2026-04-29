---
{
  "projection_kind": "taulib_declaration",
  "title": "bridge_damage",
  "permalink": "/verify/taulib/docs/book-iii-bridge-forbidden-moves/bridge-damage/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Bridge.ForbiddenMoves`.",
  "declaration_id": "TauLib.BookIII.Bridge.ForbiddenMoves::bridge_damage",
  "declaration_slug": "bridge-damage",
  "kind": "def",
  "name": "bridge_damage",
  "module_name": "TauLib.BookIII.Bridge.ForbiddenMoves",
  "module_url": "/verify/taulib/docs/book-iii-bridge-forbidden-moves/",
  "source_line_start": 145,
  "source_line_end": 150,
  "registry_ids": [
    "III.T43"
  ],
  "related_registry_items": [
    {
      "id": "III.T43",
      "title": "Move-Bridge Correspondence",
      "url": "/registry/object/III.T43/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ForbiddenMoves.lean#L145-L150",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Bridge.ForbiddenMoves",
        "url": "/verify/taulib/docs/book-iii-bridge-forbidden-moves/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ForbiddenMoves.lean#L145-L150",
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

- Module: [TauLib.BookIII.Bridge.ForbiddenMoves](/verify/taulib/docs/book-iii-bridge-forbidden-moves/)
- Source path: [`TauLib/BookIII/Bridge/ForbiddenMoves.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ForbiddenMoves.lean#L145-L150)
- Source range: L145-L150
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T43` — Move-Bridge Correspondence

## Immediate Comment / Docstring

```lean
/-- [III.T43] Bridge degradation: how each forbidden move affects the
    bridge functor. Returns the "bridge damage" category:
    - 0 = no damage (move not applicable)
    - 1 = mild (bridge loses injectivity)
    - 2 = severe (bridge loses faithfulness)
    - 3 = break (bridge degenerates entirely) -/
```

## Source Excerpt

```lean
def bridge_damage : ForbiddenMove -> Nat
  | .unbounded_fanout           => 2   -- loses faithfulness on large diagrams
  | .global_equality            => 1   -- loses injectivity on equality checks
  | .succinct_circuits          => 3   -- bridge breaks (P vs NP)
  | .exponential_quantification => 3   -- bridge breaks (exponential blowup)
  | .nonlocal_disguise          => 1   -- loses injectivity on representations
```
