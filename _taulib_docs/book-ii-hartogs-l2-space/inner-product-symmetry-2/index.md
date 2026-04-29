---
{
  "projection_kind": "taulib_declaration",
  "title": "inner_product_symmetry_2",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-l2-space/inner-product-symmetry-2/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Hartogs.L2Space`.",
  "declaration_id": "TauLib.BookII.Hartogs.L2Space::inner_product_symmetry_2",
  "declaration_slug": "inner-product-symmetry-2",
  "kind": "theorem",
  "name": "inner_product_symmetry_2",
  "module_name": "TauLib.BookII.Hartogs.L2Space",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-l2-space/",
  "source_line_start": 189,
  "source_line_end": 192,
  "registry_ids": [
    "II.D82"
  ],
  "related_registry_items": [
    {
      "id": "II.D82",
      "title": "L² Inner Product",
      "url": "/registry/object/II.D82/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/L2Space.lean#L189-L192",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.L2Space",
        "url": "/verify/taulib/docs/book-ii-hartogs-l2-space/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/L2Space.lean#L189-L192",
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

- Module: [TauLib.BookII.Hartogs.L2Space](/verify/taulib/docs/book-ii-hartogs-l2-space/)
- Source path: [`TauLib/BookII/Hartogs/L2Space.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/L2Space.lean#L189-L192)
- Source range: L189-L192
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.D82` — L² Inner Product

## Immediate Comment / Docstring

```lean
/-- [II.D82] Symmetry of inner product at stage 2. -/
```

## Source Excerpt

```lean
theorem inner_product_symmetry_2 :
    inner_product_symmetry_check
      (fun x => (x : Int)) (fun x => (x * x : Int)) 2 = true := by
  native_decide
```
