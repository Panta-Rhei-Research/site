---
{
  "projection_kind": "taulib_declaration",
  "title": "tower_strict",
  "permalink": "/verify/taulib/docs/book-iii-arithmetic-tower-assembly/tower-strict/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Arithmetic.TowerAssembly`.",
  "declaration_id": "TauLib.BookIII.Arithmetic.TowerAssembly::tower_strict",
  "declaration_slug": "tower-strict",
  "kind": "theorem",
  "name": "tower_strict",
  "module_name": "TauLib.BookIII.Arithmetic.TowerAssembly",
  "module_url": "/verify/taulib/docs/book-iii-arithmetic-tower-assembly/",
  "source_line_start": 116,
  "source_line_end": 117,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/TowerAssembly.lean#L116-L117",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/TowerAssembly.lean#L116-L117",
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
- Source path: [`TauLib/BookIII/Arithmetic/TowerAssembly.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/TowerAssembly.lean#L116-L117)
- Source range: L116-L117
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
-- ============================================================
-- FORMAL VERIFICATION (native_decide)
-- ============================================================
```

## Source Excerpt

```lean
theorem tower_strict :
    tower_strict_check = true := by native_decide
```
