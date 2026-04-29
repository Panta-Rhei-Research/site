---
{
  "projection_kind": "taulib_declaration",
  "title": "yp_baryogenesis_shared_factor",
  "permalink": "/verify/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/yp-baryogenesis-shared-factor/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.BaryogenesisAsymmetry`.",
  "declaration_id": "TauLib.BookV.Cosmology.BaryogenesisAsymmetry::yp_baryogenesis_shared_factor",
  "declaration_slug": "yp-baryogenesis-shared-factor",
  "kind": "theorem",
  "name": "yp_baryogenesis_shared_factor",
  "module_name": "TauLib.BookV.Cosmology.BaryogenesisAsymmetry",
  "module_url": "/verify/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/",
  "source_line_start": 101,
  "source_line_end": 102,
  "registry_ids": [
    "V.T171"
  ],
  "related_registry_items": [
    {
      "id": "V.T171",
      "title": "(5/6) Threshold Factor Shared with Y_p = 20/81",
      "url": "/registry/object/V.T171/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L101-L102",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.BaryogenesisAsymmetry",
        "url": "/verify/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L101-L102",
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

- Module: [TauLib.BookV.Cosmology.BaryogenesisAsymmetry](/verify/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/)
- Source path: [`TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L101-L102)
- Source range: L101-L102
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T171` — (5/6) Threshold Factor Shared with Y_p = 20/81

## Immediate Comment / Docstring

```lean
/-- Y_p = 20/81 = (8/27) * (5/6): helium fraction shares the (5/6) factor
    with the baryon asymmetry formula. [V.T171]

    This is verified as a rational identity:
    (20 : Rat) / 81 = 8 / 27 * (5 / 6). -/
```

## Source Excerpt

```lean
theorem yp_baryogenesis_shared_factor : (20 : Rat) / 81 = 8 / 27 * (5 / 6) := by
  norm_num
```
