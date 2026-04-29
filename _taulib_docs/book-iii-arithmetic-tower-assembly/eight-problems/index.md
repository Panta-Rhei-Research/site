---
{
  "projection_kind": "taulib_declaration",
  "title": "eight_problems",
  "permalink": "/verify/taulib/docs/book-iii-arithmetic-tower-assembly/eight-problems/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Arithmetic.TowerAssembly`.",
  "declaration_id": "TauLib.BookIII.Arithmetic.TowerAssembly::eight_problems",
  "declaration_slug": "eight-problems",
  "kind": "theorem",
  "name": "eight_problems",
  "module_name": "TauLib.BookIII.Arithmetic.TowerAssembly",
  "module_url": "/verify/taulib/docs/book-iii-arithmetic-tower-assembly/",
  "source_line_start": 142,
  "source_line_end": 148,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/TowerAssembly.lean#L142-L148",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/TowerAssembly.lean#L142-L148",
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
- Source path: [`TauLib/BookIII/Arithmetic/TowerAssembly.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/TowerAssembly.lean#L142-L148)
- Source range: L142-L148
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T40` — Enrichment Tower Assembly

## Immediate Comment / Docstring

```lean
/-- [III.T40] Structural: all 8 problems covered. -/
```

## Source Excerpt

```lean
theorem eight_problems :
    [problem_level .RH, problem_level .Poincare,
     problem_level .NS, problem_level .YM, problem_level .Hodge,
     problem_level .BSD, problem_level .Langlands,
     problem_level .PvsNP].length = 8 := rfl

end Tau.BookIII.Arithmetic
```
