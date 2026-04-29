---
{
  "projection_kind": "taulib_declaration",
  "title": "yp_is_20_81",
  "permalink": "/verify/taulib/docs/book-v-cosmology-helium-fraction/yp-is-20-81/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.HeliumFraction`.",
  "declaration_id": "TauLib.BookV.Cosmology.HeliumFraction::yp_is_20_81",
  "declaration_slug": "yp-is-20-81",
  "kind": "theorem",
  "name": "yp_is_20_81",
  "module_name": "TauLib.BookV.Cosmology.HeliumFraction",
  "module_url": "/verify/taulib/docs/book-v-cosmology-helium-fraction/",
  "source_line_start": 195,
  "source_line_end": 198,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/HeliumFraction.lean#L195-L198",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.HeliumFraction",
        "url": "/verify/taulib/docs/book-v-cosmology-helium-fraction/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/HeliumFraction.lean#L195-L198",
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

- Module: [TauLib.BookV.Cosmology.HeliumFraction](/verify/taulib/docs/book-v-cosmology-helium-fraction/)
- Source path: [`TauLib/BookV/Cosmology/HeliumFraction.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/HeliumFraction.lean#L195-L198)
- Source range: L195-L198
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Y_p = (8/27) × (5/6) = 20/81, verified as 8 × 5 × 81 = 20 × 27 × 6. -/
```

## Source Excerpt

```lean
theorem yp_is_20_81 :
    he_packing.pack_num * domain_correction.corr_num * he_prediction.yp_den =
    he_prediction.yp_num * he_packing.pack_den * domain_correction.corr_den :=
  by native_decide
```
