---
{
  "projection_kind": "taulib_declaration",
  "title": "sector_product_depth_3",
  "permalink": "/verify/taulib/docs/book-iii-hinge-hinge-theorem/sector-product-depth-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Hinge.HingeTheorem`.",
  "declaration_id": "TauLib.BookIII.Hinge.HingeTheorem::sector_product_depth_3",
  "declaration_slug": "sector-product-depth-3",
  "kind": "theorem",
  "name": "sector_product_depth_3",
  "module_name": "TauLib.BookIII.Hinge.HingeTheorem",
  "module_url": "/verify/taulib/docs/book-iii-hinge-hinge-theorem/",
  "source_line_start": 355,
  "source_line_end": 357,
  "registry_ids": [
    "III.T41"
  ],
  "related_registry_items": [
    {
      "id": "III.T41",
      "title": "Hinge Theorem",
      "url": "/registry/object/III.T41/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/HingeTheorem.lean#L355-L357",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Hinge.HingeTheorem",
        "url": "/verify/taulib/docs/book-iii-hinge-hinge-theorem/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/HingeTheorem.lean#L355-L357",
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

- Module: [TauLib.BookIII.Hinge.HingeTheorem](/verify/taulib/docs/book-iii-hinge-hinge-theorem/)
- Source path: [`TauLib/BookIII/Hinge/HingeTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/HingeTheorem.lean#L355-L357)
- Source range: L355-L357
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T41` — Hinge Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T41] Structural: B * C * X = Prim(3) = 30 at depth 3. -/
```

## Source Excerpt

```lean
theorem sector_product_depth_3 :
    split_zeta_b 3 * split_zeta_c 3 * split_zeta_x 3 = primorial 3 := by
  native_decide
```
