---
{
  "projection_kind": "taulib_declaration",
  "title": "tower_assembly_check",
  "permalink": "/corpus/taulib/docs/book-iii-arithmetic-tower-assembly/tower-assembly-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Arithmetic.TowerAssembly`.",
  "declaration_id": "TauLib.BookIII.Arithmetic.TowerAssembly::tower_assembly_check",
  "declaration_slug": "tower-assembly-check",
  "kind": "def",
  "name": "tower_assembly_check",
  "module_name": "TauLib.BookIII.Arithmetic.TowerAssembly",
  "module_url": "/corpus/taulib/docs/book-iii-arithmetic-tower-assembly/",
  "source_line_start": 98,
  "source_line_end": 101,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/TowerAssembly.lean#L98-L101",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Arithmetic.TowerAssembly",
        "url": "/corpus/taulib/docs/book-iii-arithmetic-tower-assembly/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/TowerAssembly.lean#L98-L101",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "data/computed value",
      "status": "data/computed value"
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

- Module: [TauLib.BookIII.Arithmetic.TowerAssembly](/corpus/taulib/docs/book-iii-arithmetic-tower-assembly/)
- Source path: [`TauLib/BookIII/Arithmetic/TowerAssembly.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/TowerAssembly.lean#L98-L101)
- Source range: L98-L101
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- `III.T40` — Enrichment Tower Assembly

## Immediate Comment / Docstring

```lean
/-- [III.T40] Tower assembly: tower is strict, coverage is complete,
    and scaling chain is coherent. -/
```

## Source Excerpt

```lean
def tower_assembly_check (bound db : TauIdx) : Bool :=
  tower_strict_check &&
  millennium_coverage_check &&
  scaling_chain_check bound db
```
