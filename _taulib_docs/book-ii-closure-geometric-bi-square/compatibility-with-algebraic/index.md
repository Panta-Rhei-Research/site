---
{
  "projection_kind": "taulib_declaration",
  "title": "compatibility_with_algebraic",
  "permalink": "/corpus/taulib/docs/book-ii-closure-geometric-bi-square/compatibility-with-algebraic/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Closure.GeometricBiSquare`.",
  "declaration_id": "TauLib.BookII.Closure.GeometricBiSquare::compatibility_with_algebraic",
  "declaration_slug": "compatibility-with-algebraic",
  "kind": "theorem",
  "name": "compatibility_with_algebraic",
  "module_name": "TauLib.BookII.Closure.GeometricBiSquare",
  "module_url": "/corpus/taulib/docs/book-ii-closure-geometric-bi-square/",
  "source_line_start": 158,
  "source_line_end": 162,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/GeometricBiSquare.lean#L158-L162",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Closure.GeometricBiSquare",
        "url": "/corpus/taulib/docs/book-ii-closure-geometric-bi-square/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/GeometricBiSquare.lean#L158-L162",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookII.Closure.GeometricBiSquare](/corpus/taulib/docs/book-ii-closure-geometric-bi-square/)
- Source path: [`TauLib/BookII/Closure/GeometricBiSquare.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/GeometricBiSquare.lean#L158-L162)
- Source range: L158-L162
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Compatibility: the algebraic bi-square characterization is
    preserved. Forgetting geometry recovers I.T41. -/
```

## Source Excerpt

```lean
theorem compatibility_with_algebraic (f : StageFun) :
    TowerCoherent f ↔
    (∀ n k l : TauIdx, k ≤ l → reduce (f.b_fun n l) k = f.b_fun n k) ∧
    (∀ n k l : TauIdx, k ≤ l → reduce (f.c_fun n l) k = f.c_fun n k) :=
  algebraic_core.bi_square_char f
```
