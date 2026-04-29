---
{
  "projection_kind": "taulib_declaration",
  "title": "euler_product_3",
  "permalink": "/verify/taulib/docs/book-iii-doors-split-complex-zeta/euler-product-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Doors.SplitComplexZeta`.",
  "declaration_id": "TauLib.BookIII.Doors.SplitComplexZeta::euler_product_3",
  "declaration_slug": "euler-product-3",
  "kind": "theorem",
  "name": "euler_product_3",
  "module_name": "TauLib.BookIII.Doors.SplitComplexZeta",
  "module_url": "/verify/taulib/docs/book-iii-doors-split-complex-zeta/",
  "source_line_start": 193,
  "source_line_end": 197,
  "registry_ids": [
    "III.T16"
  ],
  "related_registry_items": [
    {
      "id": "III.T16",
      "title": "Bipolar Euler Product",
      "url": "/registry/object/III.T16/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SplitComplexZeta.lean#L193-L197",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Doors.SplitComplexZeta",
        "url": "/verify/taulib/docs/book-iii-doors-split-complex-zeta/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SplitComplexZeta.lean#L193-L197",
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

- Module: [TauLib.BookIII.Doors.SplitComplexZeta](/verify/taulib/docs/book-iii-doors-split-complex-zeta/)
- Source path: [`TauLib/BookIII/Doors/SplitComplexZeta.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SplitComplexZeta.lean#L193-L197)
- Source range: L193-L197
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T16` — Bipolar Euler Product

## Immediate Comment / Docstring

```lean
/-- [III.T16] Structural: B · C · X = Prim(3) at depth 3. -/
```

## Source Excerpt

```lean
theorem euler_product_3 :
    split_zeta_b 3 * split_zeta_c 3 * split_zeta_x 3 = primorial 3 := by
  native_decide

end Tau.BookIII.Doors
```
