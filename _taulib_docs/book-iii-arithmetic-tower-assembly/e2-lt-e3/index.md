---
{
  "projection_kind": "taulib_declaration",
  "title": "e2_lt_e3",
  "permalink": "/verify/taulib/docs/book-iii-arithmetic-tower-assembly/e2-lt-e3/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Arithmetic.TowerAssembly`.",
  "declaration_id": "TauLib.BookIII.Arithmetic.TowerAssembly::e2_lt_e3",
  "declaration_slug": "e2-lt-e3",
  "kind": "theorem",
  "name": "e2_lt_e3",
  "module_name": "TauLib.BookIII.Arithmetic.TowerAssembly",
  "module_url": "/verify/taulib/docs/book-iii-arithmetic-tower-assembly/",
  "source_line_start": 139,
  "source_line_end": 139,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/TowerAssembly.lean#L139-L139",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/TowerAssembly.lean#L139-L139",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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
- Source path: [`TauLib/BookIII/Arithmetic/TowerAssembly.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/TowerAssembly.lean#L139-L139)
- Source range: L139-L139
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T40` — Enrichment Tower Assembly

## Immediate Comment / Docstring

```lean
/-- [III.T40] Structural: E₂ < E₃. -/
```

## Source Excerpt

```lean
theorem e2_lt_e3 : EnrLevel.lt .E2 .E3 = true := rfl
```
