---
{
  "projection_kind": "taulib_declaration",
  "title": "NucleosynthesisProducts",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-supernovae/nucleosynthesis-products/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Astrophysics.Supernovae`.",
  "declaration_id": "TauLib.BookV.Astrophysics.Supernovae::NucleosynthesisProducts",
  "declaration_slug": "nucleosynthesis-products",
  "kind": "structure",
  "name": "NucleosynthesisProducts",
  "module_name": "TauLib.BookV.Astrophysics.Supernovae",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-supernovae/",
  "source_line_start": 202,
  "source_line_end": 209,
  "registry_ids": [
    "V.D128"
  ],
  "related_registry_items": [
    {
      "id": "V.D128",
      "title": "r-Process as Rapid Charge Loading --- V.D61",
      "url": "/registry/object/V.D128/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/Supernovae.lean#L202-L209",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.Supernovae",
        "url": "/verify/taulib/docs/book-v-astrophysics-supernovae/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/Supernovae.lean#L202-L209",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "status": "defined"
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

- Module: [TauLib.BookV.Astrophysics.Supernovae](/verify/taulib/docs/book-v-astrophysics-supernovae/)
- Source path: [`TauLib/BookV/Astrophysics/Supernovae.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/Supernovae.lean#L202-L209)
- Source range: L202-L209
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D128` — r-Process as Rapid Charge Loading --- V.D61

## Immediate Comment / Docstring

```lean
/-- [V.D128] Nucleosynthesis products: the element groups produced
    by different supernova types.

    In the τ-framework, nucleosynthesis is a readout of the
    C-sector (strong nuclear) coupling at high temperatures
    where fusion reactions are defect-budget favorable. -/
```

## Source Excerpt

```lean
structure NucleosynthesisProducts where
  /-- Supernova type. -/
  sn_type : SupernovaType
  /-- Primary element groups produced. -/
  primary_products : List ElementGroup
  /-- Products are non-empty. -/
  products_nonempty : primary_products.length > 0
  deriving Repr
```
