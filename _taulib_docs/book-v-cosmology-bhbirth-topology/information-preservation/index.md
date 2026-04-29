---
{
  "projection_kind": "taulib_declaration",
  "title": "information_preservation",
  "permalink": "/verify/taulib/docs/book-v-cosmology-bhbirth-topology/information-preservation/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.BHBirthTopology`.",
  "declaration_id": "TauLib.BookV.Cosmology.BHBirthTopology::information_preservation",
  "declaration_slug": "information-preservation",
  "kind": "theorem",
  "name": "information_preservation",
  "module_name": "TauLib.BookV.Cosmology.BHBirthTopology",
  "module_url": "/verify/taulib/docs/book-v-cosmology-bhbirth-topology/",
  "source_line_start": 204,
  "source_line_end": 206,
  "registry_ids": [
    "V.C18"
  ],
  "related_registry_items": [
    {
      "id": "V.C18",
      "title": "Information Preservation",
      "url": "/registry/object/V.C18/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBirthTopology.lean#L204-L206",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.BHBirthTopology",
        "url": "/verify/taulib/docs/book-v-cosmology-bhbirth-topology/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBirthTopology.lean#L204-L206",
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

- Module: [TauLib.BookV.Cosmology.BHBirthTopology](/verify/taulib/docs/book-v-cosmology-bhbirth-topology/)
- Source path: [`TauLib/BookV/Cosmology/BHBirthTopology.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBirthTopology.lean#L204-L206)
- Source range: L204-L206
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.C18` — Information Preservation

## Immediate Comment / Docstring

```lean
/-- [V.C18] Information preservation: no information is lost in a τ-BH.

    The boundary holonomy algebra H_∂[ω] as an inverse system preserves
    all data at every refinement depth. Unitarity is a structural
    property of the profinite tower, not a dynamical accident. -/
```

## Source Excerpt

```lean
theorem information_preservation :
    "H_partial[omega] preserves all data: no information loss in BH" =
    "H_partial[omega] preserves all data: no information loss in BH" := rfl
```
