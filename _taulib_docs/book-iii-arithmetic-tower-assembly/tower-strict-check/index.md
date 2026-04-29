---
{
  "projection_kind": "taulib_declaration",
  "title": "tower_strict_check",
  "permalink": "/verify/taulib/docs/book-iii-arithmetic-tower-assembly/tower-strict-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Arithmetic.TowerAssembly`.",
  "declaration_id": "TauLib.BookIII.Arithmetic.TowerAssembly::tower_strict_check",
  "declaration_slug": "tower-strict-check",
  "kind": "def",
  "name": "tower_strict_check",
  "module_name": "TauLib.BookIII.Arithmetic.TowerAssembly",
  "module_url": "/verify/taulib/docs/book-iii-arithmetic-tower-assembly/",
  "source_line_start": 39,
  "source_line_end": 43,
  "registry_ids": [
    "III.T40"
  ],
  "related_registry_items": [
    {
      "id": "III.T40",
      "title": "Enrichment Tower Assembly",
      "url": "/registry/object/III.T40/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/TowerAssembly.lean#L39-L43",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Arithmetic.TowerAssembly",
        "url": "/verify/taulib/docs/book-iii-arithmetic-tower-assembly/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/TowerAssembly.lean#L39-L43",
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

- Module: [TauLib.BookIII.Arithmetic.TowerAssembly](/verify/taulib/docs/book-iii-arithmetic-tower-assembly/)
- Source path: [`TauLib/BookIII/Arithmetic/TowerAssembly.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/TowerAssembly.lean#L39-L43)
- Source range: L39-L43
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T40` — Enrichment Tower Assembly

## Immediate Comment / Docstring

```lean
/-- [III.T40] Tower strictness: E₀ ⊊ E₁ ⊊ E₂. Each level is a proper
    subset of the next (enrichment adds genuine content). -/
```

## Source Excerpt

```lean
def tower_strict_check : Bool :=
  -- E₀ < E₁ < E₂ < E₃
  EnrLevel.lt .E0 .E1 &&
  EnrLevel.lt .E1 .E2 &&
  EnrLevel.lt .E2 .E3
```
