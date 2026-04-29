---
{
  "projection_kind": "taulib_declaration",
  "title": "tower_projection",
  "permalink": "/verify/taulib/docs/book-iii-bridge-translation-topo/tower-projection/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Bridge.TranslationTopo`.",
  "declaration_id": "TauLib.BookIII.Bridge.TranslationTopo::tower_projection",
  "declaration_slug": "tower-projection",
  "kind": "def",
  "name": "tower_projection",
  "module_name": "TauLib.BookIII.Bridge.TranslationTopo",
  "module_url": "/verify/taulib/docs/book-iii-bridge-translation-topo/",
  "source_line_start": 55,
  "source_line_end": 55,
  "registry_ids": [
    "III.D89"
  ],
  "related_registry_items": [
    {
      "id": "III.D89",
      "title": "Topological Translation Functor",
      "url": "/registry/object/III.D89/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationTopo.lean#L55-L55",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Bridge.TranslationTopo",
        "url": "/verify/taulib/docs/book-iii-bridge-translation-topo/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationTopo.lean#L55-L55",
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

- Module: [TauLib.BookIII.Bridge.TranslationTopo](/verify/taulib/docs/book-iii-bridge-translation-topo/)
- Source path: [`TauLib/BookIII/Bridge/TranslationTopo.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationTopo.lean#L55-L55)
- Source range: L55-L55
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D89` — Topological Translation Functor

## Immediate Comment / Docstring

```lean
/-- [III.D89] Tower projection: the canonical map π_k : Z/M_{k+1} → Z/M_k.
    This is reduce(x, k) and is the fundamental topological structure. -/
```

## Source Excerpt

```lean
def tower_projection (x k : Nat) : Nat := reduce x k
```
